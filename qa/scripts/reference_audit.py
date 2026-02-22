#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REF_DIR = ROOT / "plugins" / "obsidian-cli" / "references"


@dataclass
class AuditResult:
    missing_in_refs: list
    extra_in_refs: list
    syntax_violations: list
    description_drift: list
    command_count_help: int
    command_count_refs: int

    @property
    def hard_failures(self):
        failures = []
        if self.missing_in_refs:
            failures.append(
                f"Missing commands in references: {', '.join(self.missing_in_refs)}"
            )
        failures.extend(self.syntax_violations)
        return failures


def run_help() -> str:
    try:
        out = subprocess.check_output(["obsidian", "help"], text=True, cwd=ROOT)
    except FileNotFoundError:
        print("ERROR: `obsidian` binary not found in PATH.")
        sys.exit(2)
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: Failed running `obsidian help` ({exc.returncode}).")
        sys.exit(2)
    return out


def parse_help_commands(help_text: str):
    commands = {}
    in_commands = False
    in_developer = False

    for raw in help_text.splitlines():
        line = raw.strip()
        if line.startswith("Commands:"):
            in_commands = True
            in_developer = False
            continue
        if line.startswith("Developer:"):
            in_commands = False
            in_developer = True
            continue
        if line.startswith("Examples:"):
            in_developer = False
            continue

        if not (in_commands or in_developer) or not line:
            continue

        m = re.match(r"([a-z0-9:_-]+)\s+(.*)$", line)
        if not m:
            continue
        cmd = m.group(1)
        if cmd in {"__completions", "__files"}:
            continue
        desc = m.group(2).strip()
        desc = re.sub(r"\s+", " ", desc)
        commands[cmd] = desc

    return commands


def parse_reference_commands():
    commands = {}
    syntax_violations = []
    for ref in sorted(REF_DIR.glob("obsidian-cli-*.md")):
        text = ref.read_text()

        for m in re.finditer(r"^##\s+([a-z0-9:_-]+)\s+-\s+(.+)$", text, re.M):
            commands[m.group(1)] = m.group(2).strip()

        for i, line in enumerate(text.splitlines(), start=1):
            if line.strip().startswith("obsidian ") and "--" in line:
                syntax_violations.append(
                    f"GNU-style flag syntax found at {ref.relative_to(ROOT)}:{i}: `{line.strip()}`"
                )
            if re.search(r"-\s+`--[a-zA-Z]", line):
                syntax_violations.append(
                    f"GNU-style parameter docs found at {ref.relative_to(ROOT)}:{i}: `{line.strip()}`"
                )

    return commands, syntax_violations


def normalize_desc(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\(.*?\)", "", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def tokens(text: str):
    stop = {
        "a",
        "an",
        "the",
        "and",
        "or",
        "to",
        "for",
        "of",
        "in",
        "with",
        "on",
        "all",
        "show",
        "list",
        "get",
    }
    return {t for t in normalize_desc(text).split() if len(t) > 2 and t not in stop}


def compute_drift(help_cmds, ref_cmds):
    drift = []
    for cmd in sorted(set(help_cmds) & set(ref_cmds)):
        h = tokens(help_cmds[cmd])
        r = tokens(ref_cmds[cmd])
        if not h or not r:
            continue
        ratio = len(h & r) / len(h | r)
        if ratio < 0.15:
            drift.append(
                {
                    "command": cmd,
                    "help": help_cmds[cmd],
                    "reference": ref_cmds[cmd],
                    "similarity": round(ratio, 3),
                }
            )
    return drift


def run_audit() -> AuditResult:
    help_commands = parse_help_commands(run_help())
    ref_commands, syntax_violations = parse_reference_commands()

    missing = sorted(set(help_commands) - set(ref_commands))
    extra = sorted(set(ref_commands) - set(help_commands))
    drift = compute_drift(help_commands, ref_commands)

    return AuditResult(
        missing_in_refs=missing,
        extra_in_refs=extra,
        syntax_violations=syntax_violations,
        description_drift=drift,
        command_count_help=len(help_commands),
        command_count_refs=len(ref_commands),
    )


def print_report(result: AuditResult):
    print("Reference Audit")
    print(f"- Commands in `obsidian help`: {result.command_count_help}")
    print(f"- Commands documented by headings: {result.command_count_refs}")

    if result.hard_failures:
        print("- Hard Failures:")
        for issue in result.hard_failures:
            print(f"  - {issue}")
    else:
        print("- Hard Failures: none")

    if result.description_drift:
        print("- Warnings (description drift):")
        for item in result.description_drift:
            print(
                f"  - {item['command']} (similarity={item['similarity']}) | help: {item['help']} | refs: {item['reference']}"
            )
    else:
        print("- Warnings (description drift): none")

    if result.extra_in_refs:
        print("- Warnings (documented but not in local `obsidian help`):")
        print(f"  - {', '.join(result.extra_in_refs)}")
    else:
        print("- Warnings (documented but not in local `obsidian help`): none")

    status = "FAIL" if result.hard_failures else "PASS"
    print(f"- Status: {status}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    args = parser.parse_args()

    result = run_audit()

    if args.json:
        print(
            json.dumps(
                {
                    "command_count_help": result.command_count_help,
                    "command_count_refs": result.command_count_refs,
                    "hard_failures": result.hard_failures,
                    "warnings": {
                        "description_drift": result.description_drift,
                        "documented_not_local_help": result.extra_in_refs,
                    },
                    "status": "fail" if result.hard_failures else "pass",
                },
                indent=2,
            )
        )
    else:
        print_report(result)

    if result.hard_failures:
        sys.exit(2)


if __name__ == "__main__":
    main()

# Contributing

Contributions are welcome! This skill is maintained for the Claude Code community.

## How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b docs/improvement-name` or `git checkout -b fix/command-name`
3. Make your changes
4. Test against Obsidian CLI v1.12.1 or later
5. Submit a pull request with a clear description

## What to Contribute

- Command syntax corrections or clarifications
- New reference examples
- Better command explanations
- Bug fixes in documentation
- Additional common patterns
- Improved formatting or organization

## Guidelines

### Documentation Standards

- Keep parameter format consistent with actual Obsidian CLI usage
- Use the format from [FORMAT_STANDARD.md](FORMAT_STANDARD.md)
- Include minimum 2 examples per command
- Show both basic and advanced usage
- Use relative paths (vault root) for file examples

### Commit Messages

Use semantic commit messages:
- `docs(reference): improve obsidian-cli-files examples`
- `fix(docs): correct property:set syntax in guide`
- `feat(references): add new command examples`

### Testing

Before submitting:
1. Verify command syntax: `obsidian help`
2. Check format consistency with [FORMAT_STANDARD.md](FORMAT_STANDARD.md)
3. Ensure all examples are tested and work
4. Validate file paths and parameter names

### Pull Request Process

1. Update relevant reference files in `references/`
2. Provide clear description of changes in PR
3. Reference any issues addressed
4. Ensure all links and examples work correctly

Version updates are handled automatically by GitHub workflows.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and improve
- Focus on the content, not the person

## Questions?

If you have questions about contributing:
1. Check existing issues and PRs
2. Review the reference files for similar patterns
3. Open a discussion issue with your questions

## Recognition

Contributors will be recognized in:
- Pull request acknowledgments
- Project README (for significant contributions)

Thank you for helping improve this skill!

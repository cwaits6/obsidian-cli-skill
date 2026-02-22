---
type: meeting
context: work
topic: "[engineering, team]"
---
# Standup - February 12

Attendees: Sarah, Mike, James, me

## Updates

**Sarah** — finished the auth migration, PR is up for review. Blocked on staging deploy until infra approves the new IAM role.

**Mike** — debugging flaky test in the payment service. Thinks it's a race condition in the webhook handler. Might need to add a retry with backoff.

**James** — working on the dashboard redesign. Has mockups ready for review, will share in Slack after standup.

**Me** — wrapped up the CI caching improvements (pipeline down from 12min to 4min). Starting on the Helm chart refactor today.

## Action Items

- [ ] Review Sarah's auth migration PR (me, by EOD)
- [ ] James to share dashboard mockups in #design channel
- [ ] Mike to pair with Sarah on the webhook race condition if not resolved by tomorrow
- [ ] Schedule a short demo of CI improvements for the team (me, this week)

## Notes

Sprint ends Friday. We're on track for all committed stories. Retro scheduled for Monday 2pm.

---
type: reference
context: work
topic: "[api, backend]"
---
# API Rate Limiting

Rate limiting controls how many requests a client can make in a given time window. Essential for protecting APIs from abuse and ensuring fair usage.

## Common Algorithms

### Token Bucket

Tokens are added to a bucket at a fixed rate. Each request consumes a token. If the bucket is empty, the request is rejected (or queued). Allows short bursts.

### Sliding Window

Track request counts in a sliding time window (e.g., last 60 seconds). More accurate than fixed windows but requires more storage.

### Fixed Window

Count requests in fixed intervals (e.g., per minute). Simple to implement but allows bursts at window boundaries — a client could make 100 requests at 11:59:59 and 100 more at 12:00:01.

## Response Headers

Standard headers to include:
- `X-RateLimit-Limit` — max requests per window
- `X-RateLimit-Remaining` — requests left in current window
- `X-RateLimit-Reset` — Unix timestamp when the window resets
- `Retry-After` — seconds to wait (on 429 responses)

## HTTP Status

Return `429 Too Many Requests` when limit is exceeded. Include a clear error message:

```json
{
  "error": "rate_limit_exceeded",
  "message": "Too many requests. Retry after 30 seconds.",
  "retry_after": 30
}
```

## Implementation Options

- **Nginx** — `limit_req` module for simple per-IP limiting
- **Redis** — sorted sets or Lua scripts for distributed rate limiting
- **API Gateway** — AWS API Gateway, Kong, or Traefik have built-in support
- **Application-level** — libraries like `express-rate-limit` (Node) or `django-ratelimit` (Python)

## Best Practices

- Rate limit by API key, not just IP (IPs can be shared)
- Use different limits for different endpoints (auth endpoints should be stricter)
- Return informative headers so clients can self-throttle
- Consider allowing burst capacity for well-behaved clients

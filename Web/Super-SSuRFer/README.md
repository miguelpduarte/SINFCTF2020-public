# Super-SSuRFer (Web)

## Description (problem statement)

This cool surfing website might have some flags!

## Summary (solution)

Parameter injection results in SSRF. Use the debug privkey which is always valid by injecting it into the token parameter (token would be: `A&privkey=key`).

## Related resources

https://evanhahn.com/gotchas-with-express-query-parsing-and-how-to-avoid-them/

https://www.surfertoday.com/surfing/the-complete-list-of-beach-flags-and-warning-signals (lol)

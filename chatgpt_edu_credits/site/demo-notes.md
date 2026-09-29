# Workshop demonstrations (September 29, 2026)

Slides are referenced by their on-slide chapter label (06–15), not the footer's page count, which includes the cover.

## Original outputs

- Broad Luna: `dist/demos/ecosystem-broad-luna.html`. Original HTML fragment preserved verbatim inside a standalone page wrapper. Added only document structure and base styling formerly supplied by the conversation host. Optional widget-state integration already handles the absent host.
- Bounded Luna: `dist/demos/ecosystem-bounded-luna.html`, byte-for-byte copy of the supplied result.
- Bounded Sol: `dist/demos/ecosystem-bounded-sol.html`, byte-for-byte copy of the supplied result.
- Untouched originals: `dist/demos/originals/`. Original source paths and hashes: `demo-provenance.json`.
- Exact user prompts: `dist/demos/*-prompt.txt`. Bounded Luna/Sol prompts match apart from a trailing newline.

The broad brief and bounded brief have different learning goals. The broad model was not instructed to implement predator removal. These are illustrative runs, not a controlled experiment or a model benchmark. Do not silently correct simulation behavior when presenting the originals. Scientific validity has not been certified.

## Credit estimates

Source: final cumulative `total_token_usage` from each original completed task. No summing repeated cumulative snapshots. Subtract cached input from input; output already contains reasoning. All three task records identify maximum reasoning. No speed tier was recorded: figures are standard-rate equivalents, not verified account deductions. Fast mode would be 2.5×. No allowance for unlogged/separately billed overhead.

Rates checked September 29, 2026: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu-credit-based-pricing

| Build | Uncached input | Cached input | Output | Standard credits | Displayed elapsed time |
|---|---:|---:|---:|---:|---|
| Broad Luna | 103,848 | 696,320 | 46,866 | 1.019525 | 17m 31s (facilitator) |
| Bounded Luna | 131,039 | 1,913,856 | 66,971 | 1.643199 | 24m 41s (facilitator) |
| Bounded Sol | 47,253 | 518,528 | 26,882 | 11.675790 | 9m 42s (task timestamps) |

Luna per million: 2.5 / 0.25 / 12.5. Sol: 50 / 5 / 250.
The bounded Luna task log spans 24m 48s; retain the facilitator's supplied display duration rather than replacing it silently. The September 25 interrupted starts have no reported token usage; the completed bounded Luna run resumed September 28. Estimates do not include this workshop integration work. Recheck against billing if actual deductions are needed.

## HPC Day planner

New working example based on the supplied HPC-Day-2026-Agenda.pdf, copied to `dist/assets/`. Includes all-day session blocks, printed individual industry-talk times, time/topic filters, selections, and overlap detection. Topic labels are editorial. No fabricated times for sub-talks lacking separate slots. Conflicts exclude travel time. No original-run cost is claimed for this new example.

## Verification

- JavaScript syntax check passed.
- Browser: all revised slide headings render; no page console errors captured; no horizontal overflow at desktop or 390px mobile width.
- Planner: actual 2:30–3:30 panel conflict detected; selected entries persist when topic filter changes.
- Simulators: broad Luna step/reset; bounded Luna prediction/start/pause/reset; Sol prediction/baseline completion/removal/reset exercised in embedded previews.
- Source preservation checked as described above. Full scientific validation and exhaustive simulation testing remain outside these integration checks.

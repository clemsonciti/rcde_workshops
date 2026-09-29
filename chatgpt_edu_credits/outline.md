# Managing Your ChatGPT Edu Credits

## Workshop purpose and format

Help Clemson staff, faculty, and students monitor their ChatGPT Edu credit use and make informed
choices about when additional model capability is worth the credits and human effort involved.

- **Length:** 55 minutes, including eight minutes for questions; adaptable to 45–60 minutes.
- **Delivery:** Zoom, with one facilitator and no breakout rooms.
- **Workshop medium:** Approximately 12 slide-like pages on a ChatGPT Site, with integrated
  activities and an embedded AI assistant powered by an API endpoint.
- **Asynchronous use:** The same pages, examples, explanations, and activities form a self-guided
  workshop. Participants can revisit individual lessons afterward.
- **Prerequisites:** No coding expertise required. Participants may follow along in their Clemson
  account, but can complete the activities using supplied examples without spending credits.
- **Status:** Finalized instructional outline. Demonstration builds, measured comparisons, and
  Clemson interface checks remain production work; no demonstration outcomes are asserted here.

## Intended outcomes

By the end, participants can:

1. Find and interpret their credit usage.
2. Choose a reasonable starting model and reasoning setting.
3. Bound a task and recognize when to escalate.
4. Identify what to do when their allowance is running low.

## Tone and engagement

Speak as Clemson research support staff helping colleagues use a resource effectively. Use concrete
evidence, candid limitations, and practical decisions. Avoid sales language, influencer-style
reveals, patronizing quizzes, and claims that a model is universally superior.

Build engagement through prediction, exploration, and explanation. Participants first make a
reasonable guess, inspect an actual result, and decide what they would do next. Surprises should
come from the evidence rather than a staged success story.

Use ambitious, interesting examples, including interactive tools and coding projects. Participants
need to understand the purpose, inspect the output, and recognize success or failure; they do not
need to understand the implementation. Explain each example's purpose in plain language before
showing it. Keep code and technical build details available as optional material.

Use a conference planner as a recurring example to reduce orientation time. Supplement it with
research, learning, and staff scenarios so that one professional context does not define the
workshop. Do not reduce the examples to routine email tasks merely to make them broadly familiar.

## Agenda

| Minutes | Pages | Segment |
| --- | --- | --- |
| 0–4 | 1–2 | What can you accomplish without spending credits? |
| 4–9 | 3 | Find your allowance and interpret usage |
| 9–15 | 4 | Compare current models, modes, and prices |
| 15–23 | 5–6 | A short request can start substantial work |
| 23–31 | 7–8 | Recognize when to move up a model |
| 31–38 | 9 | Combine models across a workflow |
| 38–43 | 10 | Plan a task with the workshop assistant |
| 43–47 | 11–12 | Running low, practical guidelines, and exit check |
| 47–55 | 12 | Questions |

## 1. What can you accomplish without spending credits?

**Time:** 4 minutes. **Pages:** 1–2.

Introduce the outcomes and show three appealing finished results: a useful explanation, a sourced
research briefing, and an illustration suitable for a presentation. Ask which could be produced
without consuming credits. Reveal the relevant model behavior and included feature allowances.

Suggested opening:

> Some useful things you can do in ChatGPT don't use any credits. Other tasks can use a substantial
> amount from a single request. Today we'll look at how to tell the difference, check your usage,
> and decide when the additional processing is worth it.

The official rate card checked during outline development lists five Deep Research queries and
three image generations per rolling 24-hour period for Edu without consuming credits. Teach the
rolling window rather than implying a midnight reset. Confirm applicability in Clemson before
delivery, and distinguish these feature allowances from image creation inside Work/Codex. [1]

Explain that ordinary Instant responses do not consume credits, but automatic routing to a
reasoning model can incur credits. Do not promise that every request submitted with Instant
selected is credit-free. [1]

**Site activity:** Make a prediction, then reveal the explanation. A follow-up scenario asks
whether another image generation is included given a stated usage history and time window.

**Takeaway:** Check what is included before assuming that an impressive result requires credits.

## 2. Find your allowance and interpret usage

**Time:** 5 minutes. **Page:** 3.

Demonstrate the Clemson workspace check and the usage page, using the current interface. The
source draft gives the path as profile menu → Settings → Usage.

Participants privately locate their monthly limit and usage. Supply an annotated sample display
for people without access or who prefer to observe. Do not collect or display personal balances.

**Site activity:** Interpret a fictional account with 600 of 1,000 credits used and 12 days
remaining.
Identify the 400-credit balance, then choose a next step based on upcoming work. Include two
different upcoming workloads to show why a percentage alone does not determine the decision.

Demonstrate a simple habit: check before a substantial task, check afterward, and use observed
consumption to plan similar work. Explain any reporting delay found during rehearsal; an unchanged
display immediately after a task is not proof that the task used no credits.

**Takeaway:** Use the allowance as planning information, informed by the work ahead.

## 3. Compare current models, modes, and prices

**Time:** 6 minutes. **Page:** 4.

Show the actual Clemson model picker alongside a compact, dated price reference. Explain that
model names, availability, rates, and controls change frequently. Participants should learn where
to check and how to compare rather than memorize a model hierarchy.

Separate fixed-price Chat messages from token-priced Work/Codex tasks. In the current rate card,
Sol's Medium, High, and Extra High Chat settings share the same per-message rate; additional
reasoning can affect consumption in token-priced work. The same model name does not establish
the billing method across interfaces. [1]

Define tokens briefly as units of information processed and produced. Use this calculated example
to make the rate differences concrete without presenting it as a measured task:

| Model | Credits for 20,000 uncached input tokens and 10,000 output tokens |
| --- | ---: |
| Luna | 0.40 |
| Terra | 4.00 |
| Sol | 7.00 |
| Astra | 17.50 |

These are illustrative calculations using standard Work/Codex rates checked September 9, 2026,
excluding additional feature charges. Astra's input rate is 50 times Luna's; its output rate is
about 41.7 times Luna's. The example totals differ by 43.75 times. Different models may consume
different quantities to complete the same task, so this is not a guarantee of 50 times as many
completed tasks. [2]

**Site activity:** Switch models while holding the token quantities fixed. Then reveal a measured
comparison later in the workshop to distinguish rate differences from whole-task differences.

**Takeaway:** Check the current model, mode, and applicable rate before substantial work.

## 4. A short request can start substantial work

**Time:** 8 minutes. **Pages:** 5–6.

### Demonstration: Turn a conference program into an interactive planner

Start with a short request:

> Turn this conference program into an interactive planner that helps me choose sessions and avoid
> schedule conflicts.

Let participants explore a prebuilt result: filter sessions, select a schedule, and see conflict
warnings. Explain that the request initiates extraction, interpretation, interface construction,
and checking. No source-code knowledge is needed to assess the tool.

Compare two versions built offline before the workshop:

- **Broad request:** Leaves scope and optional features open.
- **Bounded request:** Specifies the source, relevant day, required functions, and completion
  checks.

Example bounded request:

> Use only the attached one-day program. Build a planner with topic filters and overlapping-session
> warnings. Check session names and times against the program. Finish when those functions work.

Use the same model and settings for this scope comparison where feasible. Give both versions the
same core acceptance checks. Disclose extra features or other differences that affect the
comparison.

**Site activity:** Explore both finished tools, choose which meets the stated need, and reveal
their measured credits, elapsed time, and remaining defects. Then select sources, required
features, and a stopping point to improve a broad request. AI feedback is optional for this step.

Embed the tools in the workshop Site when practical. Otherwise, provide clearly labeled links to
separately hosted prebuilt Sites and an obvious route back. Provide screenshots or short recordings
as fallbacks. Exploration should not rebuild the tools or require participants to initiate LLM work.

**Takeaway:** Bound the work the request initiates. Prompt length is not a spending estimate.

## 5. Recognize when to move up a model

**Time:** 8 minutes. **Pages:** 7–8.

### Demonstration: A plausible schedule that violates a requirement

Use a conference schedule with interacting constraints: overlapping sessions, travel time, a
required event, and preferences. Provide a short, visible checklist so anyone can judge the result.

Before the workshop, run the same well-specified task with Luna and Sol. Select a documented case
where Luna misses a substantive constraint and Sol satisfies it. Show the failure precisely, such
as recommending two events that cannot both be attended after allowing for travel.

This is a production target, not an established result. Pilot alternative tasks if needed, including
a research-method comparison with conflicting evidence or an analysis with a subtle grouping error.
Do not manufacture a failure by withholding instructions from one model. Disclose that the example
illustrates a specific run, not a universal capability boundary, and note variability seen in
pilots.

**Site activity:** Inspect model-hidden results, identify the violated requirement, and choose a
remedy. Reveal model identities, measured credits, and the checks passed or failed.

Teach a concrete escalation sequence:

1. Identify what is wrong using a requirement or source, rather than stylistic preference alone.
2. Supply missing information or clarify an ambiguous instruction first.
3. If a well-specified task still fails, try a stronger model or suitable reasoning setting.
4. Recheck the replacement against the same requirements.
5. Use human judgment where the unresolved issue requires authority or unavailable evidence.

**Takeaway:** Escalate for an identifiable task demand or failure. Higher spending does not itself
establish correctness.

## 6. Combine models across a workflow

**Time:** 7 minutes. **Page:** 9.

### Demonstration: Plan with Sol or Astra, execute bounded steps with Luna

Return to the planner so participants already understand the desired result. Show three prebuilt
approaches: Luna throughout, a stronger model throughout, and a mixed workflow.

For the mixed workflow:

1. Ask Sol or Astra to resolve difficult requirements and produce an implementation plan.
2. Review assumptions and decisions before execution.
3. Give Luna bounded implementation steps and explicit acceptance checks.
4. Check the finished behavior and escalate specific unresolved problems when necessary.

Show the actual interface controls for switching models in the selected environment. If a new
conversation is needed, demonstrate carrying the plan and required source material across. Merely
asking a model to act like another model is not a model switch.

Use a visible handoff template:

> Objective; agreed decisions; source files; required outputs; acceptance checks; unresolved
questions.

**Site activity:** Assign workflow stages to models and inspect the three finished results. Reveal
total measured credits, time, passed checks, and human corrections for each approach. Include the
cost of planning, handoffs, retries, and verification rather than comparing execution alone.

Explain when mixing models is unnecessary: the task is already simple, the handoff takes more work
than it saves, or execution still requires substantial unresolved judgment.

**Takeaway:** Place additional reasoning where it helps, and preserve the decisions needed for
execution. Mixed workflows must earn their overhead.

## 7. Plan a task with the workshop assistant

**Time:** 5 minutes. **Page:** 10.

Participants choose a supplied scenario or describe a non-sensitive task of their own. Offer varied,
ambitious scenarios rather than assigning them rigidly by job title:

- Turn a small research dataset into an interactive explorer with checks on the analysis.
- Build a study simulator in which changing assumptions changes a visual result.
- Turn an event program into a personalized planner.
- Compare several project proposals against a supplied rubric and expose trade-offs.

Participants make an initial model and scope choice. The assistant asks at most a few clarifying
questions and returns:

- A suggested starting mode, model, and reasoning setting, with a reason.
- A bounded prompt.
- Two or three checks for success.
- A specific escalation trigger.
- When to inspect actual usage.

**Site activity:** Revise one choice after feedback and save or copy the resulting task plan.
Supply a worked example for participants who prefer not to chat with the assistant.

**Takeaway:** Leave with an operational plan for a task you care about.

## 8. Running low and the guidelines to remember

**Time:** 4 minutes, followed by eight minutes of questions. **Pages:** 11–12.

Explain Clemson's confirmed reset behavior, what remains available when a limit is reached, and
the current support/request routes. The source draft describes higher-tier requests for faculty
and staff; establish the student route before delivery. Explain that a higher allowance does not
itself add models or features, consistent with the Clemson draft.

Distinguish model selections and enforced usage controls from advisory prompt wording. Asking
ChatGPT to keep a task inexpensive is not a guaranteed spending cap. An alert is not a stop control.

End with these practical guidelines:

1. **Check your workspace, usage, and available allowance.**
2. **Use included features when they fit the task.**
3. **Check current models and prices in the mode you are using.**
4. **Specify sources, required outputs, and a stopping point.**
5. **Inspect the result before spending more.**
6. **Escalate for a concrete reason; use explicit handoffs when mixing models.**
7. **Compare total credits and remaining human work.**

**Exit activity:** Present a fresh scenario. Ask participants to choose a starting approach,
identify
an escalation trigger, and state when they would check usage. Reveal an explanation and allow more
than one defensible approach where the scenario warrants it.

Keep the summary and links visible during questions. Asynchronous participants receive the same
summary and can ask the assistant follow-up questions.

## Site and assistant requirements

- Use sequential slide-like pages with progress, previous/next controls, and direct lesson links.
- Keep live teaching pages low-text. Put fuller explanations and optional technical details in
  expandable areas for asynchronous use.
- Integrate predictions, result exploration, cost reveals, model-stage selection, and task planning.
- Keep reviewed answer keys, calculations, example results, and basic navigation independent of
  LLM availability. Use the API assistant for individualized feedback and questions.
- Ground factual answers in approved Clemson guidance and dated official references. Clearly
  distinguish measured results, calculated illustrations, and recommendations.
- Do not invent exact future costs or claim access to a participant's balance. Direct participants
  to their usage display; a balance integration is not necessary for this workshop.
- Keep API operating costs separate from participant ChatGPT Edu credit figures. Do not label an
  API-run measurement as observed ChatGPT Edu spending.
- Provide keyboard-accessible activities and text explanations alongside visual results. Make
  tool comparisons usable without coding knowledge, account setup, or posting personal usage.
- Keep the assistant optional during the live session so one facilitator can maintain the pace.

## Prebuilt demonstrations and measurement

Build and host examples offline before delivery. Participants inspect finished tools and outputs
instead of waiting for live generation. Embed them where feasible or link to separate Sites.

Prepare these comparisons:

| Comparison | Evidence to collect |
| --- | --- |
| Broad versus bounded planner request | Same core checks; scope differences; credits and time |
| Luna versus Sol on a difficult task | Specific failure; source/checklist; credits and time |
| Single-model versus mixed workflow | Whole-workflow totals; handoff; quality and human corrections
|

For every displayed run, retain the prompt, source inputs, date, interface, model, reasoning/speed
settings, output, measured credits, elapsed time, and acceptance-check results. Record retries and
human corrections. Account for reporting lag and unrelated concurrent activity when reading usage.
If task-level attribution is unavailable, label the uncertainty instead of implying exact precision.

Use concrete decimal figures only when supported by measurements. Do not reuse illustrative numbers
such as 20.4 versus 2.8 credits as though they were observed. API token-based calculations may
inform
preparation, but are estimates of an equivalent workload, not measured Edu charges.

Keep exploration focused: give participants one or two actions to try in each tool before the cost
reveal. Place additional builds in an optional gallery. Possible gallery items include a data
explorer, visual teaching simulator, and evidence-linked research comparison. These extend audience
relevance without crowding the live agenda.

## Production checks and timing adaptations

Before delivery, refresh model names, rates, allowances, and screenshots against Clemson's actual
workspace. Verify routing behavior, relevant controls, reset timing, reporting delay, and support
routes. Repair the malformed rate-card hyperlink in the source material when preparing Site links.

Rehearse navigation between the workshop and any separately hosted tools. Check that each comparison
makes sense from the finished result without reading code. Confirm the assistant's recommendations
and keep static fallbacks available.

- **45 minutes:** Reduce the planner exploration by two minutes, present the mixed-model example
  without its activity to save three minutes, shorten personal practice by two minutes, and retain
  five minutes for questions. Keep the summary and exit check.
- **55 minutes:** Use the agenda above.
- **60 minutes:** Add five minutes for participant examples and questions, not another required
  topic.

## Sources and refresh notes

Product facts were checked during outline development on September 9, 2026. Refresh before delivery.
Clemson-specific arrangements come from the supplied draft and require local confirmation.

- Clemson draft: *Understanding ChatGPT Edu Models and Credit Use.docx*, supplied by the workshop
  organizer. Planned webpage path: `ai/guidelines/chatgpt-credit-use`.
- [1] [OpenAI credit-based rate card][rate-card]: included Edu feature allowances, fixed Chat rates,
  routing, and the distinction between Chat and Work/Codex pricing.
- [2] [OpenAI pricing documentation][pricing]: token-rate comparison and usage factors.
- [OpenAI usage and cost guidance][usage]: credits, alerts, and usage controls.
- [OpenAI Sites documentation][sites]: Site delivery capabilities; recheck availability and limits.

[rate-card]: https://help.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterpriseedu
[pricing]: https://learn.chatgpt.com/docs/pricing
[usage]: https://learn.chatgpt.com/docs/enterprise/chatgpt-work-usage-and-cost
[sites]: https://learn.chatgpt.com/docs/sites

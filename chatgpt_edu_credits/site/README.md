# ChatGPT Edu credit workshop Site

A static, interactive slide draft implementing the workshop outline in `../outline.md`.
Open through the registered Sites project or serve `dist/` locally with an HTTP server.

## Editing

- `dist/app.js`: slide content, notes, citations, and activities.
- `dist/styles.css`: Clemson-themed layout and responsive styles.
- `dist/index.html`: shared navigation and assistant dialog shell.
- `.openai/hosting.json`: registered Site identity and static output directory.

The 16 slides use hash links (`#1` through `#16`). Responses remain in the current browser session.
The task-plan activity downloads a text file; no data is sent to an API.
The assistant is explicitly a placeholder.

## Before workshop delivery

Replace the marked demonstration slots with the organizer's prebuilt tools and recorded results.
The schedule exercise is a constructed teaching example, not a Luna/Sol performance claim.
Record actual credits, settings, inputs, quality checks, and human corrections for each comparison.
Confirm Clemson-specific reset behavior, current model controls, and student support routes.
Refresh the linked rate card and the explicitly dated rate illustration.

## Validation

Checked all 16 slides at desktop and mobile widths. Verified quiz feedback, model-rate selection,
schedule conflict detection, state across slide navigation, the assistant dialog, and plan download.
No API service or live account usage integration is implemented.

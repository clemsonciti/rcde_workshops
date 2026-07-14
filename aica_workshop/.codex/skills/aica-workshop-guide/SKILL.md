---
name: aica-workshop-guide
description: Use only when the user's prompt explicitly invokes the `aica-workshop-guide` skill. Use for the AI Code Assistants for HPC on Palmetto workshop when a participant or instructor asks for workshop orientation, workshop terminology, logistics, transfer commands, workshop file locations, Codex setup in the workshop context, or to advance, reset, restore, or roll back workshop files to a checkpoint.
metadata:
  short-description: Guide and checkpoint helper for the AICA Palmetto workshop
---

# AICA Workshop Guide

This skill is a lightweight helper for the "AI Code Assistants for HPC on
Palmetto" workshop. It should orient users, explain workshop terms at a
participant-friendly level, provide workshop logistics, and manage checkpoint
state, not do the labs for them. It should only be used when the user explicitly
invokes the `aica-workshop-guide` skill.

## Core Rules

- Do not assume this skill is active for normal participant lab work.
- Do not use checkpoint assets as answer keys for lab/debugging help.
- If a user asks for help solving a lab task, inspect only the current working
  files and evidence they provide. Do not compare against future checkpoints.
- Use checkpoint assets only when the user explicitly asks to advance, reset,
  restore, or roll back to a checkpoint.
- For Palmetto-specific facts, commands, modules, Slurm behavior, storage,
  policy, accounts, partitions, reservations, or Codex-on-Palmetto setup, use
  the separate `palmetto-docs` skill when available. (Only available on Palmetto; not available when Codex is running locally rather than on Palmetto.)

## Workshop Locations

- Shared workshop source: `/project/rcde/cehrett/aica_workshop/`
- Expected participant copy: a personal copy of the workshop directory, usually
  under the participant's home directory.
- Main files participants edit:
  - `mc_sim/simulate.py`
  - `scripts/run_sim.py`
  - `scripts/run_sim.sbatch`
  - later, benchmark files under `scripts/`

## Workshop Logistics and File Transfers

- Sign-in sheet: <https://docs.google.com/spreadsheets/d/1LwJh9c6yNG66Ir4z4jK_zXwgabMXwzOeEcij41uaFeU/edit?usp=sharing>
- Post-workshop survey: <https://forms.gle/AiBKia82PbEKouRM8>

When a participant is in the destination directory on their laptop, give these
commands. They should replace `<username>` with their Palmetto username.

```bash
# Download a personal copy of the workshop source into the current directory.
scp -r <username>@login.palmetto.clemson.edu:/project/rcde/cehrett/aica_workshop .

# Download the Lab 3 results directory into the current directory on the laptop.
scp -r <username>@login.palmetto.clemson.edu:~/aica_workshop/results .
```

The second command assumes the participant's workshop copy is
`~/aica_workshop`; adjust that path if they placed their copy elsewhere. Explain
that `scp` securely copies files over SSH and that the final `.` means "the
current directory."

## Participant-Friendly Terms

When participants ask about a workshop term, give a concise, plain-language
definition first, then relate it to the Monte Carlo example when useful. Avoid
assuming prior HPC or Python experience.

- **Vectorize / vectorized:** Rewrite work on many values so an array library
  performs it in bulk, instead of a Python loop handling one value at a time.
  Here, it means generating and testing many random points at once.
- **NumPy:** A Python library for efficient arrays and numerical calculations.
  It is often what makes vectorized Python code fast.
- **Parallelize / parallelized:** Split independent work across multiple CPU
  cores so it can run at the same time. In this workshop, separate groups of
  random samples can be computed by different workers.
- **Benchmark:** Measure how long a program or configuration takes under
  controlled, comparable conditions. A benchmark is evidence for a performance
  claim, not just one lucky run.
- **Core:** One processing unit in a CPU that can execute work. A multi-core job
  can use several cores at once.
- **Worker:** A program process assigned a portion of the work; workers commonly
  run on separate CPU cores.
- **Sample:** One random trial in the Monte Carlo simulation. More samples
  usually make the estimate more reliable, but require more work.
- **Monte Carlo method:** A technique that estimates an answer by running many
  random trials. This workshop estimates pi from random points inside a square.
- **Slurm:** The scheduler that allocates cluster resources and runs submitted
  jobs on Palmetto.

## Workshop Flow

Use this section to answer orientation questions like "what is Lab 1?" or
"which file should I edit?" Keep answers task-focused. Do not reveal future
checkpoint implementation details.

### Setup

Participants should already have Palmetto SSH access, Palmetto onboarding,
ChatGPT EDU workspace access, and local Codex CLI installed. In the workshop
they load and log into Codex on Palmetto, copy workshop files to their laptop,
and copy workshop files to their Palmetto home directory. For Palmetto Codex
login details, use `palmetto-docs`.

### Running Example

The workshop uses a small Monte Carlo pi estimation project:

- package code: `mc_sim/`
- command-line runner: `scripts/run_sim.py`
- Slurm submission script: `scripts/run_sim.sbatch` (introduced after Lab 1)
- benchmark files are introduced later in Lab 3

### Demo 1

Goal: show local development with an AI code assistant while keeping changes
small and validated.

Tasks demonstrated:

- inspect `mc_sim/simulate.py` and run the baseline
- diagnose why the initial pi estimate is wrong
- add docstrings and clearer names without changing intended behavior
- refactor into smaller functions while keeping the CLI stable
- add a vectorized implementation

### Lab 1

Goal: participants improve the Python code themselves with assistant support.

Participant tasks:

- make the script optionally multicore
- update both the simulation module and command-line runner as needed
- add a `--num-workers` style optional argument that defaults to 1
- add a warning when `n_samples` is too low for a reliable estimate
- verify that high sample counts give a reasonable pi estimate
- verify that low sample counts produce the warning

### Demo 2

Goal: demonstrate a repeatable Slurm debugging loop with Codex CLI on Palmetto.

Tasks demonstrated:

- submit a Slurm job that fails unexpectedly
- locate and read the job output or error log
- ask Codex for ranked hypotheses and a targeted fix
- apply one small fix
- rerun and interpret the result
- verify Palmetto-specific claims with `palmetto-docs`

### Lab 2

Goal: participants debug and improve the Slurm submission workflow.

Participant tasks:

- edit `scripts/run_sim.sbatch` and, if needed, related Python files
- make the job use a worker count equal to the cores allocated by Slurm
- verify any Slurm environment variables and other suspicious script details
- verify core usage with `jobperf [job id]`
- explain what changed and why it improved the run

### Lab 3

Goal: use an assistant for bounded benchmarking boilerplate and evaluate
performance with evidence.

Participant tasks:

- draft a benchmark Python script and a benchmark Slurm script
- compare vectorized vs non-vectorized execution
- compare single-core vs multicore execution
- run four configurations with 12 cores and 1M samples
- run each configuration ten times and report mean/std runtime
- sweep worker counts from 1 through 12 with 5M samples
- produce a markdown timing table and a runtime plot
- understand the generated code well enough to explain it

### Prompting Practices

Encourage participants to ask for small, reviewable changes; provide the file,
command, and log; request ranked hypotheses; request validation commands; and
change one thing at a time.

## Checkpoints

Checkpoint files live under `assets/checkpoints/` in this skill. The alias
manifest is `assets/checkpoints/manifest.json`.

Use `scripts/checkpoint.py` for checkpoint operations. The user should not need
to learn this command; run it internally when they ask in natural language.

Typical requests:

- "Advance me to after Lab 1."
- "Reset me to the start of Demo 2."
- "Put me at checkpoint v4."
- "Roll back to before Lab 3."

Before applying a checkpoint, the script archives replaced files under
`.workshop_archives/` in the workshop repo. It preserves relative paths.

## Checkpoint Map

- `v1` / `start`: original baseline before Demo 1.
- `v2` / `after-demo-1`: after Demo 1, before Lab 1.
- `v3` / `after-lab-1` / `before-demo-2`: after Lab 1, before Demo 2.
- `v4` / `after-demo-2` / `before-lab-2`: after Demo 2, before Lab 2.
- `v5` / `after-lab-2` / `before-lab-3`: after Lab 2, before Lab 3.
- `v6` / `after-lab-3`: after Lab 3.

## Safe Workflow

For checkpoint requests:

1. Resolve the requested checkpoint or alias.
2. If ambiguous, ask one concise clarifying question.
3. Run a dry run if the user asks what would change.
4. Apply the checkpoint only after an explicit request to advance/reset/restore.
5. Report the checkpoint applied and the archive directory.

For lab/debugging requests:

1. Work from current files, logs, and command output only.
2. Use small, reviewable changes.
3. Use `palmetto-docs` for Palmetto-specific claims.
4. Do not reveal or copy future checkpoint solutions.

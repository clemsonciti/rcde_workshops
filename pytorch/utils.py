from IPython.display import display, Markdown, clear_output
import os
import json
import glob
import time
import pandas as pd

def create_answer_box(question, question_id, shared_folder='/project/rcde/cehrett/pytorch_intro/responses'):
    user_id = os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

    display(Markdown(f"{question}"))
    display(Markdown("**Enter your response below. Press Enter on an empty line to finish.**"))

    response = _collect_multiline_input().strip()
    if not response:
        print("No answer saved because the response was empty.")
        return

    data = {
        'user_id': user_id,
        'question': question,
        'response': response
    }

    os.makedirs(shared_folder, exist_ok=True)

    filename = f"{shared_folder}/{user_id}_{sanitize_filename(question_id)}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Answer saved to {filename}\n")


def _collect_multiline_input():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        if line == '':
            break

        lines.append(line)

    return '\n'.join(lines)

def sanitize_filename(text):
    return ''.join(c if c.isalnum() else '_' for c in text)

def show_responses(question_id, shared_folder='/project/rcde/cehrett/pytorch_intro/responses',
                   live=False, refresh_seconds=5):
    """Display responses for a question, optionally refreshing in-place."""
    question_ids = _normalize_question_ids(question_id)

    if live:
        _show_responses_live(question_ids, shared_folder, refresh_seconds)
        return

    for qid in question_ids:
        records = _load_response_records(qid, shared_folder)
        _render_responses(qid, records)


def _show_responses_live(question_ids, shared_folder, refresh_seconds):
    last_snapshot = None

    try:
        while True:
            responses_by_question = {
                qid: _load_response_records(qid, shared_folder)
                for qid in question_ids
            }
            snapshot = json.dumps(responses_by_question, sort_keys=True)

            if snapshot != last_snapshot:
                clear_output(wait=True)
                _render_live_header(question_ids, refresh_seconds)
                for qid in question_ids:
                    _render_responses(qid, responses_by_question[qid])
                last_snapshot = snapshot

            time.sleep(refresh_seconds)
    except KeyboardInterrupt:
        clear_output(wait=True)
        responses_by_question = {
            qid: _load_response_records(qid, shared_folder)
            for qid in question_ids
        }
        _render_live_header(question_ids, refresh_seconds, stopped=True)
        for qid in question_ids:
            _render_responses(qid, responses_by_question[qid])


def _normalize_question_ids(question_id):
    if isinstance(question_id, str):
        return [question_id]

    return list(question_id)


def _render_live_header(question_ids, refresh_seconds, stopped=False):
    question_label = ', '.join(f"`{qid}`" for qid in question_ids)

    if stopped:
        display(Markdown(f"**Live responses stopped for {question_label}.**"))
        return

    display(Markdown(
        f"**Live responses for {question_label}**  \n"
        f"Refreshing every {refresh_seconds} seconds. Interrupt the kernel to stop."
    ))


def _load_response_records(question_id, shared_folder):
    qid = sanitize_filename(question_id)          # ensure we use the same sanitising rule
    pattern = os.path.join(shared_folder, f'*_{qid}.json')
    files = glob.glob(pattern)

    records = []
    for fp in files:
        try:
            with open(fp, 'r') as f:
                records.append(json.load(f))
        except Exception as e:
            print(f"⚠️  Skipped {fp}: {e}")

    return records


def _render_responses(question_id, records):
    if not records:
        display(Markdown(f"**No responses yet for `{question_id}`.**"))
        return

    df = pd.DataFrame(records).loc[:, ['user_id', 'question', 'response']]
    question = df.question[0]
    df.sort_values('user_id', inplace=True)

    display(Markdown(f"#### {question}\n (ID: {question_id}, {len(df)} submitted)"))
    display(
        df[['user_id', 'response']].style
        .hide(axis='index')
        .set_properties(subset=['response'], **{
            'white-space': 'pre-wrap',
            'text-align': 'left',
            'vertical-align': 'top'
        })
        .set_properties(subset=['user_id'], **{
            'vertical-align': 'top'
        })
    )

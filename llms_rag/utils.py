import ipywidgets as widgets
from IPython.display import display, clear_output, Markdown
import os
import json
import glob
import pandas as pd

def create_answer_box(question, question_id, shared_folder='/project/rcde/cehrett/python_sklearn/'):
    user_id = os.environ.get('USER') or os.environ.get('USERNAME') or 'unknown_user'

    # Display the question as a Markdown header
    display(Markdown(f"{question}"))

    answer_box = widgets.Text(
        value='',
        placeholder='Type your answer here',
        description='',
        disabled=False,
        layout=widgets.Layout(width='500px')
    )

    submit_button = widgets.Button(
        description='Submit',
        button_style='success'
    )

    output = widgets.Output()

    def handle_submit(b):
        with output:
            clear_output()
            response = answer_box.value.strip()
            if not response:
                print("Please enter a non-empty answer.")
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

            print(f"Answer saved to {filename}")

    submit_button.on_click(handle_submit)
    display(answer_box, submit_button, output)

def sanitize_filename(text):
    return ''.join(c if c.isalnum() else '_' for c in text)

def show_responses(question_id, shared_folder='/project/rcde/cehrett/python_sklearn/'):
    """
    Scan `shared_folder` for all files that end with _{question_id}.json,
    read them, and display a nicely formatted table of user_id → response.
    """
    qid = sanitize_filename(question_id)          # ensure we use the same sanitising rule
    pattern = os.path.join(shared_folder, f'*_{qid}.json')
    files = glob.glob(pattern)

    if not files:
        display(Markdown(f"**No responses yet for `{question_id}`.**"))
        return

    records = []
    for fp in files:
        try:
            with open(fp, 'r') as f:
                records.append(json.load(f))
        except Exception as e:
            print(f"⚠️  Skipped {fp}: {e}")

    # Build a DataFrame for pretty display
    df = pd.DataFrame(records).loc[:, ['user_id', 'question', 'response']]
    question = df.question[0]
    df.sort_values('user_id', inplace=True)

    display(Markdown(f"#### {question}\n (ID: {question_id}, {len(df)} submitted)"))
    display(df[['user_id','response']].style.hide(axis='index'))


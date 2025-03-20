import torch
import textwrap

# Set a system prompt to be prepended to the user prompt.
# This is a simple example, but you could use a more complex system prompt.
system_prompt = "Solve the following math problem."

wrapper = textwrap.TextWrapper(width=80)

# Define a function to format the prompt and apply loss masking.
# This function builds a full text with a "User:" prompt and an "Assistant:" response.
# It then computes which tokens belong to the prompt (to be masked in the loss)
# The function assumes that each example has a `problem` and a `solution`, which is true for the MATH-500 dataset.
def tokenize_and_mask(example, tokenizer, max_length=1024, system_prompt=system_prompt):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": example['problem']},
        {"role": "assistant", "content": example['solution']}
    ]

    # Tokenize the prompt (without special tokens) to know its length.
    prompt_ids = tokenizer.apply_chat_template(
        messages[:-1],
        return_tensors='pt',
        return_dict=True,
        add_special_tokens=False
    )["input_ids"][0]  # Remove batch dimension

    # Tokenize the full conversation (with special tokens and truncation)
    tokenized = tokenizer.apply_chat_template(
        messages,
        truncation=True,
        max_length=max_length,
        add_special_tokens=True,
        return_tensors="pt",
        return_dict=True,
    )
    input_ids = tokenized["input_ids"][0]  # Remove batch dimension
    attention_mask = tokenized["attention_mask"][0]  # Remove batch dimension

    # Create labels as a copy of input_ids.
    labels = input_ids.clone()  
    prompt_length = len(prompt_ids)
    labels[:prompt_length] = torch.tensor([-100] * prompt_length)

    return {"input_ids": input_ids, "labels": labels, "attention_mask": attention_mask}

def tokenize_for_generation(example, tokenizer):
    # Build a prompt with the system and user messages only, for generation (not for training)
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": example['problem']}
    ]

    # Tokenize the full conversation
    tokenized = tokenizer.apply_chat_template(
        messages,
        truncation=True,
        add_special_tokens=True,
        return_tensors="pt",
        return_dict=True,
        add_generation_prefix=True, # Doesn't seem to work with Qwen2.5-0.5B-Instruct
    )

    generation_prefix = '<|im_start|>assistant\n'
    generation_prefix_tokenized = tokenizer(generation_prefix, return_tensors='pt')["input_ids"]
    
    input_ids = tokenized["input_ids"][0]  # Remove batch dimension
    attention_mask = tokenized["attention_mask"][0]

    # Unsqueeze generation_prefix_tokenized to match dimensions
    generation_prefix_tokenized = generation_prefix_tokenized.squeeze(0)

    # Add the generation prefix to the input_ids
    input_ids = torch.cat([input_ids, generation_prefix_tokenized], dim=0)
    attention_mask = torch.cat([attention_mask, torch.ones_like(generation_prefix_tokenized)], dim=0)

    return {"input_ids": input_ids, "attention_mask": attention_mask}

def generate_and_print(sample_dataset, sample_dataset_tokenized, model, tokenizer):
    outputs = []
    for sample in sample_dataset_tokenized:
        input_ids_batch = sample['input_ids'].unsqueeze(0).to(model.device)
        attention_mask_batch = sample['attention_mask'].unsqueeze(0).to(model.device)

        generated_ids = model.generate(
            input_ids=input_ids_batch,
            attention_mask=attention_mask_batch,
            max_new_tokens=512,  # change as needed
        )
        generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
        outputs.append(generated_text)

    for i, sample in enumerate(sample_dataset_tokenized):
        # Retrieve the original problem and solution from the un-tokenized dataset
        original = sample_dataset[i]
        print("Problem:")
        print(wrapper.fill(original["problem"]))
        print("\nTrue Solution:")
        print(wrapper.fill(original["solution"]))
        print("\nModel's Solution:")
        model_output = outputs[i].split("assistant\n")[-1].strip()
        print(wrapper.fill(model_output))
        print("\n" + "-" * 80 + "\n")

# Create a simple data collator
def data_collator(features, tokenizer):
    input_ids = torch.nn.utils.rnn.pad_sequence(
        [f["input_ids"].clone().detach() for f in features],
        batch_first=True,
        padding_value=tokenizer.pad_token_id,
    )
    labels = torch.nn.utils.rnn.pad_sequence(
        [f["labels"].clone().detach() for f in features],
        batch_first=True,
        padding_value=-100,
    )
    attention_mask = torch.nn.utils.rnn.pad_sequence(
        [f["attention_mask"].clone().detach() for f in features],
        batch_first=True,
        padding_value=0,
    )
    return {
        "input_ids": input_ids,
        "labels": labels,
        "attention_mask": attention_mask,
    }


# This last function is just to help display powerpoint slides inline in the Jupyter notebooks.
from IPython.display import display, HTML

def display_pdf(pdf_filename, folder="slides", width=1000, height=800):
    """
    Display a PDF in an iframe with a fallback message if the PDF fails to load.

    Parameters:
    - pdf_filename (str): The filename of the PDF (e.g., "Slides1.pdf").
    - folder (str): The folder where PDFs are stored (default: "slides").
    - width (int): The width of the iframe (default: 1000).
    - height (int): The height of the iframe (default: 800).
    """

    pdf_path = f"{folder}/{pdf_filename}"

    html_code = f"""
    <div id="pdf-container">
        <iframe src="{pdf_path}" width="{width}" height="{height}" onerror="showFallback()" id="pdf-frame"></iframe>
    </div>
    <div id="fallback-message" style="display: none;">
        <p><strong>⚠️ Unable to load PDF.</strong></p>
        <p>Please <a href="{pdf_path}" target="_blank">click here</a> to open it in a new tab.</p>
    </div>
    <script>
        function showFallback() {{
            document.getElementById("pdf-container").style.display = "none";
            document.getElementById("fallback-message").style.display = "block";
        }}

        // Timeout at 1.5s
        setTimeout(function() {{
            var iframe = document.getElementById("pdf-frame");
            if (!iframe.contentDocument || iframe.contentDocument.body.childElementCount === 0) {{
                showFallback();
            }}
        }}, 1500);
    </script>
    """

    display(HTML(html_code))

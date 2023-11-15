from datasets import load_dataset
from torch.utils.data import DataLoader, default_collate
from transformers import AutoTokenizer

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

class PubMedDataset:
    def __init__(
        self,
        root: str,
        max_tokens: int = 512,
        tokenizer_model: str = "dmis-lab/biobert-base-cased-v1.2",
    ):
        """
        Create a pytorch dataset suitable for LLM training. This class uses the huggingface dataset
        class to load the text data. It also returns dataloader objects for use with native
        pytorch code. Batches will be truncated to `max_tokens` or to the size of the shortest
        document in the batch.

        Args:
        - root (str): the file path to a directory containing pubmed train.txt and test.txt files
        - max_tokens (int): the maximum number of tokens allowed in a sequence.
        - tokenizer_model (str): the model 
        """

        self.root = root
        self.max_tokens = max_tokens
        self.train_test_files = {"train": root + "train.txt", "test": root + "test.txt"}
        self.dataset = load_dataset("text", data_files=self.train_test_files)

        self.tokenizer_model = tokenizer_model
        self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer_model)

    def get_dataloader(self, split, **dataloader_kwargs):
        """
        Return a pytorch dataloader for the specified `split`. Accepts any arguments
        accepted by DataLoader except for `collate_fn`.
        """
        return DataLoader(
            self.dataset[split], collate_fn=self._custom_collate, **dataloader_kwargs
        )

    def decode_batch(self, batch_input_ids):
        """
        Returns the natural language text for a batch of token input ids.
        """
        return [self.tokenizer.decode(doc) for doc in batch_input_ids]

    def _clean_and_tokenize(self, text_batch):
        # get rid of unwanted opening/closing quotes
        text_batch = [t[1:-1] for t in text_batch]

        # tokenize
        text_batch = self.tokenizer(
            text_batch,
            padding=True,
            truncation=True,
            max_length=self.max_tokens,
            return_tensors="pt",
        )

        return text_batch

    def _custom_collate(self, batch_list):
        batch = default_collate(batch_list)
        batch["text"] = self._clean_and_tokenize(batch["text"])

        return batch["text"]

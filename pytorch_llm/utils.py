import torch
import torch.nn.functional as F


def masked_cross_entropy(logits, targets, mask):
    """
    Args:
    - logits: The next token prediction logits. Last element removed. Shape (N, V, L-1)
    - targets: Ids of the correct next tokens. First element removed (N, L-1)
    - mask: the attention mask tensor. First element removed (N, L-1)
    """
    token_loss = F.cross_entropy(logits, targets, reduction="none")

    # total loss zeroing out the padding terms
    total_loss = (token_loss * mask).sum() 

    # average per-token loss
    num_real = mask.sum()
    mean_loss = total_loss / num_real

    return mean_loss


def test(model, dataloader, reporting_interval=5):
    model.eval()
    for ix, batch in enumerate(dataloader):
        x = batch["input_ids"][:, :-1].to("cuda")  # remove last
        targets = batch["input_ids"][:, 1:].to("cuda")  # remove first
        mask = batch["attention_mask"][:, 1:].to("cuda")  # remove first

        with torch.no_grad():  # turn off gradient tracking since this is for evaluation
            logits = model(x).permute(0, 2, 1)
            loss = masked_cross_entropy(logits, targets, mask)

        if ix % reporting_interval == 0:
            print(f"Batch {ix} testing loss: {loss.item()}")


def train(model, dataloader, optimizer, reporting_interval=20):
    model.train()
    for ix, batch in enumerate(dataloader):
        x = batch["input_ids"][:, :-1].to("cuda")  # remove last
        targets = batch["input_ids"][:, 1:].to("cuda")  # remove first
        mask = batch["attention_mask"][:, 1:].to("cuda")  # remove first

        logits = model(x).permute(0, 2, 1)
        loss = masked_cross_entropy(logits, targets, mask)

        # do the gradient optimization stuff
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if ix % reporting_interval == 0:
            print(f"Batch {ix} training loss: {loss.item()}")


def generate(model, idx, max_new_tokens):
    model.eval()
    """
    Recursively generate a sequence one token at a time
    """
    # idx is (N, L) array of indices in the current context
    for _ in range(max_new_tokens):
        # get the predictions
        with torch.no_grad():
            logits = model(idx)  # [N, L, V]

        # last time step is prediction for next token
        logits = logits[:, -1]  # becomes (N, V)

        # apply softmax to get probabilities
        probs = F.softmax(logits, dim=-1)  # (N, V)

        # sample from the distribution
        idx_next = torch.multinomial(probs, num_samples=1)  # (N, 1)

        # append sampled index to the running sequence
        idx = torch.cat((idx, idx_next), dim=1)  # (N, L+1)
        
    return idx

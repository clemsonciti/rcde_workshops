.


# Retrieval-Augmented Generation (RAG): Enhancing LLMs for Research Applications

**Workshop Overview:** This two-day hands-on workshop will introduce graduate students from diverse disciplines to Retrieval-Augmented Generation (RAG), a technique that combines **Large Language Models (LLMs)** with **document retrieval** to create powerful research assistants. We will use an open-source 7B-parameter LLM (e.g. **Qwen-7B** or a similar model) with access to an NVIDIA A100 GPU, and leverage Python libraries such as **Hugging Face Transformers**, **Sentence-Transformers**, **FAISS**, and **NetworkX**. Participants will learn RAG fundamentals on Day 1 and explore advanced customizations on Day 2. Each module below contains explanatory Markdown, code snippets (or pseudocode) in Python, interactive prompts (`create_answer_box`) for engagement, and suggestions for images/diagrams to reinforce concepts. Prior sessions on LLMs or PyTorch are **not required** (though we will point out connections where relevant). By the end, you’ll understand how to build and tailor RAG pipelines for research applications, including key best practices and recent advancements.

## Day 1: Fundamentals of RAG

### Module 1: Introduction to RAG

**1.1 What is RAG and Why Do We Need It?**
Retrieval-Augmented Generation (RAG) is a design pattern that combines a pretrained Large Language Model with an external data retrieval system to generate answers **grounded in relevant external knowledge**. In essence, RAG-enabled LLMs can "consult" a knowledge source (such as a document database or corpus of papers) before answering a question. This **fills a crucial gap** in standard LLMs: while an LLM’s billions of parameters encode general linguistic and factual patterns, the model might not know **specific, up-to-date, or niche information** that wasn’t in its training data. By retrieving documents on-the-fly related to a user’s query, RAG enables the LLM to produce more accurate and *current* responses.

Some motivations for using RAG in research applications include:

* **Reducing Hallucinations:** LLMs often produce confident answers that are factually incorrect (hallucinations) when they lack domain knowledge. RAG mitigates this by providing factual context from real documents, which **grounds the model’s output in evidence**. The LLM is less likely to “make up” an answer if it can reference actual source text.
* **Extending Knowledge Beyond Training Data:** Even a powerful model (GPT-style or otherwise) has a fixed training cutoff and may not include specialized or recent research findings. RAG allows *querying an external knowledge base* (e.g. a library of scientific articles or company data) so the model can incorporate **new data outside its original training**. This is far more efficient than continually retraining or fine-tuning the LLM on new documents.
* **Maintaining Trust with Sources:** Especially in academic or scientific settings, it’s important to **cite sources and give provenance** for claims. A RAG system can return not just an answer but also the source documents or citations that support that answer. This transparency builds user trust, much like footnotes in a research paper.
* **Ease and Cost-Efficiency:** Augmenting a frozen LLM with retrieval is relatively easy to implement and *cheaper than large-scale fine-tuning*. Lewis et al. (2020), who coined the term RAG, noted that you can often implement a basic RAG pipeline in only a few lines of code. You avoid the expense of updating model weights; instead, you maintain an external database of knowledge that can be **hot-swapped or updated on the fly**. This makes RAG attractive for rapidly-changing fields where new literature appears regularly.

&#x20;*Figure: A typical Retrieval-Augmented Generation pipeline.* **The user’s query** is first passed to a **retrieval module** which finds the most relevant documents from an external knowledge source (database or index). The retrieved texts (often called *contexts* or *evidence chunks*) are then fed into the **LLM** along with the original query, guiding the model to generate a **final answer grounded in those documents**. In more advanced systems, a secondary **re-ranking** model (e.g. a cross-encoder) may refine which documents are selected, and a **hybrid search** (combining semantic vectors with keyword search) can improve retrieval quality. The end result is an answer that the LLM **could not produce as accurately alone**, now enriched by domain-specific information.

**1.2 Examples and Use Cases:**

* *Open-Domain Question Answering:* The classic example of RAG is a QA system like a **research assistant**. Ask, *“What were the results of the latest climate change economic impact study?”* A RAG pipeline can fetch the relevant report or paper and have the LLM summarize or extract the answer. Without retrieval, the LLM might not recall the specific data point (especially if it was published after the model’s training). With RAG, the model can quote the paper’s findings (e.g. *“global GDP loss of \~10% at 3°C warming”* from the document).
* *Enterprise or Academic Chatbots:* Many organizations build chatbots that can answer questions about **internal documents** – for example, a university library chatbot that uses RAG to navigate **research articles, theses, or policy documents** and provide answers with citations. This ensures that the chatbot’s answers are *grounded in the institution’s actual content* and can be verified by users.
* *LLM as a “Clerk”:* RAG has been analogized to giving an LLM access to a textual **database or library** – similar to a judge asking a clerk to fetch relevant case law. The LLM (judge) handles the language and reasoning, but relies on retrieval (clerk) to supply domain knowledge or case-specific facts. This pattern is widely useful whenever we want the generative model to stay factual and **domain-aware**.

**1.3 RAG vs. Other Approaches:**
It’s helpful to distinguish RAG from two related approaches:

* *Fine-Tuning LLMs:* Fine-tuning means training the LLM on new data to internalize that knowledge. By contrast, RAG keeps the LLM fixed and *augments its input*. Fine-tuning a large model on a big corpus of papers can be very costly and time-consuming, whereas RAG can utilize the same corpus **in real-time at inference** with much less compute. Fine-tuning also increases the model’s size (and risk of overfitting), whereas RAG offloads storage to an external index.
* *Classical IR or Search Systems:* Traditional search engines (like academic databases or Google Scholar) retrieve documents based on keywords, but leave the task of reading and synthesizing to the user. RAG blends search with generation: the system not only fetches documents but also **interprets and summarizes them** to directly answer the user’s query. In short, RAG moves from *“retrieve documents”* to *“retrieve **and** read then answer”*, automating the reasoning from retrieved text to final answer.

> **❓ Quick Check:** *In your own words, what is one key advantage of using RAG for a research assistant, as opposed to using an LLM alone?*
> *(Think about accuracy, up-to-dateness, or the ability to cite sources.)*
> `create_answer_box("📝 **Your Answer:** One key advantage of RAG is... ", id="mod1_advantage_rag")`

### Module 2: Document Retrieval and Embeddings

To build a RAG system, we first need the ability to **fetch relevant documents** given a query. This involves two core concepts: *document indexing* (storing representations of documents for quick search) and *embeddings* (vector representations of text that enable semantic similarity search).

**2.1 From Keywords to Vectors:** Traditional information retrieval relied on keyword matching and statistical scoring (e.g. TF-IDF or BM25). For example, if you search for "climate change impacts", a keyword-based engine finds documents containing those terms. However, keywords can be limiting – different words can express the same concept (synonyms), and exact matches may miss relevant documents that use different phrasing. Modern RAG pipelines instead use **dense vector retrieval**: both queries and documents are converted into high-dimensional numeric vectors that capture **semantic meaning**, and search is performed by finding nearest vectors rather than exact word matches. This enables finding conceptually related text even if vocabulary differs (e.g. "global warming effects" could match "climate change impacts" because their vectors are close in space, even if no keywords overlap).

**2.2 What are Embeddings?**
An *embedding* is a numeric representation of an object (text, image, etc.) such that semantically similar objects have nearby representations in the vector space. For text, an embedding is typically a vector of real numbers (common dimension sizes range from 128 up to 768 or 1024 for many models). These vectors are produced by neural network models that have been trained to capture linguistic semantics. A famous example from word embeddings is:

```
vector("king") - vector("man") + vector("woman") ≈ vector("queen")
```

This demonstrates that embeddings can encode not just meaning of individual words, but relationships between concepts. In the context of RAG, we usually work with *sentence* or *paragraph embeddings* (to represent whole documents or chunks thereof). Two texts that are topically or semantically similar will yield vectors that are close by cosine similarity or Euclidean distance.

* **Similarity and Distance:** Once text is embedded into vectors, we can measure similarity by a metric like **cosine similarity** (the cosine of the angle between two vectors) or **inner product**. A higher similarity means the query and document are likely related in meaning. During retrieval, we take the query vector and find the nearest document vectors in this high-dimensional space. This operation is known as **nearest neighbor search** in the vector space.

**2.3 Preparing Documents for Retrieval – Chunking and Embedding:**
Real-world documents (e.g. research papers or long reports) can be very large, often too large to feed entirely into an LLM’s context window. A critical pre-processing step is **chunking** – dividing documents into bite-sized pieces (paragraphs, sections, or fixed-length tokens). Each chunk will be treated as a separate unit to embed and retrieve. Chunking ensures that:

* We don’t exceed the LLM’s input size when we later stuff retrieved text into its prompt.
* Each chunk is focused on a subtopic, which can improve retrieval focus. (If a 10-page document covers multiple topics, retrieving the whole thing may dilute the relevance, whereas retrieving just the relevant section chunk is more precise.)

There are two common strategies:

* *Fixed-size chunking:* Split text into segments of a certain number of tokens or characters (e.g. 500 tokens per chunk), possibly with some overlap so that context isn’t lost at boundaries. This approach is simple and fast.
* *Semantic chunking:* Split at natural semantic boundaries (e.g. paragraph breaks, or using an ML model to find coherent segments). This avoids cutting important sentences apart and preserves context better. For example, we might split a document into logical sections or even individual sentences if they stand alone. Tools like Microsoft’s **LayoutLM** or text segmentation algorithms can help find these boundaries intelligently (the Azure *Document Intelligence* service can even do semantic chunking of PDFs). Semantic chunking can improve retrieval accuracy since each chunk is self-contained in meaning.

After chunking, each chunk is **embedded** using a neural model:

* We will use the **Sentence-Transformers** library (built on Transformers and PyTorch) to obtain document embeddings. For example, a model like `"all-MiniLM-L6-v2"` (a 384-dimension MiniLM) or a domain-specific model like `"sentence-transformers/all-mpnet-base-v2"` can convert each chunk of text into a numeric vector. The choice of embedding model matters: a model trained on scientific text might better capture research jargon than one trained on casual web text. We’ll discuss this more in advanced topics, but for now we’ll use a general-purpose encoder.

* Each vector is stored in an index for fast similarity search. A popular library for this is **FAISS (Facebook AI Similarity Search)**, which efficiently handles large collections of vectors (and can use GPU acceleration). Alternatively, one could use **ANN** (Approximate Nearest Neighbors) libraries like Annoy or ScaNN, or full-fledged **vector databases** like Pinecone, Weaviate, or ElasticSearch. In our workshop, FAISS is a convenient choice since it’s simple and can be used offline.

**2.4 Example: Indexing a Small Corpus**
Let’s walk through preparing a tiny example corpus. Suppose we have a few text snippets (they could be abstracts of papers or paragraphs from articles). We’ll chunk them (if they’re short, each snippet might be one chunk) and build a vector index.

For illustration, consider two short “documents” (in reality, these might be abstracts or summaries):

* **Doc 1 (Climate Economics)** – *"Estimates of global economic damage from climate change typically focus on average temperature rise. However, factors like precipitation changes, variability, and extreme weather events also affect outcomes. A recent study projects that at +3°C warming, global GDP could decline by about 10%, with poorer low-latitude countries seeing up to 17% losses. Including climate variability and extremes adds \~2% more GDP loss globally. This suggests that focusing only on annual averages underestimates true climate impact."*

* **Doc 2 (About RAG)** – *"Large Language Models can store factual knowledge in their parameters, but they struggle with up-to-date or specialized information. Retrieval-Augmented Generation (RAG) addresses this by combining a generative LLM with a document retriever. The retriever fetches relevant text (e.g., from a research papers database) based on a query, and the LLM uses this text to produce a more accurate, grounded answer. RAG systems thereby reduce hallucinations and allow the model to cite specific sources."*

We will embed these documents and index them:

```python
!pip install sentence-transformers faiss-cpu         # Install necessary libraries (if not already installed)
import numpy as np
from sentence_transformers import SentenceTransformer

# Our example documents (already reasonably sized, so no further chunking needed here)
docs = [
    "Estimates of global economic damage from climate change typically focus on average temperature rise. However, factors like precipitation changes, variability, and extreme weather events also affect outcomes. A recent study projects that at +3\u00b0C warming, global GDP could decline by about 10%, with poorer low-latitude countries seeing up to 17% losses. Including climate variability and extremes adds ~2% more GDP loss globally. This suggests that focusing only on annual averages underestimates true climate impact.",
    "Large Language Models can store factual knowledge in their parameters, but they struggle with up-to-date or specialized information. Retrieval-Augmented Generation (RAG) addresses this by combining a generative LLM with a document retriever. The retriever fetches relevant text (e.g., from a research papers database) based on a query, and the LLM uses this text to produce a more accurate, grounded answer. RAG systems thereby reduce hallucinations and allow the model to cite specific sources."
]

# Load a pre-trained sentence embedding model (using a small, fast model for demo)
encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
doc_embeddings = encoder.encode(docs)  # This produces a list of embedding vectors (one per doc)

print("Embedding size:", len(doc_embeddings[0]))
print("Sample embedding snippet for Doc1:", doc_embeddings[0][:5], "...")
```

Running the above, you would see that each document is now a vector (for example, 384 numbers if using MiniLM). The printout might show something like:

```
Embedding size: 384  
Sample embedding snippet for Doc1: [ 0.0213  0.1234 -0.0456  0.0078  0.2301 ... ] 
```

Each vector captures the semantic content of the text. We can now use FAISS to index these vectors for similarity search:

```python
import faiss

# Initialize a FAISS index (we'll use IndexFlatIP for cosine similarity after normalization)
d = doc_embeddings.shape[1]            # dimension of embedding
index = faiss.IndexFlatIP(d)           # Index for inner-product similarity
# (For cosine, it's common to normalize vectors to unit length, so inner product == cosine similarity)

# Normalize embeddings to unit length (for cosine similarity search)
doc_embeddings_normalized = doc_embeddings / np.linalg.norm(doc_embeddings, axis=1, keepdims=True)
index.add(doc_embeddings_normalized)   # add vectors to the index

# Let's test the index by searching for one of the documents itself
D, I = index.search(doc_embeddings_normalized[0:1], k=2)
print("Nearest neighbors for Doc1 vector:", I[0], "with scores", D[0])
```

This code adds our two document vectors to the FAISS index and performs a search using Doc1’s vector as a query (just as a test). The result `I[0]` might output `[0 1]` meaning the closest vector to Doc1 is itself (index 0) and the next closest is Doc2 (index 1), along with similarity scores in `D[0]`. In practice, we’ll query with *new questions*, not the documents themselves – which is the next step.

**2.5 Hardware Considerations – Indexing and Embeddings:**
Because we have a powerful GPU available (A100 with 40GB), we can handle reasonably large corpora in this workshop:

* **Embedding model runtime:** The SentenceTransformer model we used is small and can embed hundreds of texts per second on the GPU. For example, embedding 1000 chunks of text (\~a few sentences each) might take only a few seconds on an A100.
* **Memory (GPU/CPU):** We ran the embedding model on the GPU for speed. A 7B parameter model like Qwen-7B for generation will use roughly 14 GB of GPU memory in half-precision (FP16). The embedding model (MiniLM, \~66M params) is much smaller and could even run on CPU if needed. Storing the vectors: each text chunk’s embedding (384 floats) is \~1.5 KB in memory, so even 10,000 documents would be only \~15 MB – trivial in comparison to model sizes. FAISS can be configured to use the GPU or CPU; for small/medium corpora, CPU indexing is often fine, but GPU can accelerate searches for very large collections (millions of vectors).
* **Index type:** We used a simple `IndexFlatIP` which does brute-force search (checks all vectors). This is fine for small datasets or for demonstration. For larger data (say >100k docs), one might use FAISS’s ANN indices (like `IndexIVFFlat` or HNSW) to search approximate nearest neighbors much faster, at the cost of a tiny drop in recall. In an A100 environment, even brute-force on moderately large sets (tens of thousands of vectors) is feasible, but approximate indexes scale to millions of entries efficiently.

> **❓ Knowledge Check:** What is the purpose of converting documents into vectors (embeddings) for RAG, instead of just searching documents by keywords?
> `create_answer_box("📝 **Your Answer:**", id="mod2_embedding_advantage")`
> *Hint: Think about how embeddings capture similarity in meaning, and how that might find relevant info even if wording differs.*

### Module 3: Building a Simple RAG Pipeline

Now that we can retrieve documents given a query, let’s build an end-to-end RAG pipeline. We’ll go step-by-step:

1. **User Query -> Query Embedding:** Take a user’s natural language question and compute its embedding (using the same model as our document embeddings).
2. **Similarity Search:** Use the embedding to search our FAISS index and retrieve the top-\$k\$ most relevant document chunks.
3. **Compose Prompt with Retrieved Context:** Format a prompt for the LLM that includes the retrieved text (as contextual knowledge) along with the user’s question.
4. **LLM Generation:** Use the 7B LLM (e.g. Qwen-7B) to generate an answer, expecting that it will incorporate the provided context.
5. **Output the Answer (and possibly the sources).**

We’ll demonstrate this with the small corpus from Module 2 (Docs 1 and 2). Imagine a user asks: *“According to recent studies, how much could global GDP decline at 3°C of warming?”* – This is a specific question that the model likely wouldn’t know by itself (it’s a detailed figure from a climate economics study). Our pipeline should retrieve Doc1 (the climate document) and let the model use it.

**3.1 Setting up the LLM**
We use the Hugging Face Transformers library to load the Qwen-7B model. (Note: Ensure you have access to an A100 GPU and enough memory, \~14 GB, to load this model in half precision.)

```python
!pip install transformers accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Qwen/Qwen-7B"  # Using Qwen-7B (Instruct version if available for Q&A tasks)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map="auto",             # Automatically use the GPU (A100)
    torch_dtype="auto"             # Loads in half-precision if supported to save memory
)
```

*Loading the model may take a minute or two*, as it will download weights (if not cached) and allocate GPU memory. Once loaded, we have a `model` and `tokenizer` to generate text. Qwen-7B is an **instruction-tuned** model (if we use the "-Chat" or similar version) and supports a large context (up to 8192 tokens for the base Qwen-7B, and even more for newer versions). This is beneficial for RAG, because we can feed in several retrieved documents without hitting the context size limit.

**3.2 Retrieval + Generation Workflow:**
Now let’s implement the query -> retrieval -> generation steps:

```python
# 1. User query (we'll use the example question about climate impacts)
query = "According to recent studies, how much could global GDP decline at 3°C of warming, and which regions are hit hardest?"
query_vec = encoder.encode([query])              # embed the query using our SentenceTransformer
query_vec = query_vec / np.linalg.norm(query_vec)  # normalize for cosine similarity

# 2. Similarity search in FAISS index
top_k = 2
D, I = index.search(query_vec, k=top_k)
retrieved_indices = I[0]
print("Retrieved doc indices:", retrieved_indices)

# Get the actual text of the top documents
retrieved_texts = [docs[i] for i in retrieved_indices]
print("Top-1 Retrieved text snippet:", retrieved_texts[0][:60], "...")
```

When we run the above, `retrieved_indices` should likely be `[0, 1]` meaning it found Doc1 as most relevant (index 0) and maybe Doc2 as second. Given the query is about *3°C warming and GDP decline*, Doc1 (climate economics) is clearly relevant. We can inspect the snippet printed to confirm it indeed contains the answer figure (10% GDP decline, etc.).

Now, **compose the prompt** for the LLM. There are different ways to do this, but a simple approach for an *instruction-following* model like Qwen-7B is to provide a directive like: *“Use the following documents to answer the question.”* Then list the documents, then the question. For example:

```
PROMPT:
[Document 1]\n
"Estimates of global economic damage from climate change ... up to 17% losses."\n
[Document 2]\n
"Large Language Models can store factual knowledge ... sources."\n
QUESTION: According to recent studies, how much could global GDP decline at 3°C of warming, and which regions are hit hardest?
```

We label the inserted documents as e.g. \[Document 1] etc., so the model knows this is reference material. In practice, you might include only the top 1 or 2 documents to avoid overloading the model (and because less relevant docs can introduce confusion). It’s often useful to also add an instruction like *“Answer in a concise manner, citing the source document where appropriate.”* However, since our model isn’t explicitly fine-tuned to output citations, we might not enforce citation format here (that’s an advanced topic). We’ll focus on getting the correct content.

```python
# 3. Compose the prompt with retrieved context
prompt_intro = "You are a research assistant. Use the following documents to answer the question.\n"
docs_section = ""
for idx, text in enumerate(retrieved_texts, start=1):
    docs_section += f"[Document {idx}]\n{text}\n\n"
question_section = f"Question: {query}\nAnswer:"

prompt = prompt_intro + docs_section + question_section

# 4. Generate answer using the LLM
input_ids = tokenizer(prompt, return_tensors='pt').input_ids.to(model.device)
outputs = model.generate(input_ids, max_length=256, 
                         temperature=0.2,   # lower temp for factual answers
                         do_sample=False)    # use greedy or beam search for deterministic output
answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Answer:\n", answer[len(prompt):])  # print the answer portion (excluding the prompt we fed)
```

When we run this, the model will produce an answer by reading the context. **On an A100 GPU**, generating a short answer (say 1-3 sentences) is very fast (a few hundred milliseconds for 50 tokens, though initial loading is the slow part). The output might look like:

*Generated Answer:* *According to the provided document, at +3°C warming the global GDP is projected to decline by about **10%**, with the worst effects (up to **17%** losses) in poorer low-latitude countries.*

This matches the content of Document 1. The model has effectively **“open-book” answered** the question using the data we supplied, rather than guessing from its parameters. If our pipeline worked correctly, the answer is factual and directly supported by the retrieved text.

> **🔎 Note:** In constructing prompts for RAG, one must be mindful of the **context length** and formatting. Our Qwen-7B model supports up to 8192 tokens, so it can comfortably handle a couple of documents of a few hundred tokens each plus the question. If you retrieve many documents or very long text, you may need to truncate or summarize them before prompting. There is a trade-off between including more context (to cover all possible info) and keeping the prompt concise (to focus the model and not exceed limits).

**3.3 Verifying the Pipeline** (Optional): Try asking a question that the second document can answer, for example: *“What is Retrieval-Augmented Generation and why is it useful?”* The pipeline should retrieve Doc 2 and the LLM would define RAG accordingly. This can be a quick exercise to ensure our system works for different queries.

> **💡 Try it yourself:** Modify the `query` in the code above to another question (e.g., one about RAG, or something not in our tiny corpus). Run the cells to see how the retrieval picks documents and how the LLM responds. If you ask something unrelated to any document, the retriever might return low-relevance texts, and the LLM might give a very general answer or even say it’s not in the docs. This is a good way to observe the **importance of relevant retrieval** in guiding the generation.

> **❓ Reflection:** *What are the main components of our simple RAG pipeline?* (List at least two.)
> `create_answer_box("📝 **Your Answer:** The RAG pipeline consists of ...", id="mod3_pipeline_components")`
> *Hint: One component finds information, another produces the answer.*

## Day 2: Customizing and Extending RAG for Research

Day 1 gave us a working RAG pipeline and core understanding. Day 2 will delve into **advanced retrieval techniques**, the concept of **Graph RAG** (using knowledge graphs as a knowledge source), and discuss **practical research applications**. We’ll also touch on an optional advanced topic of managing citations and verifying factual accuracy in RAG-generated answers.

### Module 4: Advanced Retrieval Techniques

In this module, we explore ways to improve the retrieval component beyond the basics. Good retrieval is crucial for RAG’s success – if the right information isn’t fetched, the LLM can’t give a good answer. Research and industry have developed several strategies to boost retrieval performance:

**4.1 Hybrid Search (Semantic + Lexical):**
Our pipeline used pure vector similarity. However, dense embeddings sometimes miss exact matches for names, numbers, or specific jargon (this is often called the **“lexical gap”**). A robust approach is to combine **keyword-based retrieval** with **vector-based retrieval**, known as *hybrid search*. For example, one can run a BM25 search (a strong traditional IR algorithm) in parallel with vector search and then merge the results. Keyword search excels at precision for rare terms (if you query "GDP 17% low-latitude", a BM25 will lock onto documents containing "17%" and "low-latitude" explicitly), whereas vector search excels at recall for conceptually similar text (it might find a passage about "tropical countries" even if you said "low-latitude"). By combining them, we **cover each other’s blind spots**. Many enterprise search systems (like ElasticSearch or Azure Cognitive Search) support hybrid queries natively. In our Python demo, we could simulate this by using a library like `whoosh` for BM25 or simply checking word overlaps as a filter on vector results.

**4.2 Reranking with Cross-Encoders:**
Vector similarity gives a rough relevance score. A more accurate (but slower) approach is to use a **cross-encoder re-ranker**. This is a model (often a smaller BERT-based model or even the LLM itself) that takes a query and a candidate passage together and outputs a relevance score. Because the cross-encoder can fully examine the pair in detail (as opposed to independent embeddings), it often is better at fine-grained relevance judgments and can consider context and nuance. The trade-off is that it’s much slower than a vector dot product. A common strategy is a **two-stage retrieval**: first use the fast vector search to narrow down to, say, top 50 candidates, then use a cross-encoder to re-score those and pick the top 5. This gives the *accuracy of a heavy model* with the *speed of approximate search*. Libraries like 🤗 *Transformers* provide cross-encoder models (e.g., `cross-encoder/ms-marco-MiniLM-L-6-v2` for general passage reranking). In a research context, reranking is useful when your initial retrieval might pull in some non-relevant texts due to ambiguous query terms – the reranker can sort those out by actually reading the text.

**4.3 Query Expansion and Reformulation:**
Sometimes user queries are short or vague. “Graph RAG advantages?” is not very descriptive. An advanced technique is to have the system **expand or reformulate the query** before searching. This could be done by an LLM prompt (“Rewrite the query in a more detailed way including synonyms”) or using domain knowledge (e.g., adding related terms). For example, if a query is “health effects of PM2.5”, an expansion might add “air pollution fine particulate matter health impacts”. This increases the chance that at least one of the terms will match the way relevant documents are indexed. Classic IR had methods like *pseudo-relevance feedback* (taking top results and extracting additional keywords), while modern approaches might directly prompt an LLM to generate a set of related queries. In RAG, you could even do multiple retrievals: first search by original query, see what terms appear in results, then search again with those terms. This iterative approach is sometimes called **retriever refinement** or **Retrieval-Augmented Generation of Thoughts** (as in a recent paper that uses multi-step retrieve-and-refine).

**4.4 Domain-Specific Embeddings:**
Embedding models trained on general text might not capture nuances of domain-specific vocabulary. For instance, in biomedical papers, the term "CT" likely means *computed tomography*, but a general model might think of *connecticut* or *count* or other meanings from common text. If your research application is in a specialized field, consider using an embedding model tuned to that field:

* E.g., **SciBERT** or **SPECTER** for scientific publications, **BioBERT** or **PubMedBERT** for biomedical literature, **PatentSBERT** for patents, etc. These models will position domain terms more appropriately in vector space. Using them can significantly improve retrieval precision when all your documents are in that domain.
* Alternatively, you can fine-tune a general embedding model on your own corpus using contrastive learning (this requires training data of similar/dissimilar pairs). While that’s beyond our scope here, it’s a powerful way to customize retrieval if you have the resources.

**4.5 Efficient Indexing and Filters:**
If your corpus is large or heterogeneous, you might incorporate **metadata filters** and sharding in retrieval:

* Metadata example: if each document has fields like publication year, author, or topic, you can restrict retrieval to certain subsets. E.g., a question about COVID-19 could be filtered to documents from 2020-2023 where that term appears.
* Index sharding: you might maintain separate indexes per category of document and query them selectively (like one index for journal articles, one for encyclopedias, etc., and choose based on query type).
* These ensure you aren’t searching irrelevant portions of data and can improve both speed and relevance.

Let’s incorporate at least one advanced method into our running example for illustration. We’ll do a simple **hybrid search** demonstration. Imagine a query that contains a very specific keyword not common in the embedding’s training data. For example: *“What is the GDP loss at 3°C?”* – The number "3°C" and "GDP" might be captured by embeddings, but maybe not strongly. We can combine a keyword search for "3°C" as well:

```python
# Simple hybrid approach: ensure any document containing "3°C" gets a boost
query = "What is the GDP loss at 3°C warming?"
query_vec = encoder.encode([query])
query_vec = query_vec / np.linalg.norm(query_vec)

# Vector search
D, I = index.search(query_vec, k=2)
candidates = list(I[0])

# Keyword filter: check for presence of "3°C" or "3°" in docs
keyword = "3°C"
for idx, text in enumerate(docs):
    if keyword in text:
        if idx not in candidates:
            candidates.append(idx)

print("Candidates by hybrid criteria:", candidates)
# Now we have a set of candidate doc indices combining vector and keyword matches
# We could further rerank them by either vector score or some heuristic.
```

This simplistic approach finds that Doc1 explicitly contains "3°C", so even if it wasn’t the top vector hit (it is, but suppose it wasn’t), we’d include it due to the keyword. In a more complex scenario, combining these signals would involve weighting and perhaps learning, but the key idea is that **combining multiple search criteria improves robustness**.

**4.6 Evaluation of Retrieval Quality:**
As you extend your retrieval techniques, it’s important to evaluate how well they work. If you have labeled data (e.g., known relevant documents for certain queries), you can measure recall/precision or use metrics like MRR (Mean Reciprocal Rank). In many research applications, you might hand-inspect a few test questions to see if the top retrieved passages are on-topic. An iterative development loop is often:

* The model gave a wrong answer or hallucinated. Check what it retrieved – was the relevant info missing? If so, improve the retriever (maybe add a synonym to the query, or fine-tune embeddings, etc.).
* If the info was there but the model still answered incorrectly, then it might be the generation side that needs adjustment (or the model needs to be told to trust the text more).

**Connections to PyTorch and Model Training:** If you attended the PyTorch fine-tuning session, you might recognize that training a better retriever (like a DPR: Dense Passage Retriever) is a task that can be done via PyTorch – by training twin encoders on question-paragraph pairs. That’s beyond our scope here, but know that you *can* train the embedding model for your specific QA task if needed (improving retrieval via learning).

> **❓ Question:** What is one technique to improve retrieval in RAG when the initial results are not satisfactory?
> *(There are many possible answers: you could mention hybrid search, reranking, query expansion, etc.)*
> `create_answer_box("📝 **Your Answer:** One technique is ...", id="mod4_improve_retrieval")`

### Module 5: Graph RAG

So far, we assumed our knowledge base is a collection of text documents or chunks, and retrieval means finding relevant text passages. **Graph RAG** is an extension of the RAG concept where the external knowledge is not free text, but a **knowledge graph**. A knowledge graph (KG) organizes information into **entities (nodes)** and **relationships (edges)**, often storing facts in triples like (Subject — *Relation* → Object). For example, a mini knowledge graph could have:

* Node: *Google (Company)*, Node: *Sundar Pichai (Person)* with edge *CEO\_of*.
* Node: *Google*, Node: *Pinterest*, with an edge *Former\_employee\_founded* perhaps linking via a person.

**5.1 Why Knowledge Graphs?**
Knowledge graphs are powerful for representing complex, multi-hop relationships explicitly. In some query types, relevant information might be spread across multiple documents, and a pure text RAG might miss the connection. For example, the query given in the Elastic blog was: *“List some startups that were founded by former employees of Google.”* A classic RAG (text-based) might find a document about one person (e.g., “X, founder of Y, previously worked at Google”), but if no single document lists all startups or all people, the LLM might not compile a complete list easily. A knowledge graph, however, could have a structure: Google -> has\_employee -> Person, Person -> founded -> Startup. By traversing the graph, you could find all People who left Google and then all Startups they founded, covering the full space of answers.

Other advantages:

* **Structured Querying:** You can write specific graph queries (like SPARQL for RDF graphs) to precisely get the info. An LLM can be used to generate these queries from natural language (prompt-to-query retrieval). For example, an LLM could turn "startups founded by ex-Google employees" into a SPARQL query that the KG executes.
* **Context beyond text:** Graphs might encode things not directly stated in any one document, by linking data. E.g., a graph can tell you that two authors shared an affiliation, or that a chemical is a type of compound – facts that might require combining sources if using text.
* **Efficient multi-hop retrieval:** Instead of retrieving two separate documents and expecting the model to figure out the connection, a graph can retrieve a connected subgraph of facts and we can then present that to the model as a synthesized context.

However, using knowledge graphs introduces challenges:

* You need to *have* a knowledge graph (which might be built from text via extraction, or available as an existing ontology).
* Integrating graph data into an LLM prompt requires deciding how to linearize it (you can’t directly feed a graph structure, you have to convert it to text or some format the model can understand).
* There’s also a trade-off: graphs are excellent for factual queries with well-defined relationships, but not everything is easily captured as a triple. Documents are still better for narrative information or contextual descriptions.

**5.2 Approaches to Graph RAG:**
Steve Hedden (2024) categorizes three methods to use KGs in RAG:

1. **Vector-based retrieval over the graph:** Treat the text associated with graph nodes or edges (like descriptions of entities) as documents – embed them and do the usual semantic search. Essentially, ignore the structure initially, just know that if you retrieve an entity node, you can then fetch its relationships. This is closest to “baseline RAG” but on graph content. It’s simple but might miss some graph-specific power.

2. **Prompt-to-Graph Query (Semantic Querying):** Use the LLM to translate the user’s question into a structured query (like SQL for relational DB or SPARQL/Cypher for graph DB). Then execute that query on the knowledge graph to get an answer or a set of relevant facts, which are then given back to the LLM to formulate an answer. For instance, the LLM could produce a SPARQL query that finds all ?startup where ?person workedAt Google and ?person founded ?startup. The KG returns a list of startups, and the LLM can present them. This approach requires that your KG has a well-defined schema and that the LLM is guided to produce correct queries (which can be tricky, but research is progressing in this area).

3. **Hybrid (Vector + Graph):** Combine both. For example, use vector search to identify an entity or a part of the graph related to the query, then use graph traversal to expand on that. In Hedden’s tutorial, he suggests vector search to get an initial relevant set of entities, then use SPARQL to refine or find connected info. This leverages the strengths of both: vector search handles vague natural language, and graph query handles precise relationship following.

No one method is universally best; it depends on the scenario. If the question is very relational (like "how A is connected to B?"), a graph query is gold. If the question is more free-form ("what’s the significance of X?"), vector search may be better.

**5.3 Building and Using a Knowledge Graph (Demo):**
We’ll create a tiny toy knowledge graph using **NetworkX** (a Python library for graph data) to illustrate how one might traverse a graph in response to a query. Consider a graph of research collaborations:

* Nodes: **Researchers** and **Papers**.
* Edges: "authored" edges connecting researchers to the papers they wrote; "cites" edges connecting one paper to another it cites.

For example:

* Alice authored Paper1; Bob authored Paper2; Paper2 cites Paper1.
* Query: "Who has their work cited by Bob?" – This implies: Bob authored some paper (Paper2); find who wrote the papers that Paper2 cites. In our graph, Paper2 cites Paper1, which was authored by Alice. So answer: Alice.

Let’s encode this in a graph and see how we’d retrieve that answer:

```python
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes (could add attributes too, but not needed for this logic)
G.add_node("Alice", type="Researcher")
G.add_node("Bob", type="Researcher")
G.add_node("Paper1", type="Paper", title="On Climate Economics")
G.add_node("Paper2", type="Paper", title="Advances in Climate Modeling")

# Add edges for authorship and citation
G.add_edge("Alice", "Paper1", relation="authored")
G.add_edge("Bob", "Paper2", relation="authored")
G.add_edge("Paper2", "Paper1", relation="cites")

# Now our graph has Alice -> Paper1 (authored), Bob -> Paper2 (authored), and Paper2 -> Paper1 (cites).
print("Nodes:", G.nodes(data=True))
print("Edges:", G.edges(data=True))
```

This will output something like:

```
Nodes: [("Alice", {"type": "Researcher"}), ("Bob", {"type": "Researcher"}), ("Paper1", {"type": "Paper", "title": "On Climate Economics"}), ("Paper2", {"type": "Paper", "title": "Advances in Climate Modeling"})]
Edges: [("Alice", "Paper1", {"relation": "authored"}), ("Bob", "Paper2", {"relation": "authored"}), ("Paper2", "Paper1", {"relation": "cites"})]
```

Now, given the *conceptual* question "Who has their work cited by Bob?", how do we get the answer from the graph? We interpret it logically: Bob authored some paper(s) -> those paper(s) cite other papers -> find the author(s) of those cited papers. In graph terms:

1. Find papers where the author is Bob (i.e., outgoing edge from Bob with relation "authored").
2. For each such paper, find what papers it cites (outgoing "cites" edges).
3. For each cited paper, find who authored it (incoming "authored" edge to that paper).
4. Collect those author names.

We can perform this traversal:

```python
# Query the graph: "Who has their work cited by Bob?"
authors_cited_by_bob = set()

# Step 1: papers authored by Bob
for _, paper, data in G.out_edges("Bob", data=True):
    if data.get("relation") == "authored":
        # Step 2: papers that this paper cites
        for _, cited_paper, cdata in G.out_edges(paper, data=True):
            if cdata.get("relation") == "cites":
                # Step 3: find author of cited_paper (incoming edge to cited_paper)
                for author, _, adata in G.in_edges(cited_paper, data=True):
                    if adata.get("relation") == "authored":
                        authors_cited_by_bob.add(author)

print("Researchers who have their work cited by Bob's paper(s):", authors_cited_by_bob)
```

If we run this, we expect `{"Alice"}` as the result, since Alice wrote Paper1 which Bob’s Paper2 cited. Indeed, the output should confirm that. In an actual RAG system, we might not do this traversal in Python code; instead, we might query a graph database via Cypher or SPARQL. But the principle is the same: using structured relationships to get an answer that would be hard to get from text alone unless a specific sentence spelled it out.

**5.4 Integrating with LLM:**
How do we feed graph results to the LLM? There are a few patterns:

* **Linearize the subgraph:** We can turn the results of a graph query into a textual form, e.g., "Bob authored Paper2. Paper2 cites Paper1. Alice authored Paper1." and give that to the LLM to answer "Who has their work cited by Bob?" The LLM would then parse this linearized knowledge and answer "Alice."
* **Embed graph context as text:** We could treat each possible graph fact as a sentence (like triple -> sentence) and include relevant ones in the prompt. In our example, including "Paper2 (authored by Bob) cites Paper1 (authored by Alice)" in the prompt would allow the model to answer accordingly.
* **LLM as reasoner on graph:** Alternatively, have the LLM do the multi-hop reasoning itself by querying step by step: some advanced systems let the LLM suggest a next hop (e.g., "Find papers by Bob", then "Find who those papers cite", etc.) but that becomes more of an *agent* with a reasoning loop (beyond a static single prompt).

The Graph RAG approach can be very powerful for certain research applications:

* In scientific research, there are knowledge graphs (like concept ontologies, citation networks). A Graph RAG might navigate a citation network to find how ideas are connected.
* In medical research, a KG might link diseases, genes, drugs, symptoms – a Graph RAG could answer complex questions like "Which genes are associated with diseases that Drug X treats?" by traversing those relations.
* Companies like Ontotext and others have been exploring Graph RAG to combine unstructured and structured knowledge. Even Microsoft’s **GraphRAG** project (by their Semantic Kernel team) is explicitly looking at hierarchical or structured retrieval instead of flat text search.

In summary, **Graph RAG** extends the paradigm: *documents -> knowledge graph triples*. It doesn’t replace text RAG but complements it, especially for **multi-hop queries** and cases where your domain knowledge is well-structured. Many real systems might use a hybrid: search documents for general info, but if the query mentions entities that exist in a knowledge base, also fetch related facts from the KG.

> **❓ Thought Question:** *Give one advantage of using a knowledge graph in a RAG system.*
> *(For example, think about connecting information or answering multi-step queries.)*
> `create_answer_box("📝 **Your Answer:**", id="mod5_graph_advantage")`

### Module 6: Practical Research Applications

Having learned the techniques, let’s discuss how RAG can be applied in *real research scenarios*. This will help cement the concepts and also spark ideas for your own projects. We’ll look at a few example use cases across disciplines:

**6.1 Literature Review Assistant:**
One of the most labor-intensive tasks for scholars is sifting through dozens or hundreds of papers to find relevant information. A RAG-powered literature review assistant can dramatically speed this up:

* **Use case:** You want to know "*What are the main approaches used in recent AI for climate modeling?*". Instead of reading 50 papers, you ask the RAG system.
* **How it works:** The system has an index of scientific abstracts or full texts. Your question is vectorized; it retrieves the most relevant passages (say, some papers that mention "AI methods for climate") and the LLM summarizes them, maybe outputting something like: *"Recent approaches include neural network downscaling, hybrid physics-AI models, and reinforcement learning for parameter tuning. For example, one paper used a CNN for downscaling climate data, while another integrated a physical model with a neural net."*
* **Benefit:** It’s like having a research assistant who has skimmed all papers and can highlight key points for you, complete with references. This doesn’t replace reading the papers in full for deep understanding, but it **helps you triage and gather insights quickly**.

**6.2 Domain-Specific Q\&A:**
Imagine a **legal researcher** asking: "What did the 2025 Data Privacy Act say about user consent for data sharing?" A RAG system trained on legal texts could retrieve the relevant clause from the act and have the LLM provide a plain language explanation. Similarly, a **medical researcher** might ask: "Which clinical trials in the last year tested \*\*\$<\$drug\$>\$ for \*\*\$<\$disease\$>\$?" – RAG could search a database of trial reports and list the findings.

* In these cases, RAG systems serve as **natural language interfaces** to specialized databases. For instance, Semantic Scholar (Allen AI) has explored a paper Q\&A chatbot that can find answers in scientific papers. Even some library search engines are adding RAG-like features, allowing users to ask a question and get a collated answer drawn from multiple sources, instead of just a list of papers.

**6.3 Multi-document Summarization and Synthesis:**
Beyond Q\&A, RAG can help generate summaries that combine information from multiple documents. For example, an economist might want a summary of "*How COVID-19 impacted supply chains according to different studies*". The system can retrieve several reports or articles on that topic and have the LLM produce a synthesized summary: *"Multiple studies indicate that COVID-19 caused initial supply chain disruptions due to lockdowns (e.g., factory closures in China), followed by shifts in consumer demand. A World Bank report noted a 20% increase in shipping costs. Researchers suggest diversifying sources and increasing inventory as mitigation strategies."* In that single paragraph, it’s pulling in facts from various documents, something a single human would have to manually compile over hours. RAG can do it in seconds, albeit you have to verify the results.

**6.4 Interactive Data Analysis Assistants:**
Consider fields like astronomy or biology where you have large datasets plus literature. An interactive RAG system could allow a researcher to query both data and documents. For instance, "Find me recent observations of **galaxy X** and summarize any theories mentioned about its structure." The system might retrieve a database entry of observations (maybe even make a chart) and paragraphs from recent papers discussing it. While the data retrieval is beyond plain RAG (that’s more data query), the concept of augmenting LLMs with *tools* or *retrieval* overlaps here (LangChain and similar frameworks often integrate non-text tools similarly).

**6.5 Educational and Multidisciplinary Use:**
For students or researchers crossing into a new field, RAG can act as a tutor. A biology student learning about AI could ask, "Explain how neural networks are used in gene sequencing research." RAG would fetch portions of a few interdisciplinary papers or tutorials and help the LLM give a tailored explanation, bridging the gap between fields. The presence of actual references ensures the explanation isn’t just generic but points to where the student can read more.

**Connecting to Existing Workshops:** If you have a background in training models (from a PyTorch session, perhaps), think of RAG as *an alternative to fine-tuning for delivering knowledge*. Instead of fine-tuning an LLM on a corpus of texts (which you might have learned to do with PyTorch), you keep the LLM fixed and just ensure those texts can be fetched at runtime. There’s also synergy: if your RAG system consistently fails on a certain type of question, you might then fine-tune the LLM or the retriever on those cases. Or if you attend a future session on **fine-tuning LLMs**, you could try *fine-tuning Qwen-7B to better utilize retrieved evidence* (some RAG research does joint training of retriever and generator).

**6.6 Example Walk-through – RAG in Academic Search:**
Let’s do a quick hypothetical example to illustrate a full workflow in an academic search context:

* **Question:** "What are the known side effects of the new Alzheimer’s drug lecanemab as reported in clinical studies?"
* **RAG process:** The system searches a corpus of medical papers and trial results for "lecanemab side effects clinical trial". It finds:

  * Document A: A 2023 NEJM paper on Lecanemab Phase 3 trial (mentions side effects like brain swelling, ARIA-E).
  * Document B: A 2024 conference abstract comparing Alzheimer drug side effects.
  * Document C: Perhaps a review article summarizing multiple trials.
* The LLM then synthesizes: *"Clinical trials of lecanemab have reported side effects including amyloid-related imaging abnormalities (ARIA-E, a type of brain swelling) and ARIA-H (microhemorrhages). In the Phase 3 trial, about 12% of patients on lecanemab experienced ARIA-E. Other common adverse events were infusion reactions and headache."*
* **Outcome:** The user gets a concise answer with specifics and presumably citations. The references (e.g. NEJM 2023) can be provided for verification. This is hugely valuable: it saved the researcher from reading through possibly dozens of pages and instead gave a targeted summary.

This example also underscores the importance of **verification**, which leads us to the optional advanced topic of ensuring these answers and citations are correct.

> **💭 Your Turn:** *Think of a question or task in your own research area that could be helped by an LLM with retrieval.* It could be finding a particular detail in literature, summarizing a topic across sources, or checking consistency between studies. How would you imagine a RAG system assisting you?
> `create_answer_box("📝 **Your Answer:** In my field of ___, I could use RAG to ...", id="mod6_application_reflection")`

## Optional Advanced Topic: Citation Management and Verification in RAG

*(This section is optional but important for research applications where trust and accuracy are paramount.)*

One appealing feature of RAG-based systems is that they can provide **citations or references** alongside the generated answer. For example, our hypothetical answers above included references like pointing to the source. However, getting an LLM to correctly cite sources is not trivial. We need to address two questions:

1. **How do we prompt or enforce the model to include citations?**
2. **How do we verify that those citations are accurate and actually support the answer?**

**A. Getting the Model to Cite Sources:**
If the RAG retrieval step already provides the relevant documents, one strategy is to format the prompt in a way that encourages citation. For instance, you might enumerate the sources as `[1] ... [2] ...` in the context and then ask the model: *"Answer the question and cite the source by number for each claim."* Many instruction-tuned models (including Qwen) will attempt to do this if asked. In fact, improved instruction tuning has led to models that can output sources upon request. Another approach is using specialized prompting or output parsing: e.g., *"Provide the answer in the following JSON format: { 'answer': ..., 'sources': \[...] }"*. This can work, but the model might still hallucinate a bit.

A **big risk** is the model might fabricate a source or a quote that sounds plausible but isn’t real. For example, GPT-4 and others have been known to produce a professional-sounding citation to a non-existent paper. Just because we retrieved documents doesn’t mean the model won’t mix things up – it could cite Document \[1] for a fact that actually came from \[2], or quote a sentence with slight alterations. **We cannot blindly trust the model’s citations.**

**B. Verification of Citations (post-hoc):**
To ensure trustworthiness, we need to verify any cited content:

* *String matching:* The simplest check: if the model outputs a sentence "global GDP could decline by 10%【source】", we can search the source document for that exact string or number. But the model might paraphrase. In our example, if the source said "10% of GDP", the model said "10% decline in GDP" – similar meaning, different words.

* *Fuzzy matching:* We can use text similarity or substring search to see if a substantial portion of the model’s statement appears in the source. For instance, use a library like **fuzzball** (Levenshtein distance) or simply `difflib.SequenceMatcher` to find the longest matching substring between the answer and the source text. If we find a very high similarity (say >90% match of a sentence length), we consider the citation verified. This was the approach described by one developer: have the LLM produce a quote or sentence from the source, then use a fuzzy search to locate it in the original document. If found, great. If not, the citation might be incorrect.

* *Cross-check via embeddings:* Another method is to take the claim (or each sentence of the answer) and vector-search it against the corpus to see if the supposed source truly comes up. For example, if the answer sentence "At +3°C warming, global GDP loss \~10%" is claimed to come from Doc1, we can embed that sentence and see if Doc1 is indeed the nearest neighbor. If the top result is a different document altogether, maybe the model attributed it incorrectly.

* *LLM as a checker:* One could even employ a second LLM pass: ask the model, "Does \[Document 1] support the statement: '...'? Answer yes or no." But as noted, having an LLM verify an LLM can be error-prone and may just reaffirm the original mistake.

The key principle is **don’t trust – verify**. In critical applications (like medical or legal), it’s recommended to automate this verification. For instance, a Nature paper in 2025 found that even systems like GPT-4 with web retrieval often cite sources that *don’t fully support their statements*, or are even contradictory. Up to 50–90% of responses had at least one unsupported claim in their cited source. This underlines that just because a fancy model gave a citation, we can’t assume it’s correct without checking. Users might not always check themselves, so our system should help.

**B.1 Implementation Note:** If we were to implement verification for our little example:

* After generating the answer, for each source \[i] it cited, we could take the sentence(s) associated with that citation and search the corresponding `docs[i]` string for them. For instance, if our answer said "... 10% decline ...【1】", search `docs[0]` for "10%". If found and the surrounding text matches context, good. If not, maybe flag it.
* We could also integrate something like this into the `create_answer_box` as an exercise: ask participants to manually verify a given citation by looking at the doc.

**C. Preventing Hallucinated Citations:**
One strategy to reduce citation hallucination is to restrict the model’s output to only reference things we explicitly gave it. For example, instead of letting it freely generate "\[1]", "\[2]" tokens (which it might use wrongly), we can try a different prompting:

* Append each retrieved document with a label like `(Source A)` and instruct the model: "When using information from a source, mention (Source A) or (Source B) in your answer." This sometimes leads the model to literally copy those tokens instead of making up its own.
* Or use an approach like **pointer generation** networks concept: identify chunks by an ID and ask for answers like "According to Source A, ...".

In practice, libraries like **LlamaIndex** provide features for inline citation: they keep track of which node (document chunk) contributed to which part of the answer and can automatically append references. Some even do a post-processing where they highlight the parts of source text that overlap with the answer, to double-check and then format the citations accordingly.

**Recent Advancements:** This is an active area of research. For instance, the *CiteFix* algorithm (2023) proposes ways to adjust an answer’s citations after generation for correctness. And evaluation metrics are being developed to score how well an answer is supported by its sources (like *“Precision\@K of supporting facts”*). We expect future LLMs to be better at source attribution inherently, but for now, **it’s on us to engineer it**.

**C.1 Ethical Aspect:** In academic writing, mis-citation can be as bad as no citation. A RAG system that outputs a real-looking reference that in fact doesn’t support the claim can mislead users. Always double-check, especially if you plan to use the content in your own work. Ideally, the system itself should highlight uncertainty (e.g., "No source found for this part") rather than confidently present unverified info.

Let’s imagine we ask our system a question and want to ensure it cites correctly. We can simulate a verification workflow:

```python
# Suppose our answer came with a citation [Document 1] for the 10% GDP decline claim.
answer_sentence = "Global GDP could decline by about 10% at +3°C warming"
source_doc = docs[0]  # Document 1 text
if answer_sentence.lower() in source_doc.lower():
    print("Exact sentence found in source - citation looks correct.")
else:
    # Try fuzzy match: find best substring match
    import difflib
    seq = difflib.SequenceMatcher(None, source_doc.lower(), answer_sentence.lower())
    match = seq.find_longest_match(0, len(source_doc), 0, len(answer_sentence))
    similarity = match.size / len(answer_sentence)
    print(f"Best fuzzy match similarity: {similarity:.2f}")
    extract = source_doc[match.a: match.a + match.size]
    print("Matched text snippet in source:", extract)
```

This code checks if the answer sentence is exactly in the source (likely not, since the model might paraphrase), then does a fuzzy longest-match check. If `similarity` is, say, 0.8 or higher, that’s a good sign the content is supported (perhaps with minor rewording). We would then consider that citation verified. If it was low, we’d suspect the citation is incorrect or the model introduced info not actually present in the source.

**Summary:** For citation management in RAG:

* Encourage the model to cite by prompt formatting or fine-tuning.
* Keep the references the model can cite limited to what you provide (maybe number them to avoid it hallucinating a random \[5]).
* Implement automated checks to ensure the generated text is found in the retrieved sources, at least approximately. If not, you might programmatically append a warning or even loop back and ask the model to try again, focusing only on what the source says.
* Always allow the user (or you as the developer) to inspect the sources themselves. A well-designed RAG app will show the passages it pulled from, so even if the answer is wrong, the user can see the raw material and potentially spot the issue.

This closes our advanced topic and the workshop. You should now have a solid understanding of how RAG works, how to implement a basic RAG pipeline with an open-source LLM, and ways to enhance it for research-grade applications. With these tools, you can build systems that act as intelligent literature reviewers, domain-specific assistants, or data explorers, all while maintaining a link to trustworthy sources.

> **❓ Final Thought:** Why is it **not enough** to simply prompt an LLM to "give sources", and what is one method we discussed to verify that a cited source truly supports the answer?
> `create_answer_box("📝 **Your Answer:**", id="adv_citation_verify")`
> *Hint: Think about hallucinations and how we used fuzzy matching.*

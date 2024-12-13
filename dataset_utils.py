from datasets import load_dataset
from .faiss_utils import setup_faiss

def load_dataset_and_prepare_faiss(embed_func):
    ds = load_dataset("LangChainDatasets/question-answering-state-of-the-union")
    questions = ds["train"]['question']
    answers = ds["train"]["answer"]
    documents = [f"Q: {q} A: {a}" for q, a in zip(questions, answers)]
    index = setup_faiss(documents, embed_func)
    return documents, index

import numpy as np
from sentence_transformers import SentenceTransformer

embed_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text):
    return np.array(embed_model.encode(text)).astype('float32')

from .database import initialize_database
from .pipeline import rag_pipeline_with_db_and_standalone_llm
from .dataset_utils import load_dataset_and_prepare_faiss
from .embeddings import embed_text

if __name__ == "__main__":
    # Initialize Database
    initialize_database()

    # Configuration
    api_key = "86d74b097800428b92e4d8ca402e069d"
    endpoint_url = "https://azureopenaiblogo.openai.azure.com/"
    api_version = "2024-08-01-preview"
    deployment_name = "gpt-35-turbo"

    # Load Dataset and Prepare FAISS
    documents, index = load_dataset_and_prepare_faiss(embed_text)

    # User Query
    user_query = "What is the weapon user is speaking about?"

    # Run RAG Pipeline
    result = rag_pipeline_with_db_and_standalone_llm(api_key, endpoint_url, api_version, deployment_name, user_query, documents, index, embed_text)
    print("RAG Response:")
    print(result)

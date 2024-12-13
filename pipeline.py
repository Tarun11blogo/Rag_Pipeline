from .database import fetch_last_qa, insert_question_answer
from .faiss_utils import retrieve_context
from .openai_utils import generate_standalone_question_with_llm, call_openai_model
from .intent import classify_intent, check_intent_score

def rag_pipeline_with_db_and_standalone_llm(api_key, endpoint_url, api_version, deployment_name, user_query, documents, index, embed_func, db_name="qa_database.db"):
    # Intent Classification
    candidate_labels = ['weapons', 'crime', 'sexual', 'finance', 'medical']
    intent_result = classify_intent(user_query, candidate_labels)

    # Check Intent Score for Blocked Categories
    if check_intent_score(intent_result):
        return "User query belongs to the blocked category"

    # Retrieve Context
    retrieved_context = retrieve_context(user_query, index, documents, embed_func)

    # Fetch Last Q&A and Generate Standalone Question
    last_question, last_answer = fetch_last_qa(db_name)
    standalone_question = generate_standalone_question_with_llm(api_key, endpoint_url, api_version, deployment_name, user_query, last_question, last_answer)

    # Call OpenAI Model
    response = call_openai_model(api_key, endpoint_url, api_version, deployment_name, standalone_question, retrieved_context)

    # Store Q&A Pair in the Database
    insert_question_answer(user_query, response, db_name)

    return response

import openai

def generate_standalone_question_with_llm(api_key, endpoint_url, api_version, deployment_name, new_question, last_question, last_answer):
    if last_question and last_answer:
        prompt = (
            f"You are a helpful assistant. "
            f"Here is the previous question and its answer:\n"
            f"Q: {last_question}\n"
            f"A: {last_answer}\n\n"
            f"Now, here is the new question: {new_question}\n\n"
            f"Generate a standalone question that incorporates the context of the previous question and answer."
        )
    else:
        return new_question

    try:
        openai.api_key = api_key
        openai.api_base = endpoint_url
        openai.api_type = "azure"
        openai.api_version = api_version

        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.5
        )

        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating standalone question: {e}")
        return new_question

def call_openai_model(api_key, endpoint_url, api_version, deployment_name, question, context):
    prompt = (
        f"You are a helpful assistant. Use the context below to answer the question:\n\n"
        f"Context: {context}\n\n"
        f"Question: {question}\n\n"
        f"Provide a detailed answer."
    )

    try:
        openai.api_key = api_key
        openai.api_base = endpoint_url
        openai.api_type = "azure"
        openai.api_version = api_version

        response = openai.ChatCompletion.create(
            engine=deployment_name,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )

        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

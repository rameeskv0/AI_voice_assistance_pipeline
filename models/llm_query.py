from langchain_ollama import OllamaLLM

def query_llm(text):

    model = OllamaLLM(model="llama3")

    modified_input = f"{text} (Respond with a maximum of 2 sentences.)"


    print(f"Querying the LLM")
    result = model.invoke(input=modified_input)

    # Return the result
    return result

if __name__ == "__main__":
    # Example query
    example_text = "What is the capital city of India?"
    response = query_llm(example_text)
    print(f"Query: {example_text}")

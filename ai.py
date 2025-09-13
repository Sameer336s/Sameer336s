!pip install -U llama-cpp-python

# !pip install llama-cpp-python

from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="bartowski/krutrim-ai-labs_Krutrim-2-instruct-GGUF",
    filename="{{GGUF_FILE}}",
)

llm.create_chat_completion(
    messages = [
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ]
)
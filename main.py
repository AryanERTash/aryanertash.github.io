import os
from openai import OpenAI

# Initialize the client
client = OpenAI(
    api_key="AIzaSyDXi6vXP6sGK2obbt1e4UCJ3tNYhDC6s_8",  # Replace with your Gemini key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini OpenAI-compatible endpoint
)

def chat_with_gemini():
    messages = [
        {"role": "system", "content": "You are a helpful assistant.Do not use any markdown formatting in your answers. And give answers in medium sized paragraphs and bullet points"}
    ]
    print("Chatbot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        messages.append({"role": "user", "content": user_input})

        try:
            resp = client.chat.completions.create(
                model="gemini-2.5-flash",  # Gemini Flash model
                messages=messages,
                temperature=0.7,
            )
        except Exception as e:
            print("Error calling API:", e)
            continue

        assistant_message = resp.choices[0].message.content
        print("Bot:", assistant_message)

        messages.append({"role": "assistant", "content": assistant_message})

if __name__ == "__main__":
    chat_with_gemini()

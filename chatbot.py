from groq import Groq
client = Groq(api_key="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")
print("Chatbot (Groq Streaming): Type 'quit','exit' or 'bye' to stop\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit","bye"]:
        print("\n Chatbot: Goodbye!")
        break
    print("Chatbot:", end="", flush=True)

    stream = client.chat.completions.create(
        model="llama3-8b-8192", #or "mixtral-8x7b-32768"
        messages=[{"role": "system", "content": "You are a helpful chatbot."},
                  {"role":"user", "content": user_input}
                  ],
                  stream=True  # Enable streaming
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)

    print()        
import ollama

print("MY AI q&a bot")
print("type exit to stop")
while True:
    question=input("you:")
    if question.lower()=="exit":
        print("bot:Goodbye!")
        break
    response=ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role":"user",
                "content":question
            }
        ]
    )
    print("bot:",response["message"]["content"])
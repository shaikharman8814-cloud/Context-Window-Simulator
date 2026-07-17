import tiktoken


encoding = tiktoken.get_encoding("cl100k_base")


MAX_TOKENS = 100


messages = [
    "Hello",
    "Teach me Python",
    "Explain AI",
    "sdfdfgedfjfjgjhrJuly and angrily tendered his resignation. The committee members realised that the resignation of their leading public figure and speaker would mean the end of the part At the time of Hitler's release from prison, politics in Germany had become less combative, and the economy had improved, limiting Hitler's opportunities for political agitation. As a result of the failed Beer Hall Putsch, the Nazi Party and its affiliated organisations"
]


context = ""

for message in messages:
    context += message + "\n"


tokens = encoding.encode(context)

print("Before")
print("----------------")
print(context)
print("Token Count:", len(tokens))


while len(tokens) > MAX_TOKENS:


    messages.pop(0)


    context = ""

    for message in messages:
        context += message + "\n"


    tokens = encoding.encode(context)

print("\nAfter")
print("----------------")
print(context)
print("Token Count:", len(tokens))
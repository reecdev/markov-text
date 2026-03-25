import random, time

tokens = []
maps = {}

def predict(word):
    if word in maps:
        try:
            return random.choice(maps[word])
        except:
            return random.choice(tokens)
    else:
        return random.choice(tokens)
    
data = input(">> ")

for word in data.split(" "):
    tokens.append(word)

for i, word in enumerate(tokens):
    if not word in maps:
        maps[word] = []
    try:
        maps[word].append(tokens[i + 1])
    except:
        continue

# ------------------------------------------------------------------------------------------------

context = data
print(prompt, end=" ")
for i in range(10000):
    prediction = predict(context[len(context)-1])
    context.append(prediction)
    print(prediction, end=" ", flush=True)

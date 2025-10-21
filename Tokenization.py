import re

with open ("LLM-Project/harrypotter.txt","r",encoding="utf-8") as f:
    raw_text=f.read()

print("Total number of charachters:",len(raw_text))

preprocessed=re.split (r'([,.:;?-_!"()\']|--|\s)',raw_text)

preprocessed=[item for item in preprocessed if item.strip()]
print(preprocessed[:30])

all_words=sorted(set(preprocessed))
vocab_size=len(all_words)

print(vocab_size)
vocab ={token:integer for integer,token in enumerate(all_words)}

for i, item in enumerate(vocab.items()):
    print(item)
    if i>=200:
        break
import re
from Tokenizer_V1 import SimpleTokenizerV1 

with open ("LLM-Project/harrypotter.txt","r",encoding="utf-8") as f:
    raw_text=f.read()

print("Total number of charachters:",len(raw_text))

preprocessed=re.split (r'([,.:;?-_!"()\']|--|\s)',raw_text)

preprocessed=[item for item in preprocessed if item.strip()]
print(preprocessed[:30])

all_words=sorted(list(set(preprocessed)))
vocab_size=len(all_words)
all_words.extend(["<|endoftext|>","<|unk|"])
vocab ={token:integer for integer,token in enumerate(all_words)}



for i, item in enumerate(vocab.items()):
    print(item)
    if i>=200:
        break

tokenizer=SimpleTokenizerV1(vocab)
text='''He is a man.'''
text2='''harry is <|endoftext|>'''
ids=tokenizer.encode(text2)
print(ids)

text1=tokenizer.decode(ids)
print(text1)
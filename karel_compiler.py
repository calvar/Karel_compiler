from karel_tokenizer import tokenize


code = open('text.txt','r')
code_tokens = tokenize(code)
code.close()

if code_tokens:
    print(code_tokens)


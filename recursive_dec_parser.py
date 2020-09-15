from karel_tokenizer import tokenize 

#-------------------------KAREL GRAMMAR------------------------------------
#start -> BEGINNING-OF-PROGRAM program END-OF-PROGRAM
#program -> definition* BEGINNING-OF-EXECUTION statement* END-OF-EXECUTION
#definition -> DEFINE-NEW-INSTRUCTION identifier AS block END
#block -> BEGIN statement* END
#statement -> iteration | loop | conditional | instruction
#iteration -> ITERATE number TIMES block
#loop -> WHILE condition DO block
#conditional -> IF condition THEN block (ELSE block)?
#instruction -> move | turnleft | turnoff | putbeeper | pickbeeper
#condition -> next-to-a-beeper | not-next-to-a-beeper | front-is-clear |
#             front-is-blocked | left-is-clear | left-is-blocked |
#             right-is-clear | right-is-blocked | facing-north |
#             not-facing-north | facing-east | not-facing-east |
#             facing-south | not-facing-south | facing-west |
#             not-facing-west | any-beepers-in-beeper-bag | no-beepers-in-bag
#identifier -> ([a-z])([-(a-z)(0-9)_]*)
#number -> [0-9]+
#

def reject():
    print("Program is rejected")
    exit()

def accept():
    print("Program is accepted")

def statement(tokens, idx, inp):
    if inp == 'move':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
    elif inp == 'turnleft':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
    elif inp == 'putbeeper':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
    elif inp == 'pickbeeper':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
    elif inp == 'turnoff':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
        """
        elif inp == 'ITERATE':
        
        elif inp == 'WHILE':
        
        elif inp == 'IF':
        """
    elif inp == ';':
        if tokens[idx-2][1] != ';':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
        else:
            reject()
    return tokens, idx, inp
    
def program(tokens, idx, inp):
    #faltan definiciones!!!!!!!!!
    if inp == 'BEGINNING-OF-EXECUTION':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp)
        if inp == 'END-OF-EXECUTION':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
        else:
            reject()
    else:
        reject()
    return tokens, idx, inp 
    
def start(tokens, idx, inp):
    if inp == 'BEGINNING-OF-PROGRAM':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp = program(tokens, idx, inp)
        if inp == 'END-OF-PROGRAM':
            inp = tokens[idx][1]
            idx += 1
        else:
            reject()
    else:
        reject()
    return tokens, idx, inp 
    
def parse(tokens, idx, inp):
    inp = tokens[idx][1]
    idx += 1
    print(inp)
    tokens, idx, inp = start(tokens, idx, inp)
    if inp == '__END__':
        accept()
    else:
        reject()

#BOE-----------------------------------------------------

code = open('text.txt','r')
code_tokens = tokenize(code)
code.close()

idx = 0
inp = ''
if code_tokens:
    #print(code_tokens)
    parse(code_tokens, idx, inp)

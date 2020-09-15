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


def statement(tokens, idx, inp, instructions):
    if inp in instructions:
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        if inp == ';':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
            tokens, idx, inp =  statement(tokens, idx, inp, instructions)
        """
        elif inp == 'ITERATE':
        
        elif inp == 'WHILE':
        
        elif inp == 'IF':
        """
    return tokens, idx, inp


def block(tokens, idx, inp, instructions):
    if inp == 'BEGIN':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp = statement(tokens, idx, inp, instructions)
        if inp == 'END' and tokens[idx-2][1] != ';':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
            if inp == ';':
                inp = tokens[idx][1]
                idx += 1
                print(inp)
                tokens, idx, inp = block(tokens, idx, inp, instructions)
        else:
            reject()
    return tokens, idx, inp

        
def program(tokens, idx, inp, instructions):
    if inp == 'DEFINE-NEW-INSTRUCTION':
        if tokens[idx][0] == 'identifier':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
            instructions.append(inp)
            inp = tokens[idx][1]
            idx += 1
            print(inp)
            if inp == 'AS':
                inp = tokens[idx][1]
                idx += 1
                print(inp)
                tokens, idx, inp = block(tokens, idx, inp, instructions) 
        else:
            reject()
    if inp == 'BEGINNING-OF-EXECUTION' and tokens[idx-2][1] == ';':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp =  statement(tokens, idx, inp, instructions)
        if inp == 'END-OF-EXECUTION' and tokens[idx-2][1] != ';':
            inp = tokens[idx][1]
            idx += 1
            print(inp)
        else:
            reject()
    else:
        reject()
    return tokens, idx, inp 


def start(tokens, idx, inp, instructions):
    if inp == 'BEGINNING-OF-PROGRAM':
        inp = tokens[idx][1]
        idx += 1
        print(inp)
        tokens, idx, inp = program(tokens, idx, inp, instructions)
        if inp == 'END-OF-PROGRAM' and tokens[idx-2][1] != ';':
            inp = tokens[idx][1]
            idx += 1
        else:
            reject()
    else:
        reject()
    return tokens, idx, inp 


def parse(tokens, idx, inp, instructions):
    inp = tokens[idx][1]
    idx += 1
    print(inp)
    tokens, idx, inp = start(tokens, idx, inp, instructions)
    if inp == '__END__':
        accept()
    else:
        reject()

#BOE-----------------------------------------------------

instructions = ['move','turnleft','pickbeeper','putbeeper','turnoff']


code = open('text.txt','r')
code_tokens = tokenize(code)
code.close()

idx = 0
inp = ''
if code_tokens:
    #print(code_tokens)
    parse(code_tokens, idx, inp, instructions)

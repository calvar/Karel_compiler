from karel_tokenizer import tokenize 

#-------------------------KAREL GRAMMAR------------------------------------
#start -> BEGINNING-OF-PROGRAM {write("#BEGINNING OF PROGRAM\n\n")} program END-OF-PROGRAM {write("#END OF PROGRAM")}
#program -> definition* BEGINNING-OF-EXECUTION {write("def main():\n") tabs+='\t'} statement* END-OF-EXECUTION {write("\n") tabs=tabs[:-1] write("main()\n\n")}
#definition -> DEFINE-NEW-INSTRUCTION {write("def ")} identifier {write("{0}()".format(inp))} AS {write(":\n")} block
#block -> BEGIN {tabs+='\t'} statement* END {write("\n") tabs=tabs[:-1]}
#statement -> iteration | loop | conditional | instruction
#iteration -> ITERATE number TIMES block
#loop -> WHILE condition DO block
#conditional -> IF condition THEN block (ELSE block)?
#instruction -> move {write(tabs+"{0}().format(inp)\n")} |
#               turnleft {write(tabs+"{0}().format(inp)\n")} |
#               turnoff {write(tabs+"{0}().format(inp)\n")} |
#               putbeeper {write(tabs+"{0}().format(inp)\n")} |
#               pickbeeper {write(tabs+"{0}().format(inp)\n")}
#condition -> next-to-a-beeper | not-next-to-a-beeper | front-is-clear |
#             front-is-blocked | left-is-clear | left-is-blocked |
#             right-is-clear | right-is-blocked | facing-north |
#             not-facing-north | facing-east | not-facing-east |
#             facing-south | not-facing-south | facing-west |
#             not-facing-west | any-beepers-in-beeper-bag | no-beepers-in-bag
#identifier -> ([a-z])([-(a-z)(0-9)_]*)
#number -> [0-9]+
#-------------------------------------------------------------------------

def reject(tokens,i):
    print(tokens[i-1][1])
    print("Program is rejected")
    exit()

    
def accept():
    print("Program is accepted")


def statement(tokens, idx, inp, instructions,tabs,OUT):
    if inp in instructions:
        OUT.write(tabs+"{0}()\n".format(inp))
        inp = tokens[idx][1]
        idx += 1
        #print(inp)
        if inp == ';':
            inp = tokens[idx][1]
            idx += 1
            #print(inp)
            tokens, idx, inp =  statement(tokens, idx, inp, instructions,tabs,OUT)
        """
        elif inp == 'ITERATE':
        
        elif inp == 'WHILE':
        
        elif inp == 'IF':
        """
    return tokens, idx, inp


def block(tokens, idx, inp, instructions,tabs,OUT):
    if inp == 'BEGIN':
        tabs += '\t' #trad
        inp = tokens[idx][1]
        idx += 1
        #print(inp)
        tokens, idx, inp = statement(tokens, idx,inp,instructions,tabs,OUT)
        if inp == 'END' and tokens[idx-2][1] != ';':
            OUT.write("\n") #trad
            tabs = tabs[:-1] #trad
            inp = tokens[idx][1]
            idx += 1
            #print(inp)
            if inp == ';':
                inp = tokens[idx][1]
                idx += 1
                #print(inp)
                tokens, idx, inp = block(tokens, idx, inp, instructions,tabs,OUT)
        else:
            reject(tokens,idx)
    return tokens, idx, inp

        
def program(tokens, idx, inp, instructions,tabs,OUT):
    if inp == 'DEFINE-NEW-INSTRUCTION':
        if tokens[idx][0] == 'identifier':
            inp = tokens[idx][1]
            idx += 1
            #print(inp)
            OUT.write("def {0}()".format(inp)) #trad
            instructions.append(inp)
            inp = tokens[idx][1]
            idx += 1
            #print(inp)
            if inp == 'AS':
                OUT.write(":\n") #trad
                inp = tokens[idx][1]
                idx += 1
                #print(inp)
                tokens, idx, inp = block(tokens,idx,inp,instructions,tabs,OUT)
            else:
                reject(tokens,idx)
        else:
            reject(tokens,idx)
    if inp == 'BEGINNING-OF-EXECUTION' and tokens[idx-2][1] == ';':
        OUT.write("def main():\n") #trad
        tabs += '\t' #trad
        inp = tokens[idx][1]
        idx += 1
        #print(inp)
        tokens, idx, inp =  statement(tokens,idx,inp,instructions,tabs,OUT)
        if inp == 'END-OF-EXECUTION' and tokens[idx-2][1] != ';':
            OUT.write("\n") #trad
            tabs = tabs[:-1] #trad
            OUT.write("main()\n\n") #trad
            inp = tokens[idx][1]
            idx += 1
            #print(inp)
        else:
            reject(tokens,idx)
    else:
        reject(tokens,idx)
    return tokens, idx, inp 


def start(tokens,idx,inp,instructions,tabs,OUT):
    if inp == 'BEGINNING-OF-PROGRAM':
        OUT.write("#BEGINNING OF PROGRAM\n\n") #trad
        inp = tokens[idx][1]
        idx += 1
        #print(inp)
        tokens, idx, inp = program(tokens,idx,inp,instructions,tabs,OUT)
        if inp == 'END-OF-PROGRAM' and tokens[idx-2][1] != ';':
            OUT.write("#END OF PROGRAM") #trad
            inp = tokens[idx][1]
            idx += 1
        else:
            reject(tokens,idx)
    else:
        reject(tokens,idx)
    return tokens, idx, inp 


def parse(tokens,idx,inp,instructions,tabs,OUT):
    inp = tokens[idx][1]
    idx += 1
    #print(inp)
    tokens, idx, inp = start(tokens,idx,inp,instructions,tabs,OUT)
    if inp == '__END__':
        accept()
    else:
        reject(tokens,idx)

#BOE-----------------------------------------------------

instructions = ['move','turnleft','pickbeeper','putbeeper','turnoff']


code = open('text.txt','r')
code_tokens = tokenize(code)
code.close()

idx = 0
inp = ''
if code_tokens:
    #print(code_tokens)

    OUT = open('text.py','w')
    tabs = ''
    parse(code_tokens, idx, inp, instructions, tabs, OUT)

    OUT.close()

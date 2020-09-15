import re

#LEXICON
#-------
tokens = {
    'separator': r'^;$',
    'number': r'^[0-9]+$',
    'identifier': r'^([a-z])([-(a-z)(0-9)_]*)$',
    'delimiter': r'^BEGIN$|^END$|^BEGINNING-OF-PROGRAM$|^END-OF-PROGRAM$|^BEGINNING-OF-EXECUTION$|^END-OF-EXECUTION$',
    'keyword': r'^DEFINE-NEW-INSTRUCTION$|^AS$|^IF$|^THEN$|^ELSE$|^ITERATE$|^TIMES$|^WHILE$|^DO$',
    'instruction': r'^move$|^turnleft$|^turnoff$|^putbeeper$|^pickbeeper$',
    'proposition': r'^next-to-a-beeper$|^not-next-to-a-beeper$|^front-is-clear$|^front-is-blocked$|^left-is-clear$|^left-is-blocked$|^right-is-clear$|^right-is-blocked$|^facing-north$|^not-facing-north$|^facing-east$|^not-facing-east$|^facing-south$|^not-facing-south$|^facing-west$|^not-facing-west$|^any-beepers-in-beeper-bag$|^no-beepers-in-bag$'
    }


def tokenize(code):
    code_tokens = []
    line_num = 1
    for line in code:
        lst = line.strip().split()
        for i in lst:
            tok = i
            sep = ''
            if i != ';' and i[-1] == ';':
                tok = tok[:-1]
                sep = ';'
            #print(tok)
            recognized = False
            for token_type in tokens:
                if re.match(tokens[token_type],tok):
                    if token_type != 'identifier':
                        #print('recognized as {0}'.format(token_type))
                        code_tokens.append((token_type,tok))
                    elif tok not in tokens['instruction']:
                        #print('recognized as {0}'.format(token_type))
                        code_tokens.append((token_type,tok))
                    recognized = True
            if not recognized:
                print('Line {0}: Symbol {1} is not a valid identifier'.format(line_num,tok))
                return []
            
            if sep == ';':
                #print(sep)
                #print('recognized as {0}'.format('separator'))
                code_tokens.append(('separator',sep))
        line_num += 1
    code_tokens.append(('program_end','__END__'))
    return code_tokens


#*****************************************
#var = 'F4_3jk-uid'
#print(re.match(tokens['identifier'],var))
#line = 'AS'
#print(re.match(tokens['keyword'],line))
#line = 'not-facing-east'
#print(re.match(tokens['proposition'],line))

#code = open('text.txt','r')
#code_tokens = tokenize(code)
#code.close()

#if code_tokens:
#    print(code_tokens)
#*****************************************

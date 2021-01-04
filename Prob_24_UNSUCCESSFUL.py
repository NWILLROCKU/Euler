lexList = []
lex = ''

def addLex(ilist):
    for i in ilist:
        global lex
        lex += str(i)
        
        if len(ilist) == 1:
            global lexList
            lexList.append(lex)
            if lex != '9876543210':
                lex = ''
                
        else:
            jlist = ilist
            jlist.remove(i)
            addLex(jlist)


alist = list(range(10))
addLex(alist)

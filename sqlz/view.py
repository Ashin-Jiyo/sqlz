# only view fetched data without column name
def view(fetched):

    # - count list function
    def dashcount(fetched):
        cn = list(fetched[0])
        for i in fetched:
             if len(cn) < len(i):
                 cn = list(i)   
        lm=[]
        lend=len(cn)
        for a in range(lend):
            ltemp=[len(str(cn[a]))]
            for i in range(len(fetched)):
                ltemp.append(len(str(fetched[i][a])))
            lm.append(max(ltemp)+2)
        return lm

    # print line function
    def line(fetched):
        count=dashcount(fetched)
        print('+', end='')
        for b in range(len(count)):
                print('-'*count[b], end='+')
        print()


    # print row function
    def row(fetched):
        fetched = fetched
        count = dashcount(fetched)
        for d in range(len(fetched)):
            print('|', end='')
            for e in range(len(fetched[d])):
                co = count[e] -len(str(fetched[d][e])) - 2
                if type(fetched[d][e]) == int:
                        print(' '*co, end=' ')
                        print(fetched[d][e], end=' |')
                else:
                        print('',fetched[d][e], end='')
                        print(' '*co, end=' |')
            print()

    
    line(fetched)
    row(fetched)
    line(fetched)
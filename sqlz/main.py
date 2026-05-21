def view(fetched,header_list=None,cur=None,tablename=None):
    
    # header list function
    def cname():
        cur.execute(f'desc {tablename}')
        d=cur.fetchall()
        l=[]
        for i in d:
            l.append(i[0])
        return l

    # - count list function
    def dashcount():
        if header_list != None:
            cn = header_list
        elif cur != None and tablename != None:
            cn = cname()
        elif len(fetched) > 0:
            cn = list(fetched[0])
        else:
            cn = []
        lm=[]
        lend=len(cn)
        for a in range(lend):
            ltemp=[len(str(cn[a]))]
            for i in range(len(fetched)):
                ltemp.append(len(str(fetched[i][a])))
            lm.append(max(ltemp)+2)
        return lm
        

    # print line function
    def line():
        count=dashcount()
        print('+', end='')
        for b in range(len(count)):
                print('-'*count[b], end='+')
        print()

    # print column header function
    def header():
        if header_list != None:
            cn = header_list
        elif cur != None and tablename != None:
            cn = cname()
        count = dashcount()
        print('|', end='')
        for c in range(len(cn)):
            co = count[c] -len(str(cn[c])) - 2
            if type(cn[c]) == int:
                    print(' '*co, end=' ')
                    print(cn[c], end=' |')
            else:
                    print('',cn[c], end='')
                    print(' '*co, end=' |')
        print()

    # print row function
    def row():
        count = dashcount()
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

    if header_list != None:
        line()
        header()
        line()
        row()
        line()
    elif cur != None and tablename != None:
        line()
        header()
        line()
        row()
        line()
    else:
        line()
        row()
        line()
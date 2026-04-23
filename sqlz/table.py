def table(cursor,tablename,fetched):
    
    # header list function
    def cname(cursor,tablename):
        cursor.execute(f'desc {tablename}')
        d=cursor.fetchall()
        l=[]
        for i in d:
            l.append(i[0])
        return l

    # - count list function
    def dashcount(fetched,cursor,tablename):
        cn = cname(cursor,tablename)
        lm=[]
        lend=len(cn)
        for a in range(lend):
            ltemp=[len(cn[a])]
            for i in range(len(fetched)):
                ltemp.append(len(str(fetched[i][a])))
            lm.append(max(ltemp)+2)
        return lm

    # print line function
    def line(fetched):
        count=dashcount(fetched,cursor,tablename)
        print('+', end='')
        for b in range(len(count)):
                print('-'*count[b], end='+')
        print()

    # print column header function
    def header(fetched,cursor,tablename):
        cn = cname(cursor,tablename)
        count = dashcount(fetched,cursor,tablename)
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
    def row(fetched,cursor,tablename):
        fetched = fetched
        count = dashcount(fetched,cursor,tablename)
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
    header(fetched,cursor,tablename)
    line(fetched)
    row(fetched,cursor,tablename)
    line(fetched)
import mysql.connector as mc
import sqlz
from sqlz import view
con = mc.connect(host='localhost', user='root', password='', database='ashin12a')
cur = con.cursor()
cur.execute('SELECT * FROM store')
d = cur.fetchall()
sqlz.table(cur,'store',d)
print()
cur.execute('SELECT * FROM store WHERE qty BETWEEN 100 AND 200')
d = cur.fetchall()
view(d)
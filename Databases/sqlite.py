import urllib.request, urllib.parse, urllib.error
import sqlite3
import re

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')
conn.commit()

fhand= urllib.request.urlopen('http://data.pr4e.org/mbox-short.txt')
text= str(fhand.read().decode())
emails=re.findall('From (\S+@\S+)',text)

for email in emails:
    cur.execute('SELECT count FROM Counts WHERE email=?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts 
                    VALUES(?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email=?',(email,))
    conn.commit()
    
sql = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sql):
    print(row[0] , row[1])
    
cur.close()
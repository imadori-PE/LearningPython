import sqlite3
import re

conn = sqlite3.connect('db.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
conn.commit()

fname = input("Enter file name: ")
if len(fname)<1:
    fname='mbox.txt'
fh = open(fname)
text=fh.read()
emails=re.findall('From \S+@(\S+)',text)

for email in emails:
    cur.execute('SELECT count FROM Counts WHERE org=?',(email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts 
                    VALUES(?,1)''',(email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org=?',(email,))
    
conn.commit()
sql = 'SELECT * FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sql):
    print(row[0] , row[1])
    
cur.close()
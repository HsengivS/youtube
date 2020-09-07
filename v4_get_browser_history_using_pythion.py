# Get Browser History using Python in Ubuntu
import sqlite3

path = "<--your-google-chrome-browser-history-path-->"

con = sqlite3.connect(path)

c = con.cursor()

c.execute("select url, title, visit_count, last_visit_time from urls")

results = c.fetchall()

for i in results[0:10]:
    print(i)

c.close()

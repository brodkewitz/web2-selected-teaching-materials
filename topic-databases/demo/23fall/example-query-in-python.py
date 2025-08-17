import sqlite3

con = sqlite3.connect("./spotify-data.db")
cur = con.cursor()
# Context manager automatically commits or rolls back changes when it exits
with con:
    avg_dance_by_user = cur.execute("""
        SELECT avg(danceability),
               username
        FROM   songs
        GROUP  BY username
        ORDER  BY avg(danceability) DESC;  
        """)
for dancer in avg_dance_by_user.fetchall():
    print(dancer)
con.close()

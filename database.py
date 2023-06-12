import sqlite3

conn = sqlite3.connect('database.db')

with conn:
    conn = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TBL_DATABASE( \
        ID INT PRIMARY KEY AUTOINCREMENT, \
        COL_FILE TEXT, \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect(database.db)

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('INFORMATION.DOCX'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('HELLO.TXT'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('MYIMAGE.PNG'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('MYMOVIE.PNG'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('WORLD.TXT'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('DATA.PDF'))
    cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                ('MYPHOTO.JPG'))
    conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT COL_FILE FROM TBL_DATABASE WHERE COL_FILE LIKE '%.TXT'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "Files ending in .txt are: {}".format()
    print(msg)
    

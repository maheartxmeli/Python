import sqlite3

# establish the connection
conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TBL_DATABASE( \
        ID INT PRIMARY KEY, \
        COL_FILE TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()

    fileList = ["information.docx", "hello.txt", "myimage.pg", "mymovie.png", "world.txt", "data.pdf", "myphoto.jpg"]
    for x in fileList:
        if x ==  "%.txt":
            cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
                        (x))
    conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    cur.execute("Select * FROM TBL_DATABASE")
    varMSG = cur.fetchall()
    for item in varMSG:
        msg = "(), ()".format(item[0],item[1])
        print(msg)

import sqlite3

# establish the connection
conn = sqlite3.connect('database.db')

#create the database table
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

    fileList = ("information.docx", "hello.txt", "myimage.png", "mymovie.png", "world.txt", "data.pdf", "myphoto.jpg")
    for x in fileList:
        if x == fileList.endswith(".txt"):
            cur.execute("INSERT INTO TBL_DATABASE(COL_FILE) VALUES (?)", \
            (x,))
            break
    conn.commit()
conn.close()

conn = sqlite3.connect('database.db')

with conn:
    cur = conn.cursor()
    cur.execute("Select * FROM TBL_DATABASE")
    print(item[1])

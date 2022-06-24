import sqlite3 

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("Insert into book Values (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()    

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows
    # conn.close()

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title = ? or author = ? or year = ? or isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book where id =?",(id,) )
    conn.commit()
    conn.close()

def update(id,title,author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author =?, year = ?, isbn=? where id = ?", (title,author, year, isbn,id))
    conn.commit()
    conn.close()    

connect()
# insert("opg","is the man",10,20)
# print (view())
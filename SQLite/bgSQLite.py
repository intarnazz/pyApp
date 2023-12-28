import sqlite3 as sq

with  sq.connect( 'saper.db' ) as con:
    cur = con.cursor()

    cur.execute("""
        DROP TABLE IF EXISTS posts
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS posts (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        post TEXT NOT NULL
    )
    """)
    cur.execute("""INSERT INTO posts(post)
        VALUES('текст поста')
    """)
    cur.execute("""INSERT INTO posts(post)
        VALUES('ещё один текст')
    """)
    cur.execute("""SELECT post 
        FROM posts
        ORDER BY post_id
    """)

    print(cur.fetchmany(100))

    # for i in cur.fetchmany(2): # .fetchmany(2) возвращщает количество записей не болие двух
    #     print( i[1] )
import sqlite3

connection=sqlite3.connect('data.db')
cursor= connection.cursor()

# # create_table="Create table users (id int,username text,password text)"
# # cursor.execute(create_table)
users=[(1,"rolf","asdf"),(2,"ann","xyz")]
insert_query="Insert into users values (?,?,?)"
cursor.executemany(insert_query,users)
connection.commit()
# select_query="Select * from users"
# result=cursor.execute(select_query)
# for i in result:
#     print(i)


def find_by_username(username):
        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()
        query="SELECT * FROM users WHERE username=?"

        result=cursor.execute(query,(username,))
        row=result.fetchone()
        print (row)
        
        

        connection.close()
find_by_username("ann")        
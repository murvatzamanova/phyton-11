# # DDL - Datalarin yaradilmasi ve tanilmasi

# # SQlite3

# import sqlite3

# connection = sqlite3.connect("1000kitap")

# # cursor: pointer
# cursor = connection.cursor() # db uzerinde proses aparmagimiz ucun lazim olan hissedir. Istenilen db uzerindeki proses cursor sayesinde bas tutacaq.

# def create__table():
#     cursor.execute("CREATE TABLE IF NOT EXISTS minkitap(name TEXT, author TEXT, publisher TEXT, pages INT)")
#     connection.commit()
  
# def add__data():
#     cursor.execute("INSERT INTO minkitap VALUES ('Müşfiqli günlər', 'Dilbər', 'Xan kitab evi', 170)") 
#     connection.commit()
    
# def dynamic_add_data(name, author, publisher, pages):
#     cursor.execute("INSERT INTO minkitap VALUES(?, ?, ?, ?)", (name, author, publisher, pages)) 
#     connection.commit()
   
# # name = input("Kitabın adı: ")   
# # author = input("Kitabın yazıçısı: ")   
# # publisher = input("Çap yeri: ")   
# # pages = int(input("Kitabın səhifəsi: "))

# # dynamic_add_data(name, author, publisher, pages)
   
   
# def show__data():
#     cursor.execute("SELECT * FROM minkitap")
#     data = cursor.fetchall()
#     for row in data:
#         print(row)
    

# def dynamic_show_data(author):
#     cursor.execute("SELECT NAME FROM minkitap WHERE AUTHOR=?", (author, ))
#     data = cursor.fetchall()
#     for row in data:
#         print(row)

# # author = input("Axtarmaq istədiyiniz kitabın yazıçısını qeyd edin: ")


# def update__publisher(old_publisher, new_publisher):
#     cursor.execute("UPDATE minkitap SET PUBLISHER = ? WHERE PUBLISHER = ?", (new_publisher, old_publisher))
#     connection.commit()
    
    
# def delete__data(name):
#     cursor.execute("DELETE NAME FROM minkitap WHERE NAME = ?", (name, ))
#     connection.commit()
    

# delete__data("Abaddon")
# # update__publisher("Xan evi", "Xan kitab evi")
# # dynamic_show_data(author)
# # show__data() 
# # add__data()  
# # create__table()
# connection.close()




# ..........NEW TASK............
# import sqlite3

# conn = sqlite3.connect('example.db')

# cursor = conn.cursor()
# create_table_sql = '''
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# '''


# cursor.execute(create_table_sql)
# conn.commit()
# conn.close()

# print("cedvel yaradildi")




import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()
create_table_query = '''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL
)
'''

cursor.execute(create_table_query)
connection.commit()

drop_table_query = 'DROP TABLE IF EXISTS employees'

cursor.execute(drop_table_query)
connection.commit()
alter_table_query = 'ALTER TABLE employees ADD COLUMN hire_date TEXT'

cursor.execute(alter_table_query)
connection.commit()

connection.commit()

cursor.close()
connection.close()

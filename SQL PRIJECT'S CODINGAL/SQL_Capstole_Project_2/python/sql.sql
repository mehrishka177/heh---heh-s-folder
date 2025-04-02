import sqlite3

conn = sqlite3.connect('database.sqlite')

print("oppened database succsesfuly")

conn.execute('''Create class 10
(sno int primary key not null,
roll_no int not null,
name text not null,
age int defult (15),
gender text not null,
email_id text not null,
contact_no reall not null);''' )

print("table created successfully")

conn.execute("insert to class 10
(sno,roll_no,NAME,AGE,GENDER,EMAIL_ID,CONTACT_NO) \
    values (3, 3, 'jeff', 15, male, 'allen@gmail.com', 990900)");

conn.commit()
print("records created succsesfully")

impord pandas as pd 
tables = pd.read_sql("""select * 
from class_10;""", conn)

tables 

class_10d = pd.read_sql("""select *
from class_10;""", conn)

class_10.head()
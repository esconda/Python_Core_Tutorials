# Author: Burak Dogancay
import sqlite3
import MySQLdb
import psycopg2


def sqLiteFunc():
  conn = sqlite3.connect("users.db") #Database connecion
  c = conn.cursor() #Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands:
  
  c.execute("CREATE TABLE user (name text, type integer)") 
  c.execute("INSERT INTO user VALUES ('Tb2', uav)")
  c.execute("INSERT INTO user VALUES ('Akinci', uav)")
  conn.commit()
  c.execute("SELECT * FROM user")
  print(c.fetchall())
  conn.close()

def mySqlFunc():
  dbConnection = MySQLdb.connect(host='host_example',port=int('port_example'),user='user_example',passwd='pass_example',db='schema_example')
  dbc = dbConnection.cursor()
  
  dbc.execute('SELECT * FROM %s' % 'table_example')
  dbConnection.commit()
  dbConnection.close()

def postreSqlFunc():
  dbConnection = psycopg2.connect(host='host_example',port=int('port_example'),user='user_example',passwd='pass_example',db='schema_example')
  dbc = dbConnection.cursor()
  
  dbc.execute('SELECT * FROM %s' % 'table_example')
  dbConnection.commit()
  dbConnection.close() 
  
  
def main():
 # Call sub class 
  sqLiteFunc()
 
 
  

  

if __name__ == '__main__':
    main()
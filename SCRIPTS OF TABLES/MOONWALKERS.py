#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")
      
mycursor = mydb.cursor()

#UDF FOR THE TABLE (COMPOSITION OF PLANETARY ELEMENTS)

def moonwalks():
  mycursor.execute("CREATE TABLE IF NOT EXISTS MOONWALKERS(\
   NAME VARCHAR(55) PRIMARY KEY,\
   MISSION VARCHAR(50),\
   DOB VARCHAR(50),\
   DOD VARCHAR(50),\
   LUNAR_EVA_DATE VARCHAR(50),\
   EVAS_PERFORMED VARCHAR(50),\
   EVA_DURATION VARCHAR(50),\
   SERVICE VARCHAR(55))")                      
    
  mycursor.execute("INSERT IGNORE INTO MOONWALKERS VALUES \
    ('NEIL ARMSTRONG','APOLLO 11', 'Aug15,1930', 'Aug21,2012', 'July21,1969', '1', '2hrs 31mins', 'NASA'),\
    ('BUZZ ALDRIN','APOLLO 11', 'Jan20,1930', 'ALIVE', 'July21,1969', '1', '2hrs 31mins', 'AirForce'), \
    ('PETE CONARD', 'APOLLO 12', 'Jun 2,1930', 'Jul 8, 1999','Nov 19-20, 1969' ,'2' ,'7hrs 45mins', 'Navy'),\
    ('ALAN BEAN', 'APOLLO 12', 'Mar 15, 1932', 'May 26, 2018','Nov 19-20, 1969' ,'2' ,'7hrs 45mins', 'Navy'),\
    ('ALAN SHEPARD', 'APOLLO 14', 'Nov 18, 1923', 'July 21,1998','Feb 5-6, 1971 ' ,'2' ,'9hrs 21mins', 'Navy'),\
    ('EDGAR MITCHELL', 'APOLLO 14', 'Sep 17,1930', 'Feb 4, 2016','Feb 5-6, 1971' ,'2' ,'9hrs 21mins', 'Navy'),\
    ('DAVID SCOTT', 'APOLLO 15', 'Jun 6, 1932', 'ALIVE','Jul 31-Aug 2, 1971' ,'3' ,'18hrs 33mins', 'AirForce'),\
    ('JAMES IRWIN', 'APOLLO 15', 'Mar 17, 1930', 'Sep 8, 1991','Jul 31-Aug 2, 1971' ,'3' ,'18hrs 33mins', 'AirForce'),\
    ('JOHN YOUNG', 'APOLLO 16', 'Sep 24, 1930', 'Jan 5, 2018','Apr 21-23, 1972' ,'3' ,'20hrs 14mins', 'Navy'),\
    ('CHARLES DUKE', 'APOLLO 16', 'Oct 3,1935', 'ALIVE','Apr 21-23, 1972' ,'3' ,'20hrs 14mins', 'Airforce'),\
    ('GENE CERNAN', 'APOLLO 17', 'Mar 14, 1934', 'Jan 16, 2017','Dec 11-14, 1972' ,'3' ,'22hrs 2mins', 'Navy'),\
    ('HARRISON SCHMITT', 'APOLLO 17', 'Jul 3, 1935', 'ALIVE','Dec 11-14, 1972' ,'3' ,'22hrs 2mins', 'NASA') \
  ")
    
  mydb.commit()

#END........
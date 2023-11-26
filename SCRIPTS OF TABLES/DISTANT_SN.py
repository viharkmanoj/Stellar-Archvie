#SYNTAX TO CONNECT PYTHON WITH DATABASE

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

def Distant_sn():
  mycursor.execute("CREATE TABLE IF NOT EXISTS DISTANT_SN (\
        TYPE VARCHAR(60),\
        NAME VARCHAR(60) PRIMARY KEY,\
        DISTANCE VARCHAR(60)\
        )")
        
#1
  mycursor.execute("INSERT IGNORE INTO DISTANT_SN (TYPE, NAME, DISTANCE)\
        VALUES ('SUPERNOVA','SN 1000+0216','Z=3.8993')")
#2
  mycursor.execute("INSERT IGNORE INTO DISTANT_SN (TYPE, NAME, DISTANCE)\
        VALUES ('TYPE LA SUPERNOVA','SN UDS 10Wil(SN WILSON)','Z=1.914')")
#3
  mycursor.execute("INSERT IGNORE INTO DISTANT_SN (TYPE, NAME, DISTANCE)\
        VALUES ('TYPE LA SUPERNOVA','SN SCP-0401(MINGUS)','Z=1.71')")
#4
  mycursor.execute("INSERT IGNORE INTO DISTANT_SN (TYPE, NAME, DISTANCE)\
        VALUES ('TYPE LA SUPERNOVA','SN 1997ff','Z=1.7')")
#5
  mycursor.execute("INSERT IGNORE INTO DISTANT_SN (TYPE, NAME, DISTANCE)\
        VALUES ('TYPE LA SUPERNOVA','SUPERNOVA PRIMO','Z=1.55')")

  mydb.commit()

#END........
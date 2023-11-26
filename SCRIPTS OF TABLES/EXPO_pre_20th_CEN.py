#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION PRE 20TH CENTURY )
def expo_pre():
      mycursor.execute("CREATE TABLE IF NOT EXISTS ET_PRE20THCEN(\
                  DATE CHAR(4), \
                  EVENT VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  REASEARCHER VARCHAR(30))")

#1
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1610', 'First telescopic observation of the night sky', 'VENICE', 'Galileo Galilei')")
#2    
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1668', 'First reflecting telescope', 'ENGLAND', 'ISSAC NEWTON')") 
#3
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1781', 'First telescopic discovery of planet (Uranus)', 'GREAT BRITAIN', 'WILLIAM HERSCHEL')")
#4
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1801', 'First discovery of asteroid (Ceres)', 'SICILY', 'Giuseppe Piazzi')")
#5
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1813', 'First exposition of the rocket equation', 'UK', 'William Moore')")
#6
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1840', 'First clear telescopic photograph of the MOON', 'UNITED STATES', 'John William Draper')")
#7
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1845', 'First proper observation of other galaxies', 'UK', 'William Parsons')")
#8
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1861', 'First proposal of using rockets for space flight', 'UK', 'William Leitch')")
#9
      mycursor.execute("INSERT IGNORE INTO ET_PRE20THCEN(DATE,EVENT,COUNTRY,REASEARCHER) VALUES\
            ('1895', 'First proposal of space elevator.', 'RUSSIA', 'Konstantin Tsiolkovsky')")
      
      
      mydb.commit()


#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (MOONS OF EARTH)

def earth_moons():
    mycursor.execute("CREATE TABLE IF NOT EXISTS earth_moons(\
                  NAME VARCHAR(50) PRIMARY KEY, \
                  DIAMETER VARCHAR(50), \
                  MASS VARCHAR(40), \
                  SEMIMAJOR_AXIS VARCHAR(50),\
                  ORBITAL_PERIOD VARCHAR(50),\
                  ORBITAL_INCLINATION VARCHAR(50),\
                  ECCENTRICITY VARCHAR(50),\
                  DISCOVERY_YEAR VARCHAR(50),\
                  DISCOVERER VARCHAR(50),\
                  TYPE VARCHAR(50))")

    mycursor.execute("INSERT IGNORE INTO earth_moons(NAME, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER,TYPE) VALUES\
      ('Moon','3474800','7.4x10^22 Kg','384400','27 DAYS','5.145°','0.055','Prehistory','?','Natural satellite')")

    mydb.commit()


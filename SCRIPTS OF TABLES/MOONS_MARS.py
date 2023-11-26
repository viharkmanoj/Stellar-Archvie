#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (MOONS OF MARS)

def mars_moons():
    mycursor.execute("CREATE TABLE IF NOT EXISTS mars_moons(\
                  NAME VARCHAR(50) PRIMARY KEY, \
                  DIAMETER VARCHAR(50),\
                  SURFACE_AREA VARCHAR(50),\
                  MASS VARCHAR(50),\
                  SEMIMAJOR_AXIS VARCHAR(50),\
                  ORBITAL_PERIOD VARCHAR(50),\
                  ORBITAL_INCLINATION VARCHAR(50),\
                  ECCENTRICITY VARCHAR(50),\
                  DISCOVERY_YEAR VARCHAR(50),\
                  DISCOVERER VARCHAR(50))")

#1
    mycursor.execute("INSERT IGNORE INTO mars_moons(NAME, DIAMETER, SURFACE_AREA, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('Phobos','22.2 km','1,548','10.7x10^15','9,377','7.66','1.093','0.0151','Asaph Hall','1877')")
#2
    mycursor.execute("INSERT IGNORE INTO mars_moons(NAME, DIAMETER, SURFACE_AREA, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('Deimos','12.6 km','483','1.5x10^15','23,460','30.31','0.93','0.00033','Asaph Hall','1877')")
    
    mydb.commit()

#END...
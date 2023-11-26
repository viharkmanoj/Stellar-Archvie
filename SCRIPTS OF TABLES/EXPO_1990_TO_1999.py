#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1990-1999)

def expo_1990_to_1999():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1990_TO_1999(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")
#1
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1990', 'First photograph of the whole Solar System', 'USA', 'Voyager 1')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1990', 'First telescope designed to be repaired in space', 'USA,ESA', 'Hubble Space Telescope')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1990', 'First time a spacecraft coming from deep space', 'ESA', 'Giotto')")
#4
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1991', 'First asteroid flyby', 'USA', 'Galileo')")
#5
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1992', 'First confirmed observation of an exoplanet', 'CANADA', ' Dale Frail')")
#6  
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1992', 'First polar orbit around the Sun', 'USA,ESA', 'Ulysses')")
#7
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1992', 'First spacecraft to map Venus in its entirety', 'USA', 'Megellan')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1995', 'Record longest duration spaceflight', 'RUSSIA', 'Mir')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1995', 'First orbit of Jupiter', 'USA', 'Galileo')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1995', 'First spacecraft to enter the atmosphere of JUPITER', 'USA', 'Galileo')")
#11 
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1995', 'First space laser-communication', 'JAPAN', 'ETS-VI')")
#12 
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1997', 'First orbital radio observatory', 'JAPAN', 'HALCA')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1997', 'First operational rover on MARS', 'USA', 'Mars Pathfinder')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1997', 'First spacecraft to use aerobraking to enter orbit', 'USA', 'Mars Global Surveyor')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_1990_TO_1999(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1998', 'First multinational space station', 'FKA,NASA,ESA,JAXA,CSA', 'ISS')")

    mydb.commit()
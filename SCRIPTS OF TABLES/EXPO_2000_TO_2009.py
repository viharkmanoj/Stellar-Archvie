#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 2000-2009)

def expo_2000_to_2009():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_2000_TO_2009(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")
#1
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2000', 'First orbit of an asteroid (433 Eros)', 'USA,ESA', 'NEAR Shoemaker')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2001', 'First landing on an asteroid (433 Eros)', 'USA', 'NEAR Shoemaker')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2001', 'First laser intersatellite link', 'ESA,FRANCE', 'Artemis')")
#4
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2004', 'First orbit of Saturn', 'USA,ITALY,ESA', 'Cassini Huygens')")
#5  
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2004', 'First sample return beyond lunar orbit (solar wind)', 'USA', 'Genesis')")
#6
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2005', 'First landing in the outer Solar System (Titan)', 'ESA,USA,ITALY', 'Cassini Huygens')")
#7  
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2005','First confirmed cryovolcano (Enceladus)', 'ESA,USA,ITALY', 'Cassini Huygens')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2005', 'First spacecraft to impact a comet (Tempel 1)', 'USA', 'Deep Impact')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2005', 'First asteroid ascent (25143 Itokawa)', 'JAPAN', 'Hayabusa')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2006', 'First sample return from a comet (81P/Wild)', 'USA', 'Stardust')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2007', 'First confirmed lakes on the surface of TITAN', 'USA,ESA,ITALY', 'Cassini Huygens')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2008', 'First spacecraft to photograph another spacecraft landing on another celestial body', 'USA', 'MRO')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2008', 'First discovery of lunar water in the form of ice', 'INDIA', 'Chandrayaan-1')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2009', 'First space telescope designated to search for Earth-like exoplanets', 'USA', 'Kepler Mission')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_2000_TO_2009(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2009', 'First images of the structures in the rings of SATURN', 'USA,ESA,ITALY', 'Cassini Huygens')")

    mydb.commit()
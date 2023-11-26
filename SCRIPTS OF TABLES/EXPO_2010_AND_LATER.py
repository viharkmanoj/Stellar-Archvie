#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 2000-2009)

def expo_2010_and_later():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_2010_AND_LATER(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")
#1
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2010', 'First solar sail', 'JAPAN', 'IKAROS')")
#2  
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2010', 'First sample return fron asteroid(25143 Itokawa)', 'JAPAN', 'Hayabusa')")
#3
    mycursor.execute("""INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2010', "First spacecraft to orbit Moon's Lagrange point (L2)", 'USA', 'ARTEMIS-P1')""")
#4
    mycursor.execute("""INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2010', "First spacecraft to orbit the Moon's Lagrange 1 point", 'USA', 'ARTEMIS-P2')""")
#5
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2011', 'First orbit of Mercury', 'USA', 'MESSENGER')")
#6  
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2011', 'First orbit of an object in the asteroid belt (4 Vesta)', 'USA', 'Dawn')")
#7
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2012', 'First use of a sky crane to land on MOON', 'USA', 'MSL')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2012', 'First spacecraft to leave the heliosphere', 'USA', 'Voyager 1')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2013', 'First laser communication with a lunar satellite', 'USA', 'LRO')")
#10  
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2014', 'First spacecraft to orbit a comet nucleus(67P/Churyumov Gerasimenko)', 'ESA', 'Rosetta')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2014', 'First soft landing on a comet (67P/Churyumov Gerasimenko)', 'ESA', 'Philae')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First flyby and orbit of a dwarf planet (Ceres)', 'USA', 'Dawn')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First flyby of an object beyond Neptune (Pluto and its moons)', 'USA', 'New Horizons')")
#14 
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First food grown in space eaten (lettuce)', 'USA,JAPAN', 'ISS')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First observation of gravitational waves', 'LSC EGO', 'LIGO Virgo')")
#16
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First propulsive landing of a rocket', 'USA', 'New Shepard 2')")
#17
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2015', 'First propulsive landing of an orbital rocket', 'USA', 'Falcon 9')")
#18 
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2016', 'First inflatable space habitat', 'USA', 'BEAM')")
#19
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2017', 'First spacecraft to enter the atmosphere of Saturn', 'USA,ESA,ITALY', 'Cassini Huygens')")
#20
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2017', 'First known interstellar object detected passing through the Solar System', 'USA', 'Oumuamua')")
#21
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2018', 'First operational rover on an asteroid (162173 Ryugu)', 'JAPAN', 'Hayabusa2')")
#22 
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2018', 'First recorded sounds from Mars', 'USA', 'InSight')")
#23
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2019', 'First flyby of a classical Kuiper belt object (486958 Arrokoth)', 'USA', 'New Horizons')")
#24
    mycursor.execute("""INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2019', 'First soft landing on the far side of the Moon', 'CHINA', "Chang'e 4")""")
#25
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2019', 'First direct photograph of a black hole and its vicinity', 'USA', 'EHT')")
#26 
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2021', 'First confirmed quake on MARS', 'USA', 'InSight')")
#27
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2021', 'First aerodynamically-powered flight on MARS', 'USA', 'Ingenuity')")
#28
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2021', 'First production of oxygen on MARS', 'USA', 'MOXIE')")
#29
    mycursor.execute("""INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2021', "First spacecraft to fly through the atmosphere of a star (the Sun's corona)", 'USA', 'Parker Solar Probe')""")
#30 
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2021', 'Launch of the largest space telescope to date', 'USA,ESA,CANADA', 'JSWT')")
#31
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2022', 'First asteroid measurably deflected by a spacecraft', 'USA', 'DART')")
#32
    mycursor.execute("INSERT IGNORE INTO ET_2010_AND_LATER(DATE, MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('2023', 'First landing at the lunar south pole on MOON', 'INDIA', 'Chandrayaan-3')")
    
    mydb.commit()
    
        
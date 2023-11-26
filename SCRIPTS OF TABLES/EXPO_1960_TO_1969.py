#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1960-1969)

def expo_1960_to_1969():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1960_TO_1969(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")
#1
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1960', 'First solar probe', 'USA', 'Pioneer 5')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1960', 'First plants and animals to return alive from Earth orbit', 'USSR', 'Sputnik 5')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1960', 'First rocket engine fired in spac', 'USA', 'Pioneer P-30')")
#4
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1960', 'First probe launched to Mars', 'USSR', 'Mars 1M')")
#5
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First hominidae in space(Ham)', 'USA', 'M-R 2')")
#6
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First launch from Earth orbit of upper stage into a heliocentric orbit', 'USSR', 'Venera 1')")
#7
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First human spaceflight (Yuri Gagarin)', 'USSR', 'Vostok 1')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First human-piloted space flight (Alan Shepard)', 'USA', 'Freedom 7')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First planetary flyby(venus)', 'USSR', 'Venera 1')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1961', 'First crewed space flight lasting over twenty four hours by Gherman Titov', 'USSR', 'Vostok 2')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First orbital solar observatory', 'USA', 'OSO-1')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First spacecraft to impact the far side of the Moon', 'USA', 'Ranger 4')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First communication between two crewed space vehicles in orbit', 'USSR', 'Vostok 3,4')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First auroral research rocket launched into the ionosphere', 'NORWAY', 'Ferdinand 1')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First Mars flyby (11,000 km) but contact was lost', 'USSR', 'Mars 1')")
#16 
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1962', 'First planetary flyby with data returned (Venus)', 'USA', 'Mariner 2')")
#17
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1963', 'First woman in space (Valentina Tereshkova)', 'USSR', 'Vostok 6')")
#18 
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1963', 'First reusable crewed spacecraft (suborbital)', 'USA', 'X-15 Flight 90')")
#19
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1964', 'First multi-person crew (3) in orbit', 'USSR', 'Voskhod 1')")
#20
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1965', 'First space walk/extra-vehicular activity (Alexei Leonov)', 'USSR', 'Voskhod 2')")
#21
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1965', 'First crewed spacecraft to change orbit', 'USA', 'Gemini 3')")
#22
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1965', 'First flyby of Mars (returned pictures)', 'USA', 'Mariner 4')")
#23
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1965', 'First photographs of another planet from deep space (Mars)', 'USA', '	Mariner 4')")
#24
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1965', 'First orbital rendezvous (parallel flight, no docking)', 'USA', 'Gemini 6A/Gemini 7')")
#25
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First soft landing on MOON', 'USSR', 'Luna 9')")
#26
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First impact into another planet (Venus)', 'USSR', 'Venera 3')")
#27 
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First orbital docking between two spacecraft', 'USA', 'Gemini 8')")
#28
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First artificial satellite around MOON', 'USSR', 'Luna 10')")
#29
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First soft-landing on the Moon', 'USA', 'Surveyor 1')")
#30
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1966', 'First picture of Earth from MOON', 'USA', 'Lunar Orbiter 1')")
#31
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1967', 'First polar orbit around the Moon', 'USA', 'Lunar Orbiter 4')")
#32
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1967', 'First photos of the Lunar south pole', 'USA', 'Lunar Orbiter 4')")
#33
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1967', 'First automated (crewless) docking', 'USSR', 'Cosmos 186/Cosmos 188')")
#34
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1967', 'First liftoff from MOON', 'USA', 'Surveyor 6')")
#35
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1968', 'First animals to travel to and around the Moon', 'USSR', 'Zond 5')")
#36
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1968', 'First orbital ultraviolet observatory', 'USA', 'OAO-2')")
#37
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1968', 'First human excursion beyond low Earth orbit', 'USA', 'Apollo 8')")
#38
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1968', 'First human flight to MOON and its gravity influence', 'USA', 'Apollo 8')")
#39
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', 'First crew exchange in space', 'USSR', 'Soyuz 4,5')")
#40
    mycursor.execute("""INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', "First spacecraft to parachute in Venus's atmosphere", 'USSR', 'Venera 5')""")
#41
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', 'First docking of two crewed spacecraft around another celestial body', 'USA', 'Apollo 10')")
#42
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', 'First human on The MOON', 'USA', 'Apollo 11')")
#43
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', 'First sample return from another celestial body', 'USA', 'Apollo 11')")
#44
    mycursor.execute("INSERT IGNORE INTO ET_1960_TO_1969(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1969', 'First meet up between human explorers and a robotic spacecraft in space', 'USA', 'Apollo 12/Surveyor 3')")
    
    mydb.commit()
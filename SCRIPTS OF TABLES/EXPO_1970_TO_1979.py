#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1970-1979)

def expo_1970_to_1979():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1970_TO_1979(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")
#1
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1970', 'First automatic sample return from the Moon', 'USSR', 'Luna 16')")  
#2  
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1970', 'First lunar rover', 'USSR', 'Lunokhod 1')")  
#3
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1970', 'First X-ray orbital observatory', 'USA', 'Uhuru')")  
#4
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1970', 'First soft landing on another planet (Venus)', 'USSR', 'Venera 7')")  
#5
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First space station', 'USSR', 'Salyut 1')")  
#6
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First crewed orbital observatory', 'USSR', 'Orion 1')")  
#7  
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First motor vehicle on another celestial body', 'USA', 'Apollo 15')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First spacecraft to orbit another planet (Mars)', 'USA', 'Mariner 9')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First spacecraft to impact another planet (Mars)', 'USSR', 'Mars 2')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1971', 'First signals from Martian surface', 'USSR', 'Mars 3')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1972', 'First spacecraft to use all-nuclear electrical power (SNAP-19 RTGs)', 'USA', 'Pioneer 10')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1972', 'First spacecraft to enter the asteroid belt', 'USA', 'Pioneer 10')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1972', 'First orbital gamma ray observatory', 'USA', 'SAS 2')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1973', 'First mission sent to study Mercury', 'USA', 'Mariner 10')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1973', 'First flyby of Jupiter', 'USA', 'Pioneer 10')")
#16
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1974', 'First spacecraft to return data on a long-period comet', 'USA', 'Mariner 10')")
#17
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1974', 'First use of solar wind for spacecraft orientation', 'USA', 'Mariner 10')")
#18
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1974', 'First flyby of Mercury', 'USA', 'Mariner 10')")
#19
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1974', 'First spacecraft to flyby the same planet multiple times (Mercury)', 'USA', 'Mariner 10')")
#20
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1975', 'First multinational crewed mission', 'USSR,USA', 'Apollo-Soyuz Test Project')")
#21
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1975', 'First spacecraft to orbit Venus', 'USSR', 'Venera 9')")
#22
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1975', 'First successful photos from the surface of another planet (Venus)', 'USSR', 'Venera 9')")
#23
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1976', 'First successful photos and soil samples from the surface of Mars', 'USA', 'Viking Lander')")
#24
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1978', 'First real time remotely operated ultraviolet orbital observatory', 'USA,ESA,UK', 'Int Ultraviolet Explorer')")
#25
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1978', 'First spacecraft to orbit the Sun at Lagrange 1', 'USA', 'ISEE-3/ICE')")
#26
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1978', 'First extended (multi-year) orbital exploration of Venus', 'USA', 'Pioneer Venus Orbiter')")
#27
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1979', 'Jupiter flyby', 'USA', 'Voyager 1')")
#28
    mycursor.execute("INSERT IGNORE INTO ET_1970_TO_1979(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1979', 'First flyby of Saturn', 'USA', 'Pioneer 11')")

    mydb.commit()
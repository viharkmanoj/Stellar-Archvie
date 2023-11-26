#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1900-1956)
def expo_1900_to_1956():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1900_TO_1956(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(50))")
#1 
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1903', 'Exploration of the Universe with Rocket-Propelled Vehicles publication', 'RUSSIA', 'Konstantin Tsiolkovsky')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1914', 'Goddard is awarded of patents on multistage and liquid-fueled rockets', 'UNITED STATES', 'Robert H. Goddard')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1917', 'First observation of an extrasolar planet', 'NETHERLANDS', 'Adriaan van Maanen')")
#4
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1919', 'Discussion of a Method of Reaching Extreme Altitudes', 'UNITED STATES', 'Robert H. Goddard')")
#5
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1923', 'Publication of Die Rakete zu den Planetenräumen', 'GERMANY', 'Hermann Oberth')")
#6
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1924', 'Society for Studies of Interplanetary Travel founded', 'USSR', 'Yuri Kondratyuk')")
#7
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1926', 'Goddard launches the first liquid-fueled rocket', 'UNITED STATES', 'Robert H. Goddard')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1927', 'Verein für Raumschiffahrt formed', 'GERMANY', 'By all top european scientists')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1927', 'Discussion on rocket mechanics and orbital effects', 'USSR', 'Yuri Kondratyuk')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1928', 'Discussion space travel and its potential uses', 'USSR', 'Herman Potočnik')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1928', 'Lippisch Ente, first successful rocket-powered full-size aircraft', 'GERMANY', 'Max Valier')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1929', 'Opel RAK.1, first successful public flight of a rocket-powered aircraft', 'GERMANY', 'Max Valier')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1933', 'British Interplanetary Society founded', 'UK', 'Philip E. Cleator')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1933', 'First detection of radio waves from an astronomical object', 'UNITED STATES', 'Karl Jansky')")
#15
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1933', 'Establishment of the Soviet rocket research lab', 'USSR', 'Valentin Glushko')")
#16
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1944', 'First spaceflight in history', 'GERMANY', 'V-2 rocket (MW 18014)')")
#17
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1945', 'First discussion of geostationary satellites as a means of communication', 'UK', 'Arthur C. Clarke')")
#18
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1946', 'First space research flight (cosmic radiation experiments)', 'UNITED STATES', 'Improved V-2 rocket')")
#19
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1946', 'First pictures of Earth from 105 km', 'UNITED STATES', 'V-2')")
#20
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1947', 'First animals in space (fruit flies)', 'UNITED STATES', 'V-2')")
#21
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1949', 'First two-stage liquid-fueled rocket', 'UNITED STATES', 'Bumper-5')")
#22
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1949', 'First mammal in space (Albert II, a rhesus monkey)', 'UNITED STATES', 'V-2')")
#23
    mycursor.execute("INSERT IGNORE INTO ET_1900_TO_1956(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1956', 'First rocket to pass the thermopause and enter the exosphere', 'UNITED STATES', 'Jupiter-C')")


    mydb.commit()
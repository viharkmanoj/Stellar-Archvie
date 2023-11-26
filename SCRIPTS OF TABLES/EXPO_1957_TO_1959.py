#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1957-1959)

def expo_1957_to_1959():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1957_TO_1959(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")

#1
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1957', 'First artificial satellite', 'USSR', 'Sputnik 1')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1957', 'First mammal in orbit (The dog Laika)', 'USSR', 'Sputnik 2')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1958', 'Confirmed existence of the Van Allen radiation belt', 'USA', 'Explorer 1')")
#4
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1958', 'First use of solar power in space', 'USA', 'Vanguard 1')")
#5
    mycursor.execute("""INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1959', "First spacecraft to attempt to impact the Moon's surface", 'USSR', 'Luna 1')""")
#6
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1959', 'First weather satellite', 'USA', 'Vanguard 2')")
#7  
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1959', 'First photograph of Earth from Earth orbit', 'USA', 'Explorer 6')")
#8    
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1959', 'First delivery of national pennants to a celestial body', 'USSR', 'Luna 2')")
#9  
    mycursor.execute("INSERT IGNORE INTO ET_1957_TO_1959(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1959', 'First photos of far side of moon from space', 'USSR', 'Luna 3')")

    mydb.commit()
#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (TIMELINE OF SPACE EXPLORATION DURIN 1970-1979)

def expo_1980_to_1989():
    mycursor.execute("CREATE TABLE IF NOT EXISTS ET_1980_TO_1989(\
                  DATE CHAR(4), \
                  MISSION VARCHAR(130) PRIMARY KEY, \
                  COUNTRY VARCHAR(20), \
                  MISSION_NAME VARCHAR(30))")

#1
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1980', 'Saturn flyby close encounter of Titan', 'USA', 'Voyager 1')")
#2
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1981', 'First reusable crewed orbital spacecraft (Space Shuttle)', 'USA', 'STS-1')")
#3
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1982', 'First Venus soil samples', 'USSR', 'Venera 13')") 
#4
    mycursor.execute("""INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1982', "First spacecraft to conduct a deep survey of Earth's magnetic tail", 'USA', 'ISEE-3/ICE')""")
#5
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1982', 'First mixed gender crew aboard space station', 'USSR', 'Salyut 7')")
#6
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1982', 'First plants grown in space (Arabidopsis)', 'USSR', 'Salyut 7')")
#7
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1983', 'First Infrared orbital observatory', 'USA,UK', 'IRAS')")
#8
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1983', 'First spacecraft beyond the orbit of Neptune', 'USA', 'Pioneer 10')")
#9
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1984', 'First untethered spacewalk (Bruce McCandless II)', 'USA', 'STS-41-B')")
#10
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1984', 'First spacewalk by a woman (Svetlana Savitskaya)', 'USSR', 'Salyut 7')")
#11
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1985', 'First balloon deployed on another planet (Venus)', 'USSR', 'Vega 1')")
#12
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1985', 'First spacecraft to flyby a comet (21P/Giacobini-Zinner)', 'USA', 'ISEE-3/ICE')")
#13
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1986', 'First spacecraft to flyby Uranus', 'USA', 'Voyager 2')")
#14
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1986', 'First consistently inhabited long-term research space station', 'USSR', 'MIR')")
#15
    mycursor.execute("""INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1986', "First close up observations of a comet (Halley's Comet)", 'ESA', 'Giotto')""")
#16
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1988', 'First suspected detection of an exoplanet Gamma Cephei Ab', 'CANADA', 'Bruce Campbell')")
#17
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1989', 'First astrometric satellite', 'ESA', 'Hipparcos')")
#18
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1989', 'First spacecraft to flyby Neptune', 'USA', 'Voyager 2')")
#19
    mycursor.execute("INSERT IGNORE INTO ET_1980_TO_1989(DATE , MISSION, COUNTRY, MISSION_NAME) VALUES\
            ('1989', 'First orbital cosmic microwave observatory', 'USA', 'COBE')")    

    mydb.commit()
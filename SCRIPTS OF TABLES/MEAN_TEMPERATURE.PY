import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")           

mycursor = mydb.cursor()

def MEAN_TEMPERATURE():
    mycursor.execute("CREATE TABLE IF NOT EXISTS MEAN_TEMPERATURE(\
        PLANET VARCHAR(50) PRIMARY KEY,\
        TEMPERATURE VARCHAR(50) )")
    
#1
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('MERCURY','333°F') ")
# 2
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('VENUS','867°F') ")
# 3
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('EARTH','59°F') ")
# 4
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('MARS','-85°F') ")
# 5
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('JUPITER','-160°F') ")
# 6
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('SATURN','-220°F') ")
# 7
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('URANUS','-320°F') ")
# 8
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('NEPTUNE','-330°F') ")
# 9
    mycursor.execute("INSERT IGNORE INTO MEAN_TEMPERATURE(PLANET,TEMPERATURE)\
        VALUES('PLUTO','-375°F') ")

    mydb.commit()

#END.....
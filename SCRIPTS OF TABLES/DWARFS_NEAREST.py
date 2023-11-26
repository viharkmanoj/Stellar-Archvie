import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")           

mycursor = mydb.cursor()


def DWARFS_NEAREST():
 mycursor.execute("CREATE TABLE IF NOT EXISTS DWARFS_NEAREST(\
      STAR VARCHAR(50) PRIMARY KEY,\
      DISTANCE VARCHAR(50))")
#1
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('SIRIUS B','8.58 LY')")
# 2
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('PROCYON B','11.43 LY')")
# 3
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('VAN MAANENS STAR','14.04 LY')")
# 4
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('GJ 440','15.09 LY')")
# 5
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('40 ERIDANI B','16.25 LY')")
# 6
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('STEIN 2051 B','18.06 LY')")
# 7
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('LP 44-113','20.0 LY')")
# 8
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('G 99-44','20.9 LY')")
# 9
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('L 97-12','25.8 LY')")
# 10
 mycursor.execute("INSERT IGNORE INTO DWARFS_NEAREST(STAR,DISTANCE)\
      VALUES('WOLF 489','26.7 LY')")


 mydb.commit()

#END....
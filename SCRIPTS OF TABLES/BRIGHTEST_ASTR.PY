#SYNTAX TO CONNECT PYTHON WITH DATABASE

import mysql.connector    
  
mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()
 

def BRIGHTEST_ASTRO():
    mycursor.execute("CREATE TABLE IF NOT EXISTS BRIGHTEST_ASTRO(\
        ASETROID VARCHAR(40) PRIMARY KEY,\
        MAGNITUDE VARCHAR(40),\
        SEMIMAJOR_AXIS VARCHAR(40),\
        ECCENTRICITY VARCHAR(45),\
        DIAMETER VARCHAR(40),\
        YEAR_OF_DISCOVERY VARCHAR(40))")

#1
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('99942 APOPHIS','3.4','0.922','0.191','0.32','2004')")
# 2
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('4 VESTA','5.20','2.361','0.089172','529','1807')")
# 3
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('2 PALLAS','6.49','2.773','0.230725','544','1802')")
# 4
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('1 CERES','6.65','2.766','0.079905','952','1801')")
# 5
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('7 IRIS','6.73','2.385','0.231422','200','1847')")
# 6
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('433 EROS','6.8','1.458','0.222725','4114','1898')")
# 7
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('153814 2001 WN5','6.85','1.711','0.467207','0.93','2001')")
# 8
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('367943 DUENDE','7.04','0.910','0.089319','0.0008','2012')")
# 9
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('6 HEBE','7.5','2.425','0.201726','186','1847')")
# 10
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('3 JUNO','7.5','2.668','0.258194','233','1804')")
# 11
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('18 MELPORMENE','7.5','2.296','0.218708','141','1852')")
# 12
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('152680 1998 KJ9','7.74','1.448','0.639770','0.5','1998')")
# 13
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('15 EUNOMIA','7.9','2.643','0.187181','268','1851')")
# 14
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('8 FLORA','7.9','2.202','0.156207','128','1847')")
# 15
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('324 BAMBERGA','8','2.682','0.338252','229','1892')")
# 16
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('1036 GANYMED','8.1','2.6657','0.533710','32','1924')")
# 17
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('9 METIS','8.1','2.387','0.121441','190','1879')")
# 18
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('192 NAUSIKAA','8.2','2.404','0.246216','103','1879')")
# 19
    mycursor.execute("INSERT IGNORE INTO BRIGHTEST_ASTRO(ASETROID,MAGNITUDE,SEMIMAJOR_AXIS,ECCENTRICITY,DIAMETER,YEAR_OF_DISCOVERY)\
        VALUES('20 MASSALIA','8.3','2.409','0.142880','145','1852')")

    mydb.commit()

#END.....
import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")           

mycursor = mydb.cursor()


def NEAREST_STAR():
 mycursor.execute("CREATE TABLE IF NOT EXISTS NEAREST_STAR(\
        STAR_SYSTEM VARCHAR(50) PRIMARY KEY,\
        DISTANCE_IN_LIGHT_YEAR VARCHAR(50),\
        STELLAR_TYPE VARCHAR(50),\
        OBSERVED_PLANETS VARCHAR(2))")

#1
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR, STELLAR_TYPE, OBSERVED_PLANETS)\
    VALUES('ALPHA CENTAURI','4.24-4.37','M;G;K','1')")
# 2
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('BARDNARDS STAR','5.96','M ','---')")
# 3
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WOLF 359','7.78','M','---')")
# 4
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LALANDE 21185','8.29','M','---')")
# 5
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('SIRIUS','8.58','A;D','---')")
# 6
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LUYTEN 726-8','8.73','M;M','---')")
# 7
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('ROSS 154','9.68','M','---')")
# 8
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('ROSS 248','10.32','M','---')")
# 9
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('EPSILON ERIDANI','10.52','K','2')")
# 10
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LACAILLE 9352','10.74','M','---')")
# 11
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('ROSS 128','10.92','M','---')")
# 12
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('EZ AQUARII','11.27','M;M;M','---')")
# 13
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('PROCYON','11.40','F;D','---')")
# 14
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('61 CYGNI','11.40','K;K','---')")
# 15
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('STRUVE 2398','11.53','M;M','---')")
# 16
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GROOMBRIDGE 34','11.62','M;M','---')")
# 17
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('EPSILON INDI','11.82','K;T;T','---')")
# 18
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('DX CANCRI','11.83','M','---')")
# 19
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('TAU CETI','11.89','G','5')")
# 20
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GJ 1061','11.99','M','---')")
# 21
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('YZ CETI','12.13','M','---')")
# 22
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LUYTEN STAR','12.37','M','---')")
# 23
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('TEEGARDEN STAR','12.51','M','---')")
# 24
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('SCR 1845-6357','12.57','M;T','---')")
# 25
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('KAPTEYN STAR','12.78','M','---')")
# 26
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LACAILLE 8760','12.87','M','---')")
# 27
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('KRUGER 60','13.15','M;M','---')")
# 28
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('DEN 1048-3956','13.17','M','---')")
# 29
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('UGPS 0722-05','13.26','T','---')")
# 30
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('ROSS 614','13.35','M;M','---')")
# 31
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WISE 1541-2250','13.70','Y','---')")
# 32
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WISE 0350-5658','13.70','Y','---')")
# 33
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WOLF 1061','13.82','M','---')")
# 34
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('VAN MAANEN STAR','14.07','D','---')")
# 35
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 1','14.23','M','---')")
# 36
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WOLF 424','14.31','M;M','---')")
# 37
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('TZ ARIETIS','14.51','M','---')")
# 38
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 687','14.80','M','---')")
# 39
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LHS 292','14.80','M','---')")
# 40
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 674','14.81','M','1')")
# 41
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GJ 1245','14.81','M;M;M','---')")
# 42
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 440','15.06','D','---')")
# 43
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GJ 1002','1531','M','---')")
# 44
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 876','15.34','M','4')")
# 45
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LHS 288','15.61','M','---')")
# 46
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('WISE 1405+5534','15.76','Y','---')")
# 47
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 412','15.83','M;M','---')")
# 48
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GROOMBRIDGE 1618','15.85','K','---')")
# 49
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('AD LEONIS','15.94','M','---')")
# 50
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('DENIS J081730.0-615520','16.07','T','---')")
# 51
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('GLIESE 832','16.08','M','1')")
# 52
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('LP 944-020','16.19','M','---')")
# 53
 mycursor.execute("INSERT IGNORE INTO NEAREST_STAR(STAR_SYSTEM, DISTANCE_IN_LIGHT_YEAR,STELLAR_TYPE,OBSERVED_PLANETS)\
    VALUES('DEN 0255-4700','16.20','L','---')")

 mydb.commit()

#END......
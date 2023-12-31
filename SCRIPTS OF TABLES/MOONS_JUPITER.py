#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (MOONS OF JUPITER)

def jupiter_moons():
    mycursor.execute("CREATE TABLE IF NOT EXISTS jupiter_moons(\
                  NAME VARCHAR(50) PRIMARY KEY, \
                  ABS_MAGN VARCHAR(50),\
                  DIAMETER VARCHAR(50), \
                  MASS VARCHAR(50), \
                  SEMIMAJOR_AXIS VARCHAR(50),\
                  ORBITAL_PERIOD VARCHAR(50),\
                  ORBITAL_INCLINATION VARCHAR(50),\
                  ECCENTRICITY VARCHAR(50),\
                  DISCOVERY_YEAR VARCHAR(50),\
                  DISCOVERER VARCHAR(50))")

#1
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('METIS','10.5','43','≈3,6','128000','+0.2948','0.060','0.0002','1979','SYNNOTT')")
#2
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ADRASTEA','12','16.4','≈0.20','129000','+0.2983','0.030','0.0015','1979','JEWITT')")
#3
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('AMALTHEA','7.1','167','208','181400','+0.4999','0.374','0.0032','1892','BARDNARD')")
#4
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('THEBE','9','98.6','≈43','221900','+0.6761','1.076','0.0175','1979','SYNNOTT')")
#5
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('IO','-1.7','3643.2','8931800','421800','+1.7627','0.050','0.0041','1610','GALLILEO')")
#6
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EUROPA','-1.4','3121.6','4799800','671100','+3.5255','0.470','0.0090','1610','GALILEO')")
#7
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('GANYMEDE','-2.1','5268.2','14819000','1070400','+7.1556','0.200','0.0013','1610','GALILEO')")
#8
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CALLISTO','-1.2','4820.6','10759000','1882700','+16.690','0.192','0.0074','1610','GALLILEO')")
#9
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('THEMISTO','13.3','≈9','≈0.038','7398500','+130.03','43.8','0.340','1975/2000','SHEPPARD ET AL')")
#10
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('LEDA','12.7','21.5','≈0.52','11146400','+240.93','28.6','0.162','1974','KOWAL')")
#11
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ERSA','16.0','≈3','≈0.0014','11401000','+249.23','29.1','0.116','2018','SHEPPARD')")
#12
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2018 J 2','16.5','≈3','≈0.0014','11419700','+249.92','28.3','0.152','2018','SHEPPARD')")
#13
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HIMALIA','8.0','139.6','420','11440600','+250.56','28.1','0.160','1904','PERRINE')")
#14
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('PANDIA','16.2','≈3','≈0.0014','1148100','+251.91','29.0','0.179','2017','SHEPPARD')")
#15
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('LYSITHEA','11.2','42.2','≈3.9','11700800','+259.20','27.2','0.117','1938','NICHOLSON')")
#16
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ELARA','9.7','79.9','≈27','11712300','+259.64','27.9','0.211','1905','PERRINE')")
#17
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2011 J 3','16.3','≈3','≈0.0014','11716800','+259.84','27.6','0.192','2011','SHEPPARD')")
#18
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('DIA','16.1','≈4','≈0.0034','12260300','+278.21','29.0','0.232','2000','SHEPPARD ET AL')")
#19
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2018 J 4','16.7','≈2','≈0.00042','16328500','+427.63','50.2','0.177','2018','SHEPPARD')")
#20
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CARPO','16.2','≈3','≈0.0014','17042300','+456.29','53.2','0.416','2003','SHEPPARD')")
#21
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('VALETUDO','17.0','≈1','≈0.000052','18694200','+527.61','34.5','0.217','2016','SHEPPARD')")
#22
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EURORIE','16.3','≈2','≈0.00042','19265800','-550.69','145.7','0.148','2001','SHEPPARD ET AL')")
#23
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 18','16.4','≈2','≈0.00042','20336300','-598.12','145.3','0.090','2003','GLADMAN')")
#24
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EUPHEME','16.6','≈2','≈0.00042','20768600','-617.73','148.0','0.241','2003','SHEPPARD')")
#25
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J 3','17.2','≈2','≈0.00042','20776700','-618.33','147.9','0.239','2021','SHEPPARD')")
#26
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2010 J 2','17.4','≈1','≈0.000052','20793000','-618.84','148.1','0.248','2010','VEILLET')")
#27
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2016 J 1','17.0','≈1','≈0.000052','20802600','-618.49','144.7','0.232','2016','SHEPPARD')")
#28
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('MNEME','16.3','≈2','≈0.00042','20821000','-620.07','148.0','0.247','2003','GLADMAN')")
#29 
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EURANTHE','16.4','≈3','≈0.0014','20827000','-620.44','148.0','0.239','2001','SHEPPARD ET AL')")
#30                                                                            
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 16','16.3','≈2','≈0.00042','20882600','-622.88','148.0','0.243','2003','GLADMAN')")
#31
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HARPALYKE','15.9','≈4','≈0.0034','20892100','-623.32','147.7','0.232','2000','SHEPPARD ET AL')")
#32
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ORTHOSIE','16.6','≈2','≈0.00042','20901000','-622.59','144.3','0.299','2003','SHEPPARD')")
#33
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HELIKE','16','≈4','≈0.0034','20915700','-626.33','154.4','0.153','2021','SHEPPARD')")
#34
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J2','17.3','≈1','≈0.000052','20926600','-625.14','148.1','0.242','2021','SHEPPARD')")
#35
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('PRAXIDIKE','14.9','7','≈0.018','20935400','-625.39','148.3','0.246','2000','SHEPPARD ET AL')")
#36
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J3','16.5','≈2','≈0.00042','20941000','-625.60','147.9','0.231','2017','SHEPPARD')")
#37
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J1','17.3','≈1','≈0.000052','20954700','-627.14','150.5','0.228','2021','SHEPPARD')")
      
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J12','17','≈1','≈0.000052','20963100','-627.24','150','0.235','2003','SHEPPARD')")
#38
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J7','16.6','≈2','≈0.00042','20964800','-626.56','147.3','0.233','2017','SHEPPARD')")
#39
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('THELXINOE','16.3','≈2','≈0.00042','20976000','-628.03','150.6','0.228','2003','GLADMAN ET AL')")
#40
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('THYONE','15.8','≈4','≈0.0034','20978000','-627.18','147.5','0.233','2001','SHEPPARD ET AL')")
#41
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J2','16.7','≈2','≈0.00042','20997700','-628.79','150.2','0.225','2003','SHEPPARD')")
#42
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ANANKE','11.7','29.1','≈1.3','21034500','-629.79','147.6','0.237','1951','NICHOLSON')")
#43
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2022 J 3','17.4','≈1','≈0.000052','21047700','-630.67','148.2','0.249','2022','SHEPPARD')")
#44
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('LOCASTE','15.5','≈5','≈0.0065','21066700','-631.59','148.8','0.227','2000','SHEPPARD ET AL')")
#45
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HERMIPPE','15.5','≈4','≈0.0034','21108500','-633.90','150.2','0.219','2001','SHEPPARD ET AL')")
#46
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 9','16.2','≈3','≈0.0014','21768700','-666.11','155.5','0.200','2017','SHEPPARD')")
#47
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('PHILOPHROSYNE','16.7','≈2','≈0.00042','22604600','-702.54','146.3','0.229','2003','SHEPPARD')")
#48
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2016 J 3','16.7','≈2','≈0.00042','22719300','-713.64','164.6','0.251','2016','SHEPPARD')")
#49
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2022 J 1 ','17','≈1','≈0.000052','22725200','-738.33','164.5','0.257','2022','SHEPPARD')")
#50
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('PASITHEE','16.8','≈2','≈0.00042','22846700','-719.47','164.6','0.270','2001','SHEPPARD ET AL')")
#51
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 8','17.1','≈1','≈0.000052','22849500','-719.76','164.8','0.255','2017','SHEPPARD')")
#52
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J 6','17.3','≈1','≈0.000052','22870300','-720.97','164.9','0.271','2021','SHEPPARD ET AL')")
#53
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 24','16.6','≈2','≈0.00042','22887400','-721.60','164.5','0.259','2003','SHEPPARD ET AL')")
#54
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EURYDOME','16.2','≈3','≈0.0014','22899000','-717.31','149.1','0.294','2001','SHEPPARD ET AL')")
#56
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2011 J2','16.8','≈1','≈0.000052','22909200','-718.32','151.9','0.355','2011','SHEPPARD')")
#57
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 4','16.7','≈2','≈0.00042','22926500','-718.10','148.2','0.328','2003','SHEPPARD')")
#58
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CHALDENE','16','≈4','≈0.0034','22930500','-723.71','164.7','0.265','2000','SHEPPARD ET AL')")
#59
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 2 ','16.4','≈2','≈0.00042','22953200','-724.71','164.5','0.272','2017','SHEPPARD ET AL')")
#60
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ISONOE','16','≈4','≈0.0034','22981300','-726.27','164.8','0.249','2000','SHEPPARD ET AL')")
#61
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2022 J 2','17.6','≈1','≈0.000052','23013800','-781.56','164.7','0.265','2022','SHEPPARD')")
#62
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J 4','17.4','≈1','≈0.000052','23019700','-728.28','164.6','0.265','2021','SHEPPARD')")
#63
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('KALLICHORE','16.3','≈2','≈0.00042','23021800','-728.26','164.8','0.252','2003','SHEPPARD')")
#64
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ERINOME','16','≈3','≈0.0014','23032900','-728.48','164.4','0.276','2000','SHEPPARD ET AL')")
#65
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('KALE','16.3','≈2','≈0.00042','23052600','-729.64','164.6','0.262','2001','SHEPPARD ET AL')")
#66
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EIRENE','15.8','≈4','≈0.0034','23055800','-729.84','164.6','0.258','2003','SHEPPARD')")
#67
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('AITNE','16','≈3','≈0.0014','23064400','-730.00','164.6','0.277','2001','SHEPPARD ET AL')")
#68
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('EUKELADE','16','≈4','≈0.0034','23067400','-730.30','164.6','0.277','2003','SHEPPARD')")
#69
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('ARCHE','16.2','≈3','≈0.0014','23097800','-731.88','164.6','0.261','2002','SHEPPARD')")
#70
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('TAYGETE','15.6','≈5','≈0.0065','23108000','-732.45','164.7','0.253','2000','SHEPPARD ET AL')")
#71
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2016 J 4','17.3','≈1','≈0.000052','23113800','-727.01','147.1','0.294','2016','SHEPPARD')")
#72
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2011 J 1','16.7','≈2','≈0.00042','23124500','733.21','164.6','0.271','2011','SHEPPARD')")
#73
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CARME','10.6','46.7','≈5.3','23144400','-734.19','164.8','0.256','1938','NICHOLSON')")
#74
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HERSE','16.5','≈2','≈0.00042','23150500','-734.52','164.4','0.262','2003','GLADMAN ET AL')")
#75
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 19','16.6','≈2','≈0.00042','23156400','-734.78','164.7','0.265','2003','GLADMAN')")
#76
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2010 J 1','16.5','≈2','≈0.00042','23189800','-736.51','164.5','0.252','2011','JACOBSON ET AL')")
#77
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 9','16.9','≈1','≈0.000052','23199400','-736.86','164.8','0.263','2003','SHEPPARD')")
#78
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 5','16.5','≈2','≈0.00042','23206200','-737.28','164.8','0.257','2018','SHEPPARD')")
#79
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 6','16.6','≈2','0.017','23302600','-742.02','164.8','0.260','2001','SHEPPARD')")
#80
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('KALYKE','15.4','6.9','≈0.017','23302600','-742.02','164.8','0.260','2001','SHEPPARD ET AL')")
#81
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('HEGEMONE','15.9','≈3','≈0.0014','23348700','-739.81','152.6','0.358','2003','SHEPPARD')")
#82
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2018 J 3','17.3','≈1','≈0.00052','23400300','-747.02','164.9','0.268','2023','SHEPPARD')")
#83
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2021 J 5','16.8','≈2','≈0.00042','23414600','-747.74','164.9','0.272','2023','SHEPPARD ET AL')")
#84
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('PASIPHAE','10.1','57.8','≈10','23468200','-743.61','148.4','0.412','1908','MELOTTE')")
#85
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('SPONDE','16.7','≈2','≈0.00042','23543300','-748.29','149.3','0.322','2002','SHEPPARD ET AL')")
#86
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 10','16.9','≈2','0.00042','23576300','-755.43','164.4','0.264','2003','SHEPPARD')")
#87
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('MEGACLITE','15','≈5','≈0.0065','23644600','-752.86','149.8','0.421','2001','SHEPPARD ET AL')")
#88
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CYLLENE','16.3','≈2','≈0.00042','23654700','-751.97','146.8','0419','2003','SHEPPARD')")
#89
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('SINOPE','11.1','35','≈2.2','23683900','-758.85','157.3','0.264','1914','NICHOLSON')")
#90
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2017 J 1','16.8','≈2','≈0.00042','23744800','-756.41','145.8','0.328','2017','SHEPPARD')")
#91
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('AOEDE','15.6','≈4','≈0.0034','23778200','-761.42','155.7','0.436','2003','SHEPPARD')")
#92
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('AUTONOE','15.5','≈4','≈0.0034','23792500','-761.00','150.8','0.330','2001','SHEPPARD ET AL')")
#93
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('CALLIRRHOE','14.0','9.6','≈0.046','23795500','-758.87','145.1','0.297','1999','Scotti et al')")
#94
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('S/2003 J 23','16.6','≈2','≈0.00042','23829300','-760.00','144.7','0.313','2003','SHEPPARD')")
#95
    mycursor.execute("INSERT IGNORE INTO jupiter_moons(NAME, ABS_MAGN, DIAMETER, MASS, SEMIMAJOR_AXIS, ORBITAL_PERIOD, ORBITAL_INCLINATION, ECCENTRICITY, DISCOVERY_YEAR, DISCOVERER) VALUES\
      ('KORE','16.6','≈2','≈0.00042','24205200','-776.76','141.5','0.328','2003','SHEPPARD')")

    mydb.commit()

#END...
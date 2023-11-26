#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (HABITABLE EXOPLANETS)

def habitable_exoplanets():
    mycursor.execute("CREATE TABLE IF NOT EXISTS habitable_exoplanets(\
                  OBJECT VARCHAR(50) PRIMARY KEY, \
                  STAR VARCHAR(50), \
                  STAR_TYPE VARCHAR(40), \
                  MASS VARCHAR(50),\
                  RADIUS VARCHAR(50),\
                  DENSITY VARCHAR(50),\
                  FLUX VARCHAR(50),\
                  TEMPERATURE VARCHAR(50),\
                  PERIOD VARCHAR(50),\
                  DISTANCE VARCHAR(50))")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('EARTH','SUN','G2V','1.00','1.00','5.514','1.00','255','365.25','0')")
    
    mycursor.execute("""INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ("TEEGARDEN'S STAR B","TEEGARDEN'S",'M7V','>=1.05','~1.02','-','1.15','264','4.91','12.5')""")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TOI-700 D','TOI 700','M2V','~1.72','1.14','-','0.87','246','37.4','101')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1649C','KEPLER-1649','M5V','~1.20','1.06','-','0.75','237','19.5','301')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TRAPPIST-1D','TRAPPIST-1','M8V','0.39','0.78','3.39','1.12','258','4.05','41')")
    
    mycursor.execute("""INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('LUYTEN B',"LUYTEN'S STAR",'M3V','>=2.89','~1.35','-','1.06','258','4.05','41')""")
    
    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('LP 890-9 C','LP 890-9','M6V','-','1.37','-','0.91','272','8.46','105')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('K2-72E','K2-72','M?V','~2.21','1.29','-','1.30','261','24.2','217')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 1061 D','GLIESE 1061','M5V','>=1.64','~1.16','-','0.69','218','13.0','12')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 1002 B','GELIESE 1002','M5V','>=1.08','~1.03','-','0.667','231','10.3','15.8')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 1061 C','GELIESE 1061','M5V','>=1.74','~1.18','-','1.45','275','6.7','12')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-296E','KEPLER-296','K7V','~2.96','1.52','-','1.00','276','34.1','737')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('WOLF 1069 B','WOLF 1069','M5V','>=1.26','~1.08','-','0.65','250','15.6','31.2')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TRAPPIST-1E','TRAPPIST-1','M8V','0.69','0.92','5.65','0.65','230','6.1','41')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('PROXIMA CENTURI B','PROXIMA CENTURI','M5V','>=1.27','~1.30','-','0.70','228','11.186','4.25')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-442B','KEPLER-442','K5V','~2.36','1.35','-','0.70','233','112.3','1193')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-62F','KEPLER-62','K2V','~2.8','1.41','-','0.41','204','267.3','981')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TRAPPIST-1F','TRAPPIST-1','M8V','1.04','1.04','3.3±0.9','0.37','200','9.2','41')")

    mycursor.execute("""INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ("TEEGRADEN'S STAR C",'TEEGARDENS STAR','M7V','','~1.04','-','0.37','199','11.4','12.5')""")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1229B','KEPLER-1229','M?V','~2.54','1.40','-','0.32','213','86.8','865')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-186F','KEPLER-186','M1V','~1.71','1.17','-','0.29','188','129','579')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TRAPPIST-1G','TRAPPIST-1','M8V','1.32','1.13','4.186','0.25','182','12.4','41')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 1002 C','GELIESE 1002','M5V','>=1.36','~0.12','-','0.26','182','21.2','15.8')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLE-452B','KEPLER-452','G2V','~5','1.63','-','1.11','261','384.8','1799')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-62E','KEPLER-62','K2V','~4.5','1.61','-','1.15','264','122.4','981')")
    
    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER 1625B','KEPLER-1625','M?V','-','1.60','-','0.84','244','38.1','822')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('WOLF 1061C','WOLF 1061','M3V','>=3.14','~1.60','-','1.30','271','17.9','13.8')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1410B','KEPLER-1410','K?V','-','1.78','-','1.07','274','60.9','1196')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 667 CC','GELIESE 667 C','M1V','>=3.81','~1.54','-','0.88','277','28.1','23.62')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1544 B','KEPLER-1544','K2V','-','1.78','-','0.84','248','168.8','1092')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-283C','KEPLER-283','K5V','-','1,82','-','0.89','248','92.7','1526')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('ROSS-508 B','ROSS-508','M4V','>=4.00','-','-','1.32','-','10.8','37')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1638B','KEPLER-1638','G4V','-','1.87','-','1.39','276','259.3','4973')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('ROSS 128 B','ROSS 128','>=1.40','M4V','~1.80','-','1.48','280','9.87','11.0')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-440 B','KEPLER-440','K6V','-','1.91','-','1.44','273','101.1','981')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE-443 D','GELIESE-443','M2V','>=5.22','-','-','1.06','','36.1','29.6')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1653B','KEPLER-1635','K?V','-','2.17','-','1.04','258','140.3','2461')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-705B','KEPLER-705','M?V','-','2.11','-','0.77','243','56.1','903')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('K2-332B','K2-332B','M?V','-','2.20','-','1.17','','17.7','402')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-155C','KEPLER-155','MOV','-','2.24','-','1.05','','52.7','957')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('TOI-2257 B','TO-2257','M3V','-','2.24','-','1.05','','35.2','188')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-443B','KEPLER-443','K3V','-','2.35','-','0.89','247','177.7','2615')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-22B','KEPLER-22','G5V','-','2.38','-','1.10','261','289.9','635')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1701B','KEPLER-1701','K?V','-','2.22','-','1.42','275','169.1','1904')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1606B','KEPLER-1606','G?V','-','2.07','-','1.64','277','196.4','2710')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('K2-9B','K2-9','M2V','-','2.25','-','1.45','279','18.4','270')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 180 C','GELIESE 180','M2V','>=6.40','-','-','0.78','239','18.4','39')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GELIESE 163 C','GELIESE 163','M3V','>=6.80','-','-','1.25','277','25.6','49')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-1540B','KEPLER-1540','K?V','-','2.49','-','0.78','250','125.4','799')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-174D','KEPLER-174','K3V','-','2.19','-','0.59','206','247.4','1254')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('HD 40307 G','HD 40307','K2V','>=7.09','-','-','0.67','226','197.8','42')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('KEPLER-296F','KEPLER-296','K7V','-','1.80','-','0.44','225','63.3','737')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('HIP 38594 B','HIP 38594','MOV','>=8.10','-','-','1.34','','60.7','58')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('K2-288BB','K2-288 B','M3V','-','1.91','-','0.44','207','31.4','214')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('HD 216520 C','HD 216520','KOV','>=9.44','-','-','1.28','','154.4','64')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 3293 D','GLIESE 3293','M2V','>=7.60','-','-','0.59','223','48.1','66')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('LHS 1140 B','LHS 1140','M4V','6.38','1.64','7.82','0.36','214','24.7','49')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLEISE 357 D','GLIESE 357','M2V','>=6.10','-','-','0.38','200','55.7','31')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 299 C','GELIESE 299','M1V','>=8.57','-','-','0.44','216','121.9','18.8')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 514 B','GLIESE 514','M1V','>=5.20','-','-','0.27','202','140.4','25')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 180 D','GLIESE 180','M2V','>=7.56','-','-','0.26','','106.3','39')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('GLIESE 625B','GLIESE 625','M2V','>=2.82','-','-','','','14.628','21.1')")

    mycursor.execute("INSERT IGNORE INTO habitable_exoplanets(OBJECT, STAR, STAR_TYPE, MASS, RADIUS, DENSITY, FLUX, TEMPERATURE, PERIOD, DISTANCE) VALUES\
      ('L 98-59 F','L 98-59','M3V','>=2.46','-','-','>1','~280','23.15','34.6')")

    mydb.commit()

#END...
#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

def GAL_LESSER():
  mycursor.execute("CREATE TABLE IF NOT EXISTS GAL_LESSER(\
      GALAXY_NAME VARCHAR(50) PRIMARY KEY,\
      MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR VARCHAR(50),\
      MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR VARCHAR(50),\
      MORPHOLOGY VARCHAR(50),\
      ESTIMATION_METHOD VARCHAR(50)\
      )")

 # 1
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 444-46','6707x10^2','3823x10^2','cD4;E4;BrCIG','27.0 B-MAG ARCSEC^-2')")
 # 2
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('TADPOLE GALAXY','5584x10^2','1117x10^2','SB(s)C PEC','25.0 B-MAG ARCSEC^-2')")
 # 3
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('IC 1101','5532x10^2','4497x10^2','cD;S0','2MASS K-BAND TOTAL MAG')")
 # 4
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2261 BCG','5446x10^2','53338x10^2','cD;E','2MASS K-BAND TOTAL MAG')")
 # 5
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('HERCULES A','4598x10^2','2851x10^2','E;WLRG;NLRG','2MASS K-BAND TOTAL MAG')")
 # 6
  mycursor.execute("""INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ("UGC 2885 (RUBIN'S GALAXY)",'4381x10^2','2015x10^2','SA(rs)c','25.0 B-MAG ARCSEC^-2')""")
 # 7
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 1399','4123x10^2','3793x10^2','cD;E1 PEC','90% TOTAL B-LIGHT')")
 # 8
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NEVE 1','3321x10^2','2391x10^2','cD;E','2MASS K-BAND TOTAL MAG')")
 # 9
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ALCYONEUS','2429x10^2','1554x10^2','E','25.0 B-MAG ARCSEC^-2')")
 # 10
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ANDROMEDA GALAXY','1523x10^2','1523x10^2','SA(s)B','25.0 B-MAG ARCSEC^-2')")
 # 11
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('MESSIER 87','1188x10^2','9387x10','cD;E0-E1 PEC;NLRG;SY','25.0 B-MAG ARCSEC^-2')")
 # 12
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('MALLIN 1','1187x10^2','1187x10^2','S;LSB','2MASS K-BAND TOTAL MAG')")
 # 13
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 262','1011x10^2','7886x10','SA(s)0/a;Sy2','2MASS K-BAND TOTAL MAG')")
 # 14
  mycursor.execute("INSERT IGNORE INTO GAL_LESSER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('MILKY WAY','874x10^2±359x10','874x10^2±359x10','Sb;Sbc;SB(rs)bc','25.0 B-MAG ARCSEC^-2')")
    
  mydb.commit()

#END........
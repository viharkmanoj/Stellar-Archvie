#SYNTAX TO CONNECT PYTHON WITH DATABASE.
import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

def GAL_GREATER():
  mycursor.execute("CREATE TABLE IF NOT EXISTS GAL_GREATER(\
      GALAXY_NAME VARCHAR(50) PRIMARY KEY,\
      MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR VARCHAR(50),\
      MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR VARCHAR(50),\
      MORPHOLOGY VARCHAR(50),\
      ESTIMATION_METHOD VARCHAR(50)\
      )")

#1
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 383-76','1764x10^3','8821x10^2','cD5; E5; BrCIG','90% TOTAL B-light')")
 #2 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 248-6','1731x10^3','8307x10^2','S0?; BrCIG','90% TOTAL B-LIGHT')")
 #3 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 409-25','1454x10^3','9017x10^2','cD4; E4; BrCIG','90% TOTAL B-LIGHT')") 
 #4 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('Abell 3039 BCG B','129x10^4','4386x10^2','cD','2MASS K-BAND TOTAL MAG')")
 #5 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('2MASX J14102504+6337103','1134x10^3','1134x10^3','~','2MASS K-BAND TOTAL MAG')")
 #6 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 151-41','1132x10^3','453x10^3','Sc','90% TOTAL B-LIGHT')")
 #7 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('MCG-04-02-013','1115x10^3','1115x10^3','E','27.0 B-MAG ARCSEC^-2')")
 #8
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1576 BCG','1077x10^3','5172x10^2','cD db','2MASS K-BAND TOTAL MAG')")
 #9 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 306-17','1070x10^3','7061x10^2','cD3;E3','90%TOTAL B-LIGHT')")
 #10
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 350-15','1043x10^3','5216x10^2','cD3;E3','90% TOTAL B-LIGHT')")
 #11
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2397 BCG','1014x10^3','5883x10^2','cD','2MASS K-BAND TOTAL MAG')")
 #12 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1146 BCG','1009x10^3','7671x10^2','E','2MASS K-BAND TOTAL MAG')")
 #13 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 747 BCG','9953x10^2','4379x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 #14 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 1273002','9754x10^2','4194x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 #15 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 1838034','9586x10^2','5177x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 #16
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 473-5','9446x10^2','5177x10^2','Sc;BrCIG','90% TOTAL B-LIGHT')")
 #17
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1942 BCG','9392x10^2','6387x10^2','BrCIG;AGN','2MASS K-BAND TOTAL MAG')")
 # 18
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA1654332','9164x10^2','6231x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 19
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 384 BCG','9139x10^2','2742x10^2','~','2MASS K-BAND TOTAL MAG')")
 # 20
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 697 BCG','8852x10^2','6374x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 21
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 3300 BCG','8788x10^2','3867x10^2','cD','2MASS K-BAND TOTAL MAG')")
 # 22
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('OGC 666','8763X10^2','4557X10^2','BrClG','2MASS K_band TOTAL MAG')")
 # 23
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1437B BCG','8683x10^2','5384x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 24
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 443-11','8665x10^2','4073x10^2','cD;SAB0 PEC;BrCIG','27.0 B-MAG ARCSEC^-2')")
 # 25
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('4C+41.26','8623x10^2','7244x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 26
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 963 BCG','8421x10^2','6057x10^2','BrClG','2MASS K-BAND TOTAL MAG')")
 # 27
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 541-13','8407x10^2','6557x10^2','cD;E3 PEC','90% TOTAL B-LIGHT')")
 # 28
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('MACS J0024.5+3321 BCG','8306x10^2','5482x10^2','~','2MASS K-BAND TOTAL MAG')")
 # 29
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1602 BCG','822x10^3','5754x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 30
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 623','8039x10^2','611x10^3','cD;E','27.0 B-MAG ARCSEC^-2')")
 # 31
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('PGC 6616','8038x10^2','4019x10^2','E','27.0 B-MAG ARCSEC^-2')")
 # 32
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1413 BCG','8014x10^2','2564x10^2','cD;E;BrCIG','25.0 R-MAG ARCSEC^-2')")
 # 33
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 291-9','7951x10^2','4612x10^2','cD4;SA0;BrCIG','90% TOTAL B-LIGHT')")
 # 34
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1504 BCG','7902x10^2','4583x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 35 
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 1816387','7825x10^2','3365x10^2','~','2MASS K-BAND TOTAL MAG')")
 #36
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NVSS J080730+340042','7809x10^2','3592x10^2','BrCIG','2MASS K-BAND TOTAL MAG TOTAL MAG')")
 # 37
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 2463193','7797x10^2','4678x10^2','~','2MASS K-BAND TOTAL MAG')")
 # 38
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 812','7729x10^2','541x10^3','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 39
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('7C 1043+59237C','771x10^3','4009x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 40
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1785B BCG','7698x10^2','5081x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 41
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 2463193','7695x10^2','7695x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 42
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 781 ','7665x10^2','3373x10^2','BrCIG','25.0 R-MAG ARCSEC^-2')")
 # 43
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 655  ','760x10^3','5776x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 44
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 1460988','7555x10^2','4382x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 45
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 4308','752X10^3','5414X10^2','SB(S)M PEC','27.0 B-MAG ARCSEC^-2')")
 # 46
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('2MASX J01331683+2311233','7517x10^2','2781x10^2','~','2MASS K-BAND TOTAL MAG')")
 # 47
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 908 BCG  ','7502x10^2','5551x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 49
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2061 B','7477x10^2','5832x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 50
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2397 G1','7457x10^2','4325x10^2','cD','2MASS K-BAND TOTAL MAG')")
 # 51
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 198-1','7416x10^2','5636x10^2','cD4;E4','27.0 B-MAG ARCSEC^-2')")
 #bruh
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('3C 295','738x10^3','738x10^3','E/SO;LEG;BrCIG NLRG','2MASS K-BAND TOTAL MAG')")
 # 52
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 267 BCG','7367x10^2','302x10^3','BrCIG','25.0 R-MAG ARCSEC^-2')")
 # 53
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1758N BCG','7315x10^2','3219x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 54
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 360 BCG','7277x10^2','3639x10^2','cD','2MASS K-BAND TOTAL MAG')")
 # 55
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 251-21','7277x10^2','4584x10^2','SAB0-PEC;E/SO','90% TOTAL B-LIGHT')")
 # 56
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 2188433','7216x10^2','7216x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 57
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 1807 BCG','7202x10^2','4753x10^2','cD','2MASS K-BAND TOTAL MAG')")
 # 58
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 6872','717x10^3','1434x10^2','SAB(rs)C','25.5 R-MAG ARCSEC^-2')")
 # 59
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL S1077 BCG','7169x10^2','3728x1062','~','2MASS K-BAND TOTAL MAG')")
 # 60
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2125 BCG','7152x10^2','5152x10^2','E','2MASS K-BAND TOTAL MAG ')")
 # 61
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('B3 1715+425','7152x10^2','472x10^3','BrCIG;AGN','2MASS K-BAND TOTAL MAG')")
 # 62
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL 2219 BCG','7134x10^2','3853x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 63
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 552-20','710x10^3','4118x10^2','cD;E','90% TOTAL B-LIGHT')")
 # 64
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ESO 11-4','7074x10^2','4881x10^2','cD4;E4 PEC','90% TOTAL B-LIGHT')")
 # 65
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('IC 1633','7057x10^2','5434x10^2','cD;E1','27.0 B-MAG ARCSEC^2')")
 # 66
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 2262657','704x10^3','521x10^3','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 67
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 186052','7031x10^2','464x10^3','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 68
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('NGC 1759','7028x10^2','6325x10^2','cD;E','27.0 B-MAG ARCSEC^-2')")
 # 69
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('LEDA 1869814 ','7021x10^2','4633x10^2','BrCIG','2MASS K-BAND TOTAL MAG')")
 # 70
  mycursor.execute("INSERT IGNORE INTO GAL_GREATER (GALAXY_NAME, MAJOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MINOR_AXIS_DIAMETER_IN_LIGHT_YEAR, MORPHOLOGY, ESTIMATION_METHOD) VALUES\
      ('ABELL S235 BCG','7009x10^2','2523x1062','cD','2MASS K-BAND TOTAL MAG')")
    
  mydb.commit()

#END........
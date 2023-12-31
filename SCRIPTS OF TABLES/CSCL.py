#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (CURRENT SPACE CREW LIST)

def Current_space_crew_list():
  mycursor.execute("CREATE TABLE IF NOT EXISTS CURRENT_SPACE_CREW_LIST(\
      NAME VARCHAR(50) PRIMARY KEY,\
      GENDER VARCHAR(50),\
      AGE INT(2),\
      FLIGHT VARCHAR(50),\
      NATIONALITY VARCHAR(50),\
      START_OF_MISSION VARCHAR(50),\
      AGENCY VARCHAR(50),\
      LOCATION VARCHAR(50))")
      
#1      
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('FRANCISCO RUBIO','MALE', '47', 'SOYUZ MS-22', 'AMERICAN', '21 Sep,2022', 'NASA', 'ISS')")
#2
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('SERGEY PROKOPYEV','MALE', '48', 'SOYUZ MS-22', 'RUSSSIAN', '21 Sep,2022', 'ROSKOSMOS', 'ISS')") 
#3
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('DMITRY PETELIN','MALE', '40', 'SOYUZ MS-22', 'RUSSSIAN', '21 Sep,2022', 'ROSKOSMOS', 'ISS')") 
#4
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('JASMIN MOGHBELI ','FEMALE', '40', 'SpaceX Crew-7', 'AMERICAN', '26 Aug, 2023', 'NASA', 'ISS')")
#5 
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('ANDREAS MOGENSEN','MALE', '46', 'SpaceX Crew-7', 'DANISH', '26 Aug, 2023', 'ESA', 'ISS')")
#6
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('SATOSHI FURUKAWA  ','MALE', '59', 'SpaceX Crew-7', 'JAPANESE', '26 Aug, 2023', 'NASDA/JAXA', 'ISS')")
#7
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('KONSTANTIN BORISOV','MALE', '39', 'SpaceX Crew-7', 'RUSSIAN', '26 Aug, 2023', 'ROSKOSMOS', 'ISS')")
#8
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('JING HAIPENG','MALE', '56', 'Shenzhou 16', 'CHINESE', '30 May, 2023', 'PLAAC', 'TIANGONG SPACE STATION')")
#9
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('ZHU YANGZHU','MALE', '36', 'Shenzhou 16', 'CHINESE', '30 May, 2023', 'PLAAC', 'TIANGONG SPACE STATION')")
#10
  mycursor.execute("INSERT IGNORE INTO CURRENT_SPACE_CREW_LIST (NAME, GENDER, AGE, FLIGHT, NATIONALITY, START_OF_MISSION, AGENCY, LOCATION) \
      VALUES ('GUI HAICHAO','MALE', '36', 'Shenzhou 16', 'CHINESE', '30 May, 2023', 'CMSA', 'TIANGONG SPACE STATION')")
     
  mydb.commit()

#END........
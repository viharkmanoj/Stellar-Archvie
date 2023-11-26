#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

def GRB_DISTANT():
 mycursor.execute("CREATE TABLE IF NOT EXISTS GRB_DISTANT(\
    GRB VARCHAR(55) PRIMARY KEY,\
    DISTANT VARCHAR(50),\
    DATE VARCHAR(55)) ")
#1    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 090429B','Z=9.4','MAY 2011')")    
#2    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 090423','Z=8.2','APRIL 2009-MAY 20011')")
# 3    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 080913','Z=6.7','SEPTEMBER 2008-APRIL 2009')")
# 4    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 060116','Z=6.60','---')")
# 5    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 140515A','Z=6.63','---')")
# 6    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 050904','Z=6.295','SEPTEMBER 2005-SEPTEMBE 2008')")
#7    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 000131','Z=4.5','JANUARY 2000-SEPTEMBER 2005')")
#8    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 971214','Z=3.42','DECEMBER 1997-JANUARY 2000')")
#9    
 mycursor.execute("INSERT IGNORE INTO GRB_DISTANT(GRB,DISTANT,DATE)\
    VALUES('GRB 970508','Z=0.835','MAY 1997-DECEMBER 1997')")

 mydb.commit()

#END .....
#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (COMPOSITION OF PLANETARY ELEMENTS)

def Composition_of_planetary_elements():
    mycursor.execute("CREATE TABLE IF NOT EXISTS COMPOSITION_PA (\
     PLANET VARCHAR(50) PRIMARY KEY, \
     MASS_KG VARCHAR(50), \
     CarbonDioxide VARCHAR(50), \
     Nitrogen VARCHAR(50), \
     Oxygen VARCHAR(50), \
     Argon VARCHAR(50), \
     Methane VARCHAR(50), \
     Sodium VARCHAR(50), \
     Hydrogen VARCHAR(50), \
     Helium VARCHAR(50), \
     Others VARCHAR(50))")
     
#1
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Hydrogen, Helium, Others) \
      VALUES ('Sun','3*10^30', '71%', '26%', '3%')")
#2    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Oxygen, Sodium, Hydrogen, Helium, Others) \
      VALUES ('Mercury','1000', '42%', '22%', '22%', '6%', '8%')")
#3    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, CarbonDioxide, Nitrogen) \
      VALUES ('Venus','4.8*10^20', '96%', '4%')")
#4    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Nitrogen, Oxygen, Argon, Others) \
      VALUES ('Earth','1.4*10^21', '78%', '21%', '1%', '<1%')")
#5    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Argon, Sodium, Helium) \
      VALUES ('Moon','100,000', '70%', '1%', '29%')")
#6    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, CarbonDioxide, Nitrogen, Argon, Others) \
      VALUES ('Mars','2.5*10^16', '95%', '2.7%', '1.6%', '0.7%')")   
#7    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Hydrogen, Helium) \
      VALUES ('Jupiter','1.9*10^27', '89.8%', '10.2%')")
#8    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Hydrogen, Helium, Others) \
      VALUES ('Saturn','5.4*10^26', '96.3%', '3.2%', '0.5%')")
#9    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Nitrogen, Methane, Others) \
      VALUES ('Titan','9.1*10^18', '97%', '2%', '1%')")
#10    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Methane, Hydrogen, Helium) \
      VALUES ('Uranus','8.6*10^25', '2.3%', '82.5%', '15.2%')")
#11    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, Methane, Hydrogen, Helium) \
      VALUES ('Neptune','1*10^26', '1%', '80%', '19%')")
#12    
    mycursor.execute("INSERT IGNORE INTO COMPOSITION_PA (Planet, MASS_KG, CarbonDioxide, Nitrogen, Methane) \
      VALUES ('Pluto','1.3*10^14', '8%', '90%', '2%')")
    
    mydb.commit()

#END........
#UDF = used defined function.
#SYNTAX TO CONNECT PYTHON WITH DATABASE.

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987")
      
mycursor = mydb.cursor()

#UDF for creating and droping databases.

def create_database(m):
  mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(m))
  
def drop_database(n):
  mycursor.execute("DROP DATABASE IF EXISTS {}".format(n))

#creating a database for StellarArchive 

create_database("stellar_archive")
mycursor.execute("USE stellar_archive")



#EMBEDDING CONSTELLATIONS RELATION INTO THE DATABASE.
import CONSTELLATIONS
CONSTELLATIONS.CONSTELLATIONS()


#EMBEDDING CURRENT_SPACE_CREW_LIST RELATION INTO THE DATABASE
import CSCL
CSCL.Current_space_crew_list()


#EMBEDDING MOONWALKERS RELATION INTO THE DATABASE
import MOONWALKERS
MOONWALKERS.moonwalks()


#EMBEDDING GALAXIES INTO THE DATABASE
import G_GREATER
G_GREATER.GAL_GREATER()

import G_LESSER
G_LESSER.GAL_LESSER() 



#EMBEDDING SUPERNOVAS INTO THE DATABASE
import SUPERNOVAE
SUPERNOVAE.SUPERNOVAS()

import CANDIDATES_SN
CANDIDATES_SN.Candidates_sn()

import DISTANT_SN
DISTANT_SN.Distant_sn()

import YEARLY_EXTRAGALACTIC_SN
YEARLY_EXTRAGALACTIC_SN.Yearly_Extragalatic_sn()

import REMNANTS_SN
REMNANTS_SN.REMNANTS_SN()



#EMBEDDING NEBULA RELATIONS INTO THE DATABASE.
import PROTOPLANETARY_NEBULA
PROTOPLANETARY_NEBULA.protoplanetary_nebulae()

import PLANETARY_NEBULA
PLANETARY_NEBULA.planetary_nebula()

import LARGEST_NEBULAE
LARGEST_NEBULAE.largest_nebulae()



#EMBEDDING GAMMA RAY BURSTS 
import GRB_LIST
GRB_LIST.GAMMA_RAY_BURSTS_LIST()

import GRB_DISTANT
GRB_DISTANT.GRB_DISTANT()

import GRB_EXTREME
GRB_EXTREME.GRB_EXTREME()



#IMPORTING AND EMBEDDING DATA OF TIMELINE OF SPACE EXPLORATION
import EXPO_pre_20th_CEN
EXPO_pre_20th_CEN.expo_pre()

import EXPO_1900_TO_1956
EXPO_1900_TO_1956.expo_1900_to_1956()

import EXPO_1957_TO_1959
EXPO_1957_TO_1959.expo_1957_to_1959()

import EXPO_1960_TO_1969
EXPO_1960_TO_1969.expo_1960_to_1969()

import EXPO_1970_TO_1979
EXPO_1970_TO_1979.expo_1970_to_1979()

import EXPO_1980_TO_1989
EXPO_1980_TO_1989.expo_1980_to_1989()

import EXPO_1990_TO_1999
EXPO_1990_TO_1999.expo_1990_to_1999()

import EXPO_2000_TO_2009
EXPO_2000_TO_2009.expo_2000_to_2009()

import EXPO_2000_TO_2009
EXPO_2000_TO_2009.expo_2000_to_2009()

import EXPO_2010_AND_LATER
EXPO_2010_AND_LATER.expo_2010_and_later()



#IMPORTING AND EMBEDDING DATA OF STARS
import OPEN_CLUSTER
OPEN_CLUSTER.OPEN_CLUSTER()

import NEAREST_STAR
NEAREST_STAR.NEAREST_STAR()

import STAR_BRIGHT
STAR_BRIGHT.STARS_BRIGHT()

import DWARFS_NEAREST
DWARFS_NEAREST.DWARFS_NEAREST()



#IMPORTING AND EMBEDDING DATA OF SOLAR SYSTEM
import PLANETARY_FACT_SHEET
PLANETARY_FACT_SHEET.FACT_SHEET()

import MEAN_TEMPERATURE
MEAN_TEMPERATURE.MEAN_TEMPERATURE()

import COPE
COPE.Composition_of_planetary_elements()

import PLANET_ATMOSPHERE_AND_MAGNETIC_FIELD
PLANET_ATMOSPHERE_AND_MAGNETIC_FIELD.PLANET_ATMOS() 



#IMPORTING AND EMBEDDING DATA OF MOONS
import MOONS_EARTH
MOONS_EARTH.earth_moons()

import MOONS_MARS
MOONS_MARS.mars_moons()

import MOONS_JUPITER
MOONS_JUPITER.jupiter_moons()

import MOONS_SATURN
MOONS_SATURN.saturn_moons()

import MOONS_URANUS
MOONS_URANUS.uranus_moons()

import MOONS_NEPTUNE
MOONS_NEPTUNE.neptune_moons()

import MOONS_PLUTO
MOONS_PLUTO.pluto_moons()


#IMPORTING AND EMBEDDING DATA OF EXOPLANETS

import DIRECTLY_IMAGED_EXOPLANETS
DIRECTLY_IMAGED_EXOPLANETS.directly_imaged_exoplanets()

import EXOPLANET_NEAREST
EXOPLANET_NEAREST.exoplanet_nearest()

import EXOPLANETS_HABITABLE
EXOPLANETS_HABITABLE.habitable_exoplanets()

import EXOPLANET_2023
EXOPLANET_2023.EXOPLANET_2023()



#EMBEDDING BLACKHOLES INTO THE DATABASE
import BLACKHOLES
BLACKHOLES.blackholes()

import BLACKHOLES_DIR
BLACKHOLES_DIR.BLACKHOLES_DIR()



#IMPORTING AND EMBEDDING DATA OF ASTEROIDS
import SLOWEST_ROTATORS_ASTR
SLOWEST_ROTATORS_ASTR.SLOWEST_ROTATORS_ASTR()

import FASTEST_ROTATORS
FASTEST_ROTATORS.FASTEST_ROTATORS()

import MOST_MASSIVE_ASTR
MOST_MASSIVE_ASTR.MOST_MASSIVE_ASTR()

import BRIGHTEST_ASTR
BRIGHTEST_ASTR.BRIGHTEST_ASTRO()



#......................LIST OF TABLES.........................................

mycursor.execute("show tables;")
tables = mycursor.fetchall()
m = 1
for table in tables:
  print("(",m,")",table[0])
  m += 1 
  
mydb.commit()

mydb.close()
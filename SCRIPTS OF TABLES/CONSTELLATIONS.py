#SYNTAX TO CONNECT PYTHON WITH DATABASE

import mysql.connector 

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="qwerty0987",
      database="stellar_archive")

mycursor = mydb.cursor()

#UDF FOR THE TABLE (CONSTELLATIONS)

def CONSTELLATIONS():
    mycursor.execute("CREATE TABLE IF NOT EXISTS CONSTELLATIONS (\
        NAME VARCHAR(50) PRIMARY KEY,\
        FIRST_APPEARANCE VARCHAR(50),\
        MEANING_OR_MYTHOLOGY VARCHAR(50),\
        AREA_OF_SKY VARCHAR(50),\
        CELESTIAL_HEMISPHERE VARCHAR(50),\
        BRIGHTEST_STAR VARCHAR(50),\
        BEST_TIME_TO_SEE VARCHAR(50))")    
 #1       
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY, \
        CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE) VALUES ('ANDROMEDA', 'ANCIENT', 'GREEK PRINCESS', \
        '1.80%', 'NORTHERN', 'ALPHERATZ', 'SEPTEMBER')")              
#2               
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('ANTLIA', '1756', 'AIR PUMP','0.80%', 'SOUTHERN', 'ALPHA-ANT', 'FEBRUARY')")
#3
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('APUS', '1598', 'BIRD OF PARADISE','0.50%', 'SOUTHERN', 'ALPHA-APS', 'JULY')")
#4
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('AQUARIUS', 'ANCIENT', 'WAITER TO GODS','2.40%', 'SOUTHERN', 'SADALSUUD', 'AUGUGST')")         
#5 
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('AQULA', 'ANCIENT', 'RETRIEVER OF ZEUS THUNDEBOLTS','1.60%', 'EQUATOR','ALTAIR','JUNE')")         
#6
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('ARA', 'ANCIENT', 'ALTAR USED BY THE GODS','0.60%', 'SOUTHERN','ALPHA-ARA','MAY')")
#7
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('ARIES', 'ANCIENT', 'GOLDERN FLEECE WAS RECOVERED','1.10%', 'NORTHERN','HAMAL','OCTOBER')")
#8
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('AURIGA', 'ANCIENT', 'CHARIOTEER_SUN OF VULCAN','1.60%', 'NORTHERN','CAPELLA','FEBRUARY')")              
#9
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('BOOTIES', 'ANCIENT', 'HERDSMAN_SON OF ZEUS','2.20%', 'NORTHERN','ARCTURUS','MAY')")
#10
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CAELUM', '1756', 'CHISEL','0.30%', 'SOUTHERN','ALPHA-CAE','NOVEMBER')")
#11
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CAMELOPARDALIS', '1612', 'GIRAFFE','1.80%', 'NORTHERN','BETA-CAM','FEBRUARY')")
#12
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CANCER', 'ANCIENT', 'CRAB THAT BIT HERCULES FOOT','1.20%', 'NORTHERN','BETA-CNC','FEBRUARY')")
#13
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CANES VENATICI', '1687', 'HUNTING DOGS OF BOOTES','1.10%', 'NORTHERN','COR-CAROLI','APRIL')")
#14
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CANIS MAJOR', 'ANCIENT', 'ORIONS GREATER HUNTING DOG','0.90%', 'SOUTHERN','SIRIUS','JANUARY')")
#15
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CANIS MINOR', 'ANCIENT', 'ORIONS LESSER HUNTING DOG','0.40%', 'NORTHERN','PROCYON','JANUARY')")
#16
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CAPRICORNUS', 'ANCIENT', 'SEA GOAT','1.00%', 'SOUTHERN','BETA-CAP','JULY')")
#17
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CARINA', '1756', 'KEEL OF THE ARGO','1.20%', 'SOUTHERN','CANOPUS','JANUARY')")
#18
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CASSIOPEIA', 'ANCIENT', 'QUEEN CASSIOPEIA','1.50%', 'NORTHERN','GAMMA-CAS','SEPTEMBER')")
#19
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CENTAURUS', 'ANCIENT', 'WISE CENTAUR','2.60%', 'SOUTHERN','RIGIL-KENTAURUS','MARCH')")
#20
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CEPHEUS', 'ANCIENT', 'ETHOPIAN KING','1.40%', 'NORTHERN','ALDERAMN','NOVEMBER')")
#21
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CETUS', 'ANCIENT', 'SEA MONSTER', '3.00%', 'SOUTHERN', 'DIPHDA', 'SEPTEMBER')")
#22
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CHAMAELEON ', '1598', 'CHAMAELEON','0.30%', 'SOUTHERN','ALPHA-CHA','FEBRUARY')")
#23
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CIRCINUS', '1758', 'DRAFTING COMPASS','0.30%', 'SOUTHERN','ALPHA-CIR','APRIL')")
#24
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('COLUMBA', '1592', 'DOVE', '0.10%', 'SOUTHERN','PHACT','DECEMBER')")
#25
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('COMA BERENICES', '1536', 'HAIR OF QUEEN BERENICES','0.90%', 'NORTHERN','BETA-COM','MARCH')")
#26
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CORONA AUSTRALIS', 'ANCIENT', 'SOUTHERN CROWN','0.30%', 'SOUTHERN','ALPHA-CRA','MAY')")
#27
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CORONA BOREALIS', 'ANCIENT', 'NORTHERN CROWN','0.40%', 'NORTHERN','ALPHA-CCA','MAY')")
#28
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CORVUS', 'ANCIENT', 'CROWN','0.40%', 'SOUTHERN','GIENAH','MARCH')")
#29
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CRATER', 'ANCIENT ', 'CUP','0.70%', 'SOUTHERN','DELTA-CRT','APRIL')")
#30
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CRUX', '1598', 'SOUTHERN CROSS','0.20%', 'SOUTHERN','ACRUX','MARCH')")
#31
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('CYGNUS', 'ANCIENT', 'SWAN_ZEUS IN DISGUISE','1.90%', 'NORTHERN','DENEB','SUMMER')")
#32
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('DELPHINUS', 'ANCIENT', 'DOLPHIN_MESSENGER OF POSEIDON','0.50%', 'SOUTHERN','ROTANEV','JULY')")
#33
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('DORADO', '1598', 'SWORDFISH','0.40%', 'SOUTHERN','ALPHA-DOR','NOVEMBER')")
#34
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('DRACO', 'ANCIENT', 'APPLE TREE GAURD DRAGON','2.60%', 'NORTHERN','ELTANIN','JULY')")
#35
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('EQUULEUS', 'ANCIENT ', 'LITTLE HORSE ', '0.20%','NORTHERN ', 'KITALPHA','SEPTEMBER')")
#36
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('ERIDANUS', 'ANCIENT', 'MYTHICAL RIVER','2.80%', 'SUTHERN','ACHERNAR','NOVEMBER')")
#37
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('FORNAX', '1756', 'FURNACE','1.00%', 'SOUTHERN','ALPHA-FOR','OCTOBER')")
#38
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('GEMINI', 'ANCIENT', 'MYTHICAL TWINS CASTOR AND POLIUX','1.20%', 'NORTHERN','POLLUX','WINTER')")
#39
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('GRUS', '1598', 'CRANE','0.90%', 'SOUTHERN ','ALNAIR','AUGUST')")
#40
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('HERCULUS', 'ANCIENT', 'HERCULUS','3.00%', 'NORTHERN','KORNEPHOROS','MAY')")
#41
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('HOROLOGIUM', '1756', 'PENDULUM CLOCK','0.60%', 'SOUTHERN ','ALPHA-HOR','NOVEMBER')")
#42
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('HYDRA', 'ANCIENT', 'MULTI-HEADED WATER SNAKE','3.20%', 'SOUTHERN','ALPHARD','JANUARY')")
#43
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('HYDRAUS', '1598', 'LESSER WATER SNAKE','0.60%', 'SOUTHERN ','BETA-HYL','OCTOBER')")
#44
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('INDUS', '1598', 'INDIAN','0.70%', 'SOUTHERN','ALPHA-IND','AUGUST')")
#45
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LACERTA', '1690', 'LIZARD','0.50%', 'NORTHERN','ALPHA-LAC','AUGUST')")
#46
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LEO', 'ANCIENT', 'LION OF NEMEA_SLAIN OF HERCULUS','2.30%', 'EQUATOR','REGULUS','FEBRUARY')")
#47
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LEO MINOR', '1687', 'LION CLUB','0.60%', 'NORTHERN','46-LMI','FEBRUARY')")
#48
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LEPUS', 'ANCIENT', 'HARE CHASED BY ORION DOGS','0.70%', 'SOUTHERN','ARNEB','DECEMBER')")
#49
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LIBRA', 'ANCIENT', 'BALANCE','1.30%', 'EQUATOR','ZUBENESCHAMALI','MAY')")
#50
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LUPUS', 'ANCIENT', 'WOLF','0.80%', 'SOUTHERN','ALPHA-LUP','MAY')")
#51
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LYNX', '1687', 'LYNX','1.30%', 'NORTHERN','ALPHA-LYN','JANUARY')")
#52
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('LYRA', 'ANCIENT', 'LYRE PLAYED BY MUSICIAN ORPHEUS','0.70%', 'NORTHERN','VEGA','JUNE')")
#53
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('MENSA', '1756', 'TABLE MOUNTAIN,SOUTH AFRICA','0.40%', 'SOUTHERN ','ALPHA-MEN','DECEMBER')")
#54
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('MICROSCOPIUM', '1756', 'MICROSCOPE','0.50%', 'SOUTHERN','GAMMA-MIC','JULY')")
#55
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('MONOCEROS', '1612', 'UNICORN','1.20%', 'EQUATOR','ALPHA-MON','DECEMBER')")
#56
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('MUSCA', '1598', 'FLY','0.30%', 'SOUTHERN','ALPHA-MUS','MAY')")
#57
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('NORMA', '1756', 'CAPENTERS SQUARE','0.40%', 'SOUTHERN','GAMMA SQUARE-NOR','MAY')")
#58
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('OCTANS', '1756', 'OCTANT_NAVIGATIONAL INSTRUMENT','0.70%', 'SOUTHERN','V-OCT','OCTOBER')")
#59
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('OPHIUCHUS', 'ANCIENT', 'SERPENT-BEARER,GOD OF MEDICINE','2.30%', 'EQUATOR','RASALHAGUE','JUNE')")
#60
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('ORION', 'ANCIENT', 'HUNTER_SON OF POSEIDON','1.40%', 'EQUATOR','RIGEL','NORTH-WINTER & SOUTH-SUMMER')")
#61
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PAVO', '1598', 'PEACOCK','0.90%', 'SOUTHERN','PEACOCK','JULY')")
#62
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PEGASUS', 'ANCIENT', 'WINGED HORSE','2.70%', 'NORTHERN','ENIF','SEPTEMBER')")
#63
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PERSEUS', 'ANCIENT', 'HUSBAND OF ANDROMEDA_SLAYER','1.50%', 'NORTHERN','AIRFAK','NOVEMBER')")
#64
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PHEONIX', '1598', 'MYTHICAL BIRD OF REBIRTH','1.10%', 'SOUTHERN','ANKAA','OCTOBER')")
#65
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PICTOR', '1756', 'PAINTERS EASEL','0.60%', 'SOUTHERN','ALPHA-PIC','DECEMBER')")
#66
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PISCES', 'ANCIENT', 'TWO FISH SWIMMING','2.20%', 'EQUATOR','1-PSC','SEPTEMBER')")
#67
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PISCIS AUSTRINUS', 'ANCIENT', 'SOUTHERN FISH','0.60%', 'SOUTHERN','FOMALHAUT','AUGUST')")
#68
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PUPPIS', '1756', 'POOP DECK OF ARGO','1.60%', 'SOUTHERN','NAOS','JANUARY')")
#69
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('PYXIS', '1756','COMPASS', '0.50%','SOUTHERN', 'ALPHA-PYX','JANUARY')")
#70
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('RETICULUM', '1756', 'NET OF CROSSHAIRS','0.30%', 'SOUTHERN','ALPHA-RET','NOVEMBER')")
#71
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SAGITTA', 'ANCIENT', 'ARROW USED BY APPOLO','0.20%', 'EQUATOR','GAMMA-SGE','JUNE')")
#72
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SAGITTARIUS', 'ANCIENT', 'CENTAUxR ARCHER','2.10%', 'SOUTHERN','KAUS-AUSTRALIS','JULY')")
#73
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SCORPIUS', 'ANCIENT', 'SCORPION_KILLER OF ORION','1.20%', 'SOUTHERN','ANTARES','MAY')")
#74
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SCULPTOR', '1756', 'SCULPTOR','1.20%', 'SOUTHERN','ALPHA-SCL','SPETEMBER')")
#75
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SCUTUM', '1684', 'SHIELDED HONOURING KING JHON-III','0.30%', 'EQUATOR','ALPHA-SCT','JUNE')")
#76
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SERPENS', 'ANCIENT', 'SERPENTS HEAD','1.50%', 'EQUATOR','UNUKALHAI','JUNE')")
#77
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('SEXTANS', '1687', 'SEXTANT','0.80%', 'EQUATOR','ALPHA-SEX','FEBRUARY')")
#78
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('TAURUS', 'ANCIENT', 'BULL_ZEUS IN DISGUISE','1.90%', 'NORTHERN','ALDEBARAN','DECEMBER')")
#79
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('TELESCOPIUM', '1756', 'TELESCOPE','0.60%', 'SOUTHERN','ALPHA-TEL','JULY')")
#80
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('TRIANGUALUM', '1603', 'TRIANGLE','0.30%', 'NORTHERN','BETA-TRI','OCTOBER')")
#81
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('TRIANGULUM AUSTRALE', '1958', 'SOUTHERN TRIANGLE', '0.30%', 'SOUTHERN','ATRIA', 'APRIL')")
#82
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('TUCANA', '1598', 'TOUCAN', '0.70%', 'SOUTHERN', 'ALPHA-TUC', 'SEPTEMBER')")
#83
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('URSA MAJOR', 'ANCIENT', 'GREAT BEAR', '3.10%', 'NORTHERN', 'ALIOTH', 'SPRING')")
#84
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('URSA MINOR', 'ANCIENT', 'LESSER BEAR_NYMPH', '0.60%', 'NORTHERN', 'POLARIS', 'JUNE')")
#85
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('VELA', '1756', 'SAIL OF THE SHIP ARGO', '1.20%', 'SOUTHERN', 'GAMMA SQUARE-VEL', 'FEBRUARY')")
#86
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('VIRGO', 'ANCIENT', 'VIRGIN_GODDESS OF JUSTICE', '3.10%', 'EQUATOR','SPICA', 'APRIL')")
#87
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('VOLANS', '1598', 'FLYING FISH', '0.30%', 'SOUTHERN', 'GAMMA SQUARE-VOL', 'JANUARY')")
#88 
    mycursor.execute("INSERT IGNORE INTO CONSTELLATIONS (NAME, FIRST_APPEARANCE, MEANING_OR_MYTHOLOGY, AREA_OF_SKY,CELESTIAL_HEMISPHERE, BRIGHTEST_STAR, BEST_TIME_TO_SEE)\
       VALUES ('VULPECULA', '1687', 'FOX','0.70%', 'NORTHERN','ALPHA-VUL','JULY')")

    mydb.commit()    
    
#END........          
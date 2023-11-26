#IMPORT STATEMENTS

import tkinter as tk
from tkinter import ttk
import mysql.connector

# CREATION OF THE MAINWINDOW

mainwindow = tk.Tk()
mainwindow.title("STELLAR ARCHIVE")
mainwindow.minsize(height=550, width=1000)
mainwindow.configure(bg="black")

#STYLING FOR BUTTONS

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="gainsboro", 
                fieldbackground="gainsboro", foreground="black")
style.configure('Treeview.Heading', background="black", foreground="white")
custom_font = ("Small Fonts", 36, "bold")
style.configure("W.TButton", padding=10, font=("Small Fonts", 12,"bold"))
style.configure("TScrollbar",
                background="snow",
                troughcolor="gray6"  
                )

#EMPTY STRINGS USED TO FIX BUGS OR GIVE WARNINGS TO THE USER BY GUIDING
KEY = ""
WARNING = ""
WARNING2 = ""
WARNING3 = ""

#DEFINED FUNCTOINS TO SHIFT SCREENS

def home():
    def primary():
        def table():
            
            #STATING THE STRINGS GLOBAL TO FIX BUGS

            global WARNING
            global WARNING2
            global WARNING3
            global KEY
        
            #PRIMARY TAB WIDGETS DESTROY STATEMENTS.

            PRIMARY_DESC.destroy()
            CATEGO.destroy()
            TYPE.destroy()
            CATEGO_DROP.destroy()
            TYPE_DROP.destroy()
            FETCH.destroy()
            PREVIOUS.destroy()

            if WARNING == "":
                pass
            else:
                WARNING.destroy()
            
            if WARNING2 == "":
                pass
            else:
                WARNING2.destroy()

            if WARNING3 == "":
                pass
            else:
                WARNING3.destroy()

            if KEY == "":
                pass
            else:
                KEY.destroy()    
            
            selected_category = catego_var.get()
            selected_type = type_var.get()

            #FETCH AND INSERT DATA INTO TREE FUNCTION

            def fetch_and_display_table():
                
                        for row in tree.get_children():
                            tree.delete(row)
            
                        connection = None

                        try:
                            connection = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="qwerty0987",
                                database="stellar_archive"
                             )

                            cursor = connection.cursor()
        
                            cursor.execute(f"SELECT * FROM {table_name}")

                            for row in cursor.fetchall():
                                 tree.insert("", "end", values=row)

                        except mysql.connector.Error as err:
                                print("Error:", err)

                        finally:
                            if connection and connection.is_connected():
                                cursor.close()
                                connection.close()
            
            #WARNING STATEMENTS LOGIC 

            if selected_category == "":
                if selected_type == "":
                    primary()
                    WARNING2 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE & CATEGORY", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING2.pack()
                    WARNING2.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING2.place(x=0, y=90)
                    
            #DEFINING THE STRUCTURE OF TREE OF TKINTER BASED ON THE TABLE IN DATABASE
             
            elif selected_category == "CONSTELLATIONS":
                if selected_type == "":
                    table_name = "constellations"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF CONSTELLATIONS", fg="white", 
                    bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("CONSTELLATION", "FIRST APPEARANCE",
                      "MEANING", "AREA OF SKY", "HEMISPHERE", "BRIGHTEST STAR","BEST TIME TO SEE"))
                    tree.heading("#1", text="CONSTELLATION")
                    tree.heading("#2", text="FIRST APPEARANCE")
                    tree.heading("#3", text="MEANING")
                    tree.heading("#4", text="AREA OF SKY")
                    tree.heading("#5", text="HEMISPHERE")
                    tree.heading("#6", text="BRIGHTEST STAR")
                    tree.heading("#7", text="BEST TIME TO SEE")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=115)
                    tree.column("#3", width=227)
                    tree.column("#4", width=80)
                    tree.column("#5", width=100)
                    tree.column("#6", width=118)
                    tree.column("#7", width=118)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=40,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE LEAVE THE TYPE EMPTY FOR CONSTELLATION", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "PEOPLE IN SPACE RIGHT NOW":
                if selected_type == "":
                    table_name = "current_space_crew_list"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF PEOPLE IN SPACE RIGHT NOW", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "GENDER",
                      "AGE", "FLIGHT", "NATIONALITY", "START OF MISSION","AGENCY","LOCATION"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="GENDER")
                    tree.heading("#3", text="AGE")
                    tree.heading("#4", text="FLIGHT")
                    tree.heading("#5", text="NATIONALITY")
                    tree.heading("#6", text="START OF MISSION")
                    tree.heading("#7", text="AGENCY")
                    tree.heading("#8", text="LOCATION")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=100)
                    tree.column("#3", width=50)
                    tree.column("#4", width=120)
                    tree.column("#5", width=110)
                    tree.column("#6", width=118)
                    tree.column("#7", width=118)
                    tree.column("#8", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE LEAVE THE TYPE EMPTY FOR PEOPLE IN SPACE RIGHT NOW", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
                

            elif selected_category == "MOONWALKERS":
                if selected_type == "":
                    table_name = "moonwalkers"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF PEOPLE EVER WALKED ON MOON",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "MISSION",
                      "DOB", "DOD", "LUNAR EVA DATE", "EVAS PERFORMED","EVA DURATION","SERVICE"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="DOB")
                    tree.heading("#4", text="DOD")
                    tree.heading("#5", text="LUNAR EVA DATE")
                    tree.heading("#6", text="EVAS PERFORMED")
                    tree.heading("#7", text="EVA DURATION")
                    tree.heading("#8", text="SERVICE")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=115)
                    tree.column("#3", width=115)
                    tree.column("#4", width=80)
                    tree.column("#5", width=120)
                    tree.column("#6", width=118)
                    tree.column("#7", width=118)
                    tree.column("#8", width=118)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ LEAVE THE TYPE EMPTY FOR MOONWALKERS", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "GALAXIES":
                if selected_type == ">>>7x10^5 LIGHT YEARS":
                    table_name = "gal_greater"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF LARGEST GALAXIES >>>> 7x10^5 LIGHT YEARS"
                    , fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("GALAXY NAME", "MAJOR AXIS IN LIGHT YEAR",
                      "MINOR AXIS IN LIGHT YEAR", "MORPHOLOGY", "ESTIMATION_METHOD"))
                    tree.heading("#1", text="GALAXY NAME")
                    tree.heading("#2", text="MAJOR AXIS IN LIGHT YEAR")
                    tree.heading("#3", text="MINOR AXIS IN LIGHT YEAR")
                    tree.heading("#4", text="MORPHOLOGY")
                    tree.heading("#5", text="ESTIMATION_METHOD")
                    tree.column("#1", width=225) 
                    tree.column("#2", width=200)
                    tree.column("#3", width=200)
                    tree.column("#4", width=135)
                    tree.column("#5", width=185)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=20,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "<<<7x10^5 LIGHT YEARS":
                    table_name = "gal_lesser"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF LARGEST GALAXIES <<<< 7x10^5 LIGHT YEARS",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("GALAXY NAME", "MAJOR AXIS IN LIGHT YEAR",
                      "MINOR AXIS IN LIGHT YEAR", "MORPHOLOGY", "ESTIMATION_METHOD"))
                    tree.heading("#1", text="GALAXY NAME")
                    tree.heading("#2", text="MAJOR AXIS IN LIGHT YEAR")
                    tree.heading("#3", text="MINOR AXIS IN LIGHT YEAR")
                    tree.heading("#4", text="MORPHOLOGY")
                    tree.heading("#5", text="ESTIMATION_METHOD")
                    tree.column("#1", width=225) 
                    tree.column("#2", width=200)
                    tree.column("#3", width=200)
                    tree.column("#4", width=135)
                    tree.column("#5", width=185)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=20,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white", 
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
                    

            elif selected_category == "SUPERNOVAS":
                if selected_type == "DISTANT SUPERNOVAS":
                    table_name = "distant_sn"
                    TABLE_DESC = tk.Label(mainwindow, text="DISTANT SUPERNOVAS", fg="white", 
                    bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("TYPE", "SUPERNOVA NAME", "DISTANCE"))
                    tree.heading("#1", text="TYPE")
                    tree.heading("#2", text="SUPERNOVA NAME")
                    tree.heading("#3", text="DISTANCE")
                    tree["show"] = "headings"
                    tree.column("#1", width=275) 
                    tree.column("#2", width=275)
                    tree.column("#3", width=275)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=100,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "SUPERNOVA PROGENITOR CANDITATES":
                    table_name = "candidates_sn"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF SUPERNOVA PROGENITOR CANDITATES",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("IDENTIFIER", "RIGHT ASCENSION",
                      "DECLINATION", "CONSTELLATION", "DISTANCE LIGHT YEARS", "SPECTRAL CLASS",
                      "POSSIBLE SUPERNOVA TYPE"))
                    tree.heading("#1", text="IDENTIFIER")
                    tree.heading("#2", text="RIGHT ASCENSION")
                    tree.heading("#3", text="DECLINATION")
                    tree.heading("#4", text="CONSTELLATION")
                    tree.heading("#5", text="DISTANCE LIGHT YEARS")
                    tree.heading("#6", text="SPECTRAL CLASS")
                    tree.heading("#7", text="POSSIBLE TYPE")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=115)
                    tree.column("#3", width=115)
                    tree.column("#4", width=120)
                    tree.column("#5", width=120)
                    tree.column("#6", width=118)
                    tree.column("#7", width=120)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()
                
                elif selected_type == "SUPERNOVA REMNANTS":
                    table_name = "remnants_sn"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF SUPERNOVA REMNANTS",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "RIGHT ASCENSION",
                      "DECLINATION", "FIRST VISIBLE FROM EARTH", "PEAK MAGNITUDE", "DISTANCE","TYPE"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="RIGHT ASCENSION")
                    tree.heading("#3", text="DECLINATION")
                    tree.heading("#4", text="FIRST VISIBLE FROM EARTH")
                    tree.heading("#5", text="PEAK MAGNITUDE")
                    tree.heading("#6", text="DISTANCE")
                    tree.heading("#7", text="TYPE")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=115)
                    tree.column("#3", width=115)
                    tree.column("#4", width=160)
                    tree.column("#5", width=120)
                    tree.column("#6", width=100)
                    tree.column("#7", width=100)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "LIST OF DETECTED SUPERNOVAS":
                    table_name = "supernovas"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF DETECTED SUPERNOVAS", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("SUPERNOVA", "CONSTELLATION",
                      "APPARENT MAG", "DISTANCE IN LIGHTYEARS", "TYPE", "GALAXY"))
                    tree.heading("#1", text="SUPERNOVA")
                    tree.heading("#2", text="CONSTELLATION")
                    tree.heading("#3", text="APPARENT MAG")
                    tree.heading("#4", text="DISTANCE IN LIGHTYEARS")
                    tree.heading("#5", text="TYPE")
                    tree.heading("#6", text="GALAXY")
                    tree.column("#1", width=150) 
                    tree.column("#2", width=115)
                    tree.column("#3", width=115)
                    tree.column("#4", width=160)
                    tree.column("#5", width=120)
                    tree.column("#6", width=200)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "YEARLY EXTRAGALACTIC SUPERNOVA REPORT":
                    table_name = "yearly_extragalatic_sn"
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF YEARLY EXTRAGALACTIC SUPERNOVAE",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("YEAR", "TOTAL",
                      "TYPE 1", "TYPE 2", "LBV", "BRIGHTER THAN APMAG 13","APMAG OF BRIGHTEST SN OF THAT YEAR"))
                    tree.heading("#1", text="YEAR")
                    tree.heading("#2", text="TOTAL")
                    tree.heading("#3", text="TYPE 1")
                    tree.heading("#4", text="TYPE 2")
                    tree.heading("#5", text="LBV")
                    tree.heading("#6", text="BRIGHTER THAN APMAG 13")
                    tree.heading("#7", text="APMAG OF BRIGHTEST SN OF THAT YEAR")
                    tree.column("#1", width=80) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=80)
                    tree.column("#6", width=160)
                    tree.column("#7", width=250)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=100,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "NEBULAS":
                if selected_type == "LARGEST NEBULAE":
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF LARGEST NEBULAE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    table_name = "largest_nebulae"
                    tree = ttk.Treeview(mainwindow, columns=("NEBULA NAME", "MAX DIMENSION", "TYPE"))
                    tree.heading("#1", text="NEBULA NAME")
                    tree.heading("#2", text="MAX DIMENSION")
                    tree.heading("#3", text="TYPE")
                    tree["show"] = "headings"
                    tree.column("#1", width=300) 
                    tree.column("#2", width=300)
                    tree.column("#3", width=300)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=50,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()   

                elif selected_type == "PLANETARY NEBULAE":
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF PLANETARY NEBULAE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    table_name = "planetary_nebula"
                    tree = ttk.Treeview(mainwindow, columns=("NEBULA NAME", "MESSIER CATALOUGE", "NGC",
                    "DESIGNATION","DATE DISCOVERED","DISTANCE","MAGNITUDE","CONSTELLATION"))
                    tree.heading("#1", text="NEBULA NAME")
                    tree.heading("#2", text="MESSIER CATALOUGE")
                    tree.heading("#3", text="NGC")
                    tree.heading("#4", text="DESIGNATION")
                    tree.heading("#5", text="DATE DISCOVERED")
                    tree.heading("#6", text="DISTANCE")
                    tree.heading("#7", text="MAGNITUDE")
                    tree.heading("#8", text="CONSTELLATION")
                    tree["show"] = "headings"
                    tree.column("#1", width=150) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=100)
                    tree.column("#4", width=100)
                    tree.column("#5", width=120)
                    tree.column("#6", width=100)
                    tree.column("#7", width=100)
                    tree.column("#8", width=130)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=30,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()   

                elif selected_type == "PROPLANETARY NEBULAE":
                    TABLE_DESC = tk.Label(mainwindow, text="LIST OF PROPLANETARY NEBULAE", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    table_name = "protoplanetary_nebula"
                    tree = ttk.Treeview(mainwindow, columns=("NEBULA NAME","NGC",
                    "DESIGNATION","DATE DISCOVERED", "DISTANCE"))
                    tree.heading("#1", text="NEBULA NAME")
                    tree.heading("#2", text="NGC")
                    tree.heading("#3", text="DESIGNATION")
                    tree.heading("#4", text="DATE DISCOVERED")
                    tree.heading("#5", text="DISTANCE")
                    tree["show"] = "headings"
                    tree.column("#1", width=180) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=180)
                    tree.column("#4", width=100)
                    tree.column("#5", width=120)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=140,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()  

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90) 
                
                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
            
            elif selected_category == "GAMMA RAY BURSTS":
                if selected_type == "DETECTED GRB":
                    TABLE_DESC = tk.Label(mainwindow, text="DETECTED GAMMA RAY BURSTS", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    table_name = "grb_list"
                    tree = ttk.Treeview(mainwindow, columns=("BURST", " POSITION", "REDSHIFT", "DETECTED_BY"))
                    tree.heading("#1", text="BURST")
                    tree.heading("#2", text="POSITION")
                    tree.heading("#3", text="REDSHIFT")
                    tree.heading("#4", text="DETECTED_BY")
                    tree["show"] = "headings"
                    tree.column("#1", width=225) 
                    tree.column("#2", width=225)
                    tree.column("#3", width=225)
                    tree.column("#4", width=225)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=50,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()
    

                elif selected_type == "MOST DISTANT GRB":
                    table_name = "grb_distant"
                    TABLE_DESC = tk.Label(mainwindow, text="MOST DISTANT GAMMA RAY BURSTS", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("GAMMA RAY BURST", "DISTANT", "DATE"))
                    tree.heading("#1", text="GAMMA RAY BURST")
                    tree.heading("#2", text="DISTANT")
                    tree.heading("#3", text="DATE")
                    tree["show"] = "headings"
                    tree.column("#1", width=275) 
                    tree.column("#2", width=275)
                    tree.column("#3", width=275)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=100,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "GRB EXTREMES":
                    table_name = "grb_extreme"
                    TABLE_DESC = tk.Label(mainwindow, text="EXTREME GAMMA RAY BURSTS", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("GAMMA RAY BURST", "DISTANT", "DATE"))
                    tree.heading("#1", text="GAMMA RAY BURST")
                    tree.heading("#2", text="DISTANT")
                    tree.heading("#3", text="DATE")
                    tree["show"] = "headings"
                    tree.column("#1", width=275) 
                    tree.column("#2", width=275)
                    tree.column("#3", width=275)
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=100,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)
                    
                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
                        

            elif selected_category == "TIMELINE OF SPACE EXPLORATION":
                if selected_type == "PRE 20TH CENTURY":
                    table_name = " et_pre20thcen"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - 'PR\
E 20TH CENTURY'""", fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "EVENT",
                      "COUNTRY", "REASEARCHER"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="EVENT")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="REASEARCHER")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=150)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=60,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1900 - 1956":
                    table_name = " et_1900_to_1956"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1900 - 1956'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=55,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1957 - 1959":
                    table_name = "et_1957_to_1959"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1957 - 1959'""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=55,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1960 - 1969":
                    table_name = "et_1960_to_1969"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1960 - 1969'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=55,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1970 - 1979":
                    table_name = "et_1970_to_1979"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1970 - 1979'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=55,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1980 - 1989":
                    table_name = "et_1980_to_1989"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1980 - 1989'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=115)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=55,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "1990 - 1999":
                    table_name = "et_1990_to_1999"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '1990 - 1999'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=145)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=35,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "2000 - 2009":
                    table_name = "et_2000_to_2009"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '2000 - 2009'""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=145)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=35,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "2010 & LATER":
                    table_name = "et_2010_and_later"
                    TABLE_DESC = tk.Label(mainwindow, text="""TIMELINE OF SPACE EXPLORATION - '2010 & LATER'""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("DATE", "MISSION",
                      "COUNTRY", "MISSION NAME"))
                    tree.heading("#1", text="DATE")
                    tree.heading("#2", text="MISSION")
                    tree.heading("#3", text="COUNTRY")
                    tree.heading("#4", text="MISSION NAME")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=500)
                    tree.column("#3", width=145)
                    tree.column("#4", width=170)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=35,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "STARS":
                if selected_type == "OPEN CLUSTERS":
                    table_name = "open_cluster"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF OPEN CLUSTERS""", fg="white", 
                    bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("CLUSTER IDENTIFIER", "EPOCH J2000",
                      "CONSTELLATION", "DISTANCE","AGE","DIAMETER","APPARENT MAG"))
                    tree.heading("#1", text="CLUSTER IDENTIFIER")
                    tree.heading("#2", text="EPOCH J2000")
                    tree.heading("#3", text="CONSTELLATION")
                    tree.heading("#4", text="DISTANCE")
                    tree.heading("#5", text="AGE")
                    tree.heading("#6", text="DIAMETER")
                    tree.heading("#7", text="APPARENT MAG")
                    tree.column("#1", width=225) 
                    tree.column("#2", width=150)
                    tree.column("#3", width=150)
                    tree.column("#4", width=75)
                    tree.column("#5", width=75)
                    tree.column("#6", width=75)
                    tree.column("#7", width=130)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=50,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()


                elif selected_type == "THE NEAREST STARS TO EARTH":
                    table_name = "nearest_star"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF THE NEAREST STARS TO EARTH""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("STAR SYSTEM", "DISTANCE IN LIGHT YEAR",
                      "STELLAR TYPE", "OBSERVED PLANETS"))
                    tree.heading("#1", text="STAR SYSTEM")
                    tree.heading("#2", text="DISTANCE IN LIGHT YEAR")
                    tree.heading("#3", text="STELLAR TYPE")
                    tree.heading("#4", text="OBSERVED PLANETS")
                    tree.column("#1", width=200) 
                    tree.column("#2", width=180)
                    tree.column("#3", width=100)
                    tree.column("#4", width=180)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=160,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()
            
                elif selected_type == "BIGHTEST STAR":
                    table_name = "stars_bright"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF BIGHTEST STAR""", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("COMMON NAME", "ASTRONOMICAL NAME",
                      "MEANING", "APPARENT MAG","ABSOLUTE MAG","DISTANCE in LY"))
                    tree.heading("#1", text="COMMON NAME")
                    tree.heading("#2", text="ASTRONOMICAL NAME")
                    tree.heading("#3", text="MEANING")
                    tree.heading("#4", text="APPARENT MAG")
                    tree.heading("#5", text="ABSOLUTE MAG")
                    tree.heading("#6", text="DISTANCE in LY")
                    tree.column("#1", width=130) 
                    tree.column("#2", width=175)
                    tree.column("#3", width=300)
                    tree.column("#4", width=110)
                    tree.column("#5", width=110)
                    tree.column("#6", width=110)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()
            
                elif selected_type == "NEAREST WHITE DWARFS":
                    table_name = "dwarfs_nearest"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF THE NEAREST WHITE DWARFS""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("STAR", "DISTANCE"))
                    tree.heading("#1", text="STAR")
                    tree.heading("#2", text="DISTANCE")
                    tree.column("#1", width=300) 
                    tree.column("#2", width=300)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=200,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "SOLAR SYSTEM":
                if selected_type == "FACT SHEET RATION TO EARTH":
                    table_name = "fact_sheet"
                    TABLE_DESC = tk.Label(mainwindow, text="""FACT SHEET RATION WITH RESPECT TO EARTH """,
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-180)
                    KEY = tk.Label(mainwindow, text="""ESC-V = ESCAPE VELOCITY, ROT-T = ROTATION PERIOD, D-SUN = DISTANCE FROM THE SUN
ORB-T = ORBITAL PERIOD, P = PRESSURE, B = MAGNETIC FIELD""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    KEY.pack()
                    KEY.place(relx=0.5, rely=0.5, anchor="center")
                    KEY.place(x=0, y=180)
                    tree = ttk.Treeview(mainwindow, columns=("PLANET", "MASS",
                      "DIAMETER", "DENSITY","GRAVITY","ESC-V","ROT-T","LEN-DAY","D-SUN",
                      "ORB-T","ORB-V","ORB-E","OBL-ORB","P","MOON","RINGS","B"))
                    tree.heading("#1", text="PLANET")
                    tree.heading("#2", text="MASS")
                    tree.heading("#3", text="DIAMETER")
                    tree.heading("#4", text="DENSITY")
                    tree.heading("#5", text="GRAVITY")
                    tree.heading("#6", text="ESC-V")
                    tree.heading("#7", text="ROT-T")
                    tree.heading("#8", text="LEN-DAY")
                    tree.heading("#9", text="D-SUN")
                    tree.heading("#10", text="ORB-T")
                    tree.heading("#11", text="ORB-V")
                    tree.heading("#12", text="ORB-E")
                    tree.heading("#13", text="OBL-ORB")
                    tree.heading("#14", text="P")
                    tree.heading("#15", text="MOON")
                    tree.heading("#16", text="RINGS")
                    tree.heading("#17", text="B")
                    tree.column("#1", width=65) 
                    tree.column("#2", width=50)
                    tree.column("#3", width=70)
                    tree.column("#4", width=70)
                    tree.column("#5", width=60)
                    tree.column("#6", width=55)
                    tree.column("#7", width=55)
                    tree.column("#8", width=70)
                    tree.column("#9", width=60)
                    tree.column("#10", width=55)
                    tree.column("#11", width=55)
                    tree.column("#12", width=55)
                    tree.column("#13", width=70)
                    tree.column("#14", width=40)
                    tree.column("#15", width=50)
                    tree.column("#16", width=55)
                    tree.column("#17", width=40)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=4,y=150)
                    tree.config(height=10)
                    fetch_and_display_table()

                elif selected_type == "MEAN TEMPERATURE":
                    table_name = "mean_temperature"
                    TABLE_DESC = tk.Label(mainwindow, text="""MEAN TEMPERATURES OF THE PLANETS IN SOLAR SYSTEM""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-180)
                    tree = ttk.Treeview(mainwindow, columns=("PLANET", "TEMPERATURE"))
                    tree.heading("#1", text="PLANET")
                    tree.heading("#2", text="TEMPERATURE")
                    tree.column("#1", width=100) 
                    tree.column("#2", width=100)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=400,y=170)
                    tree.config(height=10)
                    fetch_and_display_table()

                elif selected_type == "COMPOSITION OF PLANETARY ELEMENTS":
                    table_name = "composition_pa"
                    TABLE_DESC = tk.Label(mainwindow, text="""COMPOSITION OF PLANETARY ELEMENTS""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-185)
                    tree = ttk.Treeview(mainwindow, columns=("PLANET", "MASS KG","CarbonDioxide",
                    "Nitrogen","Oxygen","Argon","Methane","Sodium","Hydrogen","Helium","Others"))
                    tree.heading("#1", text="PLANET")
                    tree.heading("#2", text="MASS KG")
                    tree.heading("#3", text="CarbonDioxide")
                    tree.heading("#4", text="Nitrogen")
                    tree.heading("#5", text="Oxygen")
                    tree.heading("#6", text="Argon")
                    tree.heading("#7", text="Methane")
                    tree.heading("#8", text="Sodium")
                    tree.heading("#9", text="Hydrogen")
                    tree.heading("#10", text="Helium")
                    tree.heading("#11", text="Others")
                    tree.column("#1", width=70) 
                    tree.column("#2", width=75)
                    tree.column("#3", width=90)
                    tree.column("#4", width=90)
                    tree.column("#5", width=90)
                    tree.column("#6", width=90)
                    tree.column("#7", width=90)
                    tree.column("#8", width=90)
                    tree.column("#9", width=90)
                    tree.column("#10", width=90)
                    tree.column("#11", width=90)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=15,y=130)
                    tree.config(height=13)
                    fetch_and_display_table()

                elif selected_type == "PLANETARY ATMOSPHERE & MAGNETIC FIELDS":
                    table_name = "planet_atmos"
                    TABLE_DESC = tk.Label(mainwindow, text="""PLANETARY ATMOSPHERE AND THEIR MAGNETIC FIELDS""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-185)
                    tree = ttk.Treeview(mainwindow, columns=("PLANET", "GRAVITY PULL","ESC VELOCITY",
                    "DISTANCE","ALBEDO",
                    "TEMP_IN_°F","ATM_PRESSURE","ATM_COMP","ROTATION","MAG_FIELD"))
                    tree.heading("#1", text="PLANET")
                    tree.heading("#2", text="GRAVITY PULL")
                    tree.heading("#3", text="ESC VELOCITY")
                    tree.heading("#4", text="DISTANCE")
                    tree.heading("#5", text="ALBEDO")
                    tree.heading("#6", text="TEMP IN °F")
                    tree.heading("#7", text="ATM PRESSURE")
                    tree.heading("#8", text="ATM COMP")
                    tree.heading("#9", text="ROTATION")
                    tree.heading("#10", text="MAG FIELD")
                    tree.column("#1", width=70) 
                    tree.column("#2", width=90)
                    tree.column("#3", width=100)
                    tree.column("#4", width=90)
                    tree.column("#5", width=60)
                    tree.column("#6", width=90)
                    tree.column("#7", width=90)
                    tree.column("#8", width=180)
                    tree.column("#9", width=100)
                    tree.column("#10", width=90)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=12,y=130)
                    tree.config(height=13)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)

            elif selected_category == "MOONS":
                if selected_type == "MERCURY":
                    TABLE_DESC = tk.Label(mainwindow, text="PLANET (MERCURY) HAS NO MOONS!!", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 60))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-25)
                    table_name = "notable"

                elif selected_type == "VENUS":
                    TABLE_DESC = tk.Label(mainwindow, text="PLANET (VENUS) HAS NO MOONS!!",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 60))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-25)
                    table_name = "notable"

                elif selected_type == "EARTH":
                    table_name = "earth_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'EARTH'(1)""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-185)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "DIAMETER","MASS","SEMIMAJOR AXIS",
                    "PERIOD","ORBITAL INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER","TYPE"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="DIAMETER")
                    tree.heading("#3", text="MASS")
                    tree.heading("#4", text="SEMIMAJOR AXIS")
                    tree.heading("#5", text="PERIOD")
                    tree.heading("#6", text="ORBITAL INCLINATION")
                    tree.heading("#7", text="ECCENTRICITY")
                    tree.heading("#8", text="DISCOVERY YEAR")
                    tree.heading("#9", text="DISCOVERER")
                    tree.heading("#10", text="TYPE")
                    tree.column("#1", width=70) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=90)
                    tree.column("#4", width=130)
                    tree.column("#5", width=90)
                    tree.column("#6", width=130)
                    tree.column("#7", width=90)
                    tree.column("#8", width=100)
                    tree.column("#9", width=80)
                    tree.column("#10", width=95)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=15,y=130)
                    tree.config(height=13)
                    fetch_and_display_table()

                elif selected_type == "MARS":
                    table_name = "mars_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'MARS'(2)""", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-185)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "DIAMETER","SURFACE AREA","MASS",
                    "SEMIMAJOR AXIS","PERIOD",
                    "ORBITAL INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="DIAMETER")
                    tree.heading("#3", text="SURFACE AREA")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="PERIOD")
                    tree.heading("#7", text="ORBITAL INCLINATION")
                    tree.heading("#8", text="ECCENTRICITY")
                    tree.heading("#9", text="DISCOVERY YEAR")
                    tree.heading("#10", text="DISCOVERER")
                    tree.column("#1", width=70) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=90)
                    tree.column("#4", width=80)
                    tree.column("#5", width=130)
                    tree.column("#6", width=80)
                    tree.column("#7", width=130)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=95)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=8,y=130)
                    tree.config(height=13)
                    fetch_and_display_table()

                elif selected_type == "JUPITER":
                    table_name = "jupiter_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'JUPITER'(95)""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "ABS MAGN","DIAMETER","MASS",
                    "SEMIMAJOR AXIS","PERIOD",
                    "INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="ABS MAGN")
                    tree.heading("#3", text="DIAMETER")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="PERIOD")
                    tree.heading("#7", text="INCLINATION")
                    tree.heading("#8", text="ECCENTRICITY")
                    tree.heading("#9", text="DISCOVERY YEAR")
                    tree.heading("#10", text="DISCOVERER")
                    tree.column("#1", width=110) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=80)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=120)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "SATURN":
                    table_name = "saturn_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'SATURN'(146)""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "ABS MAGN","DIAMETER","MASS",
                    "SEMIMAJOR AXIS","PERIOD",
                    "INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="ABS MAGN")
                    tree.heading("#3", text="DIAMETER")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="PERIOD")
                    tree.heading("#7", text="INCLINATION")
                    tree.heading("#8", text="ECCENTRICITY")
                    tree.heading("#9", text="DISCOVERY YEAR")
                    tree.heading("#10", text="DISCOVERER")
                    tree.column("#1", width=130) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=80)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=110)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "URANUS":
                    table_name = "uranus_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'URANUS'(27)""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "ABS MAGN","DIAMETER","MASS",
                    "SEMIMAJOR AXIS","PERIOD",
                    "INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="ABS MAGN")
                    tree.heading("#3", text="DIAMETER")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="PERIOD")
                    tree.heading("#7", text="INCLINATION")
                    tree.heading("#8", text="ECCENTRICITY")
                    tree.heading("#9", text="DISCOVERY YEAR")
                    tree.heading("#10", text="DISCOVERER")
                    tree.column("#1", width=110) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=80)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=133)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=22,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "NEPTUNE":
                    table_name = "neptune_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'NEPTUNE'(27)""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "ABS MAGN","DIAMETER","MASS",
                    "SEMIMAJOR AXIS","PERIOD","INCLINATION","ECCENTRICITY","DISCOVERY YEAR","DISCOVERER"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="ABS MAGN")
                    tree.heading("#3", text="DIAMETER")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="PERIOD")
                    tree.heading("#7", text="INCLINATION")
                    tree.heading("#8", text="ECCENTRICITY")
                    tree.heading("#9", text="DISCOVERY YEAR")
                    tree.heading("#10", text="DISCOVERER")
                    tree.column("#1", width=110) 
                    tree.column("#2", width=80)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=80)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=133)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=22,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "PLUTO":
                    table_name = "pluto_moons"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOONS OF--'PLUTO'(5)""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "DIAMETER","MASS","SEMIMAJOR AXIS",
                    "PERIOD","RESONANCE",
                    "ECCENTRICITY","INCLINATION","MAGNITUDE","DISCOVERER YEAR"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="DIAMETER")
                    tree.heading("#3", text="MASS")
                    tree.heading("#4", text="SEMIMAJOR AXIS")
                    tree.heading("#5", text="PERIOD")
                    tree.heading("#6", text="RESONANCE")
                    tree.heading("#7", text="ECCENTRICITY")
                    tree.heading("#8", text="INCLINATION")
                    tree.heading("#9", text="MAGNITUDE")
                    tree.heading("#10", text="DISCOVERER YEAR")
                    tree.column("#1", width=80) 
                    tree.column("#2", width=100)
                    tree.column("#3", width=83)
                    tree.column("#4", width=100)
                    tree.column("#5", width=80)
                    tree.column("#6", width=75)
                    tree.column("#7", width=95)
                    tree.column("#8", width=100)
                    tree.column("#9", width=90)
                    tree.column("#10", width=133)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=25,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
                
            elif selected_category == "EXOPLANETS":
                if selected_type == "DIRECTLY IMAGED":
                    table_name = "directly_imaged_exoplanets"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF DIRECTLY IMAGED EXOPLANETS""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("STAR","EXOPLANET", "JUPITER MASS",
                    "JUPITER RADIUS","PERIOD","OBSERVATION","ECCENTRICITY","DISTANCE","DISCOVERY","IMAGING TECHNIQUE"))
                    tree.heading("#1", text="STAR")
                    tree.heading("#2", text="EXOPLANET")
                    tree.heading("#3", text="JUPITER MASS")
                    tree.heading("#4", text="JUPITER RADIUS")
                    tree.heading("#5", text="PERIOD")
                    tree.heading("#6", text="OBSERVATION")
                    tree.heading("#7", text="ECCENTRICITY")
                    tree.heading("#8", text="DISTANCE")
                    tree.heading("#9", text="DISCOVERY")
                    tree.heading("#10", text="IMAGING TECHNIQUE")
                    tree.column("#1", width=110) 
                    tree.column("#2", width=120)
                    tree.column("#3", width=100)
                    tree.column("#4", width=100)
                    tree.column("#5", width=80)
                    tree.column("#6", width=90)
                    tree.column("#7", width=100)
                    tree.column("#8", width=65)
                    tree.column("#9", width=75)
                    tree.column("#10", width=135)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=3,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()    

                elif selected_type == "CONFIRMED NEAREST EXOPLANETS":
                    table_name = "exoplanet_nearest"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF CONFIRMED NEAREST EXOPLANETS""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME","DISTANCE FROM EARTH", 
                    "APPARENT MAGNITUDE","SOLAR MASS"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="DISTANCE FROM EARTH")
                    tree.heading("#3", text="APPARENT MAGNITUDE")
                    tree.heading("#4", text="SOLAR MASS")
                    tree.column("#1", width=210) 
                    tree.column("#2", width=220)
                    tree.column("#3", width=200)
                    tree.column("#4", width=200)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()   

                elif selected_type == "POTENTIALLY HABITABLE EXOPLANETS":
                    table_name = "habitable_exoplanets"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF POTENTIALLY HABITABLE EXOPLANETS""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("OBJECT", "STAR","TYPE","MASS","RADIUS","DENSITY",
                    "FLUX","TEMPERATURE","PERIOD","DISTANCE"))
                    tree.heading("#1", text="OBJECT")
                    tree.heading("#2", text="STAR")
                    tree.heading("#3", text="TYPE")
                    tree.heading("#4", text="MASS")
                    tree.heading("#5", text="RADIUS")
                    tree.heading("#6", text="DENSITY")
                    tree.heading("#7", text="FLUX")
                    tree.heading("#8", text="TEMPERATURE")
                    tree.heading("#9", text="PERIOD")
                    tree.heading("#10", text="DISTANCE")
                    tree.column("#1", width=130) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=80)
                    tree.column("#4", width=80)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=80)
                    tree.column("#8", width=100)
                    tree.column("#9", width=110)
                    tree.column("#10", width=80)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=12,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "DETECTED EXOPLANETS IN 2023":
                    table_name = "exoplanet_2023"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF DETECTED EXOPLANETS IN 2023""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME", "MASS","RADIUS","PERIOD","SEMIMAJOR AXIS","TEMP",
                    "DISCOVERY METHOD","DISTANCE","HOSTSTAR MASS","HOSTSTAR TEMP"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="MASS")
                    tree.heading("#3", text="RADIUS")
                    tree.heading("#4", text="PERIOD")
                    tree.heading("#5", text="SEMIMAJOR AXIS")
                    tree.heading("#6", text="TEMP")
                    tree.heading("#7", text="DISCOVERY METHOD")
                    tree.heading("#8", text="DISTANCE")
                    tree.heading("#9", text="STAR MASS")
                    tree.heading("#10", text="STAR TEMP")
                    tree.column("#1", width=145) 
                    tree.column("#2", width=100)
                    tree.column("#3", width=90)
                    tree.column("#4", width=110)
                    tree.column("#5", width=110)
                    tree.column("#6", width=60)
                    tree.column("#7", width=120)
                    tree.column("#8", width=95)
                    tree.column("#9", width=83)
                    tree.column("#10", width=75)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=1,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
    
            elif selected_category == "BLACKHOLES":
                if selected_type == "DETECTED BLACKHOLES":
                    table_name = "blackholes"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF DETECTED BLACKHOLES""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("BLACKHOLE NAME","TYPE", "CONSTELLATION"))
                    tree.heading("#1", text="BLACKHOLE NAME")
                    tree.heading("#2", text="TYPE")
                    tree.heading("#3", text="CONSTELLATION")
                    tree.column("#1", width=210) 
                    tree.column("#2", width=220)
                    tree.column("#3", width=210)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=170,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()   
                
                elif selected_type == "SUPERMASSIVE BLACKHOLES":
                    table_name = "blackholes_dir"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF SUPERMASSIVE BLACKHOLES""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME","SIZE", "DISTANCE_FROM_NEAREST_CONSTELLATION"
                    ,"MASS"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="SIZE")
                    tree.heading("#3", text="DISTANCE_FROM_NEAREST_CONSTELLATION")
                    tree.heading("#4", text="MASS")
                    tree.column("#1", width=93) 
                    tree.column("#2", width=370)
                    tree.column("#3", width=285)
                    tree.column("#4", width=240)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=0,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()  

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
               
            elif selected_category == "ASTEROIDS":
                if selected_type == "SLOWEST ROTATORS":
                    table_name = "slowest_rotators_astr"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF SLOWEST ROTATOR ASTEROIDS""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("MINOR PLANET DESIGNATION","ROTATION(IN HOURS)", 
                    "MAGNITUDE", "QUALITY","ORBIT OR FAMILY","SPECTRAL TYPE","DIAMETER(KM)","ABS MAG(H)"))
                    tree.heading("#1", text="MINOR PLANET DESIGNATION")
                    tree.heading("#2", text="ROTATION(IN HOURS)")
                    tree.heading("#3", text="MAGNITUDE")
                    tree.heading("#4", text="QUALITY")
                    tree.heading("#5", text="ORBIT OR FAMILY")
                    tree.heading("#6", text="SPECTRAL TYPE")
                    tree.heading("#7", text="DIAMETER(KM)")
                    tree.heading("#8", text="ABS MAG(H)")
                    tree.column("#1", width=180) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=100)
                    tree.column("#4", width=100)
                    tree.column("#5", width=120)
                    tree.column("#6", width=93)
                    tree.column("#7", width=130)
                    tree.column("#8", width=80)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=26,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "FASTEST ROTATORS":
                    table_name = "fastest_rotators"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF FASTEST ROTATOR ASTEROIDS""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 20))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("MINOR PLANET DESIGNATION","ROTATION(IN HOURS)", 
                    "MAGNITUDE","QUALITY","ORBIT OR FAMILY","SPECTRAL TYPE","DIAMETER(KM)","ABS MAG(H)"))
                    tree.heading("#1", text="MINOR PLANET DESIGNATION")
                    tree.heading("#2", text="ROTATION(IN HOURS)")
                    tree.heading("#3", text="MAGNITUDE")
                    tree.heading("#4", text="QUALITY")
                    tree.heading("#5", text="ORBIT OR FAMILY")
                    tree.heading("#6", text="SPECTRAL TYPE")
                    tree.heading("#7", text="DIAMETER(KM)")
                    tree.heading("#8", text="ABS MAG(H)")
                    tree.column("#1", width=180) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=100)
                    tree.column("#4", width=100)
                    tree.column("#5", width=120)
                    tree.column("#6", width=93)
                    tree.column("#7", width=130)
                    tree.column("#8", width=80)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=26,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "MOST MASSIVE":
                    table_name = "most_massive_astr"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF MOST MASSIVE ASTEROIDS""",
                     fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("NAME","MASS", "PRECISION",
                    "APPROX PROPORTION OF ALL ASTR"))
                    tree.heading("#1", text="NAME")
                    tree.heading("#2", text="MASS")
                    tree.heading("#3", text="PRECISION")
                    tree.heading("#4", text="APPROX PROPORTION OF ALL ASTR")
                    tree.column("#1", width=200) 
                    tree.column("#2", width=230)
                    tree.column("#3", width=200)
                    tree.column("#4", width=220)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                elif selected_type == "BRIGHTEST FROM EARTH":
                    table_name = "brightest_astro"
                    TABLE_DESC = tk.Label(mainwindow, text="""LIST OF ASTEROIDS BRIGHTEST FROM EARTH""", 
                    fg="white", bg="black", font=("Bahnschrift Condensed", 30))
                    TABLE_DESC.pack()
                    TABLE_DESC.place(relx=0.5, rely=0.5, anchor="center")
                    TABLE_DESC.place(x=0, y=-225)
                    tree = ttk.Treeview(mainwindow, columns=("ASTROID", "MAGNITUDE", "SEMIMAJOR AXIS",
                    "ECCENTRICITY","DIAMETER","YEAR OF DISCOVERY"))
                    tree.heading("#1", text="ASTEROID")
                    tree.heading("#2", text="MAGNITUDE")
                    tree.heading("#3", text="SEMIMAJOR AXIS")
                    tree.heading("#4", text="ECCENTRICITY")
                    tree.heading("#5", text="DIAMETER")
                    tree.heading("#6", text="YEAR OF DISCOVERY")
                    tree.column("#1", width=180) 
                    tree.column("#2", width=130)
                    tree.column("#3", width=150)
                    tree.column("#4", width=100)
                    tree.column("#5", width=120)
                    tree.column("#6", width=130)
                    tree["show"] = "headings"
                    tree.pack(anchor="center")
                    tree.pack(padx=0, pady=5)
                    tree.place(x=70,y=100)
                    tree.config(height=20)
                    fetch_and_display_table()

                #WARNING STATEMTS LOGIC2

                elif selected_type == "":
                    primary()
                    WARNING = tk.Label(mainwindow, text="⚠️ PLEASE SELECT A TYPE", fg="white",
                     bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING.pack()
                    WARNING.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING.place(x=0, y=90)

                else:
                    primary()
                    WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                    bg="black", font=("Bahnschrift Condensed", 12))
                    WARNING3.pack()
                    WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                    WARNING3.place(x=0, y=90)
           
            
            else:
                primary()
                WARNING3 = tk.Label(mainwindow, text="⚠️ PLEASE SELECT FROM THE FOLLOWING", fg="white",
                bg="black", font=("Bahnschrift Condensed", 12))
                WARNING3.pack()
                WARNING3.place(relx=0.5, rely=0.5, anchor="center")
                WARNING3.place(x=0, y=90)
                
            #SCROLLBAR STATEMENT FOR TREEVIEW.
            
            if table_name == "notable":
              pass
            else:
                scrollbar = ttk.Scrollbar(mainwindow, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=scrollbar.set)
                scrollbar.pack(side="right", fill="y")
            
            

            def reselect():

            #DESTRUCTOIN OF TABLE PAGE WIDGETS.
                
                if table_name == "notable":
                    TABLE_DESC.destroy()
                    BACKTOPRIME.destroy()
                    primary()
                else:
                    tree.destroy()
                    TABLE_DESC.destroy()
                    scrollbar.destroy()
                    BACKTOPRIME.destroy()
                    primary()

            #BUTTON CODE TO GO BACK FROM TABLE SCREEN TO PRIMARY SCREEN

            BACKTOPRIME = ttk.Button(mainwindow, text= "<--", command=reselect)
            BACKTOPRIME.pack()
            BACKTOPRIME.place(x=20, y=20)

        #LOGIC OF THE DROPDOWN MENUS

        def update_second_dropdown(event):
            selected_option = CATEGO_DROP.get()
            TYPE_DROP['values'] = []
            if selected_option == 'STARS':
                 TYPE_DROP['values'] = ['NEAREST WHITE DWARFS', 'BIGHTEST STAR',
                  'OPEN CLUSTERS', 'THE NEAREST STARS TO EARTH']
            elif selected_option == 'GAMMA RAY BURSTS':
                TYPE_DROP['values'] = ['DETECTED GRB', 'MOST DISTANT GRB', 'GRB EXTREMES']
            elif selected_option == 'CONSTELLATIONS':
                TYPE_DROP['values'] = ['']
            elif selected_option == 'SUPERNOVAS':
                TYPE_DROP['values'] = ['DISTANT SUPERNOVAS', 'SUPERNOVA PROGENITOR CANDITATES', 
                'SUPERNOVA REMNANTS', 'LIST OF DETECTED SUPERNOVAS', 'YEARLY EXTRAGALACTIC SUPERNOVA REPORT']
            elif selected_option == 'GALAXIES':
                TYPE_DROP['values'] = ['>>>7x10^5 LIGHT YEARS', '<<<7x10^5 LIGHT YEARS']
            elif selected_option == 'NEBULAS':
                TYPE_DROP['values'] = ['LARGEST NEBULAE', 'PLANETARY NEBULAE', 'PROPLANETARY NEBULAE']
            elif selected_option == 'BLACKHOLES':
                TYPE_DROP['values'] = ['DETECTED BLACKHOLES', 'SUPERMASSIVE BLACKHOLES']
            elif selected_option == 'EXOPLANETS':
                TYPE_DROP['values'] = ['DIRECTLY IMAGED', 'DETECTED EXOPLANETS IN 2023', 
                'CONFIRMED NEAREST EXOPLANETS', 'POTENTIALLY HABITABLE EXOPLANETS']
            elif selected_option == 'SOLAR SYSTEM':
                TYPE_DROP['values'] = ['PLANETARY ATMOSPHERE & MAGNETIC FIELDS', 
                'FACT SHEET RATION TO EARTH', 'MEAN TEMPERATURE', 'COMPOSITION OF PLANETARY ELEMENTS']
            elif selected_option == 'MOONS':
                TYPE_DROP['values'] = ['MERCURY', 'VENUS', 'EARTH', 'MARS', 'JUPITER', 'SATURN', 'URANUS', 
                'NEPTUNE', 'PLUTO']
            elif selected_option == 'TIMELINE OF SPACE EXPLORATION':
                TYPE_DROP['values'] = ['PRE 20TH CENTURY', '1900 - 1956', '1957 - 1959', '1960 - 1969', 
                '1970 - 1979', '1980 - 1989', '1990 - 1999', '2000 - 2009', '2010 & LATER']
            elif selected_option == 'PEOPLE IN SPACE RIGHT NOW':
                TYPE_DROP['values'] = ['']
            elif selected_option == 'MOONWALKERS':
                TYPE_DROP['values'] = ['']
            elif selected_option == 'ASTEROIDS':
                TYPE_DROP['values'] = ['MOST MASSIVE', 'BRIGHTEST FROM EARTH', 'SLOWEST ROTATORS',
                 'FASTEST ROTATORS']
            
        #DESTROYING ALL WIDGETS OF HOMESCREEN
        
        TITLE.destroy()
        DESC.destroy()
        START.destroy()

       #DESTROYING KEY IF EXISTS
       
        if KEY == "":
         pass
        else:
            KEY.destroy()
            
        #SETTING UP THE PRIMARY SCREEN
        
        #STYLING THE TEXT

        custom_font_for_dropdowntext = ("Small Fonts", 25, "bold")

        #APP INSTRUCTIONS

        PRIMARY_DESC = tk.Label(mainwindow, text="""⚠️Choose a category --> Select a type based on the \
specific category -->Click "Fetch" for data
            Use the back button after fetching to make new selections""", fg="white", 
            bg="black", font=("Bahnschrift Condensed", 16))
        PRIMARY_DESC.pack()
        PRIMARY_DESC.place(relx=0.5, rely=0.5, anchor="center")
        PRIMARY_DESC.place(x=0, y=-200)

        #SELECT STRING AND COMBOBOX STATEMENTS FOR CATEGORY AND TYPE 

        CATEGO = tk.Label(mainwindow, text="Select a Category: 👇", 
        font=custom_font_for_dropdowntext, fg="white", bg="black")
        CATEGO.pack(expand=True, fill="both")
        CATEGO.place(x=-100, y=-100)
        CATEGO.place(relx=0.5, rely=0.5, anchor="center")
        TYPE = tk.Label(mainwindow, text="Select a Type: 👇", 
        font=custom_font_for_dropdowntext, fg="white", bg="black")
        TYPE.pack(expand=True, fill="both")
        TYPE.place(relx=0.5, rely=0.5, anchor="center")
        TYPE.place(x=-125, y=4)
        
        catego_var = tk.StringVar()
        type_var = tk.StringVar()

        CATEGO_DROP = ttk.Combobox(mainwindow, textvariable=catego_var ,
         values=['TIMELINE OF SPACE EXPLORATION', 'PEOPLE IN SPACE RIGHT NOW', 'MOONWALKERS', 'STARS', 'CONSTELLATIONS', 
         'GAMMA RAY BURSTS', 'SUPERNOVAS', 'GALAXIES', 'NEBULAS', 'BLACKHOLES', 'EXOPLANETS', 'SOLAR SYSTEM', 'ASTEROIDS', 
         'MOONS'], height=10,width=25, font=("Small Fonts", 12))
        CATEGO_DROP.pack(padx=20, pady=12)
        CATEGO_DROP.place(x=0, y=-45)
        CATEGO_DROP.place(relx=0.5, rely=0.5, anchor="center")
        CATEGO_DROP.bind("<<ComboboxSelected>>", update_second_dropdown)

        TYPE_DROP = ttk.Combobox(mainwindow,textvariable=type_var, values=[],
         height=10,width=25, font=("Small Fonts", 12)) 
        TYPE_DROP.pack(padx=20, pady=12)
        TYPE_DROP.place(x=0, y=55)
        TYPE_DROP.place(relx=0.5, rely=0.5, anchor="center")

        #FETCH STATEMENTS TO GET THE DESIRED TABLE

        FETCH = ttk.Button(mainwindow,text = "FETCH", style = "W.TButton", command=table)
        FETCH.pack(pady = 10)
        FETCH.place(relx=0.5, rely=0.5, anchor="center")
        FETCH.place(x=0, y=155)
        
         
        #BACK TO HOMESCREEN FUNCTION
        
        def returnhome():
            PREVIOUS.destroy()
            CATEGO.destroy()
            CATEGO_DROP.destroy()
            TYPE.destroy()
            TYPE_DROP.destroy()
            PRIMARY_DESC.destroy()
            FETCH.destroy()
            home()

        #CONFIG OF BUTTON BACK TO HOMESCREEN

        PREVIOUS = ttk.Button(mainwindow, text= "<--", command=returnhome)
        PREVIOUS.pack()
        PREVIOUS.place(x=20, y=20)

    if WARNING == "":
        pass
    else:
        WARNING.destroy()
            
    if WARNING2 == "":
        pass
    else:
        WARNING2.destroy() 

    if WARNING3 == "":
                pass
    else:
       WARNING3.destroy()

    if KEY == "":
         pass
    else:
        KEY.destroy()    
            

    # STELLAR_ARCHIVE LABEL ON THE HOMESCREEN

    custom_font = ("Small Fonts", 50, "bold")
    TITLE = tk.Label(mainwindow, text="🚀 Stellar_Archive 🌌", font=custom_font, fg="white", bg="black")
    TITLE.pack(expand=True, fill="both")
    TITLE.place(relx=0.5, rely=0.5, anchor="center")
    TITLE.place(x=0, y=-170)

    #APP DESCRIPTION

    text = """Stellar Archive is a comprehensive database-driven application designed to provide a rich source of\n 
    information on a wide range of space-related topics. Built using Python and integrated with a MySQL \n
    Database, this application offers users an extensive collection of data presented in the form of tables,\n
    making it a valuable resource for space enthusiasts, researchers, and students."""
    DESC = tk.Label(mainwindow, text=text, fg="white", bg="black", font=("Bahnschrift Condensed", 16))
    DESC.place(relx=0.5, rely=0.5, anchor="center")
    DESC.place(x=0, y=15)
    

    #SCRIPT FOR CLICK TO START BUTTON

    START = ttk.Button(mainwindow, text="CLICK HERE TO START",
                command = primary, style = "W.TButton")
    START.pack(pady = 10)
    START.place(relx=0.5, rely=0.5, anchor="center")
    START.place(x=0, y=185)

home()

#CHANGING THE APP ICON FROM DEFAULT

img = tk.PhotoImage(file='C:\\Users\\vihar\\OneDrive\\Desktop\\STELLAR ARCHIVE\\GUI SCRIPT\\windowicon.png')
mainwindow.iconphoto(False, img)

#FINAL STATMENT 
mainwindow.mainloop()

#THE END.......................
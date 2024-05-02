![Cover](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/e5bd416b-0829-4e08-8b30-0fc3d2dde8e4)

# Getting started with Stellar Archive.
* [About](#About)
* [Installation](#Installation-Procedure)
  * [Package Installation](#step-1-installation)
  * [Extraction](#step-2-extraction)
  * [Database Setup](#step-3-Database-setup)
  * [Pyinstaller](#step-4-pyinstaller)
  * [Application Setup](#step-5-application-setup)
* [Demo](#DEMO)

# About
Stellar Archive is a comprehensive database driven application made using python encompassing information about various celestial entities. This application was developed during my senior year as a school project. The repository houses all the collected data, the codes utilized, and includes a guidebook detailing our approach towards the final product. 

# Installation Procedure
Follow the steps to get my application "STELLAR ARCHIVE" on your machine to utilize or test it out.

* Your device must be pre equipped with MySQL DBMS.
* You must know the details of localhost,user and passwd of your MySql server.

## Step-1 (Installation)
#### **Click on this link 👉 [Installation Package](https://github.com/viharkmanoj/Stellar-Archvie/blob/main/INSTALLATION.zip) to open a page and click "ctrl+shift+s" after landing on the page to download the installation package.**

## Step-2 (Extraction)

#### **Extract the INSTALLATION.zip to get the following folders** 👇

![Screenshot (65)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/107ea1d5-0998-4755-a02b-904a935b293a)

## Step-3 (Database Setup)
#### **1) Open the following application on your desktop.** 👇

![Screenshot (66)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/6c0c8757-2624-4708-959a-246f459c8a37)

#### **2) Click on your server.** 👇

![Screenshot (67)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/f6486300-6551-4255-b452-3d91a8f1d91a)

#### **3) Select the Data Import/Restore option.** 👇

![Screenshot (68)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/a00db75b-4ba7-4e12-a043-5ffd44fffc95)

#### **4) Select the path to the folder named "Database Data" in the INSTALLATION folder which u have just extracted**

#### **5) Select Dump Structure and Data**

#### **6) And click Start Import**

![Screenshot (69)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/e1d38fce-f7b6-47e4-a6bc-90707f9929ae)

#### **The following Dialogue stating "Import Completed" will be presented if the database is installed perfectly.** 👇

![Screenshot (70)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/01b8b64d-8e8f-4a20-9b4a-350c1559157a)

## Step-4 (Pyinstaller)

#### **To install pyinstaller, open cmd and type the following and click enter** 👇
```bash
  pip install pyinstaller
```
## Step-5 (Application Setup)

#### **1) Open "GUI SCRIPT" folder from previously extracted Installation folder.** 

#### **2) Open "Main_GUI" and edit input_host, input_user, and input_password in the lines 9,10 and 11 respectively based on your server configurations and save.**

![Screenshot (71)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/3e8d286c-de11-4e80-a540-1269e4de883c)


#### **3) Go back to the folder, right click on the folder and select open in terminal** 👇

![image (1)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/1afc3ed1-a905-4ea0-8f17-7518a15ef3a9)

#### **4) Enter the following in the terminal and click enter👇**
``` bash
pyinstaller Main_GUI.py -w --onefile --icon=icon.ico
```
![Windows PowerShell 26-11-2023 15_12_27](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/c0d2273a-dc3a-46c6-b7eb-22063200a72d)

#### **5) The following dialogue will show up if it gets installed perfectly 👇**

![Windows PowerShell 26-11-2023 15_17_12](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/f1d1ea49-a446-4ef9-b276-f448d6941f37)

#### **6) The installed application will be present in the folder named dist and u can move it to any directory in your machine 👇**

![image (2)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/abdaaeba-d886-4077-94ea-05160577ee56)

#### **🎉 YOU HAVE NOW SUCCESSFULLY INSTALLED STELLAR ARCHIVE ON YOUR MACHINE 🙌**

![Screenshot (72)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/e18173d1-d04d-42e7-8f88-60d75584052e)


# DEMO

![Stellar Archive DEMO (4)](https://github.com/viharkmanoj/Stellar-Archvie/assets/124941764/1d04a24c-2ed8-4955-8123-37f765655a86)

# Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

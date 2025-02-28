# CS-340-Client-Server-Development
## Austin Animal Center Outcomes Database
  An application that utilizes MongoDB to create and manage a database assessable by users via a CRUD Python Module and a client-facing web application dashboard. Users can create, update, read, and delete (CRUD) various documents allowing for updateable and manageable data sets. This application can be used with any data set in JSON, CSV or TSV file form.
## Motivation
  Grazioso Salvare is an innovative international rescue-animal training company which identifies dogs that are good candidates for search-and-rescue training. Certain dogs are best suited for certain applications. A local non-profit organization that operates five animal shelters in the region around Austin, Texas has agreed to aid and assist Grazioso Salvare by granting access to their inventory data. This data contains every animal each shelter is currently or previously housed and is categorized by type, breed, name, sex, age, and various other factors. Grazioso Salvare would like to access all data and sort by specifics for faster and more accurate search-and-rescue dog training. This will be an open-source application so it can be adapted by similar organizations. 
## Getting Started 
1. **To get a local copy up and running, create a database through MongoDB and upload the data via a CSV, JSON, or TSV file format.**
```
mongoimport \
--username="${MONGO_USER}" --password="${MONGO_PASS}" --port=${MONGO_PORT} \
--host=${MONGO_HOST} --db database --collection folder --authenticationDatabase admin \
--type csv/json/tsv --file filename --headerline
```
```--headerline``` is used if file type is csv  
2. **Have an administrator create user accounts to read and write documents within the database.**  
- ***Open command prompt and load the Mongo Shell with***```mongosh```  
- Once the Mongo shell is loaded, the prompt ```test> ``` should be loaded  
Switch to the admin database to create a new user.  
```
test> use admin
switched to db admin
admin> db.createUser({user:"USERNAME", pwd:"PASSWORD", roles:[{role:readWrite",db:"DATABASE"}]})

{ ok: 1}
admin>
```
- The ```{ ok: 1}``` indicates the user creation was a success.
3. **Next, use this Python code to communicate CRUD functionalities to the database by replacing the name of the class used to instantiate.**  
```python
# @author: matthewtranch_snhu

import pymongo
from pymongo import MongoClient
from pymongo import ReturnDocument

# CRUD operations for Animal collection in MongoDB
class AnimalShelter(object):
  def __init__(self, USER, PASS, HOST, PORT, DB, COL):

    # Initialize Connection, take in username and password and
    # attempt to access database with credentials
    try:
      self.client = MongoClient('mongodb://$s:%s@$s:%d' % (USER,PASS,HOST,PORT))
      self.database = self.client['%s' % (DB)]
      self.collection = self.database['%s' % (COL)]
      self.client.server_info()

      # If test has failed
      except pymongo.errors.OperationFailure:
        return 0
```  
  
4. **Finally, use the web-based dashboard to initiate the Python CRUD code with your Mongo Database.**
- The code is listed in the Dash folder. The remained CRUD methods are located in the Python folder. The Dash application was used with Jupyter Notebook to run the dash code. Once loaded, the dash should look like the image below.
![1 Initial Dash](https://github.com/user-attachments/assets/41350fa0-99e4-4c2a-8aa6-bb165921d19d)
The data is loaded into a datatable along with a pie chart displaying the different types of breeds in the displayed data. The map shows the geolocation of the selected document by selecting a single row from the datatable. Each column can be filtered, along with specific qualifications set by Grazioso Salvare. These options can be altered or removed within the Dash code. Selecting different data aspects (Water Rescue, Mountain or Wilderness Rescue, ...etc) will change the datatable and reload with the appropriate data set along with the appropriate pie chart and map.
## Roadmap  

  Initially, trying to make the dashboard ‘user-friendly’ while still limiting user-errors was a bit challenging. More recently Dash versions allow for multiple Outputs in the callbacks, but this version does not. Disabling the buttons had to be done with individual callbacks, not a big deal but in the future, this can be corrected to a single callback. Without disabling the buttons, the user could select the ‘Water Rescue’ Radio Item and then select Cats, which would display all animal type Cats while still displaying a ‘Types of Water Rescue Breeds’ pie chart.   
\
	Originally, I wanted to display all types of animals within the database in the pie chart when no other options were selected. Considering the ‘Reset’ Radio Item is set to default, there never truly is no option selected. I tried having no default but could never get the right combination of ‘while-break and if loops’ to do what I wanted. Upon first load, a ‘Total Types of Animals’ pie chart would display with the correct information, but if I clicked the ‘Cats’ button, the pie to switch to the correct ‘Total Type of Breeds’ for a second, then quickly switch back to ‘Total Types of Animals’ showing 100% Cats. In the end, I decided to go a different path that works. In the future, I would like to change to the original idea, but perhaps someone with better Dash skills knows how to accomplish this.  


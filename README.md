# CS-340-Client-Server-Development
## Austin Animal Center Outcomes Database
An application that utilizes MongoDB to create and manage a database assessable by users via a CRUD Python Module and a client-facing web application dashboard. Users can create, update, read, and delete (CRUD) various documents allowing for updateable and manageable data sets. This application can be used with any data set in JSON, CSV or TSV file form.
## Motivation
Grazioso Salvare is an innovative international rescue-animal training company which identifies dogs that are good candidates for search-and-rescue training. Certain dogs are best suited for certain applications. A local non-profit organization that operates five animal shelters in the region around Austin, Texas has agreed to aid and assist Grazioso Salvare by granting access to their inventory data. This data contains every animal each shelter is currently or previously housed and is categorized by type, breed, name, sex, age, and various other factors. Grazioso Salvare would like to access all data and sort by specifics for faster and more accurate search-and-rescue dog training. This will be an open-source application so it can be adapted by similar organizations. 
## Getting Started 
To get a local copy up and running, create a database through MongoDB and upload the data via a CSV, JSON, or TSV file format. 
```
mongoimport \
--username="${MONGO_USER}" --password="${MONGO_PASS}" --port=${MONGO_PORT} \
--host=${MONGO_HOST} --db database --collection folder --authenticationDatabase admin \
--type csv/json/tsv --file filename --headerline
```
```--headerline``` is used if file type is csv
Have an administrator create user accounts to read and write documents within the database. 

Next, use this Python code to communicate CRUD functionalities to the database by replacing the name of the class used to instantiate. Finally, use the web-based dashboard to initiate the Python CRUD code with your Mongo Database. 

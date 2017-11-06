
## Basics of MongoDB

1. Installing MongoDB on MAC "brew install mongodb"
2. Starting MongoDB, just run "mongod" from one terminal (keeps running in foreground, either background it or user another terminal for running statements on DB"
3. From another terminal, type "mongo" to initiate the shell
4. To lists the data bases
   > show dbs
5. To Show collections (a.k.a tables)
   > show collections
6. To Insert a row in the collection named "tweet"
   > db.tweet.insert({"timestamp":"Mon Nov 06 05:19:23 +0000 2017","User":"ArkangelScrap","Tweet":"RT @developerWorks: Enhance Hortonworks Data Platform (HDP) with a variety of ISV solution capabilities. https://t.co/wuEVn1PXty"})
7. To List the contents of the table 
   > db.tweet.find({})
8. Using pymongo library to read data from MongoDB (Contents in the file Pymongo.py)

 

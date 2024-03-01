import pymongo 

# Provide the mongodb localhost url to connect python to mongodb
client = pymongo.MongoClient("localhost", 27017)
# Creating a new database
database = client["mydb"]

#Creating a new collection
collection = database["products"]

#Sample data
d = {"Company Name": "INeuron",
     "product": "Affordable AI",
     "Course Offered": "Machine Learning with deployment"}

# Inserting a record
rec = collection.insert_one(d)

# Find all the records
all_records = collection.find()

#Listing down all the records
for idx, record in enumerate(all_records):
    print(f"{idx}-{record}")

from pymongo import MongoClient
from credentials import Username, Password,cluster

# Replace with your actual connection string
connection_string = f"mongodb+srv://{Username}:{Password}@{cluster}.mongodb.net"


# Create a MongoClient to the running mongod instance
client = MongoClient(connection_string)

# Access a specific database
db = client['first']

# Access a specific collection
collection = db['first_collection']

# Example: Insert a document
document = {"name": "Alice", "age": 30}
collection.insert_one(document)

# Example: Find a document
result = collection.find_one({"name": "Alice"})
print(result)

# Don't forget to close the connection when done
client.close()

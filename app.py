from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['coupon_management']

# Step 2: Create Collections
promotions_collection = db['Promotions']
coupons_collection = db['Coupons']
users_collection = db['Users']

# Step 3: Implement CRUD Operations

# Create Operation
promotion1 = {
    'name': 'Black Friday Sale',
    'discount': 20,
    'start_date': '2023-11-24',
    'end_date': '2023-11-26'
}

promotion2 = {
    'name': 'Cyber Monday Sale',
    'discount': 30,
    'start_date': '2023-11-27',
    'end_date': '2023-11-28'
}

result1 = promotions_collection.insert_one(promotion1)
result2 = promotions_collection.insert_one(promotion2)

inserted_id1 = result1.inserted_id
inserted_id2 = result2.inserted_id

# Read Operation
all_promotions = promotions_collection.find()
for promotion in all_promotions:
    print(promotion)

# Update Operation
query = {'_id': inserted_id1}
new_values = {'$set': {'discount': 40}}
promotions_collection.update_one(query, new_values)

# Delete Operation
query = {'_id': inserted_id2}
promotions_collection.delete_one(query)

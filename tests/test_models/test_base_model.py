#!/usr/bin/python3
from models.base_model import BaseModel
from datetime import datetime

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Printing the object (calls __str__)
print(my_model)

# Calling save() to update the updated_at attribute
my_model.save()
print(my_model)

# Calling to_dict() and printing the dictionary
my_model_json = my_model.to_dict()
print(my_model_json)

# Printing the JSON representation of the object
print("JSON of my_model:")
for key in my_model_json.keys():
    print(f"\t{key}: ({type(my_model_json[key])}) - {my_model_json[key]}")



AIRBNB CLONE-THE CONSOLE


OVERVIEW


This project is a command-line interface (CLI) for managing a simplified version of an AirBnB web app. It enables the creation, manipulation, and storage of AirBnB objects, utilizing object-oriented programming in Python. The main goal is to create a working console with commands to handle BaseModel and User objects, along with basic operations like create, show, update, destroy, and list.



FEATURES

Create: Add new instances to storage and print their unique ID.

Show: Retrieve an instance by class name and ID, displaying its string representation.

Update: Modify attributes of an existing instance.

Destroy: Delete an instance from storage.

All: List all instances of a class or all stored objects.



TECHNOLOGIES USED


Python 3.x: Object-Oriented Programming

File Storage: JSON-based serialization for persistent data

Datetime: For tracking object creation and update times


FILE STRUCTURE


/models

    ├── base_model.py         # Base class for all models
    ├── user.py              # User class inherits from BaseModel
    └── storage.py           # Handles JSON file for data persistence
/console.py                  # Main program file, CLI for interaction
/test                        # Unit tests for various methods
README.md                   # Project documentation



SETUP AND USAGE




1.Clone this repository:

  bash
  git clone https://github.com/yourusername/alu-AirBnB_clone.git
  cd alu-AirBnB_clone
  
2. Run the console:
   
    bash
   ./console.py

4. Use commands to interact with the program:

   a) Create an instance:
   
       sql
      (hbnb) create User

   b) Show an instance:
   
       sql
      (hbnb) show User <id>

   c) Update an instance:
   
       sql
      (hbnb) update User <id> first_name "John"

   d) Destroy an instance:
   
       bash
      (hbnb) destroy User <id>


      

EXAMPLE Interaction



(hbnb) create BaseModel

<generated-id>
  
(hbnb) show BaseModel <generated-id>

[BaseModel] (<generated-id>) {...}

(hbnb) update BaseModel <generated-id> name "AirBnB"

(hbnb) show BaseModel <generated-id>

[BaseModel] (<generated-id>) {'name': 'AirBnB', ...}



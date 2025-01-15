import json
from models.user import User
from models.base_model import BaseModel
class FileStorage:
    """Serializes and deserializes objects to/from a JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to storage."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize objects to a JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)




    def reload(self):
        """Deserialize objects: JSON TO FILE"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                from models.base_model import BaseModel
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
                        cls = eval(class_name)
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
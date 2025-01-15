from models.engine.file_storage import FileStorage

# Initialize storage
storage = FileStorage()

# Import all classes to register them with the eval function
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Call reload to load objects from the JSON file
storage.reload()

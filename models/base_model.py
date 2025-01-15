import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Constructor that either creates a new instance or initializes from a dictionary."""
        if kwargs:
            # If kwargs is not empty, use the dictionary to initialize the instance
            for key, value in kwargs.items():
                # Skip the __class__ key in kwargs
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        # Convert string representation of datetime back to datetime objects
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            # If no kwargs, create a new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
      """Update the updated_at attribute with the current datetime and save to storage."""
      self.updated_at = datetime.now()
      from models import storage
      storage.new(self)  # Add the instance to storage
      storage.save()  # Save the storage dictionary to the JSON file


    def to_dict(self):
        """Return a dictionary representation of the instance."""
        dict_rep = self.__dict__.copy()
        # Convert datetime objects to strings
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep["__class__"] = self.__class__.__name__
        return dict_rep

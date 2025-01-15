import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_create(self, args):
        """Create a new instance of a class."""
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Show an instance of a class."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        """Destroy an instance of a class."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Show all instances, optionally filtered by class."""
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        objects = [
            str(obj) for key, obj in storage.all().items()
            if not args or key.startswith(args)
        ]
        print(objects)

    def do_update(self, args):
        """Update an instance of a class."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if not obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def do_quit(self, _):
        """Quit the console."""
        return True

    def do_EOF(self, _):
        """Handle EOF to exit the console."""
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

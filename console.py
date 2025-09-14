#!/usr/bin/python3
"""
Console for AirBnB clone project.
Handles creation, display, and storage of BaseModel instances.
"""

import cmd
from models import storage
from models.base_model import BaseModel
import shlex  # to properly parse arguments


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the console."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the console."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new BaseModel instance, save it, and print its id."""
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = f"{args[0]}.{obj_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
        else:
            print(all_objs[key])

   def do_all(self, arg):
        """Print all string representations of instances."""
        all_objs = storage.all()
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return
        print([str(obj) for obj in all_objs.values()])


if __name__ == "__main__":
    HBNBCommand().cmdloop()

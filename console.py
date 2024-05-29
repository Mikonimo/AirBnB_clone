#!/usr/bin/python3
"""Contains the entry point of the command Interpreter"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """command to exit the program"""
        return True

    def do_quit(self, line):
        """command to exit the program\n"""
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def emptyline(self):
        """do nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of User"""
        lines = line.split()
        if len(lines) == 0:
            print("** class name missing **")
            return
        else:
            cls_name = lines[0]
            if cls_name in globals() and issubclass(globals()[cls_name],
                                                    BaseModel):
                obj = globals()[cls_name]()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")
                return

    def do_show(self, line):
        """Prints the string representation of an instance based
        on class name and id"""
        lines = line.split()
        if len(lines) == 0:
            print("** class name missing **")
            return
        elif lines[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        elif len(lines) == 1:
            print("** instance id missing **")
            return
        key = f"{lines[0]}.{lines[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletese an instance based on the class name and id"""
        lines = line.split()
        if len(lines) == 0:
            print("** class name missing **")
            return
        elif lines[0] not in models.storage.classes():
            print("** class doesn't exist **")
            return
        elif len(lines) == 1:
            print("** instance id missing **")
            return
        key = f"{lines[0]}.{lines[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        instance = models.storage.all()[key]
        models.storage.delete(instance)

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        lines = line.split()
        if len(lines) == 0:
            print([str(obj) for obj in models.storage.all().values()])
        else:
            class_name = lines[0]
            if class_name in globals() and issubclass(globals()[class_name],
                                                      BaseModel):
                print([str(obj) for key, obj in models.storage.all().items()
                       if key.startswith(class_name)])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attributes"""
        lines = line.split()
        if len(lines) == 0:
            print("** class name missing **")
        elif lines[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(lines) == 1:
            print("** instance id missing **")
        elif len(lines) == 2:
            print("** attribute name missing **")
        elif len(lines) == 3:
            print("** value missing **")
        else:
            key = lines[0] + '.' + lines[1]
            if key in models.storage.all():
                obj = models.storage.all()[key]
                setattr(obj, lines[2], lines[3])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

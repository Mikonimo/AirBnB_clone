#!/usr/bin/python3
"""Contains the entry point of the command Interpreter"""
import cmd
from models.base_model import BaseModel
import models


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
        """Creates a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        if line != 'BaseModel':
            print("** class doesn't exit **")
            return
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on class name and id"""
        if not line:
            print("** class name missing **")
            return
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        key = f"{line[0]}.{line[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletese an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        if line[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(line) == 1:
            print("** instance id missing **")
            return
        key = f"{line[0]}.{line[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        del models.storage.all()[key]
        models.storage.save

    def do_all(self, line):
        """Prints all string representation of all instances based
        or not on the class name"""
        if line and line != "BaseModel":
            print("** class doesn't exist **")
            return
        instances = models.storage.all()
        if line:
            print([str(inst) for key, inst in instances.items() if key.startswith(line)])
        else:
            print([str(inst) for inst in instances.values()])
        
        
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()

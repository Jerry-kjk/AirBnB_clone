#!/usr/bin/python3
"""
Defines the HBNB console.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Custom command interpreter class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Method to pass when emptyline entered.
        """
        pass 

    def do_quit(self, arg):
        """
        Quit the command interpreter.
        """
        return True

    def do_EOF(self, line):
        """
        Exit the command interpreter.
        """
        print()
        return True

    def do_create(self, line):
        """
        Usage: create BaseModel
        Creates a new instance of BaseModel and prints the id.
        """
        args = line.split(" ")
        if args[0] == "BaseModel":
            bm = BaseModel()
            bm.save()
            print(bm.id)
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance and id.
        """
        args = line.split(" ")
        if args[0] == "BaseModel":
            if len(args) > 1:
                key = args[0] + "." + args[1]
                all_objs = storage.all()
                for obj_id in all_objs.keys():
                    if key == obj_id:
                        print(all_objs[obj_id])
                        break
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance and id.
        """
        args = line.split(" ")
        if args[0] == "BaseModel":
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if (storage.all()).pop(key, None) is None:
                    print("** no instance found **")
                else:
                    models.base_model.storage.all()[key].save()
            else:
                print("** instance id missing **")
        elif args[0] == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances based.
        """
        args = line.split(" ")
        if args == [''] or args[0] == "BaseModel":
            str_obj = []
            all_objs = storage.all()
            for obj_key in all_objs.keys():
                str_obj.append(str(all_objs[obj_key]))
            print(str_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id.
        """
        args = line.split(" ")
        if args[0] == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
             key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
                    storage.all()[key].save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

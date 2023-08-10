#!/usr/bin/python3
"""
Defines the HBNB console.
"""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()

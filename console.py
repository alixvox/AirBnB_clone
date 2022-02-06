#!/usr/bin/python3
"""
This module contains the class HBNBCommand, the console
"""
import cmd, sys

class HBNBCommand(cmd.Cmd):
    """
    this class is the functionality of the console
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """ Quit command to exit the program
        """
        return True
    
    def do_quit(self, line):
        """ Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        """
        This method Allows you to...
        (ENTER ALL THE WAY THROUGH..)
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
#!/usr/bin/python3
"""
This module contains the class HBNBCommand, the console
"""
import cmd
import sys
import inspect
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class is the functionality of the console.
    """
    intro = 'Welcome to the HBNB shell!  Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program.
        Usage: CTR+D
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program.
        Usage: quit
        """
        return True

    def emptyline(self):
        """This method passes at an empty line.
        Usage: ENTER key
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel.
        Usage: create BaseModel
        """
        classes = storage.classes()
        if line == '':
            print('** class name missing **')
        elif line in classes.keys():
            obj = classes[line]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, *args):
        """Prints the string representation of an instance.
        Usage: show City 49faff9a-6318-451f-87b6-910505c55907
        """
        classes = storage.classes()
        if args[0] == '':
            print("** class name missing **")
            return
        str = args[0]
        arg = str.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        str = arg[0] + '.' + arg[1]
        objs = storage.all()
        if str in objs.keys():
            print(objs[str])
            return
        print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance of a class with id.
        Usage: delete User 2dd6ef5c-467c-4f82-9521-a772ea7d84e9"
        """
        classes = storage.classes()
        if args[0] == '' or args[0] is None:
            print("** class name missing **")
            return
        str = args[0]
        arg = str.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        str = arg[0] + '.' + arg[1]
        objs = storage.all()
        if str in objs.keys():
            del objs[str]
            storage.save()
            return
        else:
            print("** no instance found **")
            return

    def do_all(self, *args):
        """Prints all string representation of all instances
        based or not on the class name.
        Usage: all City
        Usage: all
        """
        classes = storage.classes()
        objs = storage.all()
        objs_list = []
        if args[0] == '':
            for key, value in objs.items():
                objs_list.append(str(value))
            print(objs_list)
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        for key, value in objs.items():
            if args[0] == type(value).__name__:
                objs_list.append(str(value))
        print(objs_list)

    def do_update(self, *args):
        """Updates an instance based on the class name and id
        """
        objs = storage.all()
        classes = storage.classes()
        if args[0] == '' or args[0] is None:
            print("** class name missing **")
            return
        string = args[0]
        arg = string.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        string = arg[0] + '.' + arg[1]
        if string not in objs.keys():
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        try:
            i = float(arg[3])
            if i.is_integer():
                i = int(i)
        except (TypeError, ValueError):
            if "\"" in arg[3]:
                arg[3] = arg[3].replace("\"", "")
            setattr(objs[string], arg[2], str(arg[3]))
            storage.save()
            return
        setattr(objs[string], arg[2], i)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

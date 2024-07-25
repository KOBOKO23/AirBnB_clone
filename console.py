#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command processor for the HBNB console.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def help_quit(self, arg=None):
        """
        Help for the quit command.
        """
        print("Quit command to exit the program")

    def do_EoF(self, arg):
        """
        Handle End of File (EOF) signal to exit the program.
        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()


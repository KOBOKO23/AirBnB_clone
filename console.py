#!/usr/bin/python3
"""
Command interpreter for HBNB console.
"""
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

    def help_quit(self):
        """
        Help for the quit command.
        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle End of File (EOF) signal to exit the program.
        """
        print()
        return True

    def help_EOF(self):
        """
        Help for the End of File (EOF) command.
        """
        print("Handle End of File (EOF) signal to exit the program")

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

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

    def do_EoF(self, arg):
        """
        Handle End of File (EOF) signal to exit the program.
        """
        print()
        return True

    def help_quit(self):
        """
        Help for the quit command.
        """
        print("Quit command to exit the program")

    def help_EoF(self):
        """
        Help for the End of File (EOF) command.
        """
        print("End of File (EOF) signal to exit the program")

    def emptyline(self):
        """
        Override the default behavior for empty lines.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

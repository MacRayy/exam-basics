# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination
import sys

class Controller(object):
    def argument_reader(self):
        help_display = Display()
        if len(sys.argv) == 1:
            help_display.help_text()
        elif len(sys.argv) == 2:
            help_display.help_text_no_destination()

class Display(object):
    def help_text(self):
        return print("copy [source] [destination]")

    def help_text_no_destination(self):
        return print("No destination provided")

run_copy = Controller()
run_copy.argument_reader()

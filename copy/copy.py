# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination
import sys
import os

class Controller(object):
    def argument_reader(self):
        help_display = Display()
        if len(sys.argv) == 1:
            help_display.help_text()
        elif len(sys.argv) == 2:
            help_display.help_text_no_destination()
        elif len(sys.argv) == 3:
            file_name = sys.argv[1]
            if os.path.isfile(sys.argv[1]):
                copy = Copy()
                copy.copy_file()
            else:
                help_display.no_file()

class Display(object):
    def help_text(self):
        print("copy [source] [destination]")

    def help_text_no_destination(self):
        print("No destination provided")

    def no_file(self):
        print("Source is not a file")

class Copy(object):
    def copy_file(self):
        file_to_copy = open(sys.argv[1], "r")
        file_cotent = file_to_copy.read()
        print(file_cotent)

run_copy = Controller()
run_copy.argument_reader()

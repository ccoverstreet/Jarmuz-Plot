# Jarmuz Plot
# Cale Overstreet
# January 13th, 2020
# General plotting program for the Jarmuz package manager

import sys

# Project Modules
import autoplot.autoplot as autoplot

def parse_passed_arguments(arguments):
    # Parsing function for commandline arguments. Determines whether GUI will be launched or if quickplot was used

    for i in range(1, len(arguments)):
        if arguments[i] == "-h" or arguments[i] == "--help":
            print("Jarmuz Plot")
        elif arguments[i] == "" or arguments[i] == "autoplot":
            print("Autoplotting passed files")
            autoplot.autoplotter(arguments[i + 1: len(arguments)])
            
    

def main():
    # Main entrypoint 
    
    # Check arguments passed from command line
    parse_passed_arguments(sys.argv)
      

if __name__ == "__main__":
    main()

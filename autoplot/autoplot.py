# Jarmuz Plot: Autoplot Module
# Cale Overstreet
# January 13th, 2020
# Autoplot module for Jarmuz Plot

import matplotlib.pyplot as plt

class autoplotter():
    # Autoplot uses file extensions to determine data format and attempts to plo file data. Assumes x, y, z, ... format.

    verbose = False # Determines printout

    def __init__(self, arguments):
        # Init function decides what plotting methods to call 
        self.arguments = arguments
        print(self.arguments)

        for i in range(0, len(self.arguments)):
            if self.arguments[i] == "-v" or self.arguments[i] == "--verbose":
                self.verbose = True
            else:
                self.determine_plot_method(self.arguments[i]) 

    def determine_plot_method(self, filename):
        file_extension = ""
        plot_methods = {
            "xy": self.plot_xy
        }

        # Extracting file extension
        try:
            split_filename = filename.split(".")
            if len(split_filename) > 1:
                file_extension = filename.split(".")[-1]
            else:
                print("Unable to isolate file extension for file \"{}\"".format(filename))
        except:
            print("Unable to isolate file extension")

        # Using file extension to use correct plot method 
        try:
            plot_methods["xy"](filename)
        except Exception as err:
            print(err)


    def plot_xy(self, filename):
        # Function for plotting .xy files
        try:
            file = open(filename, 'r')
        except:
            print("Opening \"{}\" failed. Incorrect filename or missing file.".format(filename))
            return

        x = [];
        y = [];

        try:
            for line in file:
                templine = line.split(" ")

                x.append(float(templine[0]))
                y.append(float(templine[1]))
        except:
            print("Unable to read data from file \"{}\". Possible format error.".format(filepath))
            return

        print("Plotting \"{}\" file.".format(filename))

        # Asking and setting plot title
        plot_title = input("Plot title ({}): ".format(filename))
        if plot_title == "":
            plot_title = filename

        # Asking and setting xlabel
        plot_xlabel = input("X-Axis Label ({}): ".format("2-Theta"))
        if plot_xlabel == "":
            plot_xlabel = "2-Theta"

        # Asking and setting ylabel
        plot_ylabel = input("Y-Axis Label ({}): ".format("Intensity (counts)"))
        if plot_ylabel == "":
            plot_ylabel = "Intensity (counts)"
        
        plt.plot(x, y)

        plt.title(plot_title)
        plt.xlim(x[0], x[-1])
        plt.xlabel(plot_xlabel)
        plt.ylabel(plot_ylabel)
        plt.show()





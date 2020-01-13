import sys
import matplotlib.pyplot as plt

def plot_xy(filepath):
    try:
        file = open(filepath, 'r')
    except:
        print("Opening \"{}\" failed. Incorrect filename or missing file.".format(filepath))
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

    print("Plotting \"{}\" file.".format(filepath))
    plt.plot(x, y)
    plt.title(filepath)
    plt.xlim(x[0], x[-1])
    plt.xlabel("2-Theta")
    plt.ylabel("Intensity (count)")
    plt.show()

def main():
    arguments = sys.argv

    for i in range(1, len(arguments)):
        plot_xy(arguments[i])

if __name__ == "__main__":
    main()

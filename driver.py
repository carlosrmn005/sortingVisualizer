import color as color
import sortFunctions
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button, TextBox, RadioButtons

low = 0
high = 100
numInArray = 50
maxNumber = 50
sortSpeed = 1  # Fast = .01; Medium = .5; Slow = 1


class Index:
    ind = 0

    def update(self, event):
        self.ind += 1
        global numInArray
        try:
            numInArray = int(text_box.text)
            if numInArray > maxNumber:
                numInArray = 50
            elif numInArray < 0:
                numInArray = 0
        except ValueError:
            numInArray = 0
        # b.remove()
        yAxis.clear()
        xAxis.clear()
        ax.cla()
        # plt.cla()
        fillXYarray(yAxis, xAxis, numInArray, low, high)
        graphSetup()

    def bubble(self, event):
        self.ind += 1
        sortButton.color = "aliceblue"
        quickButton.color = "aliceblue"
        mergeButton.color = "aliceblue"
        insertButton.color = "aliceblue"
        bubbleButton.color = "lightblue"
        selectionButton.color = "aliceblue"

    def select(self, event):
        self.ind += 1
        sortButton.color = "aliceblue"
        quickButton.color = "aliceblue"
        mergeButton.color = "aliceblue"
        insertButton.color = "aliceblue"
        bubbleButton.color = "aliceblue"
        selectionButton.color = "lightblue"

    def quick(self, event):
        self.ind += 1
        sortButton.color = "aliceblue"
        quickButton.color = "lightblue"
        mergeButton.color = "aliceblue"
        insertButton.color = "aliceblue"
        bubbleButton.color = "aliceblue"
        selectionButton.color = "aliceblue"

    def merge(self, event):
        self.ind += 1
        sortButton.color = "aliceblue"
        quickButton.color = "aliceblue"
        mergeButton.color = "lightblue"
        insertButton.color = "aliceblue"
        bubbleButton.color = "aliceblue"
        selectionButton.color = "aliceblue"

    def insert(self, event):
        self.ind += 1
        sortButton.color = "aliceblue"
        quickButton.color = "aliceblue"
        mergeButton.color = "aliceblue"
        insertButton.color = "lightblue"
        bubbleButton.color = "aliceblue"
        selectionButton.color = "aliceblue"

    def sort(self, event):
        self.ind += 1
        sortButton.color = "lightblue"

        if bubbleButton.color == "lightblue":
            bubbleSort()

        elif selectionButton.color == "lightblue":
            selectionSort()

        elif insertButton.color == "lightblue":
            insertionSort()
        elif mergeButton.color == "lightblue":
            mergeSort(yAxis, 0, len(yAxis) - 1)
        elif quickButton.color == "lightblue":
            quickSort(yAxis, 0, len(yAxis) - 1)
        sortButton.color = "aliceblue"


def bubbleSort():
    bubbleButton.color = "aliceblue"
    n = len(yAxis)  # gets the length of the array

    # Go through the whole array
    for i in range(n):  # range(start, stop, step) -> (optinal, required, optional)
        # After this for loop the last i elements should be in order
        for j in range(0, n - i - 1):
            # time.sleep(1)
            ax.cla()
            graphSetup(j, j + 1)
            plt.pause(sortSpeed)
            # If current element is greater than next element swap
            if yAxis[j] > yAxis[j + 1]:
                yAxis[j], yAxis[j + 1] = yAxis[j + 1], yAxis[j]
                ax.cla()
                graphSetup(j, j + 1)
        ax.cla()
        graphSetup()


def selectionSort():
    selectionButton.color = "aliceblue"
    n = len(yAxis)

    for i in range(n):  # go through the array
        minimum = i
        for j in range(i + 1, n):  # find the smallest element from the remaining array
            ax.cla()
            graphSetup(i, j)
            plt.pause(sortSpeed)
            if yAxis[minimum] > yAxis[j]:
                minimum = j

        yAxis[i], yAxis[minimum] = yAxis[minimum], yAxis[i]  # swap
    ax.cla()
    graphSetup()


def insertionSort():
    insertButton.color = "aliceblue"
    n = len(yAxis)

    for i in range(1, n):
        key = yAxis[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        ax.cla()
        graphSetup(i)
        plt.pause(sortSpeed)
        while j >= 0 and key < yAxis[j]:
            yAxis[j + 1] = yAxis[j]
            j -= 1
        yAxis[j + 1] = key
        ax.cla()
        graphSetup(j + 1)
        plt.pause(sortSpeed)

    ax.cla()
    graphSetup()


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        ax.cla()
        graphSetup(k)
        plt.pause(sortSpeed)
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        ax.cla()
        graphSetup(k)
        plt.pause(sortSpeed)
        arr[k] = L[i]
        i += 1
        k += 1
        ax.cla()
        graphSetup(k)
        plt.pause(sortSpeed)

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        ax.cla()
        graphSetup(k)
        plt.pause(sortSpeed)
        arr[k] = R[j]
        j += 1
        k += 1
        ax.cla()
        graphSetup(k)
        plt.pause(sortSpeed)


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    mergeButton.color = "aliceblue"
    if l < r:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2
        m_int = int(m)
        # Sort first and second halves
        mergeSort(arr, l, m_int)
        mergeSort(arr, m_int + 1, r)
        merge(arr, l, m_int, r)
        ax.cla()
        graphSetup()
        plt.pause(sortSpeed)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            ax.cla()
            graphSetup(i, high, j)
            plt.pause(sortSpeed)
            arr[i], arr[j] = arr[j], arr[i]
            ax.cla()
            graphSetup(i, high, j)
            plt.pause(sortSpeed)

    ax.cla()
    graphSetup(i + 1, high)
    plt.pause(sortSpeed)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    ax.cla()
    graphSetup(i + 1, high)
    plt.pause(sortSpeed)
    return i + 1


def quickSort(arr, low, high):
    quickButton.color = "aliceblue"
    if low < high:
        par = partition(arr, low, high)

        quickSort(arr, low, par - 1)
        quickSort(arr, par + 1, high)
    ax.cla()
    graphSetup()
    plt.pause(sortSpeed)


def graphSetup(*args):
    if len(args) == 0:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Graph")
        x_axis = ax.axes.get_xaxis()
        x_label = x_axis.get_label()
        x_label.set_visible(False)
        y_axis = ax.axes.get_yaxis()
        y_label = y_axis.get_label()
        y_label.set_visible(False)
        # plt.title("Test Graph")
        # plt.xlabel("x")
        # plt.ylabel("y")
        b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
        plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    elif len(args) == 1:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Graph")
        x_axis = ax.axes.get_xaxis()
        x_label = x_axis.get_label()
        x_label.set_visible(False)
        y_axis = ax.axes.get_yaxis()
        y_label = y_axis.get_label()
        y_label.set_visible(False)
        # plt.title("Test Graph")
        # plt.xlabel("x")
        # plt.ylabel("y")
        b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
        if args[0] >= len(yAxis):
            b[len(yAxis) - 1].set_color("orangered")
        else:
            b[args[0]].set_color("orangered")
        plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    elif len(args) == 2:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Graph")
        x_axis = ax.axes.get_xaxis()
        x_label = x_axis.get_label()
        x_label.set_visible(False)
        y_axis = ax.axes.get_yaxis()
        y_label = y_axis.get_label()
        y_label.set_visible(False)
        # plt.title("Test Graph")
        # plt.xlabel("x")
        # plt.ylabel("y")
        b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
        b[args[0]].set_color("orangered")
        b[args[1]].set_color("peachpuff")
        plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    elif len(args) == 3:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_title("Graph")
        x_axis = ax.axes.get_xaxis()
        x_label = x_axis.get_label()
        x_label.set_visible(False)
        y_axis = ax.axes.get_yaxis()
        y_label = y_axis.get_label()
        y_label.set_visible(False)
        # plt.title("Test Graph")
        # plt.xlabel("x")
        # plt.ylabel("y")
        b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
        b[args[0]].set_color("orangered")
        b[args[1]].set_color("peachpuff")
        b[args[2]].set_color("r")
        plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)


# There is an easier way to do this but Im a noob so this is my solution-------------------
# to this----------------------------------------------------------------------------------
def sortLabel():
    labelAxes.spines["top"].set_visible(False)
    labelAxes.spines["right"].set_visible(False)
    labelAxes.spines["bottom"].set_visible(False)
    labelAxes.spines["left"].set_visible(False)
    x_axis = labelAxes.axes.get_xaxis()
    x_label = x_axis.get_label()
    x_label.set_visible(False)
    y_axis = labelAxes.axes.get_yaxis()
    y_label = y_axis.get_label()
    y_label.set_visible(False)
    labelAxes.set_yticklabels([])
    labelAxes.set_xticklabels([])
    labelAxes.set_xticks([])
    labelAxes.set_yticks([])
    labelAxes.set_title("Choose a Sorting Method")


def fillXYarray(arr1, arr2, arrayNum, smallestValue, largestValue):
    for i in range(0, arrayNum):
        x = random.randint(smallestValue, largestValue)
        arr1.append(x)
        arr2.append(i)


def submit(text):
    print(text)


# Bar Charts

yAxis = []
xAxis = []

callback = Index()
fillXYarray(yAxis, xAxis, numInArray, low, high)

# Changing Window Title and removing toolbar------------------------------------------------
mpl.rcParams["toolbar"] = "None"
fig = plt.figure()
fig.canvas.set_window_title("Sorting Visualizer")

# Label stating "Choose sort method"--------------------------------------------------------
ax = plt.axes([.25, .25, .6, .6])
b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
labelAxes = plt.axes([0.65, 0.08, 0.09, 0.05])
sortLabel()
# Making the Buttons and Text Area----------------------------------------------------------
updateAxes = plt.axes([0.25, .05, .09, .05])
bubbleAxes = plt.axes([0.55, 0.07, 0.09, 0.05])
selectionAxes = plt.axes([0.65, 0.07, 0.09, 0.05])
insertAxes = plt.axes([0.75, 0.07, 0.09, 0.05])
mergeAxes = plt.axes([0.6, 0.01, 0.09, 0.05])
quickAxes = plt.axes([0.7, 0.01, 0.09, 0.05])
sortAxes = plt.axes([0.855, 0.018, 0.13, 0.095])
textBoxAxes = plt.axes([0.15, 0.05, 0.09, 0.05])

updateButton = Button(updateAxes, "Update", color="aliceblue", hovercolor="lightblue")
bubbleButton = Button(bubbleAxes, "Bubble", color="aliceblue", hovercolor="lightblue")
selectionButton = Button(selectionAxes, "Select", color="aliceblue", hovercolor="lightblue")
insertButton = Button(insertAxes, "Insert", color="aliceblue", hovercolor="lightblue")
mergeButton = Button(mergeAxes, "Merge", color="aliceblue", hovercolor="lightblue")
quickButton = Button(quickAxes, "Quick", color="aliceblue", hovercolor="lightblue")
sortButton = Button(sortAxes, "SORT", color="aliceblue", hovercolor="lightblue")
text_box = TextBox(textBoxAxes, "Type Here ", initial="", color="w")
updateButton.on_clicked(callback.update)
bubbleButton.on_clicked(callback.bubble)
selectionButton.on_clicked(callback.select)
insertButton.on_clicked(callback.insert)
mergeButton.on_clicked(callback.merge)
quickButton.on_clicked(callback.quick)
sortButton.on_clicked(callback.sort)
text_box.on_submit(submit)

# Making Radio Buttons--------------------------------------------------------------------
rax = plt.axes([0.39, 0.01, 0.1, 0.15], facecolor="w")
rax.spines["top"].set_visible(False)
rax.spines["right"].set_visible(False)
rax.spines["bottom"].set_visible(False)
rax.spines["left"].set_visible(False)
radio = RadioButtons(rax, ("Slow", "Medium", "Fast"))
for circle in radio.circles:
    circle.set_radius(0.05)


def speedFunction(label):
    global sortSpeed
    if label == "Slow":
        sortSpeed = 1
    elif label == "Medium":
        sortSpeed = .5
    elif label == "Fast":
        sortSpeed = .01
    plt.draw()


radio.on_clicked(speedFunction)
graphSetup()
plt.show()

# Histogram
# population_ages = []
# ids = [x for x in range(len(population_ages))]
# for i in range(0, 100):
#     x = random.randint(1, 100)
#     population_ages.append(x)
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# fig_size = plt.rcParams["figure.figsize"]
# print("Current size:", fig_size)
# fig_size[0] = 5
# fig_size[1] = 5
# plt.rcParams["figure.figsize"] = fig_size
# plt.axes([0.25, .25, .5, .5])
# plt.hist(population_ages, bins=100, histtype="bar", rwidth=0.5)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Test Graph")
# plt.legend()

# plt.show()

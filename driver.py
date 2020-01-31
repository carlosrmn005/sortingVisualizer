import color as color
import sortFunctions
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button, TextBox

low = 0
high = 100
numInArray = 50
maxNumber = 50


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
        # histButton1 = Button(histAxes1, "Update", color='lightgoldenrodyellow', hovercolor='0.975')


def graphSetup():
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.set_title("Graph")
    x_axis = ax.axes.get_xaxis()
    x_label = x_axis.get_label()
    x_label.set_visible(False)
    y_axis = ax.axes.get_yaxis()
    y_label = y_axis.get_label()
    y_label.set_visible(False)
    b = ax.bar(xAxis, yAxis, label="Bar1", color="royalblue")
    # plt.title("Test Graph")
    # plt.xlabel("x")
    # plt.ylabel("y")

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
ax = plt.axes([.20, .25, .6, .6])
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
bubbleButton.on_clicked(callback.update)
selectionButton.on_clicked(callback.update)
insertButton.on_clicked(callback.update)
mergeButton.on_clicked(callback.update)
quickButton.on_clicked(callback.update)
sortButton.on_clicked(callback.update)
text_box.on_submit(submit)


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

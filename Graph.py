import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from scipy.interpolate import UnivariateSpline


font = {'size': 25}
matplotlib.rc('font', **font)





def readFile(filename):
    file = open(filename,"r")
    power = []
    sum_rate = []

    for line in file:
        list = line.rstrip().split(" ")
        power.append(float(list[0]))
        sum_rate.append(float(list[1]))

    file.close()
    power = np.array(power)*100
    sum_rate = np.array(sum_rate)

    return power,sum_rate



def lineGraph(x,y,xTitle,yTitle,title,c,linewidth):
    xnew = np.linspace(x.min(), x.max(), 100)
    ysmooth = spline(x, y, xnew)
    plt.plot(xnew, ysmooth, color=c, linewidth=linewidth)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.grid(linewidth=0.5)
    plt.yticks(np.arange(0, 3, 0.5))
    #plt.xticks(np.arange(25, 100 + 5, 5))
    # plt.xticks(np.arange(50, 100 + 5, 5))
    plt.title(title)
    plt.xlim(100,0)
    plt.show()

"""
sum_rate= [2.9639,2.8778,2.8111,2.7376,2.6530,2.5423,2.4135,2.2553,2.0375,1.7510,1.8381]
sum_rate = sum_rate[::-1]
sum_rate = np.array(sum_rate)
Pconstraint=[1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0.0]
Pconstraint = Pconstraint[::-1]
Pconstraint = np.array(Pconstraint)*100
"""

f = "SumRateMax_QoSConstraint/expectationPower.txt"

max_expected_power,sum_rate = readFile(f)




lineGraph(max_expected_power,sum_rate,"Percentage of Maximum Power","Average Sum Rate","Effect of Average/Expected Power Constraint","red",2)

import matplotlib.pyplot as plt
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

point = np.genfromtxt('points.csv', delimiter=',')
distance = np.genfromtxt('distances.csv', delimiter=',')

if __name__ == "__main__":
    plt.scatter(point[:, 0], point[:, 1], c=distance)    
    plt.show()
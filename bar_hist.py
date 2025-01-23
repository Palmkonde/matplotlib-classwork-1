import matplotlib.pyplot as plt
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

bar_data = np.genfromtxt('values_for_bars.csv', delimiter=',')
hist_data = np.genfromtxt('values_for_hist.csv', delimiter=',')


def bar(data: np.ndarray) -> None:
    unique_data, counts = np.unique(bar_data, return_counts=True)
    logger.info("%s, %s", unique_data, counts)
    
    plt.bar(unique_data, counts)
    plt.ylim(min(counts) - 50, 1000)
    plt.xticks(unique_data)
    plt.show()

def hist(data: np.ndarray) -> None:
    logger.info("%s", hist_data)
    
    plt.hist(data)
    plt.show()


if __name__ == "__main__":
    hist(hist_data)

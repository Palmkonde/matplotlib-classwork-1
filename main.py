import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class PlotGraph:
    def __init__(self, range: Tuple[int, int]=(0, 10), amount: int=100) -> None:
        self.range = range
        self.x = np.linspace(start=range[0], stop=range[1], num=amount)
        
        plt.ylim(-10, 10)
    
    def f1(self) -> None:
        y = np.power(self.x, 2) 
        
        plt.plot(self.x, y)
        
        logger.info("this is y: %s", y)
    
    def f2(self) -> None:
        y = self.x * np.sin(2 * self.x)
        
        plt.plot(self.x, y)

        logger.info("this is y: %s", y)
        
    def f3(self) -> None:
        y = np.arctan(self.x)
        
        plt.plot(self.x, y)

        logger.info("this is y: %s", y)
    
    def show(self) -> None:
        plt.show()
        

if __name__ == "__main__":
    pg = PlotGraph(range=(-10, 10))
    pg.f1()
    pg.f2()
    pg.f3()
    pg.show()
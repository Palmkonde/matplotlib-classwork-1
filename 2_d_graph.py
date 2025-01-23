import matplotlib.pyplot as plt
import numpy as np
from typing import Tuple
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Plot2DGraph():
    def __init__(self, range: Tuple[int, int]=(-3, 3), amount: int=100) -> None:
        self.x = np.linspace(start=range[0], stop=range[1], num=amount)
        self.y = np.linspace(start=range[0], stop=range[1], num=amount)
        
        self.x, self.y = np.meshgrid(self.x, self.y)

        self.fig = plt.figure()
        self.ax = {
            "f1": self.fig.add_subplot(2, 2, 1, projection='3d'),
            "f2": self.fig.add_subplot(2, 2, 2, projection='3d'),
            "f3": self.fig.add_subplot(2, 1, 2, projection='3d'),
        }

        
    def f1(self) -> None:
        z = self.x * self.y
        self.ax["f1"].plot_surface(self.x, self.y, z)
        
    def f2(self) -> None:
        z = np.power(self.x, 2) + np.power(self.y, 2)
        self.ax["f2"].plot_surface(self.x, self.y, z)
    
    def f3(self) -> None:
        z = np.sin(3 * self.x) * self.y
        self.ax["f3"].plot_surface(self.x, self.y, z)

    def show(self) -> None:
        self.fig.tight_layout()
        plt.show()

if __name__ == "__main__":
    pg = Plot2DGraph()
    pg.f1()
    pg.f2()
    pg.f3()
    pg.show()

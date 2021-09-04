import numpy as np
from matplotlib import pyplot as pt

if __name__ == '__main__':
    # pt.figure("Test")
    pt.switch_backend("agg")
    pt.plot(np.linspace(0, 1, 50), np.sin(2*np.pi*np.linspace(0, 1, 50)))

    pt.savefig("./t1.png")
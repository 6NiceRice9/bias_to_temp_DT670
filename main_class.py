import numpy as np

class DT670:
    def __init__(self, z) -> None:
        #self.mV = mV
        self.z = z # if z is not None else mV
        

    def c_2_12(self):
        ZL = 1.294390
        ZU = 1.680000
        T0 = 0
        constants = (6.429274, -7.514262, -0.725882, -1.117846, -0.562041, -0.360239, -0.229751, -0.135713, -0.068203, -0.029755)
        normalized_var = ((self.z - ZL) - (ZU - self.z)) / (ZU - ZL)

        for index in range(len(constants)):
            T = T0 + constants[index] * np.cos(index * np.arccos(normalized_var))
            return print(T)

if __name__ == "__main__":
    print("executed")

#    print("got executed from script directly")


import typing
import csv
import numpy as np


class CECCalculator:
    m_size: int
    m_x = None  # np.array double
    m_y = None  # np.array double
    m_matrix = None  # np.matrix double
    m_ec_y = None
    m_ec_x1 = None  # np.array double
    m_ec_x2 = None  # np.array double
    m_ec_x3 = None  # np.array double
    m_ec_coefs = None  # np.array double
    m_f1 = None  # np.array double
    m_f2 = None  # np.array double
    m_f3 = None  # np.array double

    def R(self, x: float, a: float, mu: float, gamma: float, nu: float) -> float:
        return (
                a
                * np.exp(mu * np.log(abs(x)))
                * np.exp(-gamma * np.exp(nu * np.log(abs(x))))
                )

    def Integrate(self, x: np.typing.ndarray, y: np.typing.ndarray, ind: int) -> float:
        summ = 0.0
        for i in range(ind - 1):
            summ += (x[i + 1] - x[i]) * (y[i + 1] + y[i]) * 0.5
        return summ

    def calcY(self) -> np.typing.ndarray | None:  # будем возвращать новый y, а не менять старый
        if self.m_size == 0:
            return
        y = np.empty(self.m_size)
        for i in range(self.m_size):
            y[i] = self.m_x[i] * self.m_y[i] - self.m_x[0] * self.m_y[0]
        return y

    def calcX1(self) -> np.typing.ndarray | None:  # будем возвращать новый, а не менять старый
        if self.m_size == 0:
            return
        x1 = np.empty(self.m_size)
        for i in range(self.m_size):
            x1[i] = self.Integrate(self.m_x, self.m_y, i)
        return x1

    def calcX2(self) -> np.typing.ndarray | None:  # будем возвращать новый, а не менять старый
        if self.m_size == 0:
            return
        tmp = np.empty(self.m_size)
        for i in range(self.m_size):
            tmp[i] = self.m_y[i] * np.log(abs(self.m_y[i]))
        x2 = np.empty(self.m_size)
        for i in range(self.m_size):
            x2[i] = self.Integrate(self.m_x, tmp, i)
        return x2

    def calcX3(self) -> np.typing.ndarray | None:  # будем возвращать новый, а не менять старый
        if self.m_size == 0:
            return
        tmp = np.empty(self.m_size)
        for i in range(self.m_size):
            tmp[i] = self.m_y[i] * np.log(abs(self.m_x[i]))
        x3 = np.empty(self.m_size)
        for i in range(self.m_size):
            x3[i] = self.Integrate(self.m_x, tmp, i)
        return x3

    def Correlator(self, ind1: int, ind2: int) -> float:
        if self.m_size == 0:
            return 0.0
        if ind1 <= 0 or ind1 >= 4:
            return 0.0
        if ind2 <= 0 or ind2 >= 4:
            return 0.0
        arr1 = np.empty(self.m_size)
        arr2 = np.empty(self.m_size)
        match ind1:
            case 1:
                np.copyto(arr1, self.m_ec_x1)
            case 2:
                np.copyto(arr1, self.m_ec_x2)
            case 3:
                np.copyto(arr1, self.m_ec_x3)
            case 4:
                np.copyto(arr1, self.m_ec_y)

        match ind2:
            case 1:
                np.copyto(arr2, self.m_ec_x1)
            case 2:
                np.copyto(arr2, self.m_ec_x2)
            case 3:
                np.copyto(arr2, self.m_ec_x3)
            case 4:
                np.copyto(arr2, self.m_ec_y)

        summ = 0.0
        for i in range(self.m_size):
            summ += arr1[i] * arr2[i]
        return summ / self.m_size

    def GenerateData(self, size: int, x1: float, x2: float, a: float, mu: float, gamma: float, nu: float) -> None:
        if size <= 0:
            return
        if x1 > x2:
            return
        self.m_size = size
        self.m_x = np.empty(self.m_size)  # по идее, старые данные не нужны и вместо resize пойдет
        self.m_y = np.empty(self.m_size)
        delta = (x2 - x1) / (self.m_size - 1.0)
        for i in range(self.m_size):
            self.m_x[i] = x1 + i * delta
            self.m_y[i] = self.R(self.m_x[i], a, mu, gamma, nu)

    def LoadData(self, filename: str) -> bool:
        f = open(filename)
        data = list(f.readlines())
        self.m_size = len(data)
        self.m_x = np.empty(self.m_size)
        self.m_y = np.empty(self.m_size)
        for i, line in enumerate(data):  # i = x_i; y_i
            x, y = map(float, line.split(';'))
            self.m_x[i] = x
            self.m_y[i] = y
        f.close()
        return True

    def SaveData(self, filename: str) -> bool:
        if self.m_size == 0 or self.m_size != len(self.m_x):
            return False
        with open('filename', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='; ')
            for i in range(self.m_size):
                writer.writerow([self.m_x[i], self.m_y[i]])
        return True


    def SaveResults(self, filename: str) -> None:
        pass

    def CalcEigenCoordinates(self):
        self.m_ec_y = self.calcY()
        self.m_ec_x1 = self.calcX1()
        self.m_ec_x2 = self.calcX2()
        self.m_ec_x3 = self.calcX3()

    def CalcEigenCoefficients(self):
        self.m_matrix = np.empty((3, 4))
        for i in range(3, 0, -1):  # 3 ... 1
            s = ''
            for j in range(1, 5):  # 1 ... 4
                corr = self.Correlator(i, j)
                self.m_matrix[i - 1][j - 1] = corr  # TODO: спорный момент, так ли нужно
                s = s + " " + str(corr)
            print(i, s)
        raise NotImplementedError("Не доделал")

    def CalculateParameters(self):
        pass

    def CalculatePlotFunctions(self):
        pass


from main import CECCalculator
import matplotlib.pyplot as plt

ec = CECCalculator()
ec.GenerateData(100, 0.0001, 15.25, a=1, mu=0, gamma=0.3, nu=2, rand=0)
# ec.SaveData('ex1.csv')
ec.CalcEigenCoordinates()
ec.CalcEigenCoefficients()
ec.CalculateParameters()
ec.CalculatePlotFunctions()
# ec.SaveResults('ex1-results.csv')
plt.scatter(ec.m_x, ec.m_y, s=1, color='black')
plt.scatter(list(map(lambda x: -x, ec.m_x)), ec.m_y, s=1, color='black')
plt.show()


x1 = plt.scatter(ec.m_x, ec.m_ec_x1, s=1, label='X1(x)')
x2 = plt.scatter(ec.m_x, ec.m_ec_x2, s=1, label='X2(x)')
x3 = plt.scatter(ec.m_x, ec.m_ec_x3, s=1, label='X3(x)')
y = plt.scatter(ec.m_x, ec.m_ec_y, s=1, label='Y(x)')
plt.legend(handles=[x1, x2, x3, y])
plt.show()

plt.scatter(ec.m_ec_x1, ec.m_f1, s=1)
plt.show()
# plt.scatter(ec.m_ec_x2, ec.m_f2, s=1)
# plt.show()
# plt.scatter(ec.m_ec_x3, ec.m_f3, s=1)
# plt.show()

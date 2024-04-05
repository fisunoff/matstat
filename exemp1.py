from main import CECCalculator
import matplotlib.pyplot as plt

ec = CECCalculator()
ec.LoadData('test1.csv')
# ec.SaveData('ex1.csv')
ec.CalcEigenCoordinates()
ec.CalcEigenCoefficients()
ec.CalculateParameters()
ec.CalculatePlotFunctions()
# ec.SaveResults('ex1-results.csv')
plt.plot(ec.m_x, ec.m_y, color = 'blue')
dc = CECCalculator()
dc.GenerateData(1000, 1, 252, a=4096.560526344275, mu=0.010181032502358654, gamma=-1.8318079698320882e-08,
                nu=2.9345178170159376)
dc.SaveData('ex1.csv')
dc.CalcEigenCoordinates()
dc.CalcEigenCoefficients()
dc.CalculateParameters()
dc.CalculatePlotFunctions()
dc.SaveResults('ex1-results.csv')
plt.plot(dc.m_x, dc.m_y)
# plt.scatter(list(map(lambda x: -x, ec.m_x)), ec.m_y, s=1, color = 'blue')
plt.show()


x1 =  plt.scatter(ec.m_x, ec.m_ec_x1, s=1,label = 'X1(x)')
x2 = plt.scatter(ec.m_x, ec.m_ec_x2, s=1,label = 'X2(x)')
x3 = plt.scatter(ec.m_x, ec.m_ec_x3, s=1 ,label = 'X3(x)')
y = plt.scatter(ec.m_x, ec.m_ec_y, s=1, label = 'Y(x)')
plt.legend(handles=[x1, x2, x3, y])
plt.show()
#
# plt.scatter(ec.m_ec_x1, ec.m_f1, s=1)
# plt.show()
# plt.scatter(ec.m_ec_x2, ec.m_f2, s=1)
# plt.show()
# plt.scatter(ec.m_ec_x3, ec.m_f3, s=1)
# plt.show()

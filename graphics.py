from main import CECCalculator
import matplotlib.pyplot as plt

ec = CECCalculator()
ec.GenerateData(100, 0.25, 15.25, a=1.55, mu=1.05, gamma=0.15, nu=1.3, rand=0.3)
# ec.SaveData('ex1.csv')
ec.CalcEigenCoordinates()
ec.CalcEigenCoefficients()
ec.CalculateParameters()
ec.CalculatePlotFunctions()
# ec.SaveResults('ex1-results.csv')
plt.scatter(ec.m_x, ec.m_y, s=1)
plt.show()


plt.scatter(ec.m_x, ec.m_ec_x1, s=1)
plt.scatter(ec.m_x, ec.m_ec_x2, s=1)
plt.scatter(ec.m_x, ec.m_ec_x3, s=1)
plt.scatter(ec.m_x, ec.m_ec_y, s=1)
plt.show()

plt.scatter(ec.m_ec_x1, ec.m_f1, s=1)
plt.scatter(ec.m_ec_x2, ec.m_f2, s=1)
plt.scatter(ec.m_ec_x3, ec.m_f3, s=1)
plt.show()

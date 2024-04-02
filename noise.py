from main import CECCalculator
import matplotlib.pyplot as plt

ec = CECCalculator()
ec.GenerateData(1000, 0.25, 15.25, a=1.55, mu=1.05, gamma=0.15, nu=1.3, rand=0.0)
ec.CalcEigenCoordinates()
ec.CalcEigenCoefficients()
a, mu, nu, gamma = ec.CalculateParameters()


ec_new = CECCalculator()
ec_new.GenerateData(1000, 0.25, 15.25, a=a, mu=mu, gamma=gamma, nu=nu, rand=0.0)
ec_new.CalcEigenCoordinates()
ec_new.CalcEigenCoefficients()
ec_new.CalculateParameters()

plt.scatter(ec.m_x, ec.m_y, s=1)
plt.scatter(ec_new.m_x, ec_new.m_y, s=1)
plt.show()


ec = CECCalculator()
ec.GenerateData(1000, 0.25, 15.25, a=1.55, mu=1.05, gamma=0.15, nu=1.3, rand=0.5)
ec.CalcEigenCoordinates()
ec.CalcEigenCoefficients()
a, mu, nu, gamma = ec.CalculateParameters()


ec_new = CECCalculator()
ec_new.GenerateData(1000, 0.25, 15.25, a=a, mu=mu, gamma=gamma, nu=nu, rand=0.0)
ec_new.CalcEigenCoordinates()
ec_new.CalcEigenCoefficients()
ec_new.CalculateParameters()

plt.scatter(ec.m_x, ec.m_y, s=1)
plt.scatter(ec_new.m_x, ec_new.m_y, s=1)
plt.show()
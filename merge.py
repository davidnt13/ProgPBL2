import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# in mmol/hr now
bc = pd.read_csv('bc.csv')
healthy = pd.read_csv('healthy.csv')
pcos = pd.read_csv('pcos.csv')
dh = pd.read_csv('dh.csv')

days = np.linspace(0, 30, 43200)

# Case 1 Hormones
plt.figure()
plt.plot(days, healthy['LH11'][1:], label='LH')
plt.plot(days, np.maximum(healthy['prog11'][1:] + 4.1, 5), label='Progesterone')
plt.plot(days, healthy['est11'][1:], label='Estrogen')

plt.xlabel("Time (days)")
plt.ylabel(" Hormone Concentration (mmol/L)")
plt.title("Case 1: Hormone Levels Over the Menstrual Cycle")
plt.xlim(0, 30)
plt.ylim(0, 60)
plt.legend(loc='upper left')

# plt.savefig("case1hormones.png")
# plt.show()

# Case 2 Hormones
plt.figure()
plt.plot(days, bc['LH11'][1:], label='LH')
plt.plot(days, np.maximum(healthy['prog11'][1:] + 9.3, 9.8), label='Progesterone')
# plt.plot(days, bc['prog11'][1:] * 0.75 / maxProg , label='Progesterone') # *(10**(-3)) * 314.16 * 10**(6)
plt.plot(days, bc['est11'][1:] * 5e7, label='Estrogen')

plt.xlabel("Time (days)")
plt.ylabel(" Hormone Concentration (mmol/L)")
plt.title("Case 2: Hormone Levels Over the Menstrual Cycle")
plt.xlim(0, 30)
plt.ylim(0, 60)
plt.legend(loc='upper left')

# plt.savefig("case2hormones.png")
# plt.show()

# Case 3 Hormones
plt.figure()
plt.plot(days, pcos['LH11'][1:], label='LH')
plt.plot(days, pcos['prog11'][1:] *(10**(-3)) * 314.16 * 10**(6), label='Progesterone')
plt.plot(days, pcos['est11'][1:], label='Estrogen')

plt.xlabel("Time (days)")
plt.ylabel("Hormone Concentration (mmol/L)")
plt.title("Case 3: Hormone Levels Over the Menstrual Cycle")
plt.xlim(0, 30)
plt.ylim(0, 60)
plt.legend(loc='upper left')

# plt.savefig("case3hormones.png")
# plt.show()

# Allo
plt.figure()
plt.plot(days, 9.573e-4*np.maximum(healthy['prog11'][1:] + 4.1, 5), label='Case 1')
plt.plot(days, 9.573e-4*np.maximum(healthy['prog11'][1:] + 9.3, 9.8), label='Case 2')
plt.plot(days, 9.573e-4*pcos['prog11'][1:] *(10**(-3)) * 314.16 * 10**(6), label='Case 3')
plt.plot(days, 0.025*np.ones(43200), '--', color='gray', label="Threshold")

plt.xlabel("Time (days)")
plt.ylabel("Brain Allopregnanolone Concentration (mmol/L)")
plt.title("Brain Allopregnanolone Levels Over the Menstrual Cycle")
plt.xlim(0, 30)
plt.ylim(0, 0.035)
plt.legend(loc='upper left')

# plt.savefig("allo.png")
# plt.show()


# Insulin
plt.figure()
plt.plot(days, 1.44*(6 + 0.025*np.maximum(healthy['prog11'][1:] + 4.1, 5) + 0.086*healthy['est11'][1:]), label='Case 1')
plt.plot(days, 1.5+1.44*(6 + 0.045*np.maximum(healthy['prog11'][1:] + 9.3, 9.8) + 0.096*bc['est11'][1:]*5e7), label='Case 2')
plt.plot(days, 1.44*(6 + 0.025*pcos['prog11'][1:] *(10**(-3)) * 314.16 * 10**(6) + 0.086*pcos['est11'][1:]), label='Case 3')
plt.plot(days, 15 * np.ones(43200), '--', label="Threshold", color='gray')

plt.xlabel("Time (days)")
plt.ylabel("ROB Insulin Concentration (mIU/L)")
plt.title("ROB Insulin Levels Over the Menstrual Cycle")
plt.xlim(0, 30)
plt.legend(loc='upper left')

plt.savefig("insulin.png")
plt.show()

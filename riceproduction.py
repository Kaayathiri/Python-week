import matplotlib.pyplot as plt
Year=[2010,2011,2012,2013,2014,2015]
rice=[10,20,40,60,70,40]

plt.xlabel("Years")
plt.ylabel("Rice Production")
plt.title("Rice Production over time")
plt.plot(Year,rice)
plt.show()
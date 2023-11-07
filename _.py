import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = np.random.randint(2,20,100)
y = np.random.randint(2,20,100)
df = pd.DataFrame({"x": x, "y": y})

sns.barplot(data = df, x = "x", y = "y")
plt.savefig("barplot.png")
plt.show()
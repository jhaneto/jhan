import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('C:\\Users\\win10\\Desktop\\num.txt', encoding = 'cp860')
unique, counts = np.unique(data, return_counts = True)
print(unique, counts)
plt.hist(data);

num_sixes = (data == 6).sum()
num_total = data.size
num_sixes
num_total

from scipy.stats import binom
n = np.arange(num_total)
prob_n = binom.pmf(n, num_total, 1/6)
plt.plot(n, prob_n, label='Prob num')
plt.axvline(num_total / 6, ls ='--', lw=1, label="Mean num")
plt.axvline(num_sixes, ls=":", color = "#ff7272", label = "Obs num")
plt.xlabel(f"Num sixes rolled out of {num_total} rolls")
plt.ylabel("Probability")
plt.legend();
print(f"Num sixes rolled out of {num_total} rolls")

d = binom(num_total, 1/6)
plt.plot(n, d.sf(n))
plt.axvline(num_sixes, ls="--")
sf = d.sf(num_sixes)
plt.xlabel("Num sixes")
plt.ylabel("SF")
print(f" Only {sf * 100:.1f}% of the time with a fair dice you'd roll thie many or more sixes.")



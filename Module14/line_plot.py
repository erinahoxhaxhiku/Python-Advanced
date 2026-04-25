from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQperCountry.csv')

avg_ig_by_continent = df.groupny('Continent')['Average IQ'].mean()

plt.figure(figsize=(10,6))

avg_ig_by_continent.plot(kind='line',marker = 'o',color='skyblue')


plt.title('Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')

plt.grid(axis='both',linestyle='--', alpha=0.7)

#alpha - dukshmeria sa eshte transparente
plt.show()

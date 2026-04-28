import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

gdp = pd.read_csv("./Clean Data/gdp_per_capita.csv")
health_exp = pd.read_csv("./Clean Data/health_expenditure.csv")
health_spend = pd.read_csv("./Clean Data/health_spending.csv")
doctors = pd.read_csv("./Clean Data/doctors_per_capita.csv")

df = gdp.merge(health_exp, on=["country", "year"], how="inner")
df = df.merge(health_spend, on=["country", "year"], how="inner")
df = df.merge(doctors, on=["country", "year"], how="inner")

df.to_csv("merged_dataset.csv", index=False)


os.makedirs("results/figures", exist_ok=True)

plt.scatter(df["gdp_per_capita"], df["doctors_per_capita"])
plt.xlabel("GDP per Capita")
plt.ylabel("Doctors per Capita")
plt.title("Wealth vs Healthcare Access")
plt.show()

plt.savefig("results/figures/figure1.png", bbox_inches="tight")
plt.show()


z = np.polyfit(df["health_spending"], df["doctors_per_capita"], 1)
p = np.poly1d(z)

plt.scatter(df["health_spending"], df["doctors_per_capita"])
plt.plot(df["health_spending"], p(df["health_spending"]))
plt.xlabel("Health Spending (% of GDP)")
plt.ylabel("Doctors per Capita")
plt.title("Health Investment vs Healthcare Access")
plt.show()

plt.savefig("results/figures/figure2.png", bbox_inches="tight")
plt.show()

plt.scatter(df["gdp_per_capita"], df["health_spending"])
plt.xlabel("GDP per Capita")
plt.ylabel("Health Spending (% of GDP)")
plt.title("Wealth vs Health Investment")
plt.show()

df[["gdp_per_capita", "health_spending"]].corr()

plt.savefig("results/figures/figure3.png", bbox_inches="tight")
plt.show()


df.sort_values(by="doctors_per_capita", ascending=False).head()
df.sort_values(by="gdp_per_capita", ascending=False).head()

import seaborn as sns

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, fmt=".2f")
plt.title("Correlation Matrix of Socioeconomic and Health Indicators")

plt.savefig("results/figures/figure4.png", bbox_inches="tight")
plt.show()

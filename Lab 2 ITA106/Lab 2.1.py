import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv(r'E:\Labs ITA106\Lab 2 ITA106\btcusd_1-min_data.csv')

features = ['Open', 'High', 'Close']

plt.hist(df[features], bins = 20, label = features, edgecolor = 'black', alpha = 0.7)

plt.title('Biểu đồ phân phối của Open, High, Close', fontsize = 14, pad = 15)
plt.xlabel('Giá trị', fontsize=12)
plt.ylabel('Tần suất', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()

plt.savefig('histograms_plot.png', dpi=300)

if len(df) > 50000:
    df_sample = df.sample(n=50000, random_state=42)
else:
    df_sample = df
for feature in features:
    plt.figure(figsize=(10,6))
    sns.kdeplot(df_sample[feature], fill=True, color='skyblue', alpha=0.7)
    plt.title(f'Density Plot (KDE) of {feature} Price', fontsize=14, pad=15)
    plt.xlabel(f'{feature} Price', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f'kde_{feature.lower()}_plot.png', dpi=300)
    
plt.figure(figsize=(10,6))
sns.boxplot(data=df[features], palette='viridis')
plt.title('Boxplot of Open, High and Close Prices')
plt.xlabel('Price Attributes')
plt.ylabel('Price')
plt.grid(axis='y',alpha=0.75)
plt.tight_layout()
plt.savefig('Boxplot of Open, High, Close_plot.png', dpi=300)



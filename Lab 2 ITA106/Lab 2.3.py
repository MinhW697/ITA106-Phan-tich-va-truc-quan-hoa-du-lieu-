import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv(r'E:\Labs ITA106\Lab 2 ITA106\Housing data.csv')
for column in df.columns:
    plt.figure(figsize=(8,6))
    sns.boxplot(y=df[column])
    plt.title(f'Boxplot of {column}')
    plt.ylabel(column)
    plt.grid(axis='y', alpha=0.75)

#2.4:
corr_matrix = df.corr()
print(corr_matrix)

plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Ma trận tương quan giữa các thuộc tính')

import numpy as np
uppert_corr_matrix = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

# Đặt ngưỡng cho tương quan cao
correlation_threshold = 0.7

high_corr_pairs = []

# Duyệt qua ma trận để tìm các cặp có tương quan cao
for column in uppert_corr_matrix.columns:
    for row in uppert_corr_matrix.index:
        if not pd.isna(uppert_corr_matrix.loc[row, column]) and abs(uppert_corr_matrix.loc[row, column]) >= correlation_threshold:
            high_corr_pairs.append((row, column, uppert_corr_matrix.loc[row, column]))

if high_corr_pairs:
    print(f"Các cặp biến có tương quan cao (tuyệt đối >= {correlation_threshold}):")
    for pair in high_corr_pairs:
        print(f"  - {pair[0]} và {pair[1]}: {pair[2]:.2f}")
else:
    print("Không tìm thấy cặp biến nào có tương quan cao dựa trên ngưỡng đã cho.")
import pandas as pd
df = pd.read_csv(r'E:\Lab 1 ITA106\data.csv')
print("---Dữ liệu bị thiếu---")
print(df.isnull().sum())
df_clean = df.copy()
df_clean = df.dropna()
print(f"Kích thước dữ liệu gốc: {df.shape}")
print(f"Kích thước dữ liệu sau khi xóa dòng thiếu: {df_clean.shape}")

from sklearn.preprocessing import MinMaxScaler, StandardScaler
numerical_features = ['Price', 'StockQuantity', 'Rating']

scaler_minmax = MinMaxScaler()
df_normalized = df_clean.copy()
df_normalized[numerical_features] = scaler_minmax.fit_transform(df_clean[numerical_features])

import matplotlib.pyplot as plt 
import seaborn as sns
df_clean['StockQuantity'] = df_clean['StockQuantity'].clip(lower = 0)

q1 = df_clean['Price'].quantile(0.25)
q3 = df_clean['Price'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df_clean['Price'] = df_clean['Price'].clip(lower = lower_bound, upper = upper_bound)

numerical_cols = ['Price', 'StockQuantity', 'Rating']

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(3, 2, figsize=(12, 14))

for i, col in enumerate(numerical_cols):
    # Cột bên trái: Dữ liệu gốc trước khi làm sạch
    sns.boxplot(x=df[col], ax=axes[i, 0], color='#ff7f7f') # Màu đỏ nhạt
    axes[i, 0].set_title(f'TRƯỚC khi làm sạch: {col}', fontsize=12, fontweight='bold')
    axes[i, 0].set_xlabel('')
    
    # Cột bên phải: Dữ liệu sau khi làm sạch toàn diện
    sns.boxplot(x=df_clean[col], ax=axes[i, 1], color='#7fcf7f') # Màu xanh lá nhạt
    axes[i, 1].set_title(f'SAU khi làm sạch: {col}', fontsize=12, fontweight='bold')
    axes[i, 1].set_xlabel('')

# Tối ưu hóa hiển thị và lưu biểu đồ so sánh
plt.tight_layout()
plt.savefig('boxplot_comparison.png', dpi=300)
plt.show()
import pandas as pd 
df = pd.read_csv(r"E:\Lab 1 ITA106\retail_black_friday_sales_100k.csv")
print("---Hiển thị 10 dòng đầu tiên---")
print(df.head(10))
print("---Số lượng bản ghi và thuộc tính---")
print(df.shape)
print("---Kiểm tra dữ liệu từng cột---")
print(df.info())

numerical_cols = ["original_price", "discount_pct", "final_price", "quantity", "purchase_amount"]
sum_stats = df[numerical_cols].describe()
basic_stats = sum_stats.loc[['mean', 'min', 'max', 'std']]
print("---Các thống kê cơ bản---")
print(basic_stats)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style = "whitegrid")
fig1, axes1 = plt.subplots(3, 2, figsize=(14, 18))
axes1 = axes1.flatten()

for i, col in enumerate(numerical_cols):
    sns.histplot(df[col], bins=30, kde=True, ax=axes1[i], color='skyblue')
    axes1[i].set_title(f'Biểu đồ Histogram {col}', fontsize=14)
    axes1[i].set_xlabel(col, fontsize=12)
    axes1[i].set_ylabel('Số lượng (Count)', fontsize=12)

axes1[-1].axis('off') # Tắt ô trống cuối cùng
fig1.tight_layout()   # SỬA: Thêm dấu () để căn chỉnh khoảng cách chữ
fig1.savefig('numerical_histograms.png', bbox_inches='tight')

# ===========================================================
# PHẦN 2: KHỞI TẠO VÀ DỰNG BIỂU ĐỒ BAR CHART (BIẾN PHÂN LOẠI)
# ===========================================================
fig2, axes2 = plt.subplots(3, 2, figsize=(14, 18))
axes2 = axes2.flatten()

categorical_cols = ['age_group', 'gender', 'city', 'customer_segment', 'product_category', 'payment_method']

for i, col in enumerate(categorical_cols):
    data = df[col].value_counts().sort_values(ascending=False)

    # SỬA: Bổ sung hue và legend=False để tương thích hoàn toàn với Seaborn mới
    sns.barplot(x=data.index, y=data.values, ax=axes2[i], palette='viridis', hue=data.index, legend=False)

    # SỬA: Thay "_" bằng khoảng trắng " " để chữ đẹp hơn (Ví dụ: "Age Group" thay vì "Agegroup")
    axes2[i].set_title(f'Phân phối của {col.replace("_"," ").title()}', fontsize=14, fontweight='bold')
    axes2[i].set_xlabel('')
    axes2[i].set_ylabel('Số lượng (Count)', fontsize=12)

    for tick in axes2[i].get_xticklabels():
        tick.set_rotation(45)
        tick.set_horizontalalignment('right')

fig2.tight_layout()
fig2.savefig('categorical_attributes_grid.png', dpi=300)

# ===========================================================
# PHẦN 3: HIỂN THỊ CẢ 2 LÊN MÀN HÌNH CÙNG LÚC
# ===========================================================
# Gọi lệnh này ở cuối cùng giúp hiển thị cả 2 cửa sổ đồ thị cùng lúc mà không lo nghẽn lệnh
plt.show()
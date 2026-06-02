import pandas as pd
df = pd.read_csv(r'E:\Labs ITA106\ASM ITA106\learnx_user_behavior_dataset_10M.csv')
print("===Giới thiệu dữ liệu===")
print(df.head())
print("===Số lượng bản ghi===")
print(df.shape)
print("===Các thuộc tính===")
print(df.info())
print("===Kiểm tra giá trị thiếu===")
print(df.isnull().sum())
print("===Số lượng bản ghi trùng lặp===")
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(f"Số lượng bản ghi sau khi xóa trùng lặp: {len(df)}" )
print("===Thống kê để xem dữ liệu bất thường===")
print(df.describe())
numerical_cols = df.select_dtypes(include=['number']).columns

print("Kiểm tra ngoại lệ (Outliers) cho các cột số:")
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

    if not outliers.empty:
        print(f"\nCột '{col}' có {len(outliers)} ngoại lệ.")
        print("Các giá trị ngoại lệ:")
        print(outliers[[col]].head())
    else:
        print(f"\nCột '{col}' không có ngoại lệ đáng kể theo phương pháp IQR.")


categorical_cols = df.select_dtypes(include=['object', 'category', 'str']).columns

print("Kiểm tra giá trị bất thường cho các cột phân loại:")
for col in categorical_cols:
    print(f"\nCột '{col}':")
    value_counts = df[col].value_counts()
    print(value_counts)
    
    rare_categories = value_counts[value_counts / len(df) < 0.01]
    if not rare_categories.empty:
       print("  Các giá trị hiếm/bất thường:")
    print(rare_categories)




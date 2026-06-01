import pandas as pd
df = pd.read_csv(r'D:\ASM ITA106\learnx_user_behavior_dataset_10M.csv')
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

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

#Phân phối thời gian học trung bình
plt.figure(figsize=(10,6))
sns.histplot(df['avg_session_minutes'], bins=30, kde=True, color='skyblue')
plt.title('Phân phối thời gian trung bình mỗi phiên (phút)')
plt.xlabel('Thời gian học trung bình mỗi phiên (phút)')
plt.ylabel('Tần suất')

#Phân phối số lần truy cập mỗi tuần
plt.figure(figsize=(10,6))
sns.countplot(x='sessions_per_week', data = df, palette='viridis')
plt.title('Phân phối số lần truy cập mỗi tuần')
plt.xlabel('Số lần truy cập mỗi tuần')
plt.ylabel('Số lượng người dùng')

#Phân phối mức độ hoàn thành khóa học
plt.figure(figsize=(10,6))
sns.histplot(df['completion_rate'], bins=30, kde=True, color='lightcoral')
plt.title('Phân phối tỉ lệ hoàn thành khóa học')
plt.xlabel("Tỷ lệ hoàn thành khóa học")
plt.ylabel("Tần suất")

#Xu hướng học theo thời gian
from datetime import datetime, timedelta

reference_date = datetime(2024, 1, 1)

df["signup_date"] = df["signup_days_ago"].apply(lambda x:reference_date - timedelta(days=x))
df["signup_month"] = df["signup_date"].dt.to_period('M')

signups_by_month = df.groupby("signup_month").size().reset_index(name="num_signups")

plt.figure(figsize=(12,6))
sns.lineplot(x="signup_month", y = "num_signups", data=signups_by_month, marker = 'o', color='green')
plt.title("Xu hướng đăng kí người dùng theo tháng")
plt.xlabel("Tháng đăng kí")
plt.ylabel("Số lượng đăng kí mới")
plt.xticks(rotations=45)
plt.tight_layout()
plt.show()

#Người dùng học cực kì nhiều
df['total_study_minutes'] = df['sessions_per_week'] * df['avg_session_minutes']

# Xác định ngưỡng cho người học cực kỳ nhiều (ví dụ: top 1%)
upper_bound_study = df['total_study_minutes'].quantile(0.99)

excessive_learners = df[df['total_study_minutes'] >= upper_bound_study]

print(f"Số lượng người dùng học cực kỳ nhiều (top 1% total_study_minutes): {len(excessive_learners)}")
print(f"Ngưỡng total_study_minutes để được coi là cực kỳ nhiều: {upper_bound_study:.2f} phút/tuần")
print("\nThông tin về một số người dùng học cực kỳ nhiều:")
print(excessive_learners.head())

#Người dùng đăng kí nhiều khóa nhưng không học
# Xác định ngưỡng cho 'nhiều khóa học đăng ký' (ví dụ: trên quý vị thứ 75 hoặc top 25%)
upper_bound_courses_enrolled = df['courses_enrolled'].quantile(0.75)

# Xác định ngưỡng cho 'không học' (ví dụ: completion_rate dưới quý vị thứ 25)
lower_bound_completion_rate = df['completion_rate'].quantile(0.25)

# Hoặc, thời gian học rất thấp
lower_bound_total_study_minutes = df['total_study_minutes'].quantile(0.25)

underperforming_learners = df[
    (df['courses_enrolled'] > upper_bound_courses_enrolled) &
    (df['completion_rate'] < lower_bound_completion_rate) & 
    (df['total_study_minutes'] < lower_bound_total_study_minutes)
]

print(f"Số lượng người dùng đăng ký nhiều khóa nhưng không học: {len(underperforming_learners)}")
print(f"Ngưỡng courses_enrolled (> {upper_bound_courses_enrolled:.0f})")
print(f"Ngưỡng completion_rate (< {lower_bound_completion_rate:.2f})")
print(f"Ngưỡng total_study_minutes (< {lower_bound_total_study_minutes:.2f})")
print("\nThông tin về một số người dùng đăng ký nhiều khóa nhưng không học:")
print(underperforming_learners.head())

#Người dùng chi tiêu bất thường
# Phát hiện chi tiêu rất cao bằng IQR (Interquartile Range) hoặc percentile
Q1 = df['total_spent_usd'].quantile(0.25)
Q3 = df['total_spent_usd'].quantile(0.75)
IQR = Q3 - Q1

upper_bound_spent = Q3 + 1.5 * IQR

# Nếu Q1 và Q3 đều là 0 (hoặc rất gần 0) thì IQR cũng sẽ rất nhỏ, ngưỡng sẽ không hiệu quả.
# Trong trường hợp này, ta sẽ dùng percentile nếu hầu hết giá trị là 0.
if upper_bound_spent == Q3 or IQR == 0: # Check if IQR method is not effective due to many zeros
    upper_bound_spent = df['total_spent_usd'].quantile(0.99)

excessive_spenders = df[df['total_spent_usd'] > upper_bound_spent]

# Phát hiện trường hợp đặc biệt: premium_purchased = 1 nhưng total_spent_usd = 0
zero_spend_premium = df[(df['premium_purchased'] == 1) & (df['total_spent_usd'] == 0)]

print(f"Số lượng người dùng chi tiêu cực kỳ cao (> {upper_bound_spent:.2f} USD): {len(excessive_spenders)}")
print("\nThông tin về một số người dùng chi tiêu cực kỳ cao:")
print(excessive_spenders.head())

print(f"\nSố lượng người dùng mua premium nhưng chi tiêu 0 USD: {len(zero_spend_premium)}")
print("\nThông tin về một số người dùng mua premium nhưng chi tiêu 0 USD:")
print(zero_spend_premium.head())
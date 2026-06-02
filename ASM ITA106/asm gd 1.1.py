import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# 1. Đọc dữ liệu
df = pd.read_csv(r'E:\Labs ITA106\ASM ITA106\learnx_user_behavior_dataset_10M.csv')

sns.set_style('whitegrid')

# --- Biểu đồ 1: Phân phối thời gian học trung bình ---
plt.figure(figsize=(10,6))
sns.histplot(df['avg_session_minutes'], bins=30, kde=True, color='skyblue')
plt.title('Phân phối thời gian trung bình mỗi phiên (phút)')
plt.xlabel('Thời gian học trung bình mỗi phiên (phút)')
plt.ylabel('Tần suất')
plt.tight_layout()
# THÊM CODE LƯU ẢNH: bbox_inches='tight' giúp ảnh không bị mất chữ rìa ngoài
plt.savefig('phan_phoi_thoi_gian_hoc.png', dpi=300, bbox_inches='tight') 

# --- Biểu đồ 2: Phân phối số lần truy cập mỗi tuần ---
plt.figure(figsize=(10,6))
sns.countplot(x='sessions_per_week', data=df, hue='sessions_per_week', palette='viridis', legend=False)
plt.title('Phân phối số lần truy cập mỗi tuần')
plt.xlabel('Số lần truy cập mỗi tuần')
plt.ylabel('Số lượng người dùng')
plt.tight_layout()
# THÊM CODE LƯU ẢNH:
plt.savefig('phan_phoi_truy_cap_tuan.png', dpi=300, bbox_inches='tight')

# --- Biểu đồ 3: Phân phối mức độ hoàn thành khóa học ---
plt.figure(figsize=(10,6))
sns.histplot(df['completion_rate'], bins=30, kde=True, color='lightcoral')
plt.title('Phân phối tỉ lệ hoàn thành khóa học')
plt.xlabel("Tỷ lệ hoàn thành khóa học")
plt.ylabel("Tần suất")
plt.tight_layout()
# THÊM CODE LƯU ẢNH:
plt.savefig('phan_phoi_ti_le_hoan_thanh.png', dpi=300, bbox_inches='tight')

# --- Biểu đồ 4: Xu hướng học theo thời gian ---
reference_date = datetime(2024, 1, 1)

df["signup_date"] = df["signup_days_ago"].apply(lambda x: reference_date - timedelta(days=x))
df["signup_month"] = df["signup_date"].dt.to_period('M')

signups_by_month = df.groupby("signup_month").size().reset_index(name="num_signups")
signups_by_month["signup_month"] = signups_by_month["signup_month"].astype(str)

plt.figure(figsize=(12,6))
sns.lineplot(x="signup_month", y="num_signups", data=signups_by_month, marker='o', color='green')
plt.title("Xu hướng đăng kí người dùng theo tháng")
plt.xlabel("Tháng đăng kí")
plt.ylabel("Số lượng đăng kí mới")
plt.xticks(rotation=45) 
plt.tight_layout()
# THÊM CODE LƯU ẢNH:
plt.savefig('xu_huong_dang_ky_thang.png', dpi=300, bbox_inches='tight')

# Hiển thị tất cả biểu đồ lên màn hình (nếu bạn chỉ muốn lưu file mà không muốn hiện pop-up ảnh thì có thể xóa dòng plt.show() này đi)
plt.show()
import matplotlib.pyplot as plt
import matplotlib

# 配置Matplotlib以使用中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置图像的dpi为300
plt.figure(dpi=300)

# 准备数据
sizes = [24.7, 15.2, 8.3, 4.5, 3.9, 3.8, 3.2, 2.8]
labels = ['英语', '汉语', '西班牙语', '德语', '日语', '法语', '意大利语', '俄语']

# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('各语言对应GDP占比')
# 确保饼图是圆的而不是椭圆形
plt.axis('equal')

# 显示图表
plt.show()

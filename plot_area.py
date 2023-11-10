import matplotlib.pyplot as plt
import matplotlib

# 配置Matplotlib以使用中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置图像的dpi为300
plt.figure(dpi=300)

# 准备数据
sizes = [13.4, 23.7, 24.0, 44.4, 4.4, 16.5, 19.5, 14.4]
labels = ['汉语', '俄语', '西班牙语', '英语', '印地语', '法语', '阿拉伯语', '葡萄牙语']


plt.title('各语言对应面积占比')
# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 确保饼图是圆的而不是椭圆形
plt.axis('equal')

# 显示图表
plt.show()

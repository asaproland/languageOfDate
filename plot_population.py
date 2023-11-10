import matplotlib.pyplot as plt
import matplotlib

# 配置Matplotlib以使用中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用内置的黑体
matplotlib.rcParams['axes.unicode_minus'] = False  # 正确显示负号


# 设置图像的dpi为300
plt.figure(dpi=300)
# 准备数据
sizes = [16.2, 16.2, 7.1, 6.7, 4.2, 2.9, 2.0, 2.0, 1.7]
labels = ['汉语', '英语', '西班牙语', '印地语', '阿拉伯语', '葡萄牙语', '俄语', '孟加拉语', '日语']


plt.title('各语言对应使用人口占比')
# 绘制饼图
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# 确保饼图是圆的而不是椭圆形
plt.axis('equal')

# 显示图表
plt.show()

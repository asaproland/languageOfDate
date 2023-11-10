import matplotlib.pyplot as plt
import matplotlib

# 配置Matplotlib以使用中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 准备数据
languages = ['英语', '汉语', '西班牙语', '德语', '日语', '法语', '意大利语', '俄语']
population_ratios = [16.2, 16.2, 7.1, 6.7, 4.2, 2.9, 2.0, 2.0]
area_ratios = [44.4, 23.7, 24.0, 16.5, 4.4, 16.5, 14.4, 23.7]
gdp_ratios = [24.8, 16.5, 7.9, 3.8, 6.1, 3.5, 2.2, 2.7]

colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'grey']

# 绘制气泡图
plt.figure(figsize=(10, 8))
for i in range(len(languages)):
    plt.scatter(population_ratios[i], area_ratios[i], s=gdp_ratios[i] * 20,
                c=colors[i], alpha=0.7, label=languages[i])
    # 第一段文本靠上一点
    plt.text(population_ratios[i], area_ratios[i] + 1, f'{gdp_ratios[i]}%', ha='center', va='center', fontsize=15)

    # 第二段文本靠下一点
    plt.text(population_ratios[i], area_ratios[i] - 1, f'{languages[i]}', ha='center', va='center', fontsize=15)

# 添加标签
plt.xlabel('人口占比 (%)')
plt.ylabel('面积占比 (%)')
plt.title('各语言对应人口占比、面积占比和GDP占比')
plt.legend()

# 显示图表
plt.show()

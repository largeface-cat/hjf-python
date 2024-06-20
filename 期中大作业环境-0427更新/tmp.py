import numpy as np
import matplotlib.pyplot as plt

# 绘制雷达图
def draw_radar(data, labels, title, r=1):
    # 数据个数
    n = len(data)
    # 化为360度制
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    # 使雷达图封闭起来
    data = np.concatenate((data, [data[0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 绘图
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True) # polar参数！！
    ax.plot(angles, data, 'bo-', linewidth=2) # 画线
    ax.fill(angles, data, facecolor='r', alpha=0.25) # 填充
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.title(title)
    ax.set_rlim(0, r)
    ax.grid(True)
    plt.show()

draw_radar([0.5, 0.9, 0.7, 0.8, 0.1,0.4,0.5], ['a', 'b', 'c', 'd', 'e','f','f'], 'test')
import numpy as np

from matplotlib import pyplot as plt

from scipy.interpolate import CubicSpline

x_discrete = np.array([])
y_discrete = np.array([])
print("输入数据点数量.\n")
cnt = int(input())
print("依次输入各点x坐标和y坐标 (输入一个坐标按一次回车)")
while(cnt > 0):
    cnt -= 1
    x = float(input())
    y = float(input())
    x_discrete = np.append(x_discrete, x)
    y_discrete = np.append(y_discrete, y)
dis= np.vstack((x_discrete,y_discrete))
sorted_index = np.argsort(dis[0])
dis = dis[:,sorted_index]
x_discrete = dis[0]
y_discrete = dis[1]
cs = CubicSpline(x_discrete, y_discrete,bc_type="natural")
x_smooth = np.linspace(x_discrete.min(),x_discrete.max(),1000)
y_smooth = cs(x_smooth)

plt.title("R-I curve")
plt.ylabel("R 欧姆")
plt.xlabel("I 毫安")
plt.plot(x_smooth,y_smooth)
plt.scatter(x_discrete,y_discrete,color="red",s=80,label="原始数据点",marker="o")
plt.show()

while(True):
    print("请输入待查询的x\n")
    x_query = float(input())
    y_ans = cs(x_query)
    print(y_ans)
    print("\n")


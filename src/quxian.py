import tkinter as tk

# 创建窗口
window = tk.Tk()

# 创建画布
canvas = tk.Canvas(window, width=400, height=300)
canvas.pack()


# 绘制曲线图
def draw_curve():
    # 清空画布
    canvas.delete("all")

    # 定义数据
    data = [(0, 100), (50, 200), (100, 150), (150, 250), (200, 200), (250, 300)]

    # 遍历数据并绘制曲线
    for i in range(len(data) - 1):
        x1, y1 = data[i]
        x2, y2 = data[i + 1]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)


# 创建按钮
button = tk.Button(window, text="绘制曲线图", command=draw_curve)
button.pack()
# 运行窗口
window.mainloop()

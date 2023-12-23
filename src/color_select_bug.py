import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Color Labels")

# 颜色字典，包含六种基本颜色及其RGB值
colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Cyan": "#00FFFF",
    "Magenta": "#FF00FF"
}

selected_color = tk.StringVar()  # 存储选择的颜色


def select_color():
    color = selected_color.get()
    if color:
        print("Selected color:", color)
    else:
        print("No color selected.")


# 创建颜色标签和单选框
i = 0
for color, hex_code in colors.items():
    radiobutton = tk.Radiobutton(root, variable=selected_color, value=hex_code, command=select_color)
    radiobutton.place(anchor=tk.W, x=239, y=(148 + i * 100), width=80, height=30)
    label = tk.Label(root, text=color, bg=hex_code, padx=20, pady=10, )
    label.bind("<Button-1>", lambda event, color=hex_code: [selected_color.set(color), select_color()])
    label.place(x=339, y=135 + i * 100, width=80, height=30)
    i += 1

root.mainloop()

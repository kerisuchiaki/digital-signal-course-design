import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
color = tk.StringVar()
color.set('red')

colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Cyan": "#00FFFF",
    "Magenta": "#FF00FF"
}


def select_color(evt=None):
    if color:
        print("Selected color:", color.get())
    else:
        print("No color selected.")


# 创建颜色标签和单选框
i = 0
for color_text, hex_code in colors.items():
    radiobutton = tk.Radiobutton(root, bg=hex_code, text=color_text,
                                 variable=color, value=hex_code,command=select_color)
    # radiobutton.bind("<Button-1>", select_color) #奇怪的BUG，会出现一开始就调用一次select_color并且之后的单击单选框时都只会输出上次单击的单选框的值
    radiobutton.place(x=339, y=135 + i * 100, width=80, height=30)
    i += 1

root.mainloop()

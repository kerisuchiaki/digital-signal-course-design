import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
color = None

colors = {
    "Red": "#FF0000",
    "Green": "#00FF00",
    "Blue": "#0000FF",
    "Yellow": "#FFFF00",
    "Cyan": "#00FFFF",
    "Magenta": "#FF00FF"
}


def select_color(evt=None):
    selected_color = color
    if selected_color:
        print("Selected color:", selected_color)
    else:
        print("No color selected.")


# 创建颜色标签和单选框
i = 0
for color_text, hex_code in colors.items():
    radiobutton = tk.Radiobutton(root, bg=hex_code, text=color_text,
                                 variable=color, value=hex_code)
    radiobutton.bind("<Button-1>", select_color)
    radiobutton.place(x=339, y=135 + i * 100, width=80, height=30)
    i += 1

root.mainloop()
import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
color = tk.StringVar()
color.set('red')


def select_color(evt=None):
    selected_color = color.get()
    if selected_color:
        print("Selected color:", selected_color)
    else:
        print("No color selected.")


b1 = tk.Radiobutton(root, bg='red', text='红色',
                    variable=color, value='red', command=select_color)
b1.pack()
b2 = tk.Radiobutton(root, text='蓝色', bg='blue',
                    variable=color, value='blue', command=select_color)
b2.pack()
b3 = tk.Radiobutton(root, text='绿色', bg='green',
                    variable=color, value='green', command=select_color)
b3.pack()
root.mainloop()

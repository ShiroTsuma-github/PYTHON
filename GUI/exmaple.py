from tkinter import Tk, StringVar
from tkinter import ttk

col_weights = [1, 1, 1, 1]
row_weights = [1, 1, 1, 1]

root = Tk()
root.title('Test')
root.geometry('500x500')
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=('n', 'w', 'e', 's'))
for pos, crw in enumerate(zip(col_weights, row_weights)):
    cw = crw[0]
    rw = crw[1]
    root.columnconfigure(pos, weight=cw)
    root.rowconfigure(pos, weight=rw)

o1 = ttk.Label(root, text='Text 1', borderwidth=5, relief='solid', anchor='center')
o2 = ttk.Label(root, text='Text 2', borderwidth=5, relief='solid', anchor='center')
o3 = ttk.Label(root, text='Text 3', borderwidth=5, relief='solid', anchor='center')
o4 = ttk.Label(root, text='Text 4', borderwidth=5, relief='solid', anchor='center')
o5 = ttk.Label(root, text='Text 5', borderwidth=5, relief='solid', anchor='center')
o6 = ttk.Label(root, text='Text 6', borderwidth=5, relief='solid', anchor='center')
o7 = ttk.Label(root, text='Text 7', borderwidth=5, relief='solid', anchor='center')


o1.grid(column=0, row=0, sticky="nsew")
o2.grid(column=1, columnspan=2, rowspan=2, row=0, sticky="nsew")
o3.grid(column=3, row=0, sticky="nsew")

o4.grid(column=0, row=1, sticky="nsew")
o5.grid(column=1, row=1, sticky="nsew")
o6.grid(column=3, row=1, sticky="nsew")
o7.grid(column=3, row=1, sticky="nsew")
root.mainloop()

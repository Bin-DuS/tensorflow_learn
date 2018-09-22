import tkinter as tk
root = tk.Tk()
label = tk.Label(root,text = "hello world!")
label.pack()
btn = tk.Button(root,text = "OK")
btn.pack();
entry = tk.Entry(root)
entry.pack()
root.mainloop()
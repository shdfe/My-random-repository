import tkinter as tk

def onclick():
    exec(open('tweetbot.py').read())

root = tk.Tk()
root.title = ('TWEETAJOKE')
w = tk.Label(root, text='TWEETAJOKE')
btn = tk.Button(root, text='Click Me!', command=onclick)
btn.place(anchor = 'center')
w.pack()
btn.pack()

root.mainloop()




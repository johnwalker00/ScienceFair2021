import tkinter as tk

def init():
    window = tk.Tk()
    window.resizable(False, False)
    window.title('Title')

    txt_lbl = tk.Label(master=window, height=5, text='Common Password Alg: \nRandom Alg:', justify=tk.LEFT)
    txt_lbl.grid(row=0, column=0)

    txt_ent = tk.Entry(master=window)
    txt_ent.grid(row=1, column=0, padx=20, pady=20)

    btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing')
    btn.grid(row=1, column=1, padx=20, pady=20)

    window.mainloop()
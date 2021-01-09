from Gorithms import *
import tkinter as tk

last_common_result = ''
last_random_result = ''

def handle_click():
    if password_ent.get() == '':
        return

    password_ent.config(state=tk.DISABLED)
    btn.config(state=tk.DISABLED)

    last_common_result = test_commons(password_ent.get())

    results_lbl.config(text=f'Common Password Alg: {last_common_result}\nRandom Alg: {last_random_result}')
    password_ent.config(state=tk.NORMAL)
    btn.config(state=tk.NORMAL)


window = tk.Tk()
window.resizable(False, False)
window.title('Password Guesser')

results_lbl = tk.Label(master=window, height=5, text='', justify=tk.LEFT)
results_lbl.grid(row=0)

password_ent = tk.Entry(master=window)
password_ent.grid(row=1, column=0, padx=20, pady=10)

timeout_ent = tk.Entry(master=window)
timeout_ent.grid(row=2, column=0, padx=20, pady=10)

btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing', command=handle_click)
btn.grid(row=1, column=1, padx=20, pady=20)

window.mainloop()
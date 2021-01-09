from Gorithms import *
import tkinter as tk

last_common_result = ''
last_random_result = ''



def handle_click():
    if password_ent.get() == '':
        return
    if timeout_ent.get() == '' or int(timeout_ent.get()) == None:
        empty_lbl.config(text='Please enter a valid timeout value')
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
results_lbl.grid(row=0, column=1)

password_lbl = tk.Label(master=window, text='Password:')
password_lbl.grid(row=1, column=0)

password_ent = tk.Entry(master=window, width=50)
password_ent.grid(row=1, column=1)

timeout_lbl = tk.Label(master=window, text='Timeout (s): ')
timeout_lbl.grid(row=2, column=0)

timeout_ent = tk.Entry(master=window, width=50)
timeout_ent.grid(row=2, column=1)

btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing', command=handle_click)
btn.grid(row=1, column=2, padx=20)

empty_lbl = tk.Label(master=window, text='Please enter a password and timeout value', width=50)
empty_lbl.grid(row=3, column=1, pady=10)

window.mainloop()
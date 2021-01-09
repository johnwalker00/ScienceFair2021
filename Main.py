from Gorithms import *
import tkinter as tk

last_common_result = ''
last_dict_result = ''
last_random_result = ''

def handle_click():
    if password_ent.get() == '':
        return
    if timeout_ent.get() == '' or int(timeout_ent.get()) == None:
        status_lbl.config(text='Please enter a valid timeout value')
        return

    password_ent.config(state=tk.DISABLED)
    btn.config(state=tk.DISABLED)
    status_lbl.config(text='Working...')

    last_common_result = test_commons(password_ent.get())
    last_dict_result = test_words(password_ent.get())

    status_lbl.config(text='Please enter a password and timeout value')
    results_lbl.config(text=f'Common Password Alg {last_common_result}\nDictionary Search Alg {last_dict_result}\nRandom Alg {last_random_result}')
    password_ent.config(state=tk.NORMAL)
    btn.config(state=tk.NORMAL)


window = tk.Tk()
window.resizable(False, False)
window.title('Password Guesser')

results_lbl = tk.Label(master=window, height=5, text=f'Common Password Alg {last_common_result}\nDictionary Search Alg {last_dict_result}\nRandom Alg {last_random_result}', justify=tk.LEFT)
results_lbl.grid(row=0, column=1, pady=10)

password_lbl = tk.Label(master=window, text='Password: ', justify=tk.LEFT)
password_lbl.grid(row=1, column=0, pady=10)

password_ent = tk.Entry(master=window, width=50)
password_ent.grid(row=1, column=1, pady=10)

timeout_lbl = tk.Label(master=window, text='Timeout (s): ', justify=tk.LEFT)
timeout_lbl.grid(row=2, column=0, pady=10)

timeout_ent = tk.Entry(master=window, width=50)
timeout_ent.grid(row=2, column=1, pady=10)

btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing', command=handle_click)
btn.grid(row=1, column=2, padx=10)

status_lbl = tk.Label(master=window, text='Please enter a password and timeout value', width=70)
status_lbl.grid(row=3, column=1, pady=10)

empty_frm = tk.Frame(master=window, height=20, width=20)
empty_frm.grid(row=4, column=1, pady=10)

window.mainloop()
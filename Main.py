from os import stat
from Gorithms import *
import winsound
import tkinter as tk

status_lbl_text = 'Please enter a password and timeout value'

#Handle button click
def handle_click():
    #Init vars for changing labels
    common_result = 'was not run'
    dict_result = 'was not run'
    dict_num_result = 'was not run'
    random_result = 'was not run'

    #Ensure the user gave a password
    if password_ent.get() == '':
        return
    #Ensure the timeout value is valid
    if timeout_ent.get() == '' or int(timeout_ent.get()) == None:
        status_lbl_text = 'Please enter a valid timeout value'
        status_lbl.config(text=status_lbl_text)
        return

    #Disable input
    password_ent.config(state=tk.DISABLED)
    timeout_ent.config(state=tk.DISABLED)
    cps_cbx.config(state=tk.DISABLED)
    ds_cbx.config(state=tk.DISABLED)
    dns_cbx.config(state=tk.DISABLED)
    rnd_cbx.config(state=tk.DISABLED)
    btn.config(state=tk.DISABLED)

    #Flavor
    status_lbl_text='Calculating...'
    status_lbl.config(text=status_lbl_text)

    #Run our algs
    if run_cps.get():
        common_result = test_file(password_ent.get(), 'data/commonwords.txt')
    if run_ds.get():
        dict_result = test_file(password_ent.get(), 'data/dictionary.txt')
    if run_dns.get():
        dict_num_result = test_word_num(password_ent.get(), 'data/dictionary.txt', int(timeout_ent.get()))
    if run_rnd.get():
        random_result = random_test(password_ent.get(), int(timeout_ent.get()))
    
    #Play sound
    winsound.Beep(440, 100)

    #Display results
    status_lbl_text = 'Please enter a password and timeout value'
    status_lbl.config(text=status_lbl_text)
    cps_results_lbl.config(text=f'Common Password Search {common_result}')
    ds_results_lbl.config(text=f'Dictionary Search {dict_result}')
    dns_results_lbl.config(text=f'Dictionary and Number Search {dict_num_result}')
    rnd_results_lbl.config(text=f'Random Search {random_result}')

    #Enable input
    password_ent.config(state=tk.NORMAL)
    timeout_ent.config(state=tk.NORMAL)
    btn.config(state=tk.NORMAL)
    cps_cbx.config(state=tk.NORMAL)
    ds_cbx.config(state=tk.NORMAL)
    dns_cbx.config(state=tk.NORMAL)
    rnd_cbx.config(state=tk.NORMAL)

#Init window
window = tk.Tk()
window.resizable(False, False)
window.title('Password Guesser')

run_cps = tk.BooleanVar()
run_ds = tk.BooleanVar()
run_dns = tk.BooleanVar()
run_rnd = tk.BooleanVar()

#Checkboxes
cps_cbx = tk.Checkbutton(master=window, variable=run_cps, onvalue=True, offvalue=False)
cps_cbx.grid(row=1, column=0, sticky='e')

ds_cbx = tk.Checkbutton(master=window, variable=run_ds, onvalue=True, offvalue=False)
ds_cbx.grid(row=2, column=0, sticky='e')

dns_cbx = tk.Checkbutton(master=window, variable=run_dns, onvalue=True, offvalue=False)
dns_cbx.grid(row=3, column=0, sticky='e')

rnd_cbx = tk.Checkbutton(master=window, variable=run_rnd, onvalue=True, offvalue=False)
rnd_cbx.grid(row=4, column=0, sticky='e')

#Results labels
cps_results_lbl = tk.Label(master=window, height=1, text=f'Common Password Search', justify=tk.LEFT)
cps_results_lbl.grid(row=1, column=1, sticky='w')

ds_results_lbl = tk.Label(master=window, height=1, text=f'Dictionary Search', justify=tk.LEFT)
ds_results_lbl.grid(row=2, column=1, sticky='w')

dns_results_lbl = tk.Label(master=window, height=1, text=f'Dictionary and Number Search', justify=tk.LEFT)
dns_results_lbl.grid(row=3, column=1, sticky='w')

rnd_results_lbl = tk.Label(master=window, height=1, text=f'Random Search', justify=tk.LEFT)
rnd_results_lbl.grid(row=4, column=1, sticky='w')

#Password prompt
password_lbl = tk.Label(master=window, text='Password: ', justify=tk.LEFT)
password_lbl.grid(row=5, column=0, pady=10, sticky='e')

#Password entry box
password_ent = tk.Entry(master=window, width=50)
password_ent.grid(row=5, column=1, pady=10, sticky='w')

#Timeout prompt
timeout_lbl = tk.Label(master=window, text='Timeout (seconds): ', justify=tk.LEFT)
timeout_lbl.grid(row=6, column=0, pady=10, sticky='e')

#Timeout entry box
timeout_ent = tk.Entry(master=window, width=50)
timeout_ent.grid(row=6, column=1, pady=10, sticky='w')

#Start button
btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing', command=handle_click)
btn.grid(row=5, column=2, padx=10)

#Status label
status_lbl = tk.Label(master=window, text=status_lbl_text, width=70)
status_lbl.grid(row=7, column=1, pady=10)

#Empty, for looks only
empty_frm = tk.Frame(master=window, height=20, width=20)
empty_frm.grid(row=8, column=1, pady=10)

#Start
window.mainloop()

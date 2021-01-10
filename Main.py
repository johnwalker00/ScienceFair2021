from Gorithms import *
import tkinter as tk

#Init vars for changing labels
common_result = ''
dict_result = ''
dict_num_result = ''
random_result = ''

#Handle button click
def handle_click():
    #Ensure the user gave a password
    if password_ent.get() == '':
        return
    #Ensure the timeout value is valid
    if timeout_ent.get() == '' or int(timeout_ent.get()) == None:
        status_lbl.config(text='Please enter a valid timeout value')
        return

    #Disable input
    password_ent.config(state=tk.DISABLED)
    timeout_ent.config(state=tk.DISABLED)
    btn.config(state=tk.DISABLED)

    #Flavor
    status_lbl.config(text='Calculating...')

    #Run our algs
    common_result = test_file(password_ent.get(), 'commonwords.txt')
    dict_result = test_file(password_ent.get(), 'dictionary.txt')
    dict_num_result = test_word_num(password_ent.get(), 'dictionary.txt', int(timeout_ent.get()))

    #Display results
    status_lbl.config(text='Please enter a password and timeout value')
    results_lbl.config(text=f'Common Password Search {common_result}\nDictionary Search {dict_result}\nDictionary and Number Search {dict_num_result}\nRandom Alg {random_result}')
    
    #Enable input
    password_ent.config(state=tk.NORMAL)
    timeout_ent.config(state=tk.NORMAL)
    btn.config(state=tk.NORMAL)

#Init window
window = tk.Tk()
window.resizable(False, False)
window.title('Password Guesser')

#Results label
results_lbl = tk.Label(master=window, height=5, text=f'Common Password Search {common_result}\nDictionary Search {dict_result}\nDictionary and Number Search {dict_num_result}\nRandom Alg {random_result}', justify=tk.LEFT)
results_lbl.grid(row=0, column=1, pady=10)

#Password prompt
password_lbl = tk.Label(master=window, text='Password: ', justify=tk.LEFT)
password_lbl.grid(row=1, column=0, pady=10)

#Password entry box
password_ent = tk.Entry(master=window, width=50)
password_ent.grid(row=1, column=1, pady=10)

#Timeout prompt
timeout_lbl = tk.Label(master=window, text='Timeout (seconds): ', justify=tk.LEFT)
timeout_lbl.grid(row=2, column=0, pady=10)

#Timeout entry box
timeout_ent = tk.Entry(master=window, width=50)
timeout_ent.grid(row=2, column=1, pady=10)

#Start button
btn = tk.Button(master=window, relief=tk.RAISED, text='Start Guessing', command=handle_click)
btn.grid(row=1, column=2, padx=10)

#Status label
status_lbl = tk.Label(master=window, text='Please enter a password and timeout value', width=70)
status_lbl.grid(row=3, column=1, pady=10)

#Empty, for looks only
empty_frm = tk.Frame(master=window, height=20, width=20)
empty_frm.grid(row=4, column=1, pady=10)

#Start
window.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from PIL import ImageTk, Image
import Decryptor

def god_mod():
	if var1.get():
		try:
			Decryptor.main_strat('true', 'god_mod', selection_profile.get(), input_path.get())
		except:
			showerror('Error', 'ERROR: No such profile exists')
	else:
		try:
			Decryptor.main_strat('false', 'god_mod', selection_profile.get(), input_path.get())
		except:
			showerror('Error', 'ERROR: No such profile exists')
		

def maxinput(event):
	if selected_change.get() == 'geo':
		text_maxsize['text'] = 'maxsize:99999'
		return 99999
	elif selected_change.get() == 'maxhealth':
		text_maxsize['text'] = 'maxsize:10'
		return 10



def checkinput():
	try:
		if int(input_value.get()) > maxinput(1) or int(input_value.get()) < 1:
			input_value.delete(0, 'end')
			showerror('Error', 'ERROR: Please enter the correct number; \nMaxValue = {0};  MinValue = {1}'.format( str(maxinput(1)), '1' ))
	except:
		input_value.delete(0, 'end')
		showerror('Error', 'ERROR: Please enter the correct number')
	else:
		try:
			Decryptor.main_strat(input_value.get(), selected_change.get(), selection_profile.get(), input_path.get())
		except:
			showerror('Error', 'ERROR: No such profile exists')
		

root  = Tk()
root.title('Test')
root.geometry('500x240')
root.resizable(width=False, height=False)
root.call('wm', 'iconphoto', root._w, PhotoImage(file="images/HollowCheat.png"))


img = ImageTk.PhotoImage((Image.open("images/HollowCheatBG.gif")))
background_label = Label(root, image=img)
background_label.place(x=-50, y=-100)


button_start = Button(root, text='Start', fg='#aaafff', bg='#222222', activeforeground='#aaaaff', activebackground='#111100', width=10, height=1, font=('Consolas', 8, "bold"), command=checkinput)
button_start.place(x=319, y=110, anchor=CENTER)


button_help = Button(root, text='not working?', bg='white', font=('Consolas', 8))
button_help.place(x=273, y=55, height=13)
button_help.bind('<Button-1>', lambda x:input_path.place(x=250, y=170, anchor=CENTER))


input_value = Entry(root, justify=RIGHT, width=15, font=('Consolas', 12))
input_value.place(x=283, y=80, anchor=CENTER)
input_value.insert(0, 'Enter value')
input_value.bind('<Button-1>', lambda x: input_value.delete(0, 'end'))


input_path = Entry(root, justify=RIGHT, width=65, fg='grey', font=('Consolas', 10))
input_path.place(x=1000, y=1000, anchor=CENTER)
input_path.insert(0, 'C:\\Users\\admin\\AppData\\LocalLow\\Team Cherry\\Hollow Knight')
#input_path.bind('<Button-1>', lambda x: input_path.delete(0, 'end'))


selected_change = ttk.Combobox(root, state='readonly', values=('geo', 'maxhealth'))
selected_change.current(0)
selected_change.place(x=141, y=70, width=70)
selected_change.bind('<<ComboboxSelected>>', maxinput)


selection_profile = ttk.Combobox(root, justify=RIGHT, state='readonly', values=('1', '2', '3', '4'))
selection_profile.current(0)
selection_profile.place(x=50, y=-2, width=30)


var1 = BooleanVar()
var1.set(0)
checkbox_godmod = Checkbutton(root, variable=var1, text='God mod', bg='white', font=('Consolas', 8), width=9, command=god_mod)
checkbox_godmod.place(x=-2, y=20, height=15)


text_maxsize = Label(root, width=13, anchor='e', text='maxsize:99999', bg='#111119', fg='#aaaff1', font=('Consolas', 9, 'italic'))
text_maxsize.place(x=186, y=100)

text_version = Label(root, text='Hollow Cheat 1.1', bg='#344355', font=('Forte', 15))
text_version.place(x=346, y=212)

text_prifile = Label(root, anchor='e', bg='white', text='Profile:', font=('Consolas', 8))
text_prifile.place(x=0, y=0)


root.mainloop()
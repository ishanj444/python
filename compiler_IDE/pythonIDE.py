from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
compiler=Tk()
compiler.title('Uchiha_zoro')
filepath = ''

def setfilepath(path):
	global filepath
	filepath=path

#def runfunc():
##	exec(code)
	#print('code will run')
def runfunction():
	if filepath == '':
		savediag = Toplevel()
		text = Label(savediag, text='please save your code first')
		text.pack()
		return
	command = f'python {filepath}'
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
	output, error = process.communicate()
	editoroutput.insert('1.0',output)
	editoroutput.insert('1.0',error)

def saveas():
	if filepath=='':
		path = asksaveasfilename(filetypes=[('python','*.py'),('colab','*ipynb')])
	else:
		path=filepath	
	with open(path, 'w') as file:
		code = editor.get('1.0',END)
		file.write(code)
		setfilepath(path)

def openfile():
	path = askopenfilename(filetypes=[('python','*.py')])
	with open(path, 'r') as file:
		code = file.read()
		editor.delete('1.0',END)
		editor.insert('1.0',code) 
		setfilepath(path)

menu=Menu(compiler)

run=Menu(menu , tearoff=0)
menu.add_cascade(label='run',menu=run)
run.add_command(label='run', command=runfunction)

file=Menu(menu , tearoff=0)
menu.add_cascade(label='file',menu=file)
file.add_command(label='open', command=openfile)
file.add_command(label='save', command=saveas)
file.add_command(label='save as', command=saveas)
file.add_command(label='exit', command=exit)

compiler.config(menu=menu)

editor = Text()
editor.pack()

editoroutput = Text(height=12)
editoroutput.pack()
compiler.mainloop()


from tkinter import filedialog
from tkinter import *

class Window(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)               
		self.master = master
		self.initial_window()
		
	def initial_window(self):
		self.master.title("AIFRS")
		self.pack(fill=BOTH, expand=1)
		
		# Buttons
		startButton = Button(self, text="Start")
		startButton.place(x=745, y=30)
		stopButton = Button(self, text="Stop")
		stopButton.place(x=795, y=30)
		saveButton = Button(self, text="Save")
		saveButton.place(x=845, y=30)
		
		# Predator input
		predText = Label(self, text="Predators:")
		predText.place(x=750, y=70)
		predInput = Entry(self)
		predInput.insert(0, "")
		predInput.place(x=750, y=90)
		
		# Prey input
		preyText = Label(self, text="Prey:")
		preyText.place(x=750, y=110)
		preyInput = Entry(self)
		preyInput.insert(0, "")
		preyInput.place(x=750, y=130)
		
		# Step #
		stepText = Label(self, text="Steps:")
		stepText.place(x=750, y=150)
		stepInput = Entry(self)
		stepInput.insert(0, "")
		stepInput.place(x=750, y=170)
		
		# Episodes
		episodeText = Label(self, text="Episodes:")
		episodeText.place(x=750, y=190)
		episodeInput = Entry(self)
		episodeInput.insert(0, "")
		episodeInput.place(x=750, y=210)
		
		# Predator Reward
		rewardText1 = Label(self, text="Pred Reward:")
		rewardText1.place(x=700, y=250)
		rewardButton1 = Button(self, text="V", height=0)
		rewardButton1.place(x=780, y=240)
		rewardInput1 = Entry(self)
		rewardInput1.insert(0, "")
		rewardInput1.place(x=680, y=270)
		
		# Prey Reward
		rewardText1 = Label(self, text="Prey Reward:")
		rewardText1.place(x=830, y=250)
		rewardButton2 = Button(self, text="V", height=0)
		rewardButton2.place(x=910, y=240)
		rewardInput1 = Entry(self)
		rewardInput1.insert(0, "")
		rewardInput1.place(x=810, y=270)
		
		# Output
		outputText = Label(self, text="OUTPUT:", font=("Helvetica", 16))
		outputText.place(x=420, y=410)

root = Tk()
root.geometry("1000x600")
root.resizable(False, False)
#possible future work open file dialog:
#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)

app = Window(root)
root.mainloop()
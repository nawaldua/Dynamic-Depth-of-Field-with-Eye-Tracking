import glob
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog as fd
import sys
from guifuncts import browse_directory,view,preview
from application import application
import blurproc
def main():
	#Set up GUI
	window = tk.Tk()  #Makes main window
	window.wm_title("Focus_GUI: Root Window")
	window.config(background="#FFFFFF")

	global lbl1
	lbl1 = tk.StringVar()
	lbl1.set("Choose the required Directory")

	# Button to choose Video directory with the .jpg and .npy files
	but_direc = tk.Button(window, text = "Directory", width = 10, command = browse_directory)
	but_direc.grid(row=0, column=1)

	# Label to dynamically display the current directory    
	label1 = tk.Label(window, textvariable = lbl1)
	label1.grid(row=0, column=3)

	but_preview = tk.Button(window, text = "Preview", width = 10, command=preview)
	but_preview.grid(row=2, column=1)

	but_view = tk.Button(window, text = "View Video", width = 10, command=view)
	but_view.grid(row=4, column=1)

	but_quitApp = tk.Button(window, text = "Quit", width = 10, command = window.destroy)
	but_quitApp.grid(row=6, column=1)
	
	window.mainloop()  #Starts GUI
	
if __name__ == "__main__":
    main()

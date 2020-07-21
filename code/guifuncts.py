import glob
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog as fd
import sys
from outputfuncs import mouse_move,output_win,genpreview,preview_win

def browse_directory(lbl1):
    # Allow user to select a directory and store it in global var
    # called dirr
    global dirr
    #print(lbl1)
    dirr = fd.askdirectory()
    lbl1.set(dirr)

def view():
    # Initializing the display window
    view_win = tk.Toplevel()
    view_win.title("Video Parameters")
    
    # Button to Pre-process and Run application
    runApp_but = tk.Button(view_win, text = "Process Video", width = 10, command = application)
    runApp_but.grid(row=1, column=0)
    
    # Button to display output
    output_but = tk.Button(view_win, text = "Output Video", width = 10, command = output_win)
    output_but.grid(row=2, column=0)
    
    # Button to close and destroy current window
    close_but = tk.Button(view_win, text = "Close", width = 10, command = view_win.destroy)
    close_but.grid(row=5, column=0)
    
    quitApp_but = tk.Button(view_win, text = "Quit App", width = 10, command = window.destroy)
    quitApp_but.grid(row=6, column=0)
        

def preview():
    # Initializing the display window
    pv_win = tk.Toplevel()
    pv_win.title("Preview Parameters")
    
    input1 = tk.Label(pv_win, text = "Choose the blur level")
    input1.grid(row=0, column=0)
    
    global blurVariable
    blurVariable = tk.StringVar(pv_win)
    blurVariable.set(6) # default value

    blurOption = tk.OptionMenu(pv_win, blurVariable, 2, 6, 10, 20, 30, 40, 50, 100)
    blurOption.grid(row=0, column=1)
        
    # Button to display preview
    generate_but = tk.Button(pv_win, text = "Generate", width = 10, command = preview_win)
    generate_but.grid(row=2, column=0)
    
    # Button to close and destroy current window
    close_but = tk.Button(pv_win, text = "Close", width = 10, command = pv_win.destroy)
    close_but.grid(row=5, column=0)
    
    quitApp_but = tk.Button(pv_win, text = "Quit App", width = 10, command = window.destroy)
    quitApp_but.grid(row=6, column=0)

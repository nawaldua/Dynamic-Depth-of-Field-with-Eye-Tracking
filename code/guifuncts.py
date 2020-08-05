import tkinter as tk
from tkinter import filedialog as fd

import globalvars
from application import application
from outputfuncs import output_win, preview_win


def browse_directory():
    # Allow user to select a directory and store it in a global variable
    # called globalvars.dirr

    globalvars.dirr = fd.askdirectory()
    globalvars.lbl1.set(globalvars.dirr)


def output_folder():
    # Allow user to select a directory and store it in a global variable
    # called globalvars.dirr

    globalvars.video_folder = fd.askdirectory()
    globalvars.lbl2.set(globalvars.video_folder)


def view(window):
    # Initializing the display window
    view_win = tk.Toplevel()
    view_win.title("Video Parameters")

    # Setting the default blur kernel size
    globalvars.blurVariableMain = tk.StringVar(view_win)
    globalvars.blurVariableMain.set(6)  # default value = 6
    # Get value from Preview
    if hasattr(globalvars, 'blurVariablePreview'):
        globalvars.blurVariableMain.set(globalvars.blurVariablePreview.get())

    # Setting the default blur fall off/ variance size
    globalvars.blur_falloff_main = tk.StringVar(view_win)
    globalvars.blur_falloff_main.set(4.5)  # default value = 4.5
    # Get value from Preview
    if hasattr(globalvars, 'blur_falloff_preview'):
        globalvars.blur_falloff_main.set(globalvars.blur_falloff_preview.get())

    # Choosing Blur level
    input1 = tk.Label(view_win, text="Blur level")
    input1.grid(row=0, column=0)

    blurOption = tk.OptionMenu(view_win, globalvars.blurVariableMain, 2, 6, 10, 20, 30, 40, 50, 100)
    blurOption.grid(row=0, column=1)

    # Choosing Blur Fall Off/ Variance level
    input2 = tk.Label(view_win, text="Blur FallOff")
    input2.grid(row=1, column=0)

    variance = tk.OptionMenu(view_win, globalvars.blur_falloff_main, 3.5, 4, 4.5, 5, 5.5, 6, 8, 10, 12, 15, 20)
    variance.grid(row=1, column=1)

    # Button to Pre-process and Run application
    runApp_but = tk.Button(view_win, text="Process Video", width=10, command=application)
    runApp_but.grid(row=2, column=0)

    # Button to choose Video directory with the .jpg and .npy files
    but_direc = tk.Button(view_win, text="Video Folder", width=10, command=output_folder)
    but_direc.grid(row=3, column=0)

    # Label to dynamically display the current directory
    label2 = tk.Label(view_win, textvariable=globalvars.lbl2, bg="#FFFFFF")
    label2.grid(row=3, column=2)

    # Button to display output
    output_but = tk.Button(view_win, text="Output Video", width=10, command=output_win)
    output_but.grid(row=4, column=0)

    # Button to close and destroy current window
    close_but = tk.Button(view_win, text="Close", width=10, command=view_win.destroy)
    close_but.grid(row=5, column=0)

    quitApp_but = tk.Button(view_win, text="Quit App", width=10, command=window.destroy)
    quitApp_but.grid(row=6, column=0)


def preview(window):
    # Initializing the display window
    pv_win = tk.Toplevel()
    pv_win.title("Preview Parameters")

    # Setting the default blur kernel size
    globalvars.blurVariablePreview = tk.StringVar(pv_win)
    globalvars.blurVariablePreview.set(6)  # default value

    # Setting the default blur fall off/ variance size
    globalvars.blur_falloff_preview = tk.StringVar(pv_win)
    globalvars.blur_falloff_preview.set(4.5)  # default value = 4.5

    input1 = tk.Label(pv_win, text="Choose the blur level")
    input1.grid(row=0, column=0)

    blurOption = tk.OptionMenu(pv_win, globalvars.blurVariablePreview, 2, 6, 10, 20, 30, 40, 50, 100)
    blurOption.grid(row=0, column=1)

    input2 = tk.Label(pv_win, text="Choose the blur variance")
    input2.grid(row=1, column=0)

    variance = tk.OptionMenu(pv_win, globalvars.blur_falloff_preview, 3.5, 4, 4.5, 5, 5.5, 6, 8, 10, 12, 15, 20)
    variance.grid(row=1, column=1)

    # Button to display preview
    generate_but = tk.Button(pv_win, text="Generate", width=10, command=preview_win)
    generate_but.grid(row=2, column=0)

    # Button to close and destroy current window
    close_but = tk.Button(pv_win, text="Close", width=10, command=pv_win.destroy)
    close_but.grid(row=5, column=0)

    quitApp_but = tk.Button(pv_win, text="Quit App", width=10, command=window.destroy)
    quitApp_but.grid(row=6, column=0)

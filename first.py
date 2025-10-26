import sounddevice as sd
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory
import os

def file_path():
    global directory
    directory = askdirectory()
    if directory:
        path_label.config(text=f"Save Path: {directory}")
    else:
        path_label.config(text="No path selected")

def save_file():
    global directory
    try:
        time = int(sec.get())
        if time <= 0:
            raise ValueError("Time must be a positive integer")
        if not directory:
            raise ValueError("Please select a directory to save the file")
        addr = os.path.join(directory, "recording.wav")
        showinfo(title="Recording", message="Recording started")
        recording = sd.rec(int(time * 44100), samplerate=44100, channels=2)
        sd.wait()
        write(addr, 44100, recording)
        showinfo(title="Recording Complete", message=f"Recording saved at:\n{addr}")
    except ValueError as e:
        showwarning(title="Invalid Input", message=f"Error: {e}")
    except Exception as e:
        showwarning(title="Error", message=f"An unexpected error occurred: {e}")

def main_window():
    global sec, path_label

    win = Tk()
    win.geometry("500x700")
    win.resizable(False, False)
    win.title("Voice Recorder")
    win.config(bg="#f0f0f0")

    title = Label(win, text="Voice Recorder", font=("Helvetica", 28, "bold"), bg="#f0f0f0", fg="#333333")
    title.pack(pady=20)

    img_top = PhotoImage(file="sound 5.png")
    top_label = Label(win, image=img_top, bg="#f0f0f0")
    top_label.pack(pady=10)

    sec_frame = Frame(win, bg="#f0f0f0")
    sec_frame.pack(pady=15)

    sec = Entry(sec_frame, font=("Arial", 24), width=5, justify="center")
    sec.pack(side=LEFT, padx=10)

    sec_label = Label(sec_frame, text="Seconds", font=("Helvetica", 18), bg="#f0f0f0", fg="#333333")
    sec_label.pack(side=LEFT)

    path_btn = Button(win, text="Select Path", font=("Helvetica", 14), bg="#4CAF50", fg="white",
                      activebackground="#45A049", command=file_path)
    path_btn.pack(pady=10)

    path_label = Label(win, text="No path selected", font=("Helvetica", 12), bg="#f0f0f0", fg="#555555")
    path_label.pack(pady=5)

    img_start = PhotoImage(file="sound 3.png")
    start_btn = Button(win, image=img_start, bg="#f0f0f0", bd=0, command=save_file)
    start_btn.pack(pady=20)

    win.mainloop()

if __name__ == "__main__":
    main_window()

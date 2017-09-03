from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from pygame import mixer
import pygame as pg
import time
import os

for i in ['Angry', 'Disgust', 'Joy', 'Fear', 'Suspense', 'Neutral', 'Sad']:
    try:
        os.mkdir(i)
    except:
        pass

root = tk.Tk()
root.title('Recorder')
root.iconbitmap('mic.ico')
emo = tk.StringVar(root)
style = ttk.Style()
style.theme_use('winnative')

photo = PhotoImage(file='microphone.png').subsample(35, 35)

label1 = ttk.Label(root, text='Query')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = tk.StringVar()

def save_file():
    if len(entry2.get()) == 0:
        messagebox.showinfo("Error", "Enter Speaker's Name")
    else:
        list = os.listdir(emo.get())
        os.rename('microphone-results.wav', emo.get() + "/" + entry2.get() + str(len(list)) + ".wav")
        messagebox.showinfo("Saved", "Audio Saved as : " + emo.get() + "/" + entry2.get() + str(len(list)) + ".wav")


def callback():
    try:
        os.system("start microphone-results.wav")
    except:
        print('No Audio File Found')

def buttonClick():
    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio))
            mixer.music.load('chime2.mp3')
            mixer.music.play()
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)

        except sr.UnknownValueError:
            print('Google Speech Recognition could not Understand audio')
        except sr.RequestError as e:
            print('Could not request result from Google Speech Recogniser Service')
        else:
            pass

    with open("microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())

MyButton1 = ttk.Button(root, text='Play', width=10, command=callback)
MyButton1.grid(row=0, column=6)

label2 = ttk.Label(root, text='Speaker Name')
label2.grid(row=1, column=0, columnspan=2)
entry2 = ttk.Entry(root, width=40)
entry2.grid(row=2, column=0, columnspan=2)

label3 = ttk.Label(root, text='Emotion')
label3.grid(row=1, column=3)
emo.set('Angry')

popupMenu = tk.OptionMenu(root, emo, *{'Angry':'Angry', 'Disgust':'Disgust', 'Joy':'Joy', 'Fear':'Fear',
                                       'Suspense':'Suspense', 'Neutral':'Neutral', 'Sad':'Sad'})
popupMenu.grid(row=2, column=3)

MyButton1 = ttk.Button(root, text='Save Audio', width=10, command=save_file)
MyButton1.grid(row=2, column=4)

MyButton3 = ttk.Button(root, image=photo, command=buttonClick)#, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton3.grid(row=0, column=5)

root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()
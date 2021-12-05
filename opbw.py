import webbrowser
from tkinter import *
root = Tk( )


root.title('Abrir Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')
    webbrowser.open('www.instagram.com')
    webbrowser.open('www.youtube.com')
    webbrowser.open('www.facebook.com')



mygoogle = Button(root, text='Abrir o Google\n Instagram\n Youtube\n Facebook ', command=google).pack(pady=20)
root.mainloop()

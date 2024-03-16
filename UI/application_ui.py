import tkinter as tk
win = tk.Tk()
win.geometry('340x540')
win.title("Qr Code Generator")
win.attributes('-alpha', 0.95)
win.resizable(False, False)


tk.Label(win, text="QR Code Generator", font="Caveat 25 bold").pack(pady=10)











win.mainloop()
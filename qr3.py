import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def createQR(*args):
    data = text_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#DC143C", back_color="#00FFFF")
        res_img = img.resize((300, 280))
        tkimage = ImageTk.PhotoImage(res_img)
        qr_canvas.create_image(0, 0, anchor=tk.NW, image=tkimage)
        qr_canvas.image = tkimage
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')

def saveQR():
    data = text_entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="#FF7F50", back_color="#00FFFF")
        res_img = img.resize((280, 250))
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            res_img.save(path)
            messagebox.showinfo("Success", "QR Code is Saved")
    else:
        messagebox.showwarning("Warning", 'Enter Data in Entry First')

def clear_default_text(event):
    if text_entry.get() == "Enter text or link":
        text_entry.delete(0, tk.END)
        text_entry.configure(foreground="#8B008B")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("320x400")
root.config(bg='#DB7093')
root.resizable(0, 0)

style = ttk.Style()
style.configure("TFrame", background="lightblue")
style.configure("TButton", background="lightblue", font=("Helvetica", 10, "bold"))
style.configure("TLabel", background="lightblue", font=("Helvetica", 11))
style.configure("TEntry", font=("Helvetica", 11))

frame1 = ttk.Frame(root, relief=tk.RAISED)
frame1.place(x=10, y=5, width=300, height=270)

frame2 = ttk.Frame(root, relief=tk.SUNKEN)
frame2.place(x=10, y=285, width=300, height=100)

qr_canvas = tk.Canvas(frame1, bg="white")
qr_canvas.pack(fill=tk.BOTH)

text_entry = ttk.Entry(frame2, width=30, foreground="gray")
text_entry.insert(0, "Enter text or link")
text_entry.bind("<Return>", createQR)
text_entry.bind("<FocusIn>", clear_default_text)
text_entry.place(x=10, y=10)

btn_1 = ttk.Button(frame2, text="Create", command=createQR)
btn_1.place(x=10, y=50)

btn_2 = ttk.Button(frame2, text="Save", command=saveQR)
btn_2.place(x=110, y=50)

btn_3 = ttk.Button(frame2, text="Exit", command=root.destroy)
btn_3.place(x=210, y=50)

root.mainloop()

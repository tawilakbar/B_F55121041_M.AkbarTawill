from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2


def smoothing():
    global img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.GaussianBlur(gray, (5, 5), 0)
    img_tk = ImageTk.PhotoImage(Image.fromarray(smoothed))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk

def sharpening():
    global img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sharpened = cv2.Laplacian(gray, cv2.CV_64F)
    img_tk = ImageTk.PhotoImage(Image.fromarray(sharpened))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk
def open_image():
    global img
    path = filedialog.askopenfilename()
    img = cv2.imread(path)
    img_tk = ImageTk.PhotoImage(Image.fromarray(img))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk
root = Tk()
root.title("Aplikasi M.Akbar Tawil F55121041")
root.configure(bg='grey')
menubar = Menu(root)
root.config(menu=menubar)
nama_label = Label(root, text="M.Akbar Tawil F55121041", font=("Helvetica", 10), pady=10, bg='grey')
nama_label.pack()

kelas_label = Label(root, text="Kelas B", font=("Helvetica", 10), pady=10, bg='grey')
kelas_label.pack()
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_image)

halusmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Penghalusan", command=smoothing)
tajammenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Penajaman", command=sharpening)


canvas = Canvas(root, width=500, height=500, bg='grey')
canvas.pack()
root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk

def main():
    root = tk.Tk()
    root.title("CAT VIEWER - Lane")
    root.geometry ("500x500")

    pil_image=Image.open("cat.png")
    tk_image=ImageTk.PhotoImage(pil_image)

    label=tk.Label(root, image=tk_image)
    label.pack(padx=10, pady=10)

    root.mainloop()

if __name__=="__main__":
    main()
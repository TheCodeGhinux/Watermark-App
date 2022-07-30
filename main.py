from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk, ImageDraw, ImageFont

Theme_color = "#375362"
giy_orange = "#ec741d"
basewidth = 300


class WatermarkUi:

    def __init__(self):
        self.watermark = None
        self.img = None
        self.filename = None
        self.files = [('png Files', '*.png*')]

    def import_img(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select a File",
                                                   filetypes=(("png files",
                                                               "*.png*"),
                                                              ("jpg files",
                                                               "*.jpg*"),
                                                              ("jpeg files",
                                                               "*.jpeg*"),
                                                              ("all files",
                                                               "*.*")))
        with Image.open(self.filename) as new_img:
            wpercent = (basewidth / float(new_img.size[0]))
            hsize = int((float(new_img.size[1]) * float(wpercent)))
            new_img = new_img.resize((basewidth, hsize), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(new_img)
        img_display_label = Label(image=self.img)
        img_display_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def write_watermark(self):
        self.watermark = input_area.get()
        with Image.open(self.filename):
            img_in = Image.open(self.filename)
            draw = ImageDraw.Draw(img_in)

            # font = ImageFont.truetype(<font-file>, <font-size>)
            font = ImageFont.truetype("Merriweather-BlackItalic.ttf", 50)

            # draw.text((x, y),"Sample Text",(r,g,b))
            draw.text((0, 500), self.watermark, (236, 116, 29), font=font)

        wpercent = (basewidth / float(img_in.size[0]))
        hsize = int((float(img_in.size[1]) * float(wpercent)))
        img_in = img_in.resize((basewidth, hsize), Image.ANTIALIAS)

        img_in.save("watermarked.png")
        self.img = ImageTk.PhotoImage(img_in)
        img_display_label = Label(image=self.img)
        img_display_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def save_img(self):
        filename = filedialog.asksaveasfile(filetypes=self.files, defaultextension=".png", mode="wb")
        img_save = open("watermarked.png", "rb").read()
        filename.write(img_save)
        filename.close()


watermark = WatermarkUi()


screen = Tk()
screen.title("Watermark App")
screen.config(padx=20, pady=20, bg=Theme_color)
screen.wm_minsize(width=450, height=500)

# Create a File Explorer label
label_file_explorer = Label(screen,
                            text="WATERMARK APP BY The CODE GHINUX",
                            width=50, height=2,
                            fg=giy_orange)

upload_btn = Button(screen,
                    text="Browse Files",
                    command=watermark.import_img, fg="blue")

button_exit = Button(screen,
                     text="X",
                     bg="red",
                     fg="white",
                     command=exit)

label_file_explorer.grid(row=0, column=0)

upload_btn.grid(row=1, column=0, padx=10)

button_exit.grid(row=1, column=1, pady=10)

canvas = Canvas(width=450, height=450, bg="white")
canvas.grid(row=2, column=0, columnspan=2, pady=10)
canvas.create_image(10, 10, image=watermark.img)

input_area_label = Label(text="Watermark text: ")
input_area = Entry(width=40)

input_area_label.grid(column=0, row=3, sticky="W", padx="5", pady="5")
input_area.grid(column=0, row=3, columnspan=3)

add_btn = Button(text="Add Watermark", command=watermark.write_watermark, fg="white", bg="red", width=16)
add_btn.grid(column=0, row=5, sticky="N W", padx="5", pady="5")

save_btn = Button(text="Save", command=watermark.save_img, fg="white", bg="Green", width=16)
save_btn.grid(column=1, row=5, sticky="N W", padx="5", pady="5")

screen.mainloop()

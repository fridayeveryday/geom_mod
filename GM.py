import tkinter
from PIL import Image, ImageTk


class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.configure(background='white')
        # создаем рабочую область
        self.frame = tkinter.Frame(self.root)
        self.frame.grid()
        scale = 0.25
        self.image = Image.open("F://gm//iso.jpg")
        width, height = self.image.size
        width *= scale
        height *= scale
        self.image = self.image.resize((int(width), int(height)))
        self.photo = ImageTk.PhotoImage(self.image)

        # вставляем кнопку
        self.but = tkinter.Button(self.frame, text="прямоугольная изометрическая", command=lambda: self.my_event_handler("/gm/iso.jpg")).grid(row=1, column=1)
        self.but = tkinter.Button(self.frame, text="прямоугольная диметрическая", command=lambda: self.my_event_handler("/gm/pd.jpg")).grid(row=1, column=2)
        self.but = tkinter.Button(self.frame, text="косоугольная фронтальная из.",  command=lambda: self.my_event_handler("gm/kfi.jpg")).grid(row=2, column=1)
        self.but = tkinter.Button(self.frame, text="косоугольная горизонтальная из.", command=lambda: self.my_event_handler("/gm/kgi.jpg")).grid(row=2, column=2)

        # Добавим изображение
        self.canvas = tkinter.Canvas(self.root, height=600, width=700)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=1, column=0)
        self.canvas.configure(background='white')
        self.root.mainloop()

    def my_event_handler(self, img_path):
        print("my_event_handler")
        scale = 0.25
        self.image = Image.open(img_path)
        width, height = self.image.size
        width *= scale
        height *= scale
        self.image = self.image.resize((int(width), int(height)))
        self.photo = ImageTk.PhotoImage(self.image)
        self.c_image = self.canvas.create_image(0, 0, anchor='nw', image=self.photo)
        self.canvas.grid(row=1, column=0)


app = App()

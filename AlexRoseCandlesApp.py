import tkinter as tk
from PIL import ImageTk, Image
import webbrowser

class mainPage(tk.Tk):
        # Main window with logo image, name entry with button and next page button
        def __init__(self):
                tk.Tk.__init__(self)
                self.title("Alexander Rose Candles") # window title
                self.geometry('1200x700') # window size
                self.my_img = ImageTk.PhotoImage(Image.open("AR_Logo.png")) # image file
                self.label = tk.Label(image=self.my_img) # image label
                self.entry = tk.Entry(self) # entry
                self.button = tk.Button(self, text="Please Enter Your Name Then Click Here", command=self.on_button) # entry button
                self.label.pack()
                self.button.pack()
                self.entry.pack()

        def on_button(self):
                # Hello "name" label and "next page" button
                label = tk.Label(text="Hello " + self.entry.get()) # hello "name" label
                label.pack()
                self.button = tk.Button(self, text="Next Page", command=self.next_button).pack() # "next page" button
                self.button1 = tk.Button(self, text='Close', command=self.destroy).pack() # "close" button

        def next_button(self):
                # opens next window
                window = Website_Link(self)
                window.grab_set()

class Website_Link(tk.Toplevel):
        # toplevel window with close button, website banner, and website link button
        def __init__(self, parent):
                super().__init__(parent)
                self.title("Alexander Rose Candles")
                self.geometry('500x400') # window size
                self.my_img2 = ImageTk.PhotoImage(Image.open("AR_Cards.png")) # image file
                self.label2 = tk.Label(image=self.my_img2) # image label
                self.label = tk.Label(self, text="Please Check Out Our Website For Ordering Information!!!") # website label
                self.label.pack()
                self.label2.pack()
                self.button = tk.Button(self, text='Website', command=self.website_button).pack() # website button
                self.button = tk.Button(self, text='Close', command=self.destroy).pack() # "close" button

        def website_button(self):
                # button function leading to website
                self.url = "http://www.AlexanderRoseCandles.com"
                webbrowser.open(self.url)
                
app = mainPage()
app.mainloop()


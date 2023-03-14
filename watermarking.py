from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os



def open_file():
    global filename, filepath
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='Select file',
                                          filetypes=(('Text Files', '.txt'),
                                                     ('all files', '*.*')))
    if filename:
        filepath = os.path.abspath(filename)
    else:
        window.adderrorinfo()



def add_watermark():
    image_path = filepath
    watermark = text_entry.get()
    im = Image.open(image_path)
    
    draw = ImageDraw.Draw(im)

    text = watermark
    font = ImageFont.truetype('arial.ttf', 82)

    textwidth, textheight = draw.textsize(text, font)

    width, height = im.size

    x = width/2-textwidth/2
    y=height-textheight-300

    draw.text((x,y), text, font=font)
    try:
        im.save(r'D:\watermarked.jpeg')
    except:
        messagebox.showerror('list of configured paths: D,E,F', 'ERROR: This is an Error Message!')
    else:
        im.save(r'E:\watermarked.jpeg')
    finally:
        im.save(r'F:\watermarked.jpeg')



window = Tk()
window.title('Watermarking App')
window.geometry('400x300')


button_explore_label = Label(text="Select The Image:").grid(row=1, column=1, padx=50, pady=50)

button_explore = Button(window, text='Browse Files', command=open_file).grid(row=1, column=2)

text_label = Label(text='Enter Text:').grid(row=2, column=1)
text_entry = Entry()
text_entry.grid(row=2, column=2)

submit_button = Button(text='Submit', command=add_watermark).grid(row=4, column=1, pady=50, padx=70)

exit_button = Button(text='Exit', width=7, command=window.destroy)
exit_button.grid(row=4, column=2, padx=20, pady=50)


window.mainloop()
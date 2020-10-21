'''
Python code snippet
139-Font Browser
stevepython.wordpress.com

source:
https://github.com/jedie/python-code-snippets/blob/master/CodeSnippets/TkFontBrowser.py
'''
import tkinter
from tkinter import scrolledtext
from tkinter import font as TkFont

PANGRAMS = (
    " Jackdaws love my big sphinx of quartz. 1234567890",
)
DISPLAY_SIZES = (8, 12, 16)

class TkFontBrowser(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title(self.__class__.__name__)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.text = scrolledtext.ScrolledText(
            master=self.root, height=30, width=80
        )
        self.text.config(
            background="#ffffff", foreground="#000000",
            highlightthickness=0,
            font=('courier', 11),
        )
        self.text.grid(row=0, column=0, sticky=tkinter.NSEW)

        font_families = self.root.tk.call("font", "families")
        self.insert_text("There are %i font families:\n\n" % len(font_families))
        for no, font_family in enumerate(font_families):
            self.insert_text('\t%i.) "%s"\n' % (no, font_family), font_family=font_family)

        self.root.mainloop()

    def insert_text(self, txt, font_family=None):
        self.text.insert(tkinter.END, txt)
        if font_family is None:
            return

        for size in DISPLAY_SIZES:
            line, column = self.text.index(tkinter.INSERT).split('.')

            for pangram in PANGRAMS:
                self.text.insert(tkinter.END, "size: %i - %s\n" % (size, pangram))

            font = TkFont.Font(family=font_family, size=size)
            tag_name = "%s%i" % (font_family, size)
            self.text.tag_config(tag_name, font=font)
            self.text.tag_add(tag_name, "%s.0" % line, "%s.0+%ilines" % (line, len(PANGRAMS)))

        self.text.insert(tkinter.END, "\n\n")

font_browser = TkFontBrowser()

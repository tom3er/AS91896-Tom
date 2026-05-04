import tkinter as tk

class GermanApp:

    def __init__(self,root):
        self.root=root
        self.root.title("German Guide for Kiwi Students")
        self.root.configure(bg="#f1f5f8")
        self.root.geometry("700x600")

        #LESSON DATA
        self.lesson_data = {
            "1": {
                "name": "Lesson 1: Basics",
                "vocab": {
                    "hello": "hallo",
                    "yes": "ja",
                    "no": "nein"
                }
            },
            "2": {
                "name": "Lesson 2: Everyday Words",
                "vocab": {
                    "water": "wasser",
                    "food": "essen",
                    "school": "schule"
                }
            }
        }
        self.current_vocab = None
        self.words = []
        self.current_word = None
        self.score = 0
        self.index = 0


        self.title_font_1 = ("Helvetica", 30, "bold")
        self.title_font_2 = ("Helvetica", 19, "bold")
        self.button_font = ("Helvetica", 15, "bold")
        self.text_font = ("Helvetica", 13)

        self.button_img = tk.PhotoImage(file="button_normal.png")
        self.button_hover_img = tk.PhotoImage(file="button_hover.png")
        self.button_quit_img = tk.PhotoImage(file="button_quit.png")
        self.button_quit_hover_img = tk.PhotoImage(file="button_quit_hover.png")

        self.create_home_screen()

    #UI STYLING
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_button(self, text, command):
        btn = tk.Label(
            self.root,
            image=self.button_img,
            text=text,
            compound="center",
            font=self.button_font,
            fg="white",
            bd=0
        )
        btn.bind("<Button-1>", lambda e: command())

        btn.bind("<Enter>", lambda e: btn.config(image=self.button_hover_img))
        btn.bind("<Leave>", lambda e: btn.config(image=self.button_img))

        return btn

    #HOME SCREEN
    def create_home_screen(self):
        self.clear_screen()

        #Title
        tk.Label(
            self.root,
            text="German Guide\nfor Kiwi Students",
            font=self.title_font_1,
            fg="#324366",
            bg="#f1f5f8",
            justify="center"
        ).pack(pady=(50,30))

        #Buttons
        for key, lesson in self.lesson_data.items():
            btn = self.create_button(lesson["name"], lambda k=key: self.start_lesson(k))
            btn.pack(pady=10)

        #Subtitle
        tk.Label(
            self.root,
            text="Master essential German fast!",
            font=self.text_font,
            bg="#f1f5f8",
            fg="#324366"
        ).pack(pady=(10,20))

        #Quit Button
        self.quit_btn = tk.Label(
            self.root,
            image=self.button_quit_img,
            text="Quit",
            compound="center",
            font=self.button_font,
            fg="#1963cf",
        )
        self.quit_btn.bind("<Button-1>", lambda e: self.root.destroy())

        self.quit_btn.bind("<Enter>", lambda e: self.quit_btn.config(image=self.button_quit_hover_img))
        self.quit_btn.bind("<Leave>", lambda e: self.quit_btn.config(image=self.button_quit_img))

        self.quit_btn.pack(pady=0)


    #LESSON
    def start_lesson(self, key):
        self.clear_screen()
        self.current_lesson_key = key
        self.current_vocab = self.lesson_data[key]["vocab"]
        self.words = list(self.current_vocab.items())
        self.index = 0
        self.display_word()

    def display_word(self):
        self.clear_screen()

        en, de = self.words[self.index]

        lesson_name = self.lesson_data[self.current_lesson_key]['name']

        # Title
        tk.Label(
            self.root,
            text=lesson_name,
            font=self.title_font_2,
            fg="#324366",
            bg="#f1f5f8",
            justify="center"
        ).pack(pady=(50, 30))





#RUN APP
root = tk.Tk()
app = GermanApp(root)
root.mainloop()
import tkinter as tk
import random

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
                    "hello": "Hallo",
                    "yes": "Ja",
                    "no": "Nein"
                }
            },
            "2": {
                "name": "Lesson 2: Everyday Words",
                "vocab": {
                    "water": "Wasser",
                    "food": "Essen",
                    "school": "Schule"
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

        #Canvas
        canvas = tk.Canvas(
            self.root,
            width=370,
            height=250,
            bg="white",
            highlightthickness=0
        )
        canvas.pack()

        #Gernman word
        canvas.create_text(
            185,90,
            text=de,
            font=("Helvetica", 50, "bold"),
            fill="#324366"
        )

        #English word
        canvas.create_text(
            185, 150,
            text=en,
            font=("Helvetica", 40, "bold"),
            fill="#1963cf"
        )

        #Buttons
        nav_frame = tk.Frame(
            self.root,
            bg="#f1f5f8"
        )
        nav_frame.pack(pady=40)

        prev_btn = self.create_button("Previous", self.prev_word)
        prev_btn.pack(in_=nav_frame, side="left", padx=10)

        next_btn = self.create_button("Next", self.next_word)
        next_btn.pack(in_=nav_frame, side="left", padx=10)

    def next_word(self):
        if self.index < len(self.words) - 1:
            self.index += 1
            self.display_word()
        else:
            self.start_quiz()
    def prev_word(self):
        if self.index > 0:
            self.index -= 1
            self.display_word()

    def next_question(self):
        self.clear_screen()

        if self.index >= len(self.words):
            self.show_result()
            return

        en, de = self.words[self.index]
        self.current_word = (en, de)

        tk.Label(
            self.root,
            text=f"What is '{en}' in German?",
            font=self.title_font_1,
            fg="#324366",
            bg="#f1f5f8",
            justify="center"
        ).pack(pady=30)

        all_words=[]
        for lesson in self.lesson_data.values():
            all_words.extend(lesson["vocab"].values())

        wrong_options=[word for word in all_words if word !=de]
        wrong_choices=random.sample(wrong_options, 3)

        options = wrong_choices + [de]
        random.shuffle(options)

        for option in options:
            btn = self.create_button(option,lambda opt=option: self.check_answer(opt))
            btn.pack(pady=10)



    def check_answer(self, selected):
        pass


    def start_quiz(self):
        random.shuffle(self.words)
        self.score=0
        self.index=0
        self.next_question()



    def show_result(self):
        pass





#RUN APP
root = tk.Tk()
app = GermanApp(root)
root.mainloop()
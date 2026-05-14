import customtkinter as ctk
import tkinter as tk
import random

# ********** APP SETUP **********

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class GermanApp:
    def __init__(self,root):
        self.root=root
        self.root.title("German Guide for Kiwi Students")
        self.root.geometry("700x600")
        self.root.configure(bg="#f1f5f8")

        # ********** LESSON DATA ***********

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

        # ********** VARIABLES **********

        self.current_vocab = None
        self.words = []
        self.current_word = None
        self.score = 0
        self.index = 0

        # ********** FONTS **********

        self.title_font_1 = ("Helvetica", 30, "bold")
        self.title_font_2 = ("Helvetica", 19, "bold")
        self.button_font = ("Helvetica", 15, "bold")
        self.text_font = ("Helvetica", 13)

        self.create_home_screen()

    # ********** CLEAR SCREEN ***********

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ********** CUSTOM BUTTON **********

    def create_button(self, text, command, quit_button=False):

        if quit_button:
            fg_color = "#ffffff"
            hover_color = "#e8eef7"
            text_color = "#1963cf"
            width = 110
        else:
            fg_color = "#1963cf"
            hover_color = "#1453af"
            text_color = "white"
            width = 260

        btn = ctk.CTkButton(
              self.root,
              text = text,
              command = command,
              width = width,
              height = 55,
              corner_radius = 10,
              font = self.button_font,
              fg_color = fg_color,
              hover_color = hover_color,
              text_color = text_color,
              border_width = 0
        )

        return btn

    # ********** HOME SCREEN **********

    def create_home_screen(self):

        self.clear_screen()

        # Title

        title = tk.Label(
            self.root,
            text = "German Guide\nfor Kiwi Students",
            font = self.title_font_1,
            fg = "#324366",
            justify = "center"
        )

        title.pack(pady=(50,30))

        # Lesson Buttons

        for key, lesson in self.lesson_data.items():

            btn = self.create_button(
                lesson["name"],
                lambda k=key: self.start_lesson(k)
            )

            btn.pack(pady=10)

        # Subtitle

        subtitle = tk.Label(
            self.root,
            text = "Master essential German fast!",
            font = self.text_font,
            fg = "#324366"
        )

        subtitle.pack(pady=(15,25))

        # Quit Button

        quit_btn = self.create_button(
            "Quit",
            self.root.destroy,
            quit_button=True
        )

        quit_btn.pack()


    # ********** LESSON **********

    def start_lesson(self, key):

        self.clear_screen()

        self.current_lesson_key = key
        self.current_vocab = self.lesson_data[key]["vocab"]

        self.words = list(self.current_vocab.items())

        self.index = 0

        self.display_word()

    # ********** DISPLAY WORD **********

    def display_word(self):

        self.clear_screen()

        en, de = self.words[self.index]

        lesson_name = self.lesson_data[self.current_lesson_key]['name']

        # Lesson Title
        tk.Label(
            self.root,
            text = lesson_name,
            font = self.title_font_2,
            fg = "#324366",
            bg = "#f1f5f8",
            justify = "center"
        ).pack(pady=(50, 30))

        # Card Frame

        card = ctk.CTkFrame(
            self.root,
            width = 370,
            height = 250,
            corner_radius = 25,
            fg_color = "white"
        )

        card.pack()

        card.pack_propagate(False)

        # German Word

        german_label = tk.Label(
            card,
            text = de,
            font = ("Helvetica", 40, "bold"),
            fg = "#324366",
            bg = "white"
        )

        german_label.pack(pady=(55,10))

        # English Word

        english_label = tk.Label(
            card,
            text = en,
            font = ("Helvetica", 36, "bold"),
            fg = "#1963cf",
            bg = "white"
        )

        english_label.pack()

        # Navigation Buttons

        nav_frame = tk.Frame(
            self.root,
            bg="#f1f5f8"
        )

        nav_frame.pack(pady=40)

        prev_btn = self.create_button(
            "Previous",
            self.prev_word)

        prev_btn.pack(
            in_=nav_frame,
            side="left",
            padx=10)

        next_btn = self.create_button(
            "Next",
            self.next_word)

        next_btn.pack(
            in_=nav_frame,
            side="left",
            padx=10)

    # ********** NEXT WORD **********

    def next_word(self):

        if self.index < len(self.words) - 1:

            self.index += 1
            self.display_word()

        else:
            self.start_quiz()

    # ********** PREVIOUS WORD **********

    def prev_word(self):

        if self.index > 0:

            self.index -= 1
            self.display_word()

    # ********** QUIZ **********

    def start_quiz(self):

        random.shuffle(self.words)

        self.score=0
        self.index=0

        self.next_question()

    # ********** NEXT QUESTION **********

    def next_question(self):

        self.clear_screen()

        if self.index >= len(self.words):

            self.show_result()
            return

        en, de = self.words[self.index]

        self.current_word = (en, de)

        question = tk.Label(
            self.root,
            text=f"What is '{en}' in German?",
            font=self.title_font_1,
            fg="#324366",
            bg="#f1f5f8",
            justify="center"
        )

        question.pack(pady=30)

        all_words=[]

        for lesson in self.lesson_data.values():
            all_words.extend(lesson["vocab"].values())

        wrong_options=[word for word in all_words if word !=de]

        wrong_choices=random.sample(wrong_options, 3)

        options = wrong_choices + [de]

        random.shuffle(options)

        for option in options:

            btn = self.create_button(
                option,
                lambda opt=option: self.check_answer(opt)
            )

            btn.pack(pady=10)

    # ********** CHECK ANSWER **********

    def check_answer(self, selected):
        pass

    # SHOW RESULT **********

    def show_result(self):
        pass

# ********** RUN APP **********

root = tk.Tk()

app = GermanApp(root)

root.mainloop()
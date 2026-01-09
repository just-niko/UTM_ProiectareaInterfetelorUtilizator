# quiz_screen.py - Ecran cu test grila despre biblioteci
import tkinter as tk
from tkinter import messagebox
import config

class QuizScreen:
    """
    Clasa pentru testul grila despre biblioteci si management
    Permite utilizatorilor sa raspunda la intrebari si sa primeasca un scor
    """
    
    def __init__(self, root, navigate_to):
        """
        Initializare ecran test grila
        
        Args:
            root: fereastra principala Tkinter
            navigate_to: callback function pentru navigare
        """
        self.root = root
        self.navigate_to = navigate_to
        
        # Intrebari si raspunsuri
        self.questions = [
            {
                "question": "Ce este o biblioteca digitala?",
                "options": [
                    "O platforma online pentru acces la resurse digitale",
                    "Un magazin de carti online",
                    "O aplicatie de retele sociale"
                ],
                "correct": 0
            },
            {
                "question": "Ce inseamna ISBN?",
                "options": [
                    "International Standard Book Number",
                    "Internet Service Book Name",
                    "Internal System Book Number"
                ],
                "correct": 0
            },
            {
                "question": "Care este rolul principal al unui bibliotecar?",
                "options": [
                    "Sa vanda carti",
                    "Sa organizeze si sa faciliteze accesul la informatii",
                    "Sa predea lectii"
                ],
                "correct": 1
            },
            {
                "question": "Ce este catalogul unei biblioteci?",
                "options": [
                    "Lista preturilor cartilor",
                    "Un sistem organizat de inregistrare a resurselor",
                    "Un program de calculator"
                ],
                "correct": 1
            },
            {
                "question": "Ce reprezinta sistemul Dewey?",
                "options": [
                    "Un sistem de clasificare a cartilor",
                    "Un brand de mobilier pentru biblioteci",
                    "O aplicatie mobila"
                ],
                "correct": 0
            },
            {
                "question": "Ce este un periodic in contextul bibliotecii?",
                "options": [
                    "O carte foarte veche",
                    "O publicatie ce apare regulat (revista, ziar)",
                    "Un tip de imprumut"
                ],
                "correct": 1
            },
            {
                "question": "Ce inseamna termenul \"imprumut interbibliotecar\"?",
                "options": [
                    "Imprumut de carti intre studenti",
                    "Schimb de resurse intre biblioteci diferite",
                    "Donatii de carti"
                ],
                "correct": 1
            },
            {
                "question": "Care este avantajul principal al bibliotecilor digitale?",
                "options": [
                    "Sunt mai ieftine",
                    "Acces la resurse 24/7 de oriunde",
                    "Ocupa mai putin spatiu"
                ],
                "correct": 1
            }
        ]
        
        self.current_question = 0
        self.score = 0
        self.answers = []
        self.selected_option = tk.IntVar()
        
        # Configurare fereastra
        self.root.title(f"Test Grila - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Creare interfata
        self.create_widgets()
    
    def create_widgets(self):
        """Creare elemente grafice pentru testul grila"""
        
        # Configurare grid pentru root
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Header
        header_frame = tk.Frame(self.root, bg=config.COLOR_WARNING, height=80)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="TEST GRILA - CUNOSTINTE DESPRE BIBLIOTECI",
            font=config.FONT_TITLE,
            bg=config.COLOR_WARNING,
            fg=config.COLOR_WHITE
        ).pack(pady=15)
        
        # Container principal
        self.main_container = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        self.main_container.grid(row=1, column=0, sticky="nsew", padx=40, pady=30)
        self.main_container.grid_rowconfigure(3, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)
        
        # Frame pentru quiz
        self.quiz_frame = tk.Frame(self.main_container, bg=config.COLOR_WHITE, 
                                   relief=tk.RAISED, borderwidth=2)
        self.quiz_frame.grid(row=0, column=0, sticky="nsew", rowspan=5)
        self.quiz_frame.grid_rowconfigure(3, weight=1)
        self.quiz_frame.grid_columnconfigure(0, weight=1)
        
        # Progres
        self.progress_label = tk.Label(
            self.quiz_frame,
            text="",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY
        )
        self.progress_label.grid(row=0, column=0, pady=(20, 10), sticky="ew")
        
        # Intrebare
        self.question_label = tk.Label(
            self.quiz_frame,
            text="",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY,
            wraplength=700,
            justify=tk.LEFT
        )
        self.question_label.grid(row=1, column=0, pady=20, padx=30, sticky="ew")
        
        # Frame pentru optiuni
        self.options_frame = tk.Frame(self.quiz_frame, bg=config.COLOR_WHITE)
        self.options_frame.grid(row=2, column=0, pady=20, padx=50, sticky="nsew")
        
        # Butoane navigare
        navigation_frame = tk.Frame(self.quiz_frame, bg=config.COLOR_WHITE)
        navigation_frame.grid(row=4, column=0, pady=20, sticky="ew")
        
        self.next_button = tk.Button(
            navigation_frame,
            text="Urmatoarea intrebare",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE,
            width=25,
            height=2,
            cursor="hand2",
            command=self.next_question
        )
        self.next_button.pack()
        
        # Afișare prima întrebare
        self.show_question()
        
        # Footer cu buton înapoi
        footer_frame = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        footer_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        
        tk.Button(
            footer_frame,
            text="Inapoi la Meniu",
            font=config.FONT_NORMAL,
            bg=config.COLOR_PRIMARY,
            fg=config.COLOR_WHITE,
            width=20,
            height=2,
            cursor="hand2",
            command=lambda: self.navigate_to("menu")
        ).pack()
    
    def show_question(self):
        """Afiseaza intrebarea curenta"""
        if self.current_question < len(self.questions):
            # Actualizare progres
            self.progress_label.config(
                text=f"Intrebarea {self.current_question + 1} din {len(self.questions)}"
            )
            
            # Afisare intrebare
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])
            
            # Curata optiunile anterioare
            for widget in self.options_frame.winfo_children():
                widget.destroy()
            
            # Resetare selectie
            self.selected_option.set(-1)
            
            # Creare radio buttons pentru optiuni
            for idx, option in enumerate(q["options"]):
                rb = tk.Radiobutton(
                    self.options_frame,
                    text=option,
                    variable=self.selected_option,
                    value=idx,
                    font=config.FONT_NORMAL,
                    bg=config.COLOR_WHITE,
                    fg=config.COLOR_TEXT,
                    activebackground=config.COLOR_BACKGROUND,
                    selectcolor=config.COLOR_SUCCESS,
                    wraplength=600,
                    justify=tk.LEFT
                )
                rb.pack(anchor="w", pady=10, padx=20)
            
            # Actualizare text buton
            if self.current_question == len(self.questions) - 1:
                self.next_button.config(text="Finalizeaza testul")
        else:
            self.show_results()
    
    def next_question(self):
        """Trece la urmatoarea intrebare"""
        # Verifica daca s-a selectat un raspuns
        if self.selected_option.get() == -1:
            messagebox.showwarning(
                "Atentie",
                "Va rugam selectati un raspuns!",
                parent=self.root
            )
            return
        
        # Salveaza raspunsul
        self.answers.append(self.selected_option.get())
        
        # Verifica daca raspunsul este corect
        if self.selected_option.get() == self.questions[self.current_question]["correct"]:
            self.score += 1
        
        # Trece la urmatoarea intrebare
        self.current_question += 1
        self.show_question()
    
    def show_results(self):
        """Afiseaza rezultatele testului"""
        # Curata frame-ul
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        
        # Calcul procent
        percentage = (self.score / len(self.questions)) * 100
        
        # Determinare culoare și mesaj bazat pe scor
        if percentage >= 80:
            color = config.COLOR_SUCCESS
            message = "Excelent!"
            emoji = ""
        elif percentage >= 60:
            color = config.COLOR_WARNING
            message = "Bine!"
            emoji = ""
        else:
            color = config.COLOR_DANGER
            message = "Mai ai de invatat!"
            emoji = ""
        
        # Container rezultate
        results_container = tk.Frame(self.quiz_frame, bg=config.COLOR_WHITE)
        results_container.pack(expand=True)
        
        # Titlu
        tk.Label(
            results_container,
            text="REZULTATE TEST",
            font=config.FONT_TITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=30)
        
        # Mesaj evaluare
        tk.Label(
            results_container,
            text=message,
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=color
        ).pack(pady=10)
        
        # Scor
        score_frame = tk.Frame(results_container, bg=config.COLOR_BACKGROUND, 
                              relief=tk.RAISED, borderwidth=2)
        score_frame.pack(pady=20, padx=40)
        
        tk.Label(
            score_frame,
            text=f"Scor: {self.score} / {len(self.questions)}",
            font=("Arial", 18, "bold"),
            bg=config.COLOR_BACKGROUND,
            fg=config.COLOR_PRIMARY
        ).pack(pady=15, padx=30)
        
        tk.Label(
            score_frame,
            text=f"Procent: {percentage:.1f}%",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_BACKGROUND,
            fg=color
        ).pack(pady=(0, 15), padx=30)
        
        # Detalii răspunsuri
        details_frame = tk.Frame(results_container, bg=config.COLOR_WHITE)
        details_frame.pack(pady=20)
        
        tk.Label(
            details_frame,
            text="Detalii:",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack()
        
        correct_answers = self.score
        wrong_answers = len(self.questions) - self.score
        
        tk.Label(
            details_frame,
            text=f"Raspunsuri corecte: {correct_answers}",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SUCCESS
        ).pack(anchor="w", padx=50)
        
        tk.Label(
            details_frame,
            text=f"Raspunsuri gresite: {wrong_answers}",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_DANGER
        ).pack(anchor="w", padx=50)
        
        # Buton reluare test
        tk.Button(
            results_container,
            text="Reincearca testul",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SECONDARY,
            fg=config.COLOR_WHITE,
            width=20,
            height=2,
            cursor="hand2",
            command=self.restart_quiz
        ).pack(pady=20)
    
    def restart_quiz(self):
        """Reseteaza testul pentru o noua incercare"""
        self.current_question = 0
        self.score = 0
        self.answers = []
        self.selected_option.set(-1)
        
        # Recreeaza widget-urile
        for widget in self.quiz_frame.winfo_children():
            widget.destroy()
        
        # Recreeaza elementele
        self.progress_label = tk.Label(
            self.quiz_frame,
            text="",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY
        )
        self.progress_label.pack(pady=(20, 10))
        
        self.question_label = tk.Label(
            self.quiz_frame,
            text="",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY,
            wraplength=700,
            justify=tk.LEFT
        )
        self.question_label.pack(pady=20, padx=30)
        
        self.options_frame = tk.Frame(self.quiz_frame, bg=config.COLOR_WHITE)
        self.options_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        navigation_frame = tk.Frame(self.quiz_frame, bg=config.COLOR_WHITE)
        navigation_frame.pack(pady=20)
        
        self.next_button = tk.Button(
            navigation_frame,
            text="Urmatoarea intrebare",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE,
            width=25,
            height=2,
            cursor="hand2",
            command=self.next_question
        )
        self.next_button.pack()
        
        self.show_question()

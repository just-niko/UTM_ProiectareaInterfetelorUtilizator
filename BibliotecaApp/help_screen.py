# help_screen.py - Ecran de ajutor si informatii despre aplicatie
import tkinter as tk
from tkinter import scrolledtext
import config

class HelpScreen:
    """
    Clasa pentru ecranul de ajutor
    Ofera informatii despre aplicatie, instructiuni de utilizare si contacte
    """
    
    def __init__(self, root, navigate_to):
        """
        Initializare ecran ajutor
        
        Args:
            root: fereastra principala Tkinter
            navigate_to: callback function pentru navigare
        """
        self.root = root
        self.navigate_to = navigate_to
        
        # Configurare fereastra
        self.root.title(f"Ajutor - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Creare interfata
        self.create_widgets()
    
    def create_widgets(self):
        """Creare elemente grafice pentru ecranul de ajutor"""
        
        # Header cu titlu si buton back
        header_frame = tk.Frame(self.root, bg=config.COLOR_DANGER, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Container interior pentru titlu si buton
        header_inner = tk.Frame(header_frame, bg=config.COLOR_DANGER)
        header_inner.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        # Titlu
        tk.Label(
            header_inner,
            text="AJUTOR SI INFORMATII",
            font=config.FONT_TITLE,
            bg=config.COLOR_DANGER,
            fg=config.COLOR_WHITE
        ).pack(side=tk.LEFT, expand=True)
        
        # Buton Back
        tk.Button(
            header_inner,
            text="Inapoi la Meniu",
            font=config.FONT_NORMAL,
            bg=config.COLOR_PRIMARY,
            fg=config.COLOR_WHITE,
            width=15,
            height=1,
            cursor="hand2",
            command=lambda: self.navigate_to("menu")
        ).pack(side=tk.RIGHT, padx=10)
        
        # Container principal
        main_container = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        main_container.pack(expand=True, fill=tk.BOTH, padx=30, pady=20)
        
        # Notebook pentru taburi
        tabs_frame = tk.Frame(main_container, bg=config.COLOR_BACKGROUND)
        tabs_frame.pack(fill=tk.BOTH, expand=True)
        
        # Frame pentru butoane tab
        tab_buttons_frame = tk.Frame(tabs_frame, bg=config.COLOR_BACKGROUND)
        tab_buttons_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.current_tab = tk.StringVar(value="about")
        
        # Butoane taburi
        tabs = [
            {"name": "about", "text": "Despre", "command": lambda: self.show_tab("about")},
            {"name": "manual", "text": "Manual", "command": lambda: self.show_tab("manual")},
            {"name": "contact", "text": "Contact", "command": lambda: self.show_tab("contact")}
        ]
        
        self.tab_buttons = {}
        for tab in tabs:
            btn = tk.Button(
                tab_buttons_frame,
                text=tab["text"],
                font=config.FONT_BUTTON,
                bg=config.COLOR_SECONDARY,
                fg=config.COLOR_WHITE,
                width=20,
                height=2,
                cursor="hand2",
                command=tab["command"]
            )
            btn.pack(side=tk.LEFT, padx=5)
            self.tab_buttons[tab["name"]] = btn
        
        # Frame pentru continut taburi
        self.content_frame = tk.Frame(tabs_frame, bg=config.COLOR_WHITE, 
                                     relief=tk.RAISED, borderwidth=2)
        self.content_frame.pack(expand=True, fill=tk.BOTH)
        
        # Afisare tab implicit
        self.show_tab("about")
    
    def show_tab(self, tab_name):
        """
        Afiseaza tab-ul selectat
        
        Args:
            tab_name: numele tab-ului de afisat
        """
        # Actualizare culoare butoane
        for name, button in self.tab_buttons.items():
            if name == tab_name:
                button.config(bg=config.COLOR_SUCCESS)
            else:
                button.config(bg=config.COLOR_SECONDARY)
        
        # Curata frame-ul de continut
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Afisare continut bazat pe tab
        if tab_name == "about":
            self.show_about_content()
        elif tab_name == "manual":
            self.show_manual_content()
        elif tab_name == "contact":
            self.show_contact_content()
        
        self.current_tab.set(tab_name)
    
    def show_about_content(self):
        """Afiseaza continutul tab-ului \"Despre\""""
        content = tk.Frame(self.content_frame, bg=config.COLOR_WHITE)
        content.pack(expand=True, padx=40, pady=30)
        
        # Titlu
        tk.Label(
            content,
            text="BIBLIOTECA DIGITALA",
            font=config.FONT_TITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=(0, 20))
        
        # Informatii generale
        info_text = f"""
Versiune: 1.0.0
Data crearii: Ianuarie 2026
An: An 3 ID

Dezvoltator: Isvoranu Nicolas-Radu
Grupa: Grupa 310

Descriere:
Aceasta aplicatie este un sistem de management pentru biblioteci,
dezvoltat ca proiect la cursul de Proiectarea Interfetelor Utilizator.

Aplicatia ofera o interfata intuitiva pentru gestionarea cartilor,
membrilor bibliotecii, precum si module educationale interactive.

Tehnologii utilizate:
- Python 3.x
- Tkinter (interfata grafica)
- Programare orientata pe obiecte

Functionalitati principale:
- Sistem de autentificare securizat
- Gestionare completa a cartilor (CRUD)
- Gestionare membri bibliotecii
- Test grila interactiv
- Interfata moderna si intuitiva
- Design personalizat cu culori si fonturi
        """
        
        tk.Label(
            content,
            text=info_text.strip(),
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_TEXT,
            justify=tk.LEFT
        ).pack(pady=10)
    
    def show_manual_content(self):
        """Afiseaza continutul tab-ului \"Manual\""""
        # ScrolledText pentru manual lung
        text_widget = scrolledtext.ScrolledText(
            self.content_frame,
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_TEXT,
            wrap=tk.WORD,
            padx=20,
            pady=20
        )
        text_widget.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        manual_text = """
MANUAL DE UTILIZARE - BIBLIOTECA DIGITALA
===================================================

1. AUTENTIFICARE
─────────────────
Pentru a accesa aplicatia, introduceti credentialele de autentificare:
- Username: admin
- Parola: admin123

Sau:
- Username: student
- Parola: student123

Apasati butonul "AUTENTIFICARE" sau tasta Enter.


2. MENIU PRINCIPAL
──────────────────
Dupa autentificare, veti fi redirectionat catre meniul principal.
Aici puteti accesa urmatoarele module:

- Gestionare Carti - Administrare colectie de carti
- Gestionare Membri - Administrare membri bibliotecii
- Test Grila - Quiz interactiv despre biblioteci
- Ajutor - Informatii si manual de utilizare


3. GESTIONARE CARTI
────────────────────
In acest modul puteti:

Adaugare carte:
- Completati toate campurile din formular (Titlu, Autor, An, ISBN, Exemplare)
- Apasati butonul "Adauga carte"

Editare carte:
- Selectati o carte din tabel (click pe rand)
- Modificati campurile dorite
- Apasati butonul "Actualizeaza"

Stergere carte:
- Selectati o carte din tabel
- Apasati butonul "Sterge"
- Confirmati actiunea

Resetare formular:
- Apasati butonul "Reseteaza" pentru a sterge toate campurile

4. GESTIONARE MEMBRI
---------------------
Functionalitati similare cu gestionarea cartilor:

Campuri disponibile:
- Nume complet
- Email (validare automata)
- Telefon
- Tip membru (Student / Profesor / Personal)
- Status activ (bifa)

Operatii disponibile:
- Adaugare membru nou
- Actualizare date membru existent
- Stergere membru
- Resetare formular


5. TEST GRILA
-------------
Quiz interactiv cu 8 intrebari despre biblioteci:

Instructiuni:
- Cititi intrebarea afisata
- Selectati raspunsul corect din cele 3 optiuni
- Apasati "Urmatoarea intrebare" pentru a continua
- La final, veti primi scorul si evaluarea

Evaluare:
- 80-100%: Excelent
- 60-79%: Bine
- 0-59%: Mai ai de invatat

Dupa finalizare, puteti relua testul apasand "Reincearca testul"


6. NAVIGARE
-----------
- Folositi butonul "Inapoi la Meniu" pentru a reveni la meniul principal
- Butonul "Deconectare" va deconecteaza din aplicatie


7. SFATURI SI TRUCURI
----------------------
- Toate campurile sunt obligatorii in formulare
- Email-ul trebuie sa contina @ si .
- Numarul de exemplare trebuie sa fie pozitiv
- Selectati un rand din tabel pentru a edita/sterge
- Folositi tasta Enter pentru autentificare rapida


8. PROBLEME COMUNE
------------------
P: Nu pot adauga o carte.
R: Verificati daca ati completat toate campurile si daca numarul de exemplare este valid.

P: Nu pot edita o carte.
R: Asigurati-va ca ati selectat o carte din tabel mai intai.

P: Email-ul nu este acceptat.
R: Verificati formatul email-ului (trebuie sa contina @ si .)


9. CERINTE SISTEM
------------------
- Python 3.6 sau mai nou
- Tkinter (inclus in majoritatea distributiilor Python)
- Sistem de operare: Windows, Linux, macOS


10. DREPTURI DE AUTOR
----------------------
(c) 2026 - Isvoranu Nicolas-Radu
An: An 3 ID, Grupa 310
Curs: Proiectarea Interfetelor Utilizator
Toate drepturile rezervate.
        """
        
        text_widget.insert("1.0", manual_text)
        text_widget.config(state=tk.DISABLED)  # Read-only
    
    def show_contact_content(self):
        """Afiseaza continutul tab-ului \"Contact\""""
        content = tk.Frame(self.content_frame, bg=config.COLOR_WHITE)
        content.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Titlu
        tk.Label(
            content,
            text="INFORMATII DE CONTACT",
            font=config.FONT_TITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=(0, 20))
        
        # Container informatii
        info_container = tk.Frame(content, bg=config.COLOR_BACKGROUND, 
                                 relief=tk.RAISED, borderwidth=2)
        info_container.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
        
        # Informatii contact
        contact_info = [
            ("Student:", "Isvoranu Nicolas-Radu"),
            ("Grupa:", "An 3 ID - Grupa 310"),
            ("Email:", "nicolas.isvoranu@s.utm.ro"),
            ("Telefon:", "+40 123 456 789"),
            ("Universitate:", "Universitatea Titu Maiorescu"),
            ("Curs:", "Proiectarea Interfetelor Utilizator"),
            ("Profesor coordonator:", "Prof. Mironela Pirnau"),
        ]
        
        for label, value in contact_info:
            row = tk.Frame(info_container, bg=config.COLOR_BACKGROUND)
            row.pack(pady=10, padx=30, anchor="w", fill=tk.X)
            
            tk.Label(
                row,
                text=label,
                font=config.FONT_NORMAL,
                bg=config.COLOR_BACKGROUND,
                fg=config.COLOR_PRIMARY,
                width=25,
                anchor="w"
            ).pack(side=tk.LEFT)
            
            tk.Label(
                row,
                text=value,
                font=config.FONT_NORMAL,
                bg=config.COLOR_BACKGROUND,
                fg=config.COLOR_TEXT,
                anchor="w",
                wraplength=400,
                justify=tk.LEFT
                ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Nota
        tk.Label(
            content,
            text="Pentru suport sau raportare bug-uri, va rugam sa contactati dezvoltatorul.",
            font=("Arial", 9, "italic"),
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY,
            wraplength=600
        ).pack(pady=20)
        
        # GitHub (optional)
        github_frame = tk.Frame(content, bg=config.COLOR_WHITE)
        github_frame.pack(pady=10)
        
        tk.Label(
            github_frame,
            text="GitHub: ",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_TEXT
        ).pack(side=tk.LEFT)
        
        tk.Label(
            github_frame,
            text="github.com/just-niko/UTM",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY,
            cursor="hand2"
        ).pack(side=tk.LEFT)

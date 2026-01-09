# login_screen.py - Ecran de autentificare
import tkinter as tk
from tkinter import messagebox
import config

class LoginScreen:
    """
    Clasa pentru ecranul de autentificare
    Permite utilizatorilor sa se autentifice pentru a accesa aplicatia
    """
    
    def __init__(self, root, on_login_success):
        """
        Initializare ecran autentificare
        
        Args:
            root: fereastra principala Tkinter
            on_login_success: callback function pentru autentificare reusita
        """
        self.root = root
        self.on_login_success = on_login_success
        
        # Configurare fereastra
        self.root.title(f"Autentificare - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Centrare fereastra
        self.center_window()
        
        # Creare interfata
        self.create_widgets()
    
    def center_window(self):
        """Centrare fereastra pe ecran"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        """Creare elemente grafice pentru ecranul de login"""
        
        # Frame principal centrat
        main_frame = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Container pentru formular
        login_container = tk.Frame(main_frame, bg=config.COLOR_WHITE, 
                                   relief=tk.RAISED, borderwidth=2)
        login_container.pack(padx=40, pady=40)
        
        # Titlu
        title_label = tk.Label(
            login_container,
            text="BIBLIOTECA DIGITALA",
            font=config.FONT_TITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        )
        title_label.pack(pady=(30, 10))
        
        # Subtitlu
        subtitle_label = tk.Label(
            login_container,
            text="Sistem de Management",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Username frame
        username_frame = tk.Frame(login_container, bg=config.COLOR_WHITE)
        username_frame.pack(pady=10, padx=50)
        
        tk.Label(
            username_frame,
            text="Utilizator:",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_TEXT
        ).pack(anchor="w")
        
        self.username_entry = tk.Entry(
            username_frame,
            font=config.FONT_NORMAL,
            width=30,
            relief=tk.SOLID,
            borderwidth=1
        )
        self.username_entry.pack(pady=5)
        self.username_entry.focus()
        
        # Password frame
        password_frame = tk.Frame(login_container, bg=config.COLOR_WHITE)
        password_frame.pack(pady=10, padx=50)
        
        tk.Label(
            password_frame,
            text="Parola:",
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_TEXT
        ).pack(anchor="w")
        
        self.password_entry = tk.Entry(
            password_frame,
            font=config.FONT_NORMAL,
            width=30,
            show="*",
            relief=tk.SOLID,
            borderwidth=1
        )
        self.password_entry.pack(pady=5)
        
        # Bind Enter key pentru login
        self.password_entry.bind('<Return>', lambda e: self.login())
        
        # Buton Login
        login_button = tk.Button(
            login_container,
            text="AUTENTIFICARE",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE,
            width=25,
            height=2,
            cursor="hand2",
            relief=tk.RAISED,
            command=self.login
        )
        login_button.pack(pady=20)
        
        # Informatii de ajutor
        info_label = tk.Label(
            login_container,
            text="Cont implicit: admin / admin123",
            font=("Arial", 9),
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SECONDARY
        )
        info_label.pack(pady=(10, 30))
    
    def login(self):
        """Procesare autentificare utilizator"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        # Validare campuri goale
        if not username or not password:
            messagebox.showerror(
                "Eroare",
                "Va rugam completati toate campurile!",
                parent=self.root
            )
            return
        
        # Verificare credentiale
        if username in config.DEFAULT_USERS and config.DEFAULT_USERS[username] == password:
            messagebox.showinfo(
                "Succes",
                f"Bun venit, {username}!",
                parent=self.root
            )
            # Apelare callback pentru autentificare reusita
            self.on_login_success(username)
        else:
            messagebox.showerror(
                "Eroare",
                "Utilizator sau parola incorecta!",
                parent=self.root
            )
            # Curatare campuri
            self.password_entry.delete(0, tk.END)
            self.username_entry.focus()

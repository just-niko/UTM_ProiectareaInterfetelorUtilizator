# main_menu.py - Ecran principal cu meniu de navigare
import tkinter as tk
from tkinter import messagebox
import config

class MainMenu:
    """
    Clasa pentru ecranul principal (meniu)
    Permite navigarea catre diferitele module ale aplicatiei
    """
    
    def __init__(self, root, username, navigate_to):
        """
        Initializare meniu principal
        
        Args:
            root: fereastra principala Tkinter
            username: numele utilizatorului autentificat
            navigate_to: callback function pentru navigare
        """
        self.root = root
        self.username = username
        self.navigate_to = navigate_to
        
        # Configurare fereastra
        self.root.title(f"Meniu Principal - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Creare interfata
        self.create_widgets()
    
    def create_widgets(self):
        """Creare elemente grafice pentru meniul principal"""
        
        # Header
        header_frame = tk.Frame(self.root, bg=config.COLOR_PRIMARY, height=100)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        # Titlu în header
        title_label = tk.Label(
            header_frame,
            text="BIBLIOTECA DIGITALA",
            font=config.FONT_TITLE,
            bg=config.COLOR_PRIMARY,
            fg=config.COLOR_WHITE
        )
        title_label.pack(pady=10)
        
        # Informatii utilizator
        user_label = tk.Label(
            header_frame,
            text=f"Autentificat ca: {self.username}",
            font=config.FONT_NORMAL,
            bg=config.COLOR_PRIMARY,
            fg=config.COLOR_WHITE
        )
        user_label.pack()
        
        # Container principal pentru butoane
        main_container = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        main_container.pack(expand=True, fill=tk.BOTH, padx=50, pady=30)
        
        # Titlu sectiune
        section_title = tk.Label(
            main_container,
            text="Selecteaza o optiune:",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_BACKGROUND,
            fg=config.COLOR_PRIMARY
        )
        section_title.pack(pady=(0, 20))
        
        # Frame pentru butoane - 2 coloane
        buttons_frame = tk.Frame(main_container, bg=config.COLOR_BACKGROUND)
        buttons_frame.pack(expand=True)
        
        # Lista de optiuni meniu
        menu_options = [
            {
                "text": "Gestionare Carti",
                "icon": "",
                "color": config.COLOR_SECONDARY,
                "command": lambda: self.navigate_to("books")
            },
            {
                "text": "Gestionare Membri",
                "icon": "",
                "color": config.COLOR_SUCCESS,
                "command": lambda: self.navigate_to("members")
            },
            {
                "text": "Test Grila",
                "icon": "",
                "color": config.COLOR_WARNING,
                "command": lambda: self.navigate_to("quiz")
            },
            {
                "text": "Ajutor",
                "icon": "",
                "color": config.COLOR_DANGER,
                "command": lambda: self.navigate_to("help")
            }
        ]
        
        # Creare butoane în grid 2x2
        for idx, option in enumerate(menu_options):
            row = idx // 2
            col = idx % 2
            
            button = tk.Button(
                buttons_frame,
                text=option["text"],
                font=config.FONT_BUTTON,
                bg=option["color"],
                fg=config.COLOR_WHITE,
                width=25,
                height=3,
                cursor="hand2",
                relief=tk.RAISED,
                borderwidth=3,
                command=option["command"]
            )
            button.grid(row=row, column=col, padx=15, pady=15, sticky="nsew")
            
            # Efecte hover
            button.bind("<Enter>", lambda e, b=button, c=option["color"]: 
                       b.configure(bg=self.lighten_color(c)))
            button.bind("<Leave>", lambda e, b=button, c=option["color"]: 
                       b.configure(bg=c))
        
        # Footer cu buton logout
        footer_frame = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        footer_frame.pack(fill=tk.X, pady=20)
        
        logout_button = tk.Button(
            footer_frame,
            text="Deconectare",
            font=config.FONT_NORMAL,
            bg=config.COLOR_DANGER,
            fg=config.COLOR_WHITE,
            width=20,
            height=2,
            cursor="hand2",
            command=self.logout
        )
        logout_button.pack()
    
    def lighten_color(self, color):
        """
        Lumineaza o culoare pentru efectul de hover
        
        Args:
            color: culoarea in format hex
            
        Returns:
            culoarea luminata in format hex
        """
        # Conversie simpla pentru hover effect
        return color + "DD" if len(color) == 7 else color
    
    def logout(self):
        """Procesare deconectare utilizator"""
        result = messagebox.askyesno(
            "Confirmare",
            "Sigur doriti sa va deconectati?",
            parent=self.root
        )
        if result:
            self.navigate_to("logout")

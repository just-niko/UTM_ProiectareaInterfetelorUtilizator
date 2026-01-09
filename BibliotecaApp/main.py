# main.py - Fisier principal pentru rularea aplicatiei
"""
Aplicatie: Biblioteca Digitala - Sistem de Management
Curs: Proiectarea Interfetelor Utilizator
Autor: Student
Data: Ianuarie 2026

Descriere:
Aceasta aplicatie implementeaza un sistem complet de management pentru biblioteci,
incluzand autentificare, gestionare carti, gestionare membri, test grila si ajutor.
"""

import tkinter as tk
from tkinter import messagebox
import config
from login_screen import LoginScreen
from main_menu import MainMenu
from books_screen import BooksScreen
from members_screen import MembersScreen
from quiz_screen import QuizScreen
from help_screen import HelpScreen


class BibliotecaApp:
    """
    Clasa principala a aplicatiei - Controller
    Gestioneaza navigarea intre diferitele ecrane ale aplicatiei
    """
    
    def __init__(self):
        """Initializare aplicatie"""
        self.root = tk.Tk()
        self.root.resizable(False, False)  # Dezactivare redimensionare
        
        # Icon aplicatie (daca exista)
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass  # Ignora daca nu exista icon
        
        # Variabile aplicatie
        self.current_user = None
        self.current_screen = None
        
        # Pornire cu ecranul de login
        self.show_login()
        
        # Rulare aplicatie
        self.root.mainloop()
    
    def clear_window(self):
        """Sterge toate widget-urile din fereastra"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login(self):
        """Afiseaza ecranul de autentificare"""
        self.clear_window()
        self.current_screen = LoginScreen(self.root, self.on_login_success)
    
    def on_login_success(self, username):
        """
        Callback pentru autentificare reusita
        
        Args:
            username: numele utilizatorului autentificat
        """
        self.current_user = username
        self.show_menu()
    
    def show_menu(self):
        """Afiseaza meniul principal"""
        self.clear_window()
        self.current_screen = MainMenu(self.root, self.current_user, self.navigate)
    
    def show_books(self):
        """Afiseaza ecranul de gestionare carti"""
        self.clear_window()
        self.current_screen = BooksScreen(self.root, self.navigate)
    
    def show_members(self):
        """Afiseaza ecranul de gestionare membri"""
        self.clear_window()
        self.current_screen = MembersScreen(self.root, self.navigate)
    
    def show_quiz(self):
        """Afiseaza ecranul de test grila"""
        self.clear_window()
        self.current_screen = QuizScreen(self.root, self.navigate)
    
    def show_help(self):
        """Afiseaza ecranul de ajutor"""
        self.clear_window()
        self.current_screen = HelpScreen(self.root, self.navigate)
    
    def navigate(self, destination):
        """
        Functie de navigare intre ecrane
        
        Args:
            destination: destinatia navigarii (string)
        """
        navigation_map = {
            "login": self.show_login,
            "menu": self.show_menu,
            "books": self.show_books,
            "members": self.show_members,
            "quiz": self.show_quiz,
            "help": self.show_help,
            "logout": self.logout
        }
        
        if destination in navigation_map:
            navigation_map[destination]()
        else:
            messagebox.showerror("Eroare", f"Destinatie invalida: {destination}")
    
    def logout(self):
        """Deconectare utilizator"""
        self.current_user = None
        self.show_login()


def main():
    """Functie principala - punct de intrare in aplicatie"""
    print("=" * 60)
    print("BIBLIOTECA DIGITALA - Sistem de Management")
    print("=" * 60)
    print(f"Student: {config.STUDENT_NAME}")
    print(f"Grupa: {config.STUDENT_GROUP}")
    print("=" * 60)
    print("\nPornire aplicatie...")
    print("\nIMPORTANT: Inainte de predare, actualizati config.py cu:")
    print("   - Numele si prenumele dvs. la STUDENT_NAME")
    print("   - Grupa dvs. la STUDENT_GROUP")
    print("=" * 60)
    print("\nCredentiale login:")
    print("  Username: admin    | Parola: admin123")
    print("  Username: student  | Parola: student123")
    print("=" * 60 + "\n")
    
    # Creare si rulare aplicatie
    app = BibliotecaApp()


if __name__ == "__main__":
    main()

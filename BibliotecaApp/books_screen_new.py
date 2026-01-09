# books_screen.py - Ecran pentru gestionarea cartilor
import tkinter as tk
from tkinter import ttk, messagebox
import config

class BooksScreen:
    """
    Clasa pentru gestionarea cartilor din biblioteca
    Permite adaugare, editare, stergere si vizualizare carti
    """
    
    def __init__(self, root, navigate_to):
        """
        Initializare ecran gestionare carti
        
        Args:
            root: fereastra principala Tkinter
            navigate_to: callback function pentru navigare
        """
        self.root = root
        self.navigate_to = navigate_to
        
        # Date carti (in memorie - simulare baza de date)
        self.books = [
            {"id": 1, "titlu": "Amintiri din copilarie", "autor": "Ion Creanga", 
             "an": "1892", "isbn": "978-606-600-123-4", "exemplare": 5},
            {"id": 2, "titlu": "Moara cu noroc", "autor": "Ioan Slavici", 
             "an": "1881", "isbn": "978-606-600-124-1", "exemplare": 3},
            {"id": 3, "titlu": "Enigma Otiliei", "autor": "George Calinescu", 
             "an": "1938", "isbn": "978-606-600-125-8", "exemplare": 4},
        ]
        self.next_id = 4
        
        # Configurare fereastra
        self.root.title(f"Gestionare Carti - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Creare interfata
        self.create_widgets()
    
    def create_widgets(self):
        """Creare elemente grafice pentru gestionarea cartilor"""
        
        # Header
        header_frame = tk.Frame(self.root, bg=config.COLOR_SECONDARY, height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="GESTIONARE CARTI",
            font=config.FONT_TITLE,
            bg=config.COLOR_SECONDARY,
            fg=config.COLOR_WHITE
        ).pack(pady=15)
        
        # Container principal
        main_container = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        
        # Frame stanga - Formular
        form_frame = tk.Frame(main_container, bg=config.COLOR_WHITE, relief=tk.RAISED, borderwidth=2)
        form_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10), pady=0)
        
        tk.Label(
            form_frame,
            text="Adauga / Editeaza carte",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=15)
        
        # Campuri formular
        fields_frame = tk.Frame(form_frame, bg=config.COLOR_WHITE)
        fields_frame.pack(padx=20, pady=10)
        
        # Titlu
        tk.Label(fields_frame, text="Titlu:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, fg=config.COLOR_TEXT).grid(row=0, column=0, sticky="w", pady=5)
        self.title_entry = tk.Entry(fields_frame, font=config.FONT_NORMAL, width=25)
        self.title_entry.grid(row=0, column=1, pady=5, padx=5)
        
        # Autor
        tk.Label(fields_frame, text="Autor:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, fg=config.COLOR_TEXT).grid(row=1, column=0, sticky="w", pady=5)
        self.author_entry = tk.Entry(fields_frame, font=config.FONT_NORMAL, width=25)
        self.author_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # An publicare
        tk.Label(fields_frame, text="An publicare:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, fg=config.COLOR_TEXT).grid(row=2, column=0, sticky="w", pady=5)
        self.year_entry = tk.Entry(fields_frame, font=config.FONT_NORMAL, width=25)
        self.year_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # ISBN
        tk.Label(fields_frame, text="ISBN:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, fg=config.COLOR_TEXT).grid(row=3, column=0, sticky="w", pady=5)
        self.isbn_entry = tk.Entry(fields_frame, font=config.FONT_NORMAL, width=25)
        self.isbn_entry.grid(row=3, column=1, pady=5, padx=5)
        
        # Exemplare
        tk.Label(fields_frame, text="Exemplare:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, fg=config.COLOR_TEXT).grid(row=4, column=0, sticky="w", pady=5)
        self.copies_entry = tk.Entry(fields_frame, font=config.FONT_NORMAL, width=25)
        self.copies_entry.grid(row=4, column=1, pady=5, padx=5)
        
        # Butoane formular
        buttons_frame = tk.Frame(form_frame, bg=config.COLOR_WHITE)
        buttons_frame.pack(pady=20)
        
        tk.Button(
            buttons_frame,
            text="Adauga",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE,
            width=12,
            cursor="hand2",
            command=self.add_book
        ).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(
            buttons_frame,
            text="Actualizeaza",
            font=config.FONT_BUTTON,
            bg=config.COLOR_WARNING,
            fg=config.COLOR_WHITE,
            width=12,
            cursor="hand2",
            command=self.update_book
        ).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(
            buttons_frame,
            text="Sterge",
            font=config.FONT_BUTTON,
            bg=config.COLOR_DANGER,
            fg=config.COLOR_WHITE,
            width=12,
            cursor="hand2",
            command=self.delete_book
        ).grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(
            buttons_frame,
            text="Reseteaza",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SECONDARY,
            fg=config.COLOR_WHITE,
            width=12,
            cursor="hand2",
            command=self.clear_form
        ).grid(row=1, column=1, padx=5, pady=5)
        
        # Frame dreapta - Tabel
        table_frame = tk.Frame(main_container, bg=config.COLOR_WHITE, relief=tk.RAISED, borderwidth=2)
        table_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=(10, 0))
        
        tk.Label(
            table_frame,
            text="Lista cartilor",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=15)
        
        # Treeview pentru afisare carti
        tree_container = tk.Frame(table_frame, bg=config.COLOR_WHITE)
        tree_container.pack(expand=True, fill=tk.BOTH, padx=15, pady=(0, 15))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        columns = ("ID", "Titlu", "Autor", "An", "ISBN", "Exemplare")
        self.tree = ttk.Treeview(tree_container, columns=columns, show="headings", 
                                 yscrollcommand=scrollbar.set, height=15)
        
        # Configurare coloane
        self.tree.column("ID", width=40, anchor="center")
        self.tree.column("Titlu", width=150, anchor="w")
        self.tree.column("Autor", width=120, anchor="w")
        self.tree.column("An", width=60, anchor="center")
        self.tree.column("ISBN", width=120, anchor="center")
        self.tree.column("Exemplare", width=80, anchor="center")
        
        # Headings
        for col in columns:
            self.tree.heading(col, text=col)
        
        self.tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar.config(command=self.tree.yview)
        
        # Bind click pe treeview
        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)
        
        # Populare tabel
        self.refresh_table()
        
        # Footer cu buton inapoi
        footer_frame = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        footer_frame.pack(fill=tk.X, pady=(0, 10))
        
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
    
    def refresh_table(self):
        """Reimproaspateaza tabelul cu carti"""
        # Sterge toate inregistrarile
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adauga cartile
        for book in self.books:
            self.tree.insert("", tk.END, values=(
                book["id"], book["titlu"], book["autor"], 
                book["an"], book["isbn"], book["exemplare"]
            ))
    
    def on_tree_select(self, event):
        """Populare formular la selectarea unei carti din tabel"""
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item["values"]
            
            # Gaseste cartea in lista
            book = next((b for b in self.books if b["id"] == values[0]), None)
            if book:
                self.clear_form()
                self.title_entry.insert(0, book["titlu"])
                self.author_entry.insert(0, book["autor"])
                self.year_entry.insert(0, book["an"])
                self.isbn_entry.insert(0, book["isbn"])
                self.copies_entry.insert(0, str(book["exemplare"]))
    
    def clear_form(self):
        """Curata formularul"""
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.copies_entry.delete(0, tk.END)
    
    def add_book(self):
        """Adauga o carte noua"""
        # Validare campuri
        if not all([self.title_entry.get(), self.author_entry.get(),
                   self.year_entry.get(), self.isbn_entry.get(), 
                   self.copies_entry.get()]):
            messagebox.showerror("Eroare", "Toate campurile sunt obligatorii!", parent=self.root)
            return
        
        try:
            copies = int(self.copies_entry.get())
            if copies < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Eroare", "Numarul de exemplare trebuie sa fie un numar pozitiv!", 
                               parent=self.root)
            return
        
        # Adauga carte
        new_book = {
            "id": self.next_id,
            "titlu": self.title_entry.get(),
            "autor": self.author_entry.get(),
            "an": self.year_entry.get(),
            "isbn": self.isbn_entry.get(),
            "exemplare": copies
        }
        self.books.append(new_book)
        self.next_id += 1
        
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Succes", "Cartea a fost adaugata cu succes!", parent=self.root)
    
    def update_book(self):
        """Actualizeaza cartea selectata"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atentie", "Selectati o carte din tabel!", parent=self.root)
            return
        
        # Validare campuri
        if not all([self.title_entry.get(), self.author_entry.get(), 
                   self.year_entry.get(), self.isbn_entry.get(), 
                   self.copies_entry.get()]):
            messagebox.showerror("Eroare", "Toate campurile sunt obligatorii!", parent=self.root)
            return
        
        try:
            copies = int(self.copies_entry.get())
            if copies < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Eroare", "Numarul de exemplare trebuie sa fie un numar pozitiv!", 
                               parent=self.root)
            return
        
        # Actualizeaza
        item = self.tree.item(selected[0])
        book_id = item["values"][0]
        
        for book in self.books:
            if book["id"] == book_id:
                book["titlu"] = self.title_entry.get()
                book["autor"] = self.author_entry.get()
                book["an"] = self.year_entry.get()
                book["isbn"] = self.isbn_entry.get()
                book["exemplare"] = copies
                break
        
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Succes", "Cartea a fost actualizata!", parent=self.root)
    
    def delete_book(self):
        """Sterge cartea selectata"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atentie", "Selectati o carte din tabel!", parent=self.root)
            return
        
        result = messagebox.askyesno("Confirmare", 
                                     "Sigur doriti sa stergeti aceasta carte?", 
                                     parent=self.root)
        if result:
            item = self.tree.item(selected[0])
            book_id = item["values"][0]
            
            self.books = [b for b in self.books if b["id"] != book_id]
            
            self.refresh_table()
            self.clear_form()
            messagebox.showinfo("Succes", "Cartea a fost stearsa!", parent=self.root)

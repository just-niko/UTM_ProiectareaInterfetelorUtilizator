# members_screen.py - Ecran pentru gestionarea membrilor bibliotecii
import tkinter as tk
from tkinter import ttk, messagebox
import config

class MembersScreen:
    """
    Clasa pentru gestionarea membrilor bibliotecii
    Permite adaugare, editare, stergere si vizualizare membri
    """
    
    def __init__(self, root, navigate_to):
        """
        Initializare ecran gestionare membri
        
        Args:
            root: fereastra principala Tkinter
            navigate_to: callback function pentru navigare
        """
        self.root = root
        self.navigate_to = navigate_to
        
        # Date membri (in memorie - simulare baza de date)
        self.members = [
            {"id": 1, "nume": "Popescu Ion", "email": "ion.popescu@email.com", 
             "telefon": "0721234567", "tip": "Student", "activ": "Da"},
            {"id": 2, "nume": "Ionescu Maria", "email": "maria.ionescu@email.com", 
             "telefon": "0732345678", "tip": "Profesor", "activ": "Da"},
            {"id": 3, "nume": "Vasilescu Ana", "email": "ana.vasilescu@email.com", 
             "telefon": "0743456789", "tip": "Student", "activ": "Nu"},
        ]
        self.next_id = 4
        
        # Configurare fereastra
        self.root.title(f"Gestionare Membrii - {config.STUDENT_NAME} - {config.STUDENT_GROUP}")
        self.root.geometry(f"{config.WINDOW_WIDTH}x{config.WINDOW_HEIGHT}")
        self.root.configure(bg=config.COLOR_BACKGROUND)
        
        # Creare interfata
        self.create_widgets()
    
    def create_widgets(self):
        """Creare elemente grafice pentru gestionarea membrilor"""
        
        # Configurare grid pentru root
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Header
        header_frame = tk.Frame(self.root, bg=config.COLOR_SUCCESS, height=80)
        header_frame.grid(row=0, column=0, sticky="ew")
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="GESTIONARE MEMBRII",
            font=config.FONT_TITLE,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE
        ).pack(pady=15)
        
        # Container principal
        main_container = tk.Frame(self.root, bg=config.COLOR_BACKGROUND)
        main_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        
        # Frame sus - Formular
        form_frame = tk.Frame(main_container, bg=config.COLOR_WHITE, relief=tk.RAISED, borderwidth=2)
        form_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            form_frame,
            text="Adauga / Editeaza membru",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=10)
        
        # Campuri formular - Layout orizontal
        fields_container = tk.Frame(form_frame, bg=config.COLOR_WHITE)
        fields_container.pack(padx=20, pady=10)
        
        # Row 1
        row1 = tk.Frame(fields_container, bg=config.COLOR_WHITE)
        row1.pack(fill=tk.X, pady=5)
        
        tk.Label(row1, text="Nume complet:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, width=12, anchor="w").pack(side=tk.LEFT, padx=5)
        self.name_entry = tk.Entry(row1, font=config.FONT_NORMAL, width=25)
        self.name_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row1, text="Email:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, width=8, anchor="w").pack(side=tk.LEFT, padx=5)
        self.email_entry = tk.Entry(row1, font=config.FONT_NORMAL, width=25)
        self.email_entry.pack(side=tk.LEFT, padx=5)
        
        # Row 2
        row2 = tk.Frame(fields_container, bg=config.COLOR_WHITE)
        row2.pack(fill=tk.X, pady=5)
        
        tk.Label(row2, text="Telefon:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, width=12, anchor="w").pack(side=tk.LEFT, padx=5)
        self.phone_entry = tk.Entry(row2, font=config.FONT_NORMAL, width=25)
        self.phone_entry.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row2, text="Tip:", font=config.FONT_NORMAL, 
                bg=config.COLOR_WHITE, width=8, anchor="w").pack(side=tk.LEFT, padx=5)
        self.type_var = tk.StringVar()
        self.type_combo = ttk.Combobox(row2, textvariable=self.type_var, 
                                       values=["Student", "Profesor", "Personal"], 
                                       font=config.FONT_NORMAL, width=23, state="readonly")
        self.type_combo.pack(side=tk.LEFT, padx=5)
        self.type_combo.set("Student")
        
        # Row 3 - Activ checkbox
        row3 = tk.Frame(fields_container, bg=config.COLOR_WHITE)
        row3.pack(fill=tk.X, pady=5)
        
        self.active_var = tk.BooleanVar(value=True)
        tk.Checkbutton(
            row3,
            text="Membru activ",
            variable=self.active_var,
            font=config.FONT_NORMAL,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_SUCCESS
        ).pack(side=tk.LEFT, padx=5)
        
        # Butoane formular
        buttons_frame = tk.Frame(form_frame, bg=config.COLOR_WHITE)
        buttons_frame.pack(pady=15)
        
        tk.Button(
            buttons_frame,
            text="Adauga membru",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SUCCESS,
            fg=config.COLOR_WHITE,
            width=15,
            cursor="hand2",
            command=self.add_member
        ).grid(row=0, column=0, padx=5)
        
        tk.Button(
            buttons_frame,
            text="Actualizeaza",
            font=config.FONT_BUTTON,
            bg=config.COLOR_WARNING,
            fg=config.COLOR_WHITE,
            width=15,
            cursor="hand2",
            command=self.update_member
        ).grid(row=0, column=1, padx=5)
        
        tk.Button(
            buttons_frame,
            text="Sterge",
            font=config.FONT_BUTTON,
            bg=config.COLOR_DANGER,
            fg=config.COLOR_WHITE,
            width=15,
            cursor="hand2",
            command=self.delete_member
        ).grid(row=0, column=2, padx=5)
        
        tk.Button(
            buttons_frame,
            text="Reseteaza",
            font=config.FONT_BUTTON,
            bg=config.COLOR_SECONDARY,
            fg=config.COLOR_WHITE,
            width=15,
            cursor="hand2",
            command=self.clear_form
        ).grid(row=0, column=3, padx=5)
        
        # Frame jos - Tabel
        table_frame = tk.Frame(main_container, bg=config.COLOR_WHITE, relief=tk.RAISED, borderwidth=2)
        table_frame.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(
            table_frame,
            text="Lista membrilor inregistrati",
            font=config.FONT_SUBTITLE,
            bg=config.COLOR_WHITE,
            fg=config.COLOR_PRIMARY
        ).pack(pady=10)
        
        # Treeview pentru afișare membri
        tree_container = tk.Frame(table_frame, bg=config.COLOR_WHITE)
        tree_container.pack(expand=True, fill=tk.BOTH, padx=15, pady=(0, 15))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Treeview
        columns = ("ID", "Nume", "Email", "Telefon", "Tip", "Activ")
        self.tree = ttk.Treeview(tree_container, columns=columns, show="headings", 
                                 yscrollcommand=scrollbar.set, height=10)
        
        # Configurare coloane
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nume", width=180, anchor="w")
        self.tree.column("Email", width=200, anchor="w")
        self.tree.column("Telefon", width=120, anchor="center")
        self.tree.column("Tip", width=100, anchor="center")
        self.tree.column("Activ", width=80, anchor="center")
        
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
    
    def refresh_table(self):
        """Reimproaspateaza tabelul cu membrii"""
        # Sterge toate inregistrarile
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Adauga membrii
        for member in self.members:
            self.tree.insert("", tk.END, values=(
                member["id"], member["nume"], member["email"], 
                member["telefon"], member["tip"], member["activ"]
            ))
    
    def on_tree_select(self, event):
        """Populare formular la selectarea unui membru din tabel"""
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item["values"]
            
            # Gaseste membrul in lista
            member = next((m for m in self.members if m["id"] == values[0]), None)
            if member:
                self.clear_form()
                self.name_entry.insert(0, member["nume"])
                self.email_entry.insert(0, member["email"])
                self.phone_entry.insert(0, member["telefon"])
                self.type_combo.set(member["tip"])
                self.active_var.set(member["activ"] == "Da")
    
    def clear_form(self):
        """Curata formularul"""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.type_combo.set("Student")
        self.active_var.set(True)
    
    def validate_email(self, email):
        """Validare simpla email"""
        return "@" in email and "." in email
    
    def add_member(self):
        """Adauga un membru nou"""
        # Validare campuri
        if not all([self.name_entry.get(), self.email_entry.get(), self.phone_entry.get()]):
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!", parent=self.root)
            return
        
        if not self.validate_email(self.email_entry.get()):
            messagebox.showerror("Eroare", "Email-ul introdus nu este valid!", parent=self.root)
            return
        
        # Adauga membru
        new_member = {
            "id": self.next_id,
            "nume": self.name_entry.get(),
            "email": self.email_entry.get(),
            "telefon": self.phone_entry.get(),
            "tip": self.type_var.get(),
            "activ": "Da" if self.active_var.get() else "Nu"
        }
        self.members.append(new_member)
        self.next_id += 1
        
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Succes", "Membrul a fost adaugat cu succes!", parent=self.root)
    
    def update_member(self):
        """Actualizeaza membrul selectat"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atentie", "Selectati un membru din tabel!", parent=self.root)
            return
        
        # Validare câmpuri
        if not all([self.name_entry.get(), self.email_entry.get(), self.phone_entry.get()]):
            messagebox.showerror("Eroare", "Toate câmpurile sunt obligatorii!", parent=self.root)
            return
        
        if not self.validate_email(self.email_entry.get()):
            messagebox.showerror("Eroare", "Email-ul introdus nu este valid!", parent=self.root)
            return
        
        # Actualizează
        item = self.tree.item(selected[0])
        member_id = item["values"][0]
        
        for member in self.members:
            if member["id"] == member_id:
                member["nume"] = self.name_entry.get()
                member["email"] = self.email_entry.get()
                member["telefon"] = self.phone_entry.get()
                member["tip"] = self.type_var.get()
                member["activ"] = "Da" if self.active_var.get() else "Nu"
                break
        
        self.refresh_table()
        self.clear_form()
        messagebox.showinfo("Succes", "Membrul a fost actualizat!", parent=self.root)
    
    def delete_member(self):
        """Sterge membrul selectat"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Atentie", "Selectati un membru din tabel!", parent=self.root)
            return
        
        result = messagebox.askyesno("Confirmare", 
                                     "Sigur doriti sa stergeti acest membru?", 
                                     parent=self.root)
        if result:
            item = self.tree.item(selected[0])
            member_id = item["values"][0]
            
            self.members = [m for m in self.members if m["id"] != member_id]
            
            self.refresh_table()
            self.clear_form()
            messagebox.showinfo("Succes", "Membrul a fost sters!", parent=self.root)

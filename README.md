# Biblioteca Digitala - Sistem de Management

## Descriere Proiect

Aplicatie software pentru managementul unei biblioteci digitale, dezvoltata in Python cu Tkinter pentru cursul de Proiectarea Interfetelor Utilizator.

## Caracteristici

### Functionalitati Principale

1. **Ecran de Autentificare** - Sistem securizat de login cu validare
2. **Meniu Principal** - Hub central de navigare catre toate modulele
3. **Gestionare Carti** - CRUD complet (Create, Read, Update, Delete) pentru carti
4. **Gestionare Membri** - Administrare membri bibliotecii cu validare email
5. **Test Grila** - Quiz interactiv cu 8 intrebari despre biblioteci
6. **Ecran Ajutor** - Manual detaliat, informatii despre aplicatie si contact

### Design si Interfata

- Interfata moderna si intuitiva
- Scheme de culori personalizate
- Fonturi profesionale
- Layout responsive si organizat
- Efecte hover pe butoane

### Elemente Grafice Utilizate

- **Butoane** - Pentru navigare si actiuni
- **Entry fields** - Pentru introducere date
- **Labels** - Pentru afisare text si titluri
- **Treeview/Table** - Pentru afisare date in format tabel
- **Radio buttons** - Pentru selectie raspunsuri quiz
- **Checkboxes** - Pentru status activ/inactiv
- **Combobox** - Pentru selectie din lista predefinita
- **ScrolledText** - Pentru manual lung
- **Frame-uri** - Pentru organizare layout

## Structura Proiectului

```
BibliotecaApp/

├── main.py                 # Fisier principal - punct de intrare
├── config.py              # Configuratii globale (culori, fonturi, setari)
├── login_screen.py        # Ecran de autentificare
├── main_menu.py           # Meniu principal
├── books_screen.py        # Gestionare carti
├── members_screen.py      # Gestionare membri
├── quiz_screen.py         # Test grila
├── help_screen.py         # Ecran ajutor
└── README.md             # Acest fisier
```

## Instalare si Rulare

### Cerinte

- Python 3.6 sau mai nou
- Tkinter

### Instalare

1. Descarca sau cloneaza proiectul:
```bash
git clone https://github.com/just-niko/UTM_ProiectareaInterfetelorUtilizator.git
cd BibliotecaApp
```

2. Verifica instalarea Python:
```bash
python --version
```

### Rulare

```bash
python main.py
```

## Credentiale de Autentificare

**Administrator:**
- Username: `admin`
- Parola: `admin123`

**Student:**
- Username: `student`
- Parola: `student123`

## Manual de Utilizare

### 1. Autentificare
- Introdu username si parola
- Apasa "AUTENTIFICARE" sau Enter

### 2. Navigare
- Foloseste butoanele din meniul principal
- Fiecare modul are un buton "Inapoi la Meniu"
- Deconectare din meniul principal

### 3. Gestionare Carti
- **Adaugare**: Completeaza formularul si apasa "Adauga"
- **Editare**: Selecteaza din tabel, modifica si apasa "Actualizeaza"
- **Stergere**: Selecteaza din tabel si apasa "Sterge"

### 4. Gestionare Membri
- Similar cu gestionarea cartilor
- Validare automata email
- Checkbox pentru status activ

### 5. Test Grila
- 8 intrebari cu 3 variante fiecare
- Evaluare automata la final
- Posibilitate de reluare


## Arhitectura

### Structura Orientata pe Obiecte

Fiecare ecran este implementat ca o clasa separata:
- `LoginScreen` - Autentificare
- `MainMenu` - Meniu principal
- `BooksScreen` - Gestionare carti
- `MembersScreen` - Gestionare membri
- `QuizScreen` - Test grila
- `HelpScreen` - Ajutor
- `BibliotecaApp` - Controller principal

### Pattern-uri Utilizate

- **Separare preocuparilor** - Fiecare modul are responsabilitatea sa
- **Callback functions** - Pentru navigare intre ecrane
- **Configuratie centralizata** - Toate setarile in `config.py`

## Cerinte Proiect

- Minimum 6 ecrane grafice interconectate
- Utilizare Python cu Tkinter
- Flux logic: Login -> Menu -> Module -> Back
- Nume student si grupa in bara de titlu
- Elemente grafice diverse: butoane, entry, liste, tabele, checkbox, radio, etc.
- Cod structurat in clase
- Cod comentat si documentat
- Personalizare interfata: culori, fonturi

## Informatii Curs

- **Curs**: Proiectarea Interfetelor Utilizator
- **Universitate**: Universitatea Titu Maiorescu
- **An**: 2026
- **Tehnologie**: Python + Tkinter
- **Student**: Isvoranu Nicolas-Radu
- **Grupa**: An 3 ID - Grupa 310
- **Profesor**: Prof. Mironela Pirnau

## Contact

- Email: nicolas.isvoranu@s.utm.ro
- GitHub: github.com/just-niko/UTM_ProiectareaInterfetelorUtilizator

## Licenta

Proiect educational - Toate drepturile rezervate 2026

---

Nota: Acest proiect este realizat in scop educational pentru cursul de Proiectarea Interfetelor Utilizator din cadrul Universitatii Titu Maiorescu - Facultatea de Informatica.

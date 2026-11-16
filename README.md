# 📝 Digital Notes Management System

## Project Overview

The **Digital Notes Management System** is a menu-driven Python
command-line application for managing notes. Users can add, view,
search, edit, and delete notes. Notes are stored in a text file named
`notes.txt`, so they remain available when the program is closed and
reopened.

## Features

-   **Add notes:** Create a note with a title and content.
-   **View notes:** Display all saved notes.
-   **Search notes:** Find notes by a keyword in the title or content
    (case-insensitive).
-   **Edit notes:** Update the content of a note using its ID.
-   **Delete notes:** Remove a note using its ID.
-   **Automatic IDs:** Generate sequential IDs such as `N1`, `N2`, and
    `N3`.
-   **Persistent storage:** Load notes at startup and save changes to
    `notes.txt`.

## Requirements

-   Python 3
-   No third-party Python packages are required.

## Project Structure

``` text
Digital-Notes-Management-System/
├── main.py       # Application source code
├── notes.txt     # Notes data file (created when notes are saved)
└── README.md     # Project documentation
```

## Getting Started

1.  Make sure Python 3 is installed.
2.  Place `main.py` in your project folder.
3.  Open a terminal in that folder.
4.  Run:

``` bash
python main.py
```

On some systems, you may need to use `python3 main.py` instead.

## Using the Application

When the program starts, it displays this menu:

``` text
======================================
     DIGITAL NOTES MANAGEMENT SYSTEM
======================================
1. Add Note
2. View All Notes
3. Search Notes
4. Edit Note
5. Delete Note
6. Exit
```

Enter the number for the action you want:

  Option   Action
  -------- -----------------------
  1        Add a note
  2        View all notes
  3        Search notes
  4        Edit a note's content
  5        Delete a note
  6        Exit the application

Each note has an ID, title, and content. IDs are generated
automatically.

## Data Storage

The application reads from and writes to `notes.txt`, located in the
same directory as `main.py`. Each note is stored on one line in this
format:

``` text
N1|Shopping List|Buy groceries
N2|Study Plan|Complete Python project
```

The three fields are separated by the pipe (`|`) character:

1.  Note ID
2.  Note title
3.  Note content

When adding a note, the title and content must not contain `|`, because
it is used as the field separator. A title cannot be empty. The
application skips blank lines and ignores records that do not contain
all three fields or have an empty ID or title.

## Python Concepts Demonstrated

-   Functions
-   Lists and dictionaries
-   File handling with `pathlib`
-   Exception handling
-   Loops and conditional statements
-   String operations
-   Basic CRUD operations (Create, Read, Update, Delete)

## Current Limitations

-   Notes are stored as plain text and are not encrypted.
-   Each note is stored on a single line.
-   Editing changes the note content; the title cannot currently be
    edited through the menu.
-   The file format uses `|` as a separator, so that character is not
    supported in newly entered titles or content.

## Possible Future Improvements

-   Add support for editing note titles.
-   Support multiline note content and a safer storage format such as
    JSON.
-   Add timestamps and note categories.
-   Add sorting and filtering options.
-   Add a graphical user interface.

## Author

Add your name here.

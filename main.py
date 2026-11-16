

# DIGITAL NOTES MANAGEMENT SYSTEM
# File: notes.py

from pathlib import Path

FILENAME = "notes.txt"
NOTES_PATH = Path(__file__).resolve().with_name(FILENAME)

# 1. LOAD NOTES FROM FILE


def load_notes():
    notes = []

    try:
        with NOTES_PATH.open("r", encoding="utf-8") as file:
            for line in file:
                cleaned = line.rstrip("\n")
                if cleaned.strip() == "":
                    continue

                parts = cleaned.split("|", 2)

                if len(parts) == 3:
                    note = {
                        "id": parts[0].strip(),
                        "title": parts[1].strip(),
                        "content": parts[2]
                    }
                    if note["id"] and note["title"]:
                        notes.append(note)

    except FileNotFoundError:
        pass

    return notes


# 2. SAVE NOTES TO FILE


def save_notes(notes):
    with NOTES_PATH.open("w", encoding="utf-8") as file:
        for note in notes:
            file.write(
                str(note.get("id", "")) + "|" +
                str(note.get("title", "")) + "|" +
                str(note.get("content", "")) + "\n"
            )


# 3. GENERATE UNIQUE NOTE ID


def generate_note_id(notes):
    max_id = 0

    for note in notes:
        note_id = str(note.get("id", "")).strip()

        if not note_id:
            continue

        try:
            if note_id.upper().startswith("N"):
                number = int(note_id[1:])
            else:
                number = int(note_id)
        except (TypeError, ValueError):
            continue

        if number > max_id:
            max_id = number

    return "N" + str(max_id + 1)


# 4. ADD NOTE


def add_note(notes):
    print("\n--- Add New Note ---")

    title = input("Enter note title: ").strip()

    if title == "":
        print("Title cannot be empty. Note not saved.")
        return

    if "|" in title:
        print("Title cannot contain | character.")
        return

    content = input("Enter note content: ").strip()

    if "|" in content:
        print("Content cannot contain | character.")
        return

    note_id = generate_note_id(notes)

    new_note = {
        "id": note_id,
        "title": title,
        "content": content
    }

    notes.append(new_note)

    save_notes(notes)

    print("Note saved. ID:", note_id, "|", title)



# 5. VIEW ALL NOTES


def view_notes(notes):
    print("\n--- All Notes ---")

    if len(notes) == 0:
        print("No notes found.")
        return

    for note in notes:
        print(
            note["id"] + " | " +
            note["title"] + " | " +
            note["content"]
        )

# 6. SEARCH NOTES

def search_notes(notes):
    print("\n--- Search Notes ---")

    keyword = input("Enter search keyword: ").strip().lower()

    if keyword == "":
        print("Search keyword cannot be empty.")
        return

    found = False

    for note in notes:
        title = note["title"].lower()
        content = note["content"].lower()

        if keyword in title or keyword in content:
            print(
                note["id"] + " | " +
                note["title"] + " | " +
                note["content"]
            )
            found = True

    if not found:
        print("No matching notes found.")


# ------------------------------------------
# 7. EDIT NOTE
# ------------------------------------------

def edit_note(notes):
    print("\n--- Edit Note ---")

    note_id = input("Enter Note ID to edit: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:

            new_content = input("Enter new content: ")

            note["content"] = new_content

            save_notes(notes)

            print("Note", note_id, "updated.")
            return

    print("Note ID does not exist.")


# ------------------------------------------
# 8. DELETE NOTE
# ------------------------------------------

def delete_note(notes):
    print("\n--- Delete Note ---")

    note_id = input("Enter Note ID to delete: ").strip().upper()

    for note in notes:
        if note["id"] == note_id:

            notes.remove(note)

            save_notes(notes)

            print(
                "Note", note_id,
                "deleted. Notes left:", len(notes)
            )
            return

    print("Note ID does not exist.")


# ------------------------------------------
# 9. DISPLAY MENU
# ------------------------------------------

def show_menu():
    print("\n======================================")
    print("     DIGITAL NOTES MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Note")
    print("2. View All Notes")
    print("3. Search Notes")
    print("4. Edit Note")
    print("5. Delete Note")
    print("6. Exit")



# 10. MAIN FUNCTION


def main():

    notes = load_notes()

    while True:

        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_note(notes)

        elif choice == "2":
            view_notes(notes)

        elif choice == "3":
            search_notes(notes)

        elif choice == "4":
            edit_note(notes)

        elif choice == "5":
            delete_note(notes)

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# 11. PROGRAM EXECUTION


if __name__ == "__main__":
    main()


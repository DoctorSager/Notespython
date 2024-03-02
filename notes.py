import json
import os
from datetime import datetime

def create():
    notes = load_notes()
    new_note = {}
    new_note["id"] = len(notes) + 1
    new_note["title"] = input("Название заметки: ")
    new_note["body"] = input("Текст заметки: ")
    new_note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append(new_note)
    save_notes(notes)
    print("Заметка успешно создана!")
    
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []

def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['date']}")
        
def edit_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["body"] = input("Введите новый текст заметки: ")
            note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с таким id не найдена.")

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена!")




while True:
    
    print("\n Меню")
    print("\n1. Создать")
    print("2. Список")
    print("3. Редактировать")
    print("4. Удалить")
    print("5. Выход")
    
    userInput = input("\n Выберете пункт: ")
    
    if userInput == '1':
        create()
    elif userInput == '2':
        list_notes()
    elif userInput == '3':
        note_id = int(input("Введите id заметки для редактирования: "))
        edit_note(note_id)
    elif userInput == '4':
        note_id = int(input("Введите id заметки для удаления: "))
        delete_note(note_id)
    elif userInput == '5':
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

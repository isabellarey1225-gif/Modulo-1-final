import json
import os

# File to save students
FILE_NAME = "students.json"

# Load students from file (if exists)
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

# Validate class (6th to 11th)
def valid_class(cls):
    return cls.isdigit() and 6 <= int(cls) <= 11

# Add a new student
def add_student(students):
    print("\n--- Agregar Nuevo Estudiante ---")
    name = input("Ingresa el nombre del estudiante: ").strip()
    if not name:
        print("¡El nombre no puede estar vacío!")
        return
    
    age = input("Ingresa la edad: ").strip()
    if not age.isdigit() or int(age) < 10 or int(age) > 20:
        print("¡La edad debe estar entre 10 y 20!")
        return
    
    cls = input("Ingresa la clase (6 a 11): ").strip()
    if not valid_class(cls):
        print("¡La clase debe estar entre 6 y 11!")
        return
    
    # Check if student already exists
    for student in students:
        if student["nombre"].lower() == name.lower():
            print("¡El estudiante ya existe!")
            return
    
    students.append({
        "nombre": name,
        "edad": int(age),
        "clase": f"{cls}th"
    })
    save_students(students)
    print(f"Estudiante {name} agregado exitosamente!")

# Display all students
def view_students(students):
    if not students:
        print("\n¡No hay estudiantes registrados aún!")
        return
    
    print("\n" + "="*50)
    print(f"{'No.':<4} {'Nombre':<20} {'Edad':<6} {'Clase':<8}")
    print("="*50)
    for i, student in enumerate(students, 1):
        print(f"{i:<4} {student['name']:<20} {student['age']:<6} {student['class']:<8}")
    print("="*50)

# Search student by name
def search_student(students):
    name = input("\nIngresa el nombre a buscar: ").strip().lower()
    found = [s for s in students if name in s["name"].lower()]
    
    if not found:
        print("¡No se encontró ningún estudiante!")
        return
    
    print("\nEstudiantes encontrados:")
    for s in found:
        print(f"→ {s['name']}, Edad: {s['age']}, Clase: {s['class']}")

# Delete a student
def delete_student(students):
    view_students(students)
    if not students:
        return
    
    try:
        idx = int(input("\nIngresa el número del estudiante a eliminar: ")) - 1
        if 0 <= idx < len(students):
            removed = students.pop(idx)
            save_students(students)
            print(f"Eliminado: {removed['name']}")
        else:
            print("Número inválido!")
    except ValueError:
        print("Por favor ingresa un número válido!")

# Main menu
def main():
    students = load_students()
    
    while True:
        print("\n SISTEMA DE REGISTRO DE ESTUDIANTES ")
        print("1. Agregar estudiante")
        print("2. Ver todos los estudiantes")
        print("3. Buscar estudiante")
        print("4. Borrar estudiante")
        print("5. Salir")
        
        choice = input("\nElige una opción (1-5): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("¡Adiós! ")
            break
        else:
            print("opcion invalida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
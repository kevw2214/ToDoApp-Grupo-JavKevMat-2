#main.py
from tasl_model import TASLModel

def main():
    task = TASLModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")

if __name__ == "__main__":
    main()
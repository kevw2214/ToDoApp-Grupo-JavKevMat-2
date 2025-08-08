#main.py
from tasl_model import TASLModel

def main():
    task = TASLModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada: {task.is_completed()}")

if __name__ == "__main__":
    main()
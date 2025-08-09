#main.py
from tasl_model import TASLModel

def main():
    task = TASLModel("Estudiar para el examen")
    print(f"Tarea creada: {task.get_task_name()}")
    task.mark_as_complete()
    print(f"Tarea completada: {task.is_completed()}")
    task.set_done()
    print(f"Tarea completada: {task.is_completed()}")
    task.delete_task()
    print (f" Tarea completada: {task.is_done()}")
    task.remove_task()
    print(f"Tarea eliminada: {task.get_task_name()}")
    
if __name__ == "__main__":
    main()
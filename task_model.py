# task_model.py
class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.is_completed = False

    def get_task_name(self):
        return self.task_name
    
    def delete_task(self):
        self.task_name = None
        self.is_completed = False

    def is_completed(self):
        return self.is_completed
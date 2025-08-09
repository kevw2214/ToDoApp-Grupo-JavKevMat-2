# task_model.py
class TaskModel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.is_completed = False

    def get_task_name(self):
        return self.task_name

    def mark_as_complete(self):
        self.is_completed = True
    
    def is_completed(self):
        return self.is_completed
    
    def delete_task(self):
        self.task_name = None
        self.is_completed = False
    
    def set_done (self):
        self.is_completed = True

    def remove_task (self):
        self.task_name = None
        self.is_complete = False
    

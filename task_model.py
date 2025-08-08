# task_model.py
class TASLModel:
    def __init__(self, task_name):
        self.task_name = task_name

    def get_task_name(self):
        return self.task_name

    def mark_as_complete(self):
        self.is_completed = True
    
    def is_completed(self):
        return self.is_completed

        
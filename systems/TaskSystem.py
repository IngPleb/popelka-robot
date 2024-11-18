from model.task import Task
from systems.DriveSystem import DriveSystem


class TaskSystem:
    def __init__(self, drive_system: DriveSystem):
        self.drive_system = drive_system
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def execute_tasks(self):
        for task in self.tasks:
            if task.action == 'move_forward':
                if task.use_correction:
                    self.drive_system.move_distance(task.value)
                else:
                    self.drive_system.move_distance_without_correction(task.value)
            elif task.action == 'rotate':
                self.drive_system.rotate_angle(task.value)
            elif task.action == 'custom':
                # Custom task for that redneck engineering situations
                if 'function' in task.kwargs:
                    task.kwargs['function']()

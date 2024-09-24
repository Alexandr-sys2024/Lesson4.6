import tkinter as tk
from tkinter import simpledialog

class KanbanBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban Board")

        # Колонки для Kanban доски
        self.columns = ["To Do", "In Progress", "Testing", "Done"]
        self.frames = {}
        self.tasks = {column: [] for column in self.columns}

        # Создание фреймов для каждой колонки
        for index, column in enumerate(self.columns):
            frame = tk.Frame(self.root, bg='lightgrey', width=250, height=400, padx=5, pady=5)
            frame.grid(row=0, column=index, padx=10, pady=10)
            label = tk.Label(frame, text=column, bg='grey', width=20, height=2)
            label.pack(pady=5)
            self.frames[column] = frame

        # Кнопка для добавления новой задачи
        add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_task_button.grid(row=1, column=1, sticky="ew")

    def add_task(self):
        task_name = simpledialog.askstring("Task", "Enter task name:")
        if task_name:
            self.add_task_to_column(task_name, "To Do")

    def add_task_to_column(self, task_name, column):
        if task_name and column in self.columns:
            task_frame = tk.Frame(self.frames[column], bg='white', pady=5)
            task_frame.pack(fill=tk.X, padx=5, pady=5)
            task_label = tk.Label(task_frame, text=task_name, bg='white')
            task_label.pack(side=tk.LEFT, padx=10)
            move_button = tk.Button(task_frame, text=">", command=lambda: self.move_task(task_name, column))
            move_button.pack(side=tk.RIGHT)
            self.tasks[column].append((task_name, task_frame))

    def move_task(self, task_name, current_column):
        index = self.columns.index(current_column)
        current_tasks = self.tasks[current_column]
        for task, frame in current_tasks:
            if task == task_name:
                frame.destroy()
                current_tasks.remove((task, frame))
                new_column = self.columns[(index + 1) % len(self.columns)]
                self.add_task_to_column(task_name, new_column)
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = KanbanBoard(root)
    root.mainloop()

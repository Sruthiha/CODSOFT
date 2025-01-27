import tkinter as tk
from tkinter import messagebox, Scrollbar, Frame
import json
import os

class ToDoListApp:
    def __init__(self, root, filename='tasks.json'):
        self.root = root
        self.root.title("To-Do List 📝") 
        self.root.geometry("600x500") 
        self.root.minsize(400, 400)  
        self.filename = filename
        self.tasks = self.load_tasks()
        title_frame = Frame(self.root, bg='lightblue', bd=5, relief=tk.RAISED)
        title_frame.pack(pady=9, padx=10)
        self.title_label = tk.Label(title_frame, text="To-Do List 📝", font=('Comic Sans MS', 24, 'bold'), fg='purple', bg='lightblue')
        self.title_label.pack(pady=9)
        frame = Frame(self.root)
        frame.pack(pady=10)
        self.task_entry = tk.Entry(frame, width=40, font=('Arial', 20)) 
        self.task_entry.grid(row=0, column=0, padx=10)
        self.add_task_button = tk.Button(frame, text="Add Task", command=self.add_task, bg='lightgreen', font=('Arial', 16))  
        self.add_task_button.grid(row=1, column=0, pady=5)  

        list_frame = Frame(self.root)
        list_frame.pack(pady=20)
        self.tasks_listbox = tk.Listbox(list_frame, width=70, height=10, font=('Arial', 16), selectmode=tk.SINGLE)  
        self.tasks_listbox.pack(side=tk.LEFT)
        self.scrollbar = Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg='salmon', font=('Arial', 14))  
        self.remove_task_button.pack(pady=10)
        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg='lightblue', font=('Arial', 14))  
        self.update_task_button.pack(pady=5)
        self.complete_task_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_as_completed, bg='lightyellow', font=('Arial', 14))  
        self.complete_task_button.pack(pady=5)

        self.load_tasks_to_listbox()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def load_tasks_to_listbox(self):
        self.tasks_listbox.delete(0, tk.END)  
        for task in self.tasks:
            checkbox = "☑" if task['completed'] else "☐"
            display_text = f"{checkbox} {task['description']}"
            self.tasks_listbox.insert(tk.END, display_text)

    def add_task(self):
        task_description = self.task_entry.get()
        if task_description:
            task = {'description': task_description, 'completed': False}
            self.tasks.append(task)
            self.load_tasks_to_listbox()  
            self.save_tasks()
            self.task_entry.delete(0, tk.END)  
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.load_tasks_to_listbox()  
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            new_description = self.task_entry.get()
            if new_description:
                self.tasks[selected_task_index]['description'] = new_description
                self.load_tasks_to_listbox()  
                self.save_tasks()
                self.task_entry.delete(0, tk.END)  
            else:
                messagebox.showwarning("Warning", "You must enter a new task description.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def mark_as_completed(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks[selected_task_index]['completed'] = True
            self.load_tasks_to_listbox()  
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to mark as completed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

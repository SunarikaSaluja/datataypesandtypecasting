import tkinter as tk
from tkinter import ttk, messagebox

class TypeCastingApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Data Types and Type Casting")

        # Input label and field
        tk.Label(root, text="Enter a value:", font=("Arial", 14)).pack(pady=5)
        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=5)

        # Dropdown to choose target data type
        tk.Label(root, text="Convert to:", font=("Arial", 14)).pack(pady=5)
        self.target_type = ttk.Combobox(root, font=("Arial", 14), state="readonly")
        self.target_type['values'] = ('int', 'float', 'bool', 'str')
        self.target_type.current(0)
        self.target_type.pack(pady=5)

        # Button to process
        self.check_button = tk.Button(root, text="Detect & Convert", font=("Arial", 14), command=self.process)
        self.check_button.pack(pady=10)

        # Output labels
        self.original_type_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.original_type_label.pack()

        self.converted_value_label = tk.Label(root, text="", font=("Arial", 12), fg="green")
        self.converted_value_label.pack()

    def process(self):
        value = self.entry.get()
        target = self.target_type.get()
        original_type = self.detect_type(value)
        self.original_type_label.config(text=f"Original Type: {original_type}")

        try:
            if target == 'int':
                result = int(float(value))  # handles strings like "12.0"
            elif target == 'float':
                result = float(value)
            elif target == 'bool':
                result = bool(eval(value))
            elif target == 'str':
                result = str(value)
            self.converted_value_label.config(text=f"Converted Value: {result} (type: {type(result)._name_})")
        except Exception as e:
            self.converted_value_label.config(text=f"Conversion Error: {e}")

    def detect_type(self, value):
        try:
            if value.lower() in ['true', 'false']:
                return 'bool'
            elif value.lower() == 'none':
                return 'NoneType'
            elif '.' in value:
                float(value)
                return 'float'
            else:
                int(value)
                return 'int'
        except ValueError:
            return 'str'

if _name_ == "_main_":
    root = tk.Tk()
    app = TypeCastingApp(root)
    root.mainloop()
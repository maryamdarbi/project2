import tkinter as tk
from tkinter import messagebox
from calculator_logic import CalculatorLogic
from history_manager import HistoryManager


class CalculatorGUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.logic = CalculatorLogic()
        self.history_manager = HistoryManager()

        self.root.title("iPhone-Like Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="black")
        self.expression_entry = tk.Entry(
            self.root,
            font=("Arial", 24),
            justify="right",
            borderwidth=0,
            relief="solid",
            bg="black",
            fg="white",
        )
        self.expression_entry.pack(fill=tk.BOTH, padx=10, pady=20, ipady=10)

        self.button_frame = tk.Frame(self.root, bg="black")
        self.button_frame.pack()

        buttons = [
            ["C", "", "", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""],
        ]

        self.create_buttons(buttons)

        # History display
        self.history_text = tk.Text(
            self.root,
            height=6,
            font=("Arial", 12),
            bg="black",
            fg="white",
            borderwidth=0,
            state="disabled",
        )
        self.history_text.pack(fill=tk.BOTH, padx=10, pady=10)
        self.load_history()

    def create_buttons(self, buttons):
        for row in buttons:
            frame = tk.Frame(self.button_frame, bg="black")
            frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            for button in row:
                if button:
                    btn = tk.Button(
                        frame,
                        text=button,
                        font=("Arial", 18),
                        bg="gray" if button.isdigit() else "orange",
                        fg="white",
                        command=lambda b=button: self.on_button_click(b),
                        borderwidth=0,
                        padx=20,
                        pady=20,
                    )
                    btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def on_button_click(self, button: str):
        if button == "=":
            expression = self.expression_entry.get()
            result = self.logic.calculate(expression)
            self.history_manager.save_to_history(expression, result)
            self.update_history(expression, result)
            self.expression_entry.delete(0, tk.END)
            self.expression_entry.insert(0, result)
        elif button == "C":
            self.expression_entry.delete(0, tk.END)
        else:
            self.expression_entry.insert(tk.END, button)

    def load_history(self):
        history = self.history_manager.load_history()
        for entry in history:
            self.history_text.configure(state="normal")
            self.history_text.insert(tk.END, entry)
            self.history_text.configure(state="disabled")

    def update_history(self, expression: str, result: str):
        self.history_text.configure(state="normal")
        self.history_text.insert(tk.END, f"{expression} = {result}\n")
        self.history_text.configure(state="disabled")
        self.history_text.see(tk.END)

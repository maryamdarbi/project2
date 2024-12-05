class HistoryManager:
    def __init__(self, filename: str = "history.txt"):
        self.filename = filename

    def load_history(self) -> list[str]:
        """Loads the calculation history from a file."""
        try:
            with open(self.filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def save_to_history(self, expression: str, result: str):
        """Saves a new calculation to the history file."""
        with open(self.filename, "a") as file:
            file.write(f"{expression} = {result}\n")

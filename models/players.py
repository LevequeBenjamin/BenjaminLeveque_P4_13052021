"""Define the players."""


class Player:
    """Player class."""

    def __init__(self, last_name, first_name, birth_date, selected_sex):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = selected_sex
        self.ladder = 0
        
    def __str__(self):
        return {"last_name": self.last_name, "first_name": self.first_name, "birth_date": self.birth_date, "sex": self.sex, "ladder": self.ladder}

    def selected_sex(self):
        pass

    def save_player(self):
        """Docstrings."""
        pass

    def update_player(self):
        """Docstrings."""
        pass

    def delete_player(self):
        """Docstrings."""
        pass

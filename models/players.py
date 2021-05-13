"""Define the players."""


class Player:
    """Player class."""

    def __init__(self, last_name, first_name, date_of_birth, selected_sex):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.sex = selected_sex
        self.ladder = 0

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

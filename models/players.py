"""Define the players."""


class Player:
    """Player class."""

    def __init__(self, last_name, first_name, birth_date, selected_sex, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = selected_sex
        self.elo = elo
        self.score = 0
        self.ladder = 0

    def __str__(self):
        return f"nom: {self.last_name}, prénom: {self.first_name}"
    
    @property
    def serialize(self):
        """Serialize Player

        Returns:
            dict: a dictionary of Player
        """
        return {"last_name": self.last_name, "first_name": self.first_name,
                "birth_date": self.birth_date, "sex": self.sex,
                "elo": int(self.elo), "score": self.score,
                "ladder": self.ladder}

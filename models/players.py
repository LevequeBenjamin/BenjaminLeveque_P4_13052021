"""Define the players."""


class Player:
    """Player class."""

    def __init__(self, last_name, first_name, birth_date, sex, elo):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.elo = elo

    def __str__(self):
        return f"nom: {self.last_name}, prénom: {self.first_name}"

    @property
    def serialize_player(self):
        """Serialize Player

        Returns:
            dict: a dictionary of Player
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
        }


class Participant(Player):
    """Docstrings."""

    def __init__(self, last_name, first_name, birth_date, sex, elo):
        self.id = None
        self.score = 0
        self.ladder = 0
        Player.__init__(self, last_name, first_name, birth_date, sex, elo)

    def __str__(self):
        return f"nom: {self.last_name}, prénom: {self.first_name}"

    @property
    def serialize_player(self):
        """Serialize Participant

        Returns:
            dict: a dictionary of Participant
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
        }
    
    def add_id(self, id):
        self.id = id
    
    def add_score(self, score):
        self.score = score
    
    def add_ladder(self, ladder):
        self.ladder = ladder  

    @property
    def get_id(self):
        return self.id

    @property
    def serialize(self):
        """Serialize Participant

        Returns:
            dict: a dictionary of Participant
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
            "score": self.score,
            "ladder": self.ladder,
        }
        
    @property
    def get_elo(self):
        return self.elo

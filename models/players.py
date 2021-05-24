"""Define the players."""


class Player:
    """Player class."""

    def __init__(self, last_name, first_name, birth_date, sex, elo):
        """[summary]

        Args:
            last_name ([type]): [description]
            first_name ([type]): [description]
            birth_date ([type]): [description]
            sex ([type]): [description]
            elo ([type]): [description]
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.elo = elo

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return f"{self.last_name}, {self.first_name}"

    def serialize(self):
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

    def update_elo(self, elo):
        """[summary]

        Args:
            elo ([type]): [description]
        """
        self.elo = elo


class Participant(Player):
    """Docstrings."""

    def __init__(self, last_name, first_name, birth_date, sex, elo):
        """[summary]

        Args:
            last_name ([type]): [description]
            first_name ([type]): [description]
            birth_date ([type]): [description]
            sex ([type]): [description]
            elo ([type]): [description]
        """
        self.id = None
        self.score = 0
        self.ladder = 0
        Player.__init__(self, last_name, first_name, birth_date, sex, elo)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return f"{self.last_name}, {self.first_name}"

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
            "id": self.id
        }

    def serialize_player_match(self):
        return {"last_name": self.last_name, "first_name": self.first_name, "id": self.id}

    def add_id(self, id):
        """[summary]

        Args:
            id ([type]): [description]
        """
        self.id = id

    def add_score(self, score):
        """[summary]

        Args:
            score ([type]): [description]
        """
        self.score += score

    def add_ladder(self, ladder):
        """[summary]

        Args:
            ladder ([type]): [description]
        """
        self.ladder = ladder

    def get_id(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.id

    def get_elo(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.elo

    def get_score(self):
        return self.score

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name

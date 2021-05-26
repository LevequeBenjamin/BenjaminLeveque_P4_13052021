"""Define the players."""


class Player:
    """It is a class allowing to create a Player."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self, last_name: str, first_name: str, birth_date: str, sex: str, elo: int
    ) -> None:
        """Inits Player.

        Args:
            last_name (string): contains the last name entered by the user,
            first_name (string): contains the first name entered by the user,
            birth_date (string): contains the last birth of date entered by the user,
            sex (string): contains the sex entered by the user,
            elo (int): contains the elo classement entered by the user,
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.sex = sex
        self.elo = elo

    def __str__(self) -> str:
        """Method used to display a confirmation that the player has been
        added to the database.

        Returns:
            string: return a message for the user.
        """
        return "Le joueur {} {} a bien été ajouté !".format(
            self.last_name, self.first_name
        )

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def serialize_player(self) -> dict:
        """Method allowing to serialize a player before saving
        it in the table PLAYERS.

        Returns:
            a dictionary of Player:
                "last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "sex": self.sex,
                "elo": self.elo,
        }
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
        }

    def update_elo(self, elo: None) -> None:
        """Method allowing to modify the elo classification of a Player.

        Args:
            elo (int): contains elo classement entered by the user.
        """
        self.elo = elo


class Participant(Player):
    """It is a class allowing to create an inheritance from the Player class."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(
        self, last_name: str, first_name: str, birth_date: str, sex: str, elo: int
    ) -> None:
        """Inits Participant.

        Args:
            last_name (string): contains the last name entered by the user,
            first_name (string): contains the first name entered by the user,
            birth_date (string): contains the last birth of date entered by the user,
            sex (string): contains the sex entered by the user,
            elo (int): contains the elo classement entered by the user,
        """
        self.player_id = None
        self.score = 0
        self.ladder = 0
        self.opponents = []
        Player.__init__(self, last_name, first_name, birth_date, sex, elo)

    def __str__(self) -> str:
        """Method used to display the last name and first name of the player.

        Returns:
            string: return a message for the user.
        """
        return "{} {}".format(self.last_name, self.first_name)

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def get_last_name(self) -> str:
        """Return the player last name.

        Returns:
            Participant.last_name (string): contains the last name entered by the user.
        """
        return self.last_name

    @property
    def get_first_name(self) -> str:
        """Return the player first name.

        Returns:
            Participant.first_name (string): contains the first name entered by the user.
        """
        return self.first_name

    @property
    def get_id(self) -> int:
        """Return the player id.

        Returns:
            Participant.player_id (int): contains the id of the player taken from the database.
        """
        return self.player_id

    @property
    def get_birth_date(self):
        return self.birth_date

    @property
    def get_sex(self):
        return self.sex

    @property
    def get_elo(self) -> int:
        """Return the player elo.

        Returns:
            Participant.elo (int): contains the elo classement entered by the user.
        """
        return self.elo

    @property
    def get_score(self) -> float:
        """Return the player score.

        Returns:
            Participant.score (float): contains the total tournament score added
            up during the tournament.
        """
        return self.score

    @property
    def get_ladder(self) -> int:
        """Return the player ladder.

        Returns:
            Participant.ladder (int): contains the player ranking added at the end of the tournament.
        """
        return self.ladder

    @property
    def get_opponents(self) -> list:
        """Return the player opponents.

        Returns:
            Participant.opponents (list): contains all the opponents that the player encounters
            during the tournament.
        """
        return self.opponents

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def serialize(self) -> dict:
        """Method allowing to serialize a player before saving
        it in the table TOURNAMENTS.

        Returns:
            a dictionary of Player:
                "last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "sex": self.sex,
                "elo": self.elo,
                "score": self.score,
                "ladder": self.ladder,
                "id": self.player_id,
                "opponents": self.opponents,
        }
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
            "score": self.score,
            "ladder": self.ladder,
            "id": self.player_id,
            "opponents": self.opponents,
        }

    def serialize_player(self) -> dict:
        """Method allowing to serialize a player before saving
        it in the table PLAYERS.

        Returns:
            a dictionary of Player:
                "last_name": self.last_name,
                "first_name": self.first_name,
                "birth_date": self.birth_date,
                "sex": self.sex,
                "elo": self.elo,
        }
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "sex": self.sex,
            "elo": self.elo,
        }

    def serialize_player_match(self) -> dict:
        """Method allowing to serialize a player before create a instance of Match.

        Returns:
            a dictionary of Player:
                "last_name": self.last_name,
                "first_name": self.first_name,
                "id": self.player_id,
        }
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "id": self.player_id,
        }

    def add_id(self, player_id: int) -> None:
        """Method used to add the player id.

        Args:
            player_id (int): contains the id of the player taken from the database.
        """
        self.player_id = player_id

    def add_score(self, score: float) -> None:
        """Method used to add up the player's scores.

        Args:
            score (float): contains the score entered by the user.
        """
        self.score += score

    def add_ladder(self, ladder: int) -> None:
        """[summary]

        Args:
            ladder ([type]): [description]
        """
        self.ladder = ladder

    def append_list_opponents(self, player_id: int) -> None:
        """Method used to add opponent id to the opponents list.

        Args:
            player_id (int): contains the id of the player taken from the database.
        """
        self.opponents.append(player_id)

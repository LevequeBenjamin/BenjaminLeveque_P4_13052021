# pylint: disable=too-many-arguments
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
        return f"Le joueur {self.last_name} {self.first_name} a bien été ajouté !"

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
        super().__init__(last_name, first_name, birth_date, sex, elo)

    def __str__(self) -> str:
        """Method used to display the last name and first name of the player.

        Returns:
            string: return a message for the user.
        """
        return f"{self.last_name} {self.first_name}"

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

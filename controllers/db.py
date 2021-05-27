"""Define the db controller."""

# librairies
import logging
from tinydb import TinyDB, Query

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# database
DB = TinyDB("db/db.json")
USER = Query()
PLAYERS = DB.table("PLAYERS")
TOURNAMENTS = DB.table("TOURNAMENTS")


class DbControllerlPlayer:
    """DbControllerPlayer controller."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits DbControllerPlayer"""
        self.players = PLAYERS

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def get_players(self) -> list:
        """Returns the list of players in the PLAYERS table

        Returns:
            DbControllerPlayer.players (list): a players list
        """
        return self.players

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def get_id_player(self, last_name: str, first_name: str) -> int:
        """Method used to find the player id in the PLAYERS table

        Args:
            last_name (str): contains the last name entered by the user,
            first_name (str): contains the first name entered by the user,

        Returns:
            player_found.doc_id (int): a player id in the PLAYERS table
        """
        try:
            player_found = self.search_table_players(last_name, first_name)
            return player_found.doc_id
        except Exception as err:
            logger.error("Oops! %s :", err)

    def search_table_players(self, last_name: str, first_name: str) -> dict:
        """Method used to check if a player exist in the db.

        Args:
            last_name (str): contains the last name entered by the user,
            first_name (str): contains the first name entered by the user,

        Returns:
            player_found (dict): a player found in the bd
        """
        for player in self.players:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                player_found = player
                return player_found
        return None

    def search_table_players_with_id(self, player_id: id) -> dict:
        """Method used to check if a player exist in the database.

        Args:
            player_id (int): contains the player id.

        Returns:
            PLayer : return player if is
            found in the bd
        """
        for player in self.players:
            if player.doc_id == player_id:
                player_found = player
                return player_found
        return None

    def update_player(self, player: object, player_id: int) -> None:
        """Method used to modify a player in the database.

        Args:
            player (PLayer): a Player instance
            player_id (int): contains the player id.
        """
        try:
            self.players.update(player.serialize_player(), doc_ids=[player_id])
        except Exception as err:
            logger.error("Oops! %s :", err)

    def save_table_players(self, player: object) -> None:
        """Method used to save player in database.

        Args:
            player (Player): a Player instance
        """
        try:
            self.players.insert(player.serialize_player())
        except Exception as err:
            logger.error("Oops! %s :", err)

    # def update_table_players(self, player):
    #     """[summary]

    #     Args:
    #         player ([type]): [description]
    #     """
    #     try:
    #         self.players.update(player.serialize(), doc_ids=[player.get_id])
    #     except Exception as err:
    #         logger.error("Oops! %s :", err)


class DbControllerTournament:
    """DbControllerTournament controller."""

    # - - - - - - - - - - - #
    # special methods       #
    # - - - - - - - - - - - #

    def __init__(self):
        """Inits DbControllerTournament"""
        self.tournaments = TOURNAMENTS

    # - - - - - - - - - - - #
    # properties            #
    # - - - - - - - - - - - #

    @property
    def get_tournois(self):
        """Returns the list of tournaments in the TOURNAMENTS table

        Returns:
            DbControllerTournament.tournaments (list): a tournament list
        """
        return self.tournaments

    # - - - - - - - - - - - #
    # methods               #
    # - - - - - - - - - - - #

    def get_id_tournament(self, name: str) -> int:
        """Method used to find the tournament id in the PLAYERS table

        Args:
            name (string): contains the name entered by the user.

        Returns:
            tournament_found.doc_id (int): a tournament id in the PLAYERS table
        """
        tournament_found = self.search_table_tournaments(name)
        if tournament_found:
            return tournament_found.doc_id
        return None

    def search_table_tournaments(self, name: str) -> dict:
        """Method used to check if a tournament exist in the db.

        Args:
            name (string): contains the name entered by the user.

        Returns:
            tournament_found (dict) : contains the tournament found in the bd
        """
        tournament_found = ""
        for tournament in self.tournaments:
            if tournament["name"] == name:
                tournament_found = tournament
        return tournament_found

    def search_table_tournament_with_id(self, tournament_id: int) -> dict:
        """Method used to check if a tournament exist in the db.

        Args:
            tournament_id (int): contains the tournament id

        Returns:
            tournament_found (dict) : contains the tournament found in the bd
        """
        tournament_found = ""
        for tournament in self.tournaments:
            if tournament.doc_id == tournament_id:
                tournament_found = tournament
        return tournament_found

    def save_table_tournament(self, tournament: object) -> None:
        """Method used to save tournament in database.

        Args:
            tournament (Tournament): a Tournament instance
        """
        try:
            self.tournaments.insert(tournament.serialize())
        except Exception as err:
            logger.error("Oops! %s :", err)

    def update_table_tournament(self, tournament: object) -> None:
        """Method used to modify a tournament in the database

        Args:
            tournament (Tournament): a Tournament instance
        """
        try:
            self.tournaments.update(
                tournament.serialize(), doc_ids=[tournament.tournament_id]
            )
        except Exception as err:
            logger.error("Oops! %s :", err)

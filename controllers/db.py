"""Define the db controller."""

# librairies
from tinydb import TinyDB, Query
import logging

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# database
DB = TinyDB("db/db.json")
USER = Query()
PLAYERS = DB.table("PLAYERS")
TOURNAMENTS = DB.table("TOURNAMENTS")


class DbControllerlPlayer:
    """DbCtrlPlayer controller."""
    
    def get_players(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return PLAYERS

    def get_id_player(self, last_name, first_name):
        """[summary]

        Args:
            last_name ([type]): [description]
            first_name ([type]): [description]

        Returns:
            [type]: [description]
        """
        player_found = self.search_table_players(last_name, first_name)
        if player_found:
            return player_found.doc_id
        return None

    def check_table_players(self, last_name, first_name):
        """Check if a player exist in the db.

        Args:
            last_name (str): player lastname
            first_name (str): player firstname

        Returns:
            Bolean: return True if a player is
            found in the db or False
        """
        for player in PLAYERS:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                return True
        return False

    def search_table_players(self, last_name, first_name):
        """Check if a player exist in the db.

        Args:
            last_name (str): player lastname
            first_name (str): player firstname

        Returns:
            PLayer : return player if is
            found in the bd
        """
        player_found = ""
        for player in PLAYERS:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                player_found = player
        return player_found

    def search_table_players_with_id(self, id):
        """Check if a player exist in the db.

        Args:
            last_name (str): player lastname
            first_name (str): player firstname

        Returns:
            PLayer : return player if is
            found in the bd
        """
        player_found = ""
        for player in PLAYERS:
            if player.doc_id == id:
                player_found = player
        return player_found
    
    def update_player(self, player, id):
        try:
            PLAYERS.update(player.serialize(), doc_ids=[id])
        except Exception as err:
            logger.error("Oops! %s :", err)

    def save_table_players(self, player):
        """Save player in database.

        Args:
            player (Object): Player instance
        """
        try:
            PLAYERS.insert(player.serialize())
        except Exception as err:
            logger.error("Oops! %s :", err)

    def update_table_players(self, player):
        try:
            PLAYERS.update(player.serialize(), doc_ids=[player.get_id()])
        except Exception as err:
            logger.error("Oops! %s :", err)


class DbControllerTournament:
    """[summary]
    """

    def get_tournois(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return TOURNAMENTS
    
    def get_id_tournament(self, name):
        """[summary]

        Args:
            name ([type]): [description]

        Returns:
            [type]: [description]
        """
        tournament_found = self.search_table_tournaments(name)
        if tournament_found:
            return tournament_found.doc_id
        return None

    def search_table_tournaments(self, name):
        """Check if a player exist in the db.

        Args:
            last_name (str): player lastname
            first_name (str): player firstname

        Returns:
            PLayer : return player if is
            found in the bd
        """
        tournament_found = ""
        for tournament in TOURNAMENTS:
            if tournament["name"] == name:
                tournament_found = tournament
        return tournament_found
    
    def search_table_tournament_with_id(self, id):
        """Check if a player exist in the db.

        Args:
            last_name (str): player lastname
            first_name (str): player firstname

        Returns:
            PLayer : return player if is
            found in the bd
        """
        tournament_found = ""
        for tournament in TOURNAMENTS:
            if tournament.doc_id == id:
                tournament_found = tournament
        return tournament_found

    def save_table_tournament(self, tournament):
        """Save tournament in database.

        Args:
            tournament (Object): Tournament instance
        """
        try:
            TOURNAMENTS.insert(tournament.serialize())
        except Exception as err:
            logger.error("Oops! %s :", err)

    def update_table_tournament(self, tournament):
        """[summary]

        Args:
            tournament ([type]): [description]
        """
        try:
            TOURNAMENTS.update(tournament.serialize(), doc_ids=[tournament.get_id()])
        except Exception as err:
            logger.error("Oops! %s :", err)

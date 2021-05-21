from tinydb import TinyDB, Query
import logging

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# database
db = TinyDB("db/db.json")
User = Query()
table_players = db.table("table_players")
table_tournaments = db.table("table_tournaments")


class DbCtrlPlayer:
    def get_id_player(self, last_name, first_name):
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
        for player in table_players:
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
        for player in table_players:
            if player["last_name"] == last_name and player["first_name"] == first_name:
                player_found = player
        return player_found

    def save_table_players(self, player):
        """Save player in database.

        Args:
            player (Object): Player instance
        """
        try:
            table_players.insert(player.serialize_player)
        except Exception as err:
            logger.error("Oops! %s :", err)
            
    def update_table_players(self, player):
        try:
            table_players.update(player.serialize, doc_ids=[player.get_id])
        except Exception as err:
            logger.error("Oops! %s :", err)


class DbCtrlTournament:
    """[summary]
    """

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
        for tournament in table_tournaments:
            if tournament["name"] == name:
                tournament_found = tournament
        return tournament_found

    def save_table_tournament(self, tournament):
        """Save tournament in database.

        Args:
            tournament (Object): Tournament instance
        """
        try:
            table_tournaments.insert(tournament.serialize)
        except Exception as err:
            logger.error("Oops! %s :", err)

    def update_table_tournament(self, tournament):
        try:
            table_tournaments.update(tournament.serialize, doc_ids=[tournament.get_id])
        except Exception as err:
            logger.error("Oops! %s :", err)
"""Define the players controller."""

# librairies
from views.user import UserView
from colorama import Fore
import logging
import time

# models
from models.players import Player
from models.players import Participant

# controller
from controllers.db import DbControllerlPlayer, DbControllerTournament

# views
from views.player import PlayerView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlayerController:
    """Main controller."""

    def __init__(self):
        """[summary]
        """
        self.db_player = DbControllerlPlayer()
        self.db_tournament = DbControllerTournament()
        self.player_view = PlayerView()
        self.user_view = UserView()

    def print_players(self):
        self.user_view.header()
        self.player_view.menu()
        players = self.db_player.get_players()
        self.player_view.print_players(players)

    def set_new_player(self):
        """Create a new Player instance and save it in the database."""
        try:
            last_name = self.player_view.prompt_player_lastname()
            first_name = self.player_view.prompt_player_firstname()
            if not self.db_player.check_table_players(last_name, first_name):
                birth_date = self.player_view.prompt_player_birthdate()
                sex = self.player_view.prompt_player_sex()
                elo = self.player_view.prompt_player_elo()

                player = Player(last_name, first_name, birth_date, sex, elo)
                self.db_player.save_table_players(player)
                self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX + f"\nLe joueur {last_name} {first_name} "
                                              "a bien été ajouté !")
            else:
                self.user_view.user_print_err(f"\nLe joueur {last_name} {first_name} "
                                              "est déjà présent dans la base de données.")
            self.user_view.separator_white()
        except Exception as err:
            logger.error("Oops! %s", err)

    def set_list_players(self, tournament):
        """Creates 8 Players instance, save in database and
        add to the list players in Tournament instance.

        Args:
            tournament (Object): Tournament instance
        """
        current_players = []
        j = len(tournament.serialize_players())
        while j in range(0, 7):
            j = len(tournament.serialize_players())
            self.user_view.header()
            self.player_view.print_current_players(tournament.serialize_players())
            if j == 0:
                print(f"Créez le {j+1}er joueur.")
            else:
                print(f"Créez le {j+1}eme joueur.")
            try:
                last_name = self.player_view.prompt_player_lastname()
                first_name = self.player_view.prompt_player_firstname()
                if [last_name, first_name] not in current_players:
                    if not self.db_player.check_table_players(last_name, first_name):
                        birth_date = self.player_view.prompt_player_birthdate()
                        sex = self.player_view.prompt_player_sex()
                        elo = self.player_view.prompt_player_elo()

                        player = Participant(last_name, first_name, birth_date, sex, elo)
                        tournament.append_list_players(player)
                        self.db_player.save_table_players(player)
                        player_id = self.db_player.get_id_player(last_name, first_name)
                        player.add_id(player_id)
                        self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX
                                                      + f"\nLe joueur {last_name} {first_name} a bien "
                                                      "été ajouté et enregistré dans la base de données!")
                        time.sleep(1.4)
                    else:
                        player_found = self.db_player.search_table_players(
                            last_name, first_name
                        )
                        player = Participant(
                            player_found["last_name"],
                            player_found["first_name"],
                            player_found["birth_date"],
                            player_found["sex"],
                            player_found["elo"],
                        )
                        print(player_found.doc_id)
                        player.add_id(player_found.doc_id)
                        tournament.append_list_players(player)
                        self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX + f"\nLe joueur {last_name} {first_name} "
                                                      "a bien été ajouté!")
                        self.user_view.user_print_msg("Ses informations sont importés depuis la base de données.")
                        time.sleep(1.4)
                    current_players.append([last_name, first_name])
                else:
                    self.user_view.user_print_err(
                        f"\nLe joueur {last_name} {first_name} est déjà présent dans le tournoi !")
                    time.sleep(1.4)
                self.db_tournament.update_table_tournament(tournament)
            except Exception as err:
                logger.error("Oops! %s", err)

    def update_players_elo(self):
        players = self.db_player.get_players()
        self.player_view.print_players(players)
        id = self.player_view.prompt_player_id()
        player_found = self.db_player.search_table_players_with_id(id)
        if player_found:
            player = Player(player_found["last_name"], player_found["first_name"],
                            player_found["birth_date"], player_found["sex"], player_found["elo"])
            self.player_view.print_one_player(player_found)
            elo = self.player_view.prompt_player_elo()
            player.update_elo(elo)
            self.db_player.update_player(player, id)
        else:
            self.user_view.user_print_err("Aucun joueur avec cet ID n'a été trouvé.")

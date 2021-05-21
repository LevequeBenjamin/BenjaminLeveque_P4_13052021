
from views.user import UserView
from colorama import Fore

import logging

from models.players import Player
from models.players import Participant

from controllers.db import DbCtrlPlayer, DbCtrlTournament

from views.player import PlayerView

# logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlayerCtrl:
    def __init__(self):
        self.db_player = DbCtrlPlayer()
        self.db_tournament = DbCtrlTournament()
        self.player_view = PlayerView()
        self.user_view = UserView()

    @property
    def set_new_player(self):
        """Create a new Player instance and save it in the database."""
        try:
            last_name = self.player_view.prompt_player_lastname
            first_name = self.player_view.prompt_player_firstname
            if not self.db_player.check_table_players(last_name, first_name):
                birth_date = self.player_view.prompt_player_birthdate
                sex = self.player_view.prompt_player_sex
                elo = self.player_view.prompt_player_elo

                player = Player(last_name, first_name, birth_date, sex, elo)
                self.db_player.save_table_players(player)
                self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX + f"\nLe joueur {last_name} {first_name} "
                                              "a bien été ajouté !")
            else:
                self.user_view.user_print_err(f"\nLe joueur {last_name} {first_name} "
                                              "est déjà présent dans la base de données.")
            self.user_view.separator_white
        except Exception as err:
            logger.error("Oops! %s", err)

    def set_list_players(self, tournament):
        """Creates 8 Players instance, save in database and
        add to the list players in Tournament instance.

        Args:
            tournament (Object): Tournament instance
        """
        for j in range(1, 9):
            if j == 1:
                print(f"Créez le {j}er joueur.")
            else:
                print(f"Créez le {j}eme joueur.")
            try:
                last_name = self.player_view.prompt_player_lastname
                first_name = self.player_view.prompt_player_firstname
                if not self.db_player.check_table_players(last_name, first_name):
                    birth_date = self.player_view.prompt_player_birthdate
                    sex = self.player_view.prompt_player_sex
                    elo = self.player_view.prompt_player_elo

                    player = Participant(last_name, first_name, birth_date, sex, elo)
                    tournament.append_list_players(player.serialize)
                    self.db_player.save_table_players(player)
                    player_id = self.db_player.get_id_player(last_name, first_name)
                    player.add_id(player_id)
                    self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX
                                                  + f"\nLe joueur {last_name} {first_name} a bien "
                                                  "été ajouté et enregistré dans la base de données!")
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
                    player.add_id(player_found.doc_id)
                    tournament.append_list_players(player.serialize)
                    self.user_view.user_print_msg(Fore.LIGHTYELLOW_EX + f"\nLe joueur {last_name} {first_name} "
                                                  "a bien été ajouté!")
                    self.user_view.user_print_msg("Ses informations sont importés depuis la base de données.")
                self.user_view.separator_white
            except Exception as err:
                logger.error("Oops! %s", err)
        self.db_tournament.update_table_tournament(tournament)

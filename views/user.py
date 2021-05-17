"""User views."""

from colorama import Fore
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class UserView:
    """User view"""
    
    @property
    def prompt_start_program(self):
        user_choice = 3
        while user_choice not in range(0, 3):
            try:
                user_choice = int(
                    input(Fore.LIGHTBLUE_EX + "Que voulez-vous faire ? : "))
            except (ValueError, TypeError):
                print(Fore.LIGHTRED_EX + "Oops! Je n'ai pas compris votre choix.")
            except Exception as err:
                logger.error("Oops! %s", err)
        return user_choice


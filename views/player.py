"""Player views."""

# librairies
from colorama import Fore


class PlayerView:
    """User view"""

    def prompt_player_lastname(self) -> str:
        """Prompt for get player last name.

        Returns:
            str: last name for class Player
        """
        confirm = ""
        while confirm != "Y":
            last_name = input(
                Fore.LIGHTCYAN_EX + "entrez le nom du joueur : "
            ).capitalize()
            if not last_name:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer un nom svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le nom du joueur est : {last_name}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return last_name
                    elif confirm == "N":
                        print("Veuillez entrez le nom du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_player_firstname(self) -> str:
        """Prompt for get player first name.

        Returns:
            str: first name for class Player
        """
        confirm = ""
        while confirm != "Y":
            first_name = input(
                Fore.LIGHTCYAN_EX + "entrez le prénom du joueur : "
            ).capitalize()
            if not first_name:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer un prénom svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le prénom du joueur est : {first_name}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return first_name
                    elif confirm == "N":
                        print("Veuillez entrez le prenom du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_player_birthdate(self) -> str:
        """Prompt for get player birth date.

        Returns:
            str: birth date for class Player
        """
        confirm = ""
        while confirm != "Y":
            birth_date = input(
                Fore.LIGHTCYAN_EX + "entrez la date de naissance du joueur : "
            )
            if not birth_date:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer un nom svp"
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le nom du joueur est : {birth_date}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return birth_date
                    elif confirm == "N":
                        print("Veuillez entrez la date de naissance du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_player_sex(self) -> str:
        """Prompt for get player sex.

        Returns:
            str: sex for class Player
        """
        confirm = ""
        while confirm != "Y":
            sex = input(
                Fore.LIGHTCYAN_EX
                + "Veuillez entrer (M) pour masculin ou (F) pour feminin : "
            ).upper()
            if not sex or sex != "M" and sex != "F":
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "Veuillez entrer une commande valide svp."
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le sexe du joueur est : {sex}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return sex
                    elif confirm == "N":
                        print("Veuillez entrez le sex du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

    def prompt_player_elo(self) -> int:
        """prompt for get player elo

        Returns:
            str: elo for class Player
        """
        confirm = ""
        while confirm != "Y":
            elo = input(
                Fore.LIGHTCYAN_EX
                + "entrez le classement Elo du joueur en caractère numerique: "
            )
            if not elo.isnumeric() or not elo:
                print(
                    Fore.LIGHTRED_EX + "Je n'ai pas compris ce que vous voulez dire, "
                    "veuillez entrer le classement Elo du joueur en caractère numerique svp."
                )
            else:
                print(Fore.LIGHTGREEN_EX + f"Le classement elo du joueur est: {elo}")
                while confirm != "Y" or "N":
                    confirm = input(
                        Fore.LIGHTCYAN_EX + "Vous confirmez ? (Y/N) : "
                    ).upper()
                    if confirm == "Y":
                        return int(elo)
                    elif confirm == "N":
                        print("Veuillez entrez le classement Elo du joueur svp.")
                        break
                    else:
                        print(
                            Fore.LIGHTRED_EX
                            + "Je n'ai pas compris ce que vous voulez dire."
                        )

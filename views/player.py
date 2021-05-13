"""Docstrings."""


class PlayerView:
    """User view"""


    def prompt_player_lastname(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            last_name = input("entrez le nom du joueur : ").capitalize()
            print(f"Le nom du joueur est : {last_name}")
            confirm = input("Vous confirmez ? (Y/N) : ").upper()
            if confirm == "Y":
                return last_name
            elif confirm == "N":
                print("Veuillez entrez le nom du joueur svp.")
                
    def prompt_player_firstname(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            first_name = input("entrez le prénom du joueur : ").capitalize()
            print(f"Le prénom du joueur est : {first_name}")
            confirm = input("Vous confirmez ? (Y/N) : ").upper()
            if confirm == "Y":
                return first_name
            elif confirm == "N":
                print("Veuillez entrez le prenom du joueur svp.")
    
    def prompt_player_dateofbirth(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            date_of_birth = input("entrez la date de naissance du joueur : ")
            print(f"Le nom du joueur est : {date_of_birth}")
            confirm = input("Vous confirmez ? (Y/N) : ").upper()
            if confirm == "Y":
                return date_of_birth
            elif confirm == "N":
                print("Veuillez entrez la date de naissance du joueur svp.")
                
    def prompt_player_sex(self):
        """Prompt for tournament"""
        confirm = ""
        while confirm != "Y":
            sex = input("Veuillez entrer (M) pour masculin ou (F) pour feminin : ").upper()
            if not sex or sex != "M" and sex != "F":
                print("Veuillez entrer une commande valide svp.")
            else:
                print(f"Le sexe du joueur est : {sex}")
                confirm = input("Vous confirmez ? (Y/N) : ").upper()
                if confirm == "Y":
                    return sex
                elif confirm == "N":
                    print("Veuillez entrez le sex du joueur svp.")

    
    

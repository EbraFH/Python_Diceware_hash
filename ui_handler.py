from global_validator import *

class UIHandler:
    @staticmethod
    def show_menu(options: list) -> None:
        """
        Method displays a ui menu, according to the given list
        :param options: Options to include in the menu
        :raises ValueError - If the given options' list is invalid
        :return: None
        """
        if not GlobalValidator.validate_strings_list(options):
            raise ValueError("To display a choices' menu, a choices list is required")

        # Displaying all options the user can choose from
        for index, option in enumerate(options):
            print(f"{(index + 1)}: {option}")

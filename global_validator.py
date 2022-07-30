class GlobalValidator:
    @staticmethod
    def validate_range(bottom_range_value: int, top_range_value: int) -> bool:
        """
        Method checks if two given values can be a string
        :param bottom_range_value: Bottom range value to validate
        :param top_range_value: Top range value to validate
        :return: True if two given values are valid range values and False otherwise
        """
        return isinstance(bottom_range_value, int) and isinstance(top_range_value,
                                                                  int) and bottom_range_value < top_range_value

    @staticmethod
    def validate_positive_integer(integer_to_check: int) -> bool:
        """
        Method checks if the given value is a positive integer
        :param integer_to_check: Value to check
        :return: True if the given value is a positive integer value and False otherwise
        """
        return isinstance(integer_to_check, int) and integer_to_check > 0

    @staticmethod
    def validate_strings_list(list_to_check: list) -> bool:
        """
        Method checks if the given value is a list of strings
        :param list_to_check: List to check
        :return: True if the given value is a strings list and False otherwise
        """
        return isinstance(list_to_check, list) and all(isinstance(element, str) for element in list_to_check)

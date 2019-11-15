import functools


class SnakeNamingStrategy:

    @staticmethod
    def class_to_table_name(class_name: str):
        return SnakeNamingStrategy.add_underscores(class_name)
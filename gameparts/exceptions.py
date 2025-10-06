class FieldIndexError(IndexError):
    def __str__(self):
        return "Значение должно быть >= 0 и < 3"


class CellOccupiedError(Exception):
    def __str__(self):
        return "Ячейка занята"

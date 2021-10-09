class Unprintable_Card(Card):
    """Карта, номинал и масть которой
    не могут быть выведены на экран. """

    def __str__(self):
        return "<нельзя напечатать>"

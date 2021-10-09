
class Positionable_Card(Card):
    """ Карта, которую можно положить
    лицом или рубашкой вверх. """

    def __init__(self, rank, suit, face_up = True):
        super(). __init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up
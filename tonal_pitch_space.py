from pychord2 import Chord

class TonalPitchSpace:
    """ Classe representando um Tonal Pitch Space de Lerdahl

    :param str root: A nota raiz do campo harmônico
    :param str quality: A qualidade desse campo harmônico (maior ou menor - M/m)
    :param [str] 

    """
    def __init__(self, root, quality):
        self.root = root
        self.quality = quality

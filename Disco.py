class Disco: 
    def __init__(self, peso):
        self._peso = peso;

    def get_peso(self):
        return int(self._peso)

    def to_string(self):
        print(self._peso)
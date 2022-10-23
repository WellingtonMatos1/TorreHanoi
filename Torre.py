class Torre:
    def __init__(self, nome, fila_discos):
        self._nome = nome;
        self._fila_discos = fila_discos;
        

    def desempilha(self):
            return self._fila_discos.pop()


    def empilha(self, disco):
        self._fila_discos.append(disco)


    def to_string(self):
            print("\ntorre: " + str(self._nome))
            print("pilha: ")
            for disco in self._fila_discos:
                disco.to_string()
            print("\n")


    def get_tamanho(self):
        return len(self._fila_discos)

    def ultimo_disco(self):
        if self.get_tamanho() == 0:
            return 0
        else:
            return self._fila_discos[self.get_tamanho() - 1]
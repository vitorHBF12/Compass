class Passaro:
    def voar(self):
        print("Voando...")

    def emitir_som(self, som):
        print("Emitindo som...")
        print(som)


class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som("Piu Piu")


if __name__ == "__main__":
    pato = Pato()
    print("Pato")
    pato.voar()
    pato.emitir_som()

    print()

    pardal = Pardal()
    print("Pardal")
    pardal.voar()
    pardal.emitir_som()

def conta_vogais(string):
    # Definimos uma função lambda para verificar se um caractere é uma vogal.
    def Ehvogal(char): return char.lower() in 'aeiou'

    # Filtramos apenas os caracteres da string que são vogais.
    volgal = filter(Ehvogal, string)

    # Usamos a função len para contar o número de vogais na sequência filtrada.
    contador = len(list(volgal))

    return contador

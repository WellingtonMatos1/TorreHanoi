from Disco import Disco
from Torre import Torre

def menu():
    print(' ╔══════════════════════╗\n',
          '║   ###   MENU   ###   ║\n',
          '║ # 1 - INICIAR JOGO # ║ \n',
          '║ # 2 - FECHAR       # ║\n',
          '║   ###  -----   ###   ║\n',
          '╚══════════════════════╝')
    valor = int(input('Digite a operação desejada: '))

    if valor == 1:
        return print('### DISCOS ###',)
    elif valor == 2:
        return exit()
    else:
        print('Digite um valor válido: ')
        menu()

def mover_disco():
    print("Mover Disco:")
    saida = int(input("Digite de qual torre deseja remover o disco: "))
    destino = int(input("Digite para qual torre deseja enviar: "))
    if saida == 1:
        saida = Torre1
    elif saida == 2:
        saida = Torre2
    elif saida == 3:
        saida = Torre3

    if destino == 1:
        destino = Torre1
    elif destino == 2:
        destino = Torre2
    elif destino == 3:
        destino = Torre3

    if saida.get_tamanho() == 0:
        print("A torre está vazia")
    else:
        ultimo_disco = saida.ultimo_disco()
        if destino.ultimo_disco() == 0 or disco.get_peso() < destino.ultimo_disco().get_peso():
            saida.desempilha()
            destino.empilha(ultimo_disco)
        else:
            print("Para sobrepor um disco é necesário que seu peso seja menor que o do disco anterior")


def validacao_da_quantidade_de_discos():
    ok = False
    while True:
        quantidade_de_discos = int(input('Digite o valor de discos desejados: '))
        if quantidade_de_discos > 2 and quantidade_de_discos <= 8:
            ok = True
        else:
            print("O número de discos minímo é de 3 e máxima de 8")
        if ok:
            break
    return quantidade_de_discos

if __name__ == "__main__":
    menu()
    quantidade_de_discos = validacao_da_quantidade_de_discos()
    discos = []
    for i in range (-quantidade_de_discos, 0):
        disco = Disco(-i)
        discos.append(disco)


    Torre1 = Torre(1, discos)
    Torre2 = Torre(2, [])
    Torre3 = Torre(3, [])

    while Torre3.get_tamanho() != int(quantidade_de_discos):
        mover_disco()

        Torre1.to_string()
        Torre2.to_string()
        Torre3.to_string()

    print("Você ganhou!!!!")



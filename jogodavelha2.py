tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def exibeTabuleiro():
    for linha in tabuleiro:
        print(f'{linha[0]} | {linha[1]} | {linha[2]}')
        print('-' * 10)

jogador = 'X'
def jogada(linha, coluna):
    tabuleiro[linha][coluna] = jogador
    if jogador == 'X':
        return 'O'
    else:
        return 'X'

def temVencedor():
    for linha in range(3):    
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][1] == tabuleiro[linha][0] and
            tabuleiro[linha][1] == tabuleiro[linha][2]
        ):
            print(f'Parabens! Jogador {tabuleiro[linha][0]} venceu!')
            return True
    for coluna in range(3):
        if(
            tabuleiro[0][coluna]!=' ' and
            tabuleiro[1][coluna] == tabuleiro[0][coluna] and
            tabuleiro[1][coluna]== tabuleiro[2][coluna]
        ):
            print(f'Parabens! Jogador {tabuleiro[0][coluna]} venceu.')   
            return True     
    if(
        tabuleiro[1][1] != ' ' and
        (
        (tabuleiro[0][0] == tabuleiro[1][1] and
         tabuleiro[1][1] == tabuleiro[2][2]
        )or
        (
         tabuleiro[1][1] == tabuleiro[0][2] and
         tabuleiro[0][2] == tabuleiro[2][0]   
        )
        )    
    ):
        print(f'Parabens! {tabuleiro[1][1]} venceu!')
        return True
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ' :
                return False
    print('Empatou!')
    return True       

jogar = True
while jogar:
    print(f'Eh a vez do jogador {jogador}')
    try:
        linha = int(input('Qual linha voce quer jogar? '))
        coluna = int(input('Qual coluna voce quer jogar? '))
        if tabuleiro[linha][coluna] == ' ':
            jogador = jogada(linha,coluna)
            exibeTabuleiro()
            if temVencedor() or temEmpate():
                resp = input('Voce quer jogar novamente? [s/n] ')
                if resp.lower() == 's':
                    jogar = True
                    for linha in range(3):
                        for coluna in range(3):
                            tabuleiro[linha][coluna] = ' '
                            
                    exibeTabuleiro()
                else:
                    break
        else: print('Jogada Invalida! Tente denovo')    
    except IndexError:
        print('Jogada Invalida! Tente numeros de 0 a 2.')
    except ValueError:
        print('Tente numeros de 0 a 2.')


print()

class JogoDaVelha:
    
   
def __init__(self):
        self.tabuleiro = [[
        self.tabuleiro =

        self.tabuleiro

        self.tab
' ' for _ in range(3)] for _ in range(3)]
        self.jogador_atual = 
        self.jogador_atual =

        self.jogador_atual

        self.jogador

        self.jog

        self.j

        self
'X'
        self.jogadas_restantes = 
        self.jogadas_restantes = 

        self.jogadas_restantes =

        self.jogadas_restantes

        self.jogadas_restant

        self.jogadas_re

        self.jogadas

        self.jog

        self.j

        self

       
9

    

   


def imprimir_tabuleiro(self):
        
       
for linha in self.tabuleiro:
            
           
print('|'.join(linha))
            
           
print('-' * 5)

    

   


def fazer_jogada(self, linha, coluna):
        
       
if self.tabuleiro[linha][coluna] == ' ':
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_restantes -= 
            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_restantes -= 

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_restantes -=

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_restantes

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_restant

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas_re

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jog

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.j

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self

            self.tabuleiro[linha][coluna] = self.jogador_atual
           

            self.tabuleiro[linha][coluna] = self.jogador_atual

            self.tabuleiro[linha][coluna] = self.jogador

            self.tabuleiro[linha][coluna] = self.jog

            self.tabuleiro[linha][coluna] = self.j

            self.tabuleiro[linha][coluna] = self

            self.tabuleiro[linha][coluna] =

            self.tabuleiro[linha][coluna]

            self.tabuleiro[linha][coluna

            self.tabuleiro[linha][col

            self.tabuleiro[linha][

            self.tabuleiro[linha

            self.tabuleiro[

            self.tabuleiro

            self.tabule

            self.tab

            self
1

            

           


# Verificar se houve um vencedor
            
           
if self.verificar_vencedor():
                
               
print(f'Jogador {self.jogador_atual} venceu!')
                
               
return True

            

           
# Verificar se houve um empate
            
           
if self.jogadas_restantes == 0:
                
               
print('O jogo empatou!')
                
               
return True

            

           


# Alternar o jogador atual
            self.jogador_atual = 
            self.jogador_atual =

            self.jogador_atual

            self.jogador

            self.jog

            self.j

            self

           
'O' if self.jogador_atual == 'X' else 'X'
        
       
else:
            
           
print('Posição inválida. Tente novamente.')

        

       


return False

    

   


def verificar_vencedor(self):
        
       
# Verificar linhas
        
       
for linha in self.tabuleiro:
            
           
if linha.count(linha[0]) == 3 and linha[0] != ' ':
                
               
return True

        

       


# Verificar colunas
        
       
for coluna in range(3):
            
           
if self.tabuleiro[0][coluna] == self.tabuleiro[1][coluna] == self.tabuleiro[2][coluna] != ' ':
                
               
return True

        

       


# Verificar diagonais
        
       
if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
            
           
return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
            
           
return True

        

       


return False
import random

print("Bem vindo ao jogo da velha")
print("Vamos começar um desafio contra o computador?")
print(
    "Ganha quem conseguir uma linha, coluna na diagonal do grid com o mesmo simbolo"
)

print
("Você precisa escolher uma posição para marcar uma numeração")
print("ganha quem completar uma coluna primeiro")
print("_ _ _")
print("_ _ _")
print("_ _ _")

print("Escolha um número de 1 a 9 para sua jogada, conforme o grid a seguir")
print("1 2 3")
print("4 5 6")
print("7 8 9")


def imprime_grid(grid):
  print("O status do grid é:")
  for indice in range(len(grid)):
    print(grid[indice], end=" ")
    if indice == 2 or indice == 5 or indice == 8:
      print("")


def verifica_grid(grid, jogador):
  # testando linha
  if grid[0] == jogador and grid[1] == jogador and grid[2] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[3] == jogador and grid[4] == jogador and grid[5] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[6] == jogador and grid[7] == jogador and grid[8] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2

  # testando colunas
  if grid[0] == jogador and grid[3] == jogador and grid[6] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[1] == jogador and grid[4] == jogador and grid[7] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[2] == jogador and grid[5] == jogador and grid[8] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2


# testando diagonais
  if grid[0] == jogador and grid[4] == jogador and grid[8] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2
  if grid[2] == jogador and grid[4] == jogador and grid[6] == jogador:
    if jogador == "X":
      return 1
    else:
      return 2

  return 0

quantidade_escolhas = 0

grid = ["_"] * 9
while True:

  escolha = int(input("Qual é a sua escolha?"))

  while grid[escolha - 1] != "_":
    print("Escolha outra casinha")
    imprime_grid(grid)
    escolha = int(input("qual é a sua escolha"))

  grid[escolha - 1] = "X"
  quantidade_escolhas += 1

  vencedor = verifica_grid(grid, "X")

  if vencedor != 0:
    break
  if quantidade_escolhas == 9:
    break

  imprime_grid(grid)

  escolha_computador = random.randint(1, 9)
  while grid[escolha_computador - 1] != "_":
    escolha_computador = random.randint(1, 9)

  grid[escolha_computador - 1] = "O"
  quantidade_escolhas += 1

  vencedor = verifica_grid(grid, "O")
  if vencedor != 0:
    break
  imprime_grid(grid)
if vencedor == 1:
  print("parabéns, você ganhou")
elif vencedor == 2:
  print("Você perdeu, o computador ganhou")
else:
  print("Deu velha, ninguém venceu, foi empate!")

imprime_grid(grid)

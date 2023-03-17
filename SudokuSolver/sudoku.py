def find_empty(board):
    """
    Encontra uma célula vazia no tabuleiro.
    Retorna uma tupla com as coordenadas da célula vazia ou None se não houver células vazias.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


def is_valid(board, num, pos):
    """
    Verifica se um número é válido para ser colocado em uma determinada posição no tabuleiro.
    Retorna True se for válido e False caso contrário.
    """
    # Verifica a linha
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Verifica a coluna
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Verifica o quadrante
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    """
    Resolve o Sudoku recursivamente.
    Retorna True se o Sudoku foi resolvido com sucesso e False caso contrário.
    """
    # Encontra uma célula vazia
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    # Testa números de 1 a 9 na célula vazia
    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            # Chama recursivamente a função solve para a próxima célula vazia
            if solve(board):
                return True

            board[row][col] = 0

    return False


# Exemplo de uso
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(board):
    for row in board:
        print(row)
else:
    print("Não foi possível resolver o Sudoku.")


'''

O código começa definindo uma função `find_empty` que encontra uma célula vazia no tabuleiro. Em seguida, define uma função `is_valid` que verifica se um número é válido para ser colocado em uma determinada posição no tabuleiro.

A função principal `solve` é responsável por resolver o Sudoku recursivamente. Ela utiliza as funções `find_empty` e `is_valid` para testar possíveis valores em cada célula vazia, e chama a si mesma recursivamente para tentar resolver o Sudoku.

O exemplo de uso define um tabuleiro inicial e chama a função `solve` para tentar resolvê-lo. Se a solução for encontrada, o código imprime a solução na tela. Caso contrário, ele imprime uma mensagem informando que não foi possível resolver o Sudoku.

'''

import numpy as np


def transposta():

    linha = int(input("Informe quantas linhas tem sua matriz: "))
    coluna = int(input("Informe quantas colunas tem sua matriz: "))

    print("\n")

    A = np.empty([linha, coluna], dtype=float)

    for i in range(0, linha):
        for j in range(0, coluna):
            A[i][j] = float(
                input("Insira o elemento [{}][{}] da matriz: ".format(i + 1, j + 1)))

    print("\n\nA matriz digitada é:\n\n{}\n\n".format(A))

    A_T = np.transpose(A)

    print("A matriz transposta é:\n\n{}\n\n". format(A_T))

    A = np.transpose(A_T)

    print("A matriz transposta da transpostada é:\n\n{}".format(A))

    return None


transposta()

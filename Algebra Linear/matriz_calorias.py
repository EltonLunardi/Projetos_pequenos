
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

A = np.array([[213, 651, 304, 420],
              [225, 688, 321, 441],
              [237, 726, 338, 468],
              [249, 764, 356, 492]])
print("A matriz A é\n\n", A)

B = np.array([[1.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 2.0],
              [0.4, 0.5, 0.0, 0.0],
              [0.0, 0.0, 0.5, 2.0],
              [0.4, 0.5, 0.0, 0.0]])
print("A matriz B é\n\n", B)

x = A[3]
x = np.transpose(x)

Calorias = np.dot(B, x)
print("A matriz com valores de calorias gastas é:\n\n", Calorias)

DiasdaSemana = ['Segunda-feira', 'Terça-feira',
                'Quarta-feira', 'Quinta-feira', 'Sexta-feira']

plt.figure(figsize=(8, 5))
plt.xlabel('Dias da Semana')
plt.ylabel('Calorias Gastas')
plt.plot(DiasdaSemana, Calorias, label='Calorias Gastas/Dia')
plt.legend()
plt.grid(True)
plt.title('Gráfico de Calorias Gastas por Alysson')

plt.figure(figsize=(8, 5))
plt.xlabel('Dias da Semana')
plt.ylabel('Calorias Gastas')
plt.barh(DiasdaSemana, Calorias, label='Calorias Gastas/Dia')
plt.legend()
plt.grid(True)
plt.title('Gráfico de Calorias Gastas por Alysson')

C = np.array([[0.10, 0.30, 0.15],
              [0.30, 0.40, 0.25],
              [0.10, 0.20, 0.15]])
print("A matriz C é:\n\n", C)

D = np.array([[4000, 4500, 4500, 4000],
              [2000, 2600, 2400, 2200],
              [5800, 6200, 6000, 6000]])
print("A matriz D é:\n\n", D)

Custos = np.dot(C, D)
print("A matriz de Custos é:\n\n", Custos)

Trimestres = ['Verão', 'Outono', 'Inverno', 'Primaveira']
MateriaPrima = Custos[0]
Pessoal = Custos[1]
DespesasGerais = Custos[2]
plt.figure(figsize=(12, 8))
plt.xlabel('Trimestres')
plt.ylabel('Dinheiro(R$)')
plt.plot(Trimestres, MateriaPrima, label='Matéria-Prima')
plt.plot(Trimestres, Pessoal, label='Pessoal')
plt.plot(Trimestres, DespesasGerais, label='Despesas Gerais')
plt.legend()
plt.grid(True)
plt.title('Gráfico de Custos por Categoria em cada Trimestre')

import pandas as pd
import matplotlib.pyplot as plt

# Cada linha registra as viagens iniciadas em uma estação, por dia e período.
dados = pd.read_csv("bicicletas.csv")

# 1. Em qual estação começaram mais viagens?
por_estacao = dados.groupby("estacao")["viagens"].sum()
por_estacao = por_estacao.sort_values(ascending=False)
print("1. Viagens por estação")
print(por_estacao)

# 2. Qual período teve mais viagens no conjunto dos três dias?
por_periodo = dados.groupby("periodo")["viagens"].sum()
print("\n2. Viagens por período")
print(por_periodo)

# 3. Qual foi a média diária, juntando todas as estações e períodos?
por_dia = dados.groupby("dia")["viagens"].sum()
media_diaria = por_dia.mean()
print("\n3. Viagens por dia")
print(por_dia)
print(f"Média diária: {media_diaria:.1f} viagens")

# 4. A estação mais movimentada no sábado foi a mesma do total?
sabado = dados[dados["dia"] == "Sábado"]
por_estacao_sabado = sabado.groupby("estacao")["viagens"].sum()
por_estacao_sabado = por_estacao_sabado.sort_values(ascending=False)
print("\n4. Viagens por estação no sábado")
print(por_estacao_sabado)

# Gráfico 1: comparar as estações no conjunto dos três dias.
por_estacao.plot(kind="bar", color="#236b8e", rot=0)
plt.title("Viagens por estação em três dias (dados fictícios)")
plt.xlabel("Estação de partida")
plt.ylabel("Viagens")
plt.tight_layout()
plt.savefig("viagens_por_estacao.png", dpi=140)
plt.close()

# Gráfico 2: ver a diferença entre manhã e tarde.
por_periodo.plot(kind="bar", color="#ab5935", rot=0)
plt.title("Viagens por período em três dias (dados fictícios)")
plt.xlabel("Período")
plt.ylabel("Viagens")
plt.tight_layout()
plt.savefig("viagens_por_periodo.png", dpi=140)
plt.close()

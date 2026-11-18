# Uso de bicicletas compartilhadas

Projeto introdutório com quatro perguntas sobre viagens iniciadas em três estações. A base tem 18 linhas de **dados fictícios**, criados para estudo, com três dias e dois períodos por dia. Cada linha informa dia, período, estação de partida e quantidade de viagens.

## Perguntas e resultados calculados

| Pergunta | Resultado |
| --- | --- |
| Qual estação teve mais partidas? | Centro, com 168 viagens. Campus teve 150 e Parque, 140. |
| Qual período teve mais viagens? | Tarde, com 235, ante 223 pela manhã. Diferença de 12 viagens. |
| Qual foi a média diária? | 152,7 viagens. Segunda teve 148, quarta 156 e sábado 154. |
| Qual estação liderou no sábado? | Parque com 79, seguido de Centro com 51 e Campus com 24. |

No total foram 458 viagens. Centro liderou o conjunto dos três dias. No recorte de sábado, Parque teve mais viagens. O exemplo mostra que olhar um recorte pode revelar uma distribuição diferente do total. As conclusões se limitam aos valores fictícios desta tabela.

## Como executar

Com Python 3.10 ou superior, baixe o repositório e abra o terminal na pasta dos arquivos.

```bash
python -m pip install -r requirements.txt
python analise.py
```

O script imprime as quatro respostas e salva dois gráficos de barras na pasta do projeto, `viagens_por_estacao.png` e `viagens_por_periodo.png`. Os gráficos comparam os totais por estação e por período. As imagens são geradas ao executar o programa.

## Entendendo o código

1. As duas primeiras linhas carregam pandas e Matplotlib, bibliotecas instaladas pelo comando acima. Os apelidos `pd` e `plt` permitem chamar seus comandos.
2. `read_csv` lê a tabela. Os colchetes selecionam colunas.
3. `groupby` reúne linhas da mesma estação, período ou dia e `sum` soma suas viagens. `sort_values` organiza os totais do maior para o menor.
4. `mean` calcula a média dos três totais diários.
5. O filtro `dados[dados["dia"] == "Sábado"]` seleciona as linhas do sábado.
6. `plot` cria as barras. Os comandos `plt` colocam títulos e rótulos, ajustam o espaço, salvam e fecham cada figura.

## Base e reprodução

O CSV foi criado para este exercício, sem informações de pessoas ou de operações reais. Cada viagem é contada na estação em que começou. Os rótulos Segunda, Quarta e Sábado identificam três dias do exemplo. A tabela já vem preenchida com quantidades inteiras positivas.

Execução realizada com pandas 2.2.3 e Matplotlib 3.10.8. Os totais por estação, período, dia e o recorte de sábado também foram conferidos separadamente a partir do CSV.

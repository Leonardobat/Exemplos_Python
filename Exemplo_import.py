# -*- coding: utf-8 -*-
""" Exemplo 2 da Aula do Mini Curso de Python.

    Neste arquivo está presente um exemplo de módulo importado.
    :Author: Leonardo B.
"""
import math

capital = float(input("Valor total do Financiamento: "))
periodo = int(input("Tempo do Financiamento em meses: "))
valor_parcela = float(input("Valor da parcela proposta: "))

montante = valor_parcela * periodo
juros_totais = montante - capital
taxa_de_juros = math.pow((montante / capital), (1 / periodo)) - 1
taxa_de_juros_anuais = math.pow((montante / capital), (12 / periodo)) - 1

msg = """Você pegou um financiamento de R$ {0} num periodo de {1} meses
O Financiador ofereceu uma parcela mensal de R$ {2}, o que acarreta em:\n
\tValor total do financiamento de R$ {3}\n 
\tValor total de juros pagos de R$ {4}\n
\tTaxa de juros mensal será de {5} %, ou {6} % ao ano.
""".format(
    capital,
    periodo,
    valor_parcela,
    montante,
    juros_totais,
    round(taxa_de_juros * 100, 2),
    round(taxa_de_juros_anuais * 100, 2),
)
print(msg)

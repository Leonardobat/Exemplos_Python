# -*- coding: utf-8 -*-
# My Git => https://github.com/Leonardobat/Exemplos_Python
""" Jogo de Advinhação Numérico
    Usa o módulo random para advinhar números.
    1 - Pede para o usuário um valor de 1-4 digitos.
    2 - Usa um sistema de "Maior ou Menor" para determinar o valor.
"""
from random import randrange

def gerar_teto(digitos):
    if digitos == 1:
        teto = 9
    elif digitos == 2:
        teto = 99
    if digitos == 3:
        teto = 999
    elif digitos == 4:
        teto = 9999
    return teto

num_digitos = randrange(1,4)
print("Pense um número {0} digitos".format(num_digitos))
input("Pressione Enter para continuar")
piso, teto = 0, gerar_teto(num_digitos)
numero_gerado = randrange(piso, teto)
acertou = input("O valor é {0}? ".format(numero_gerado)).lower()

while acertou != "sim":
    dica = input("O valor é maior ou menor que {0}? ".format(numero_gerado)).lower()
    if dica == "maior":
        piso = numero_gerado
    elif dica == "menor":
        teto = numero_gerado
    numero_gerado = randrange(piso, teto)
    acertou = input("O valor é {0}? ".format(numero_gerado)).lower()

print("O valor é", numero_gerado)

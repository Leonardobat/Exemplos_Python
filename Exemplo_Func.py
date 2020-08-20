# -*- coding: utf-8 -*-
""" Exemplo 1 da Aula do Mini Curso de Python.

    Neste arquivo está presente um exemplo simples de função.
    :Author: Leonardo B.
"""
palavra_raw = input("Insira a palavra: ")
letra = input("Qual a letra deseja retirar? ")


def remove_letra(palavra, letra) -> str:
    num_letras = palavra.count(letra)
    print(
        "Você removeu a letra {0} da palavra {1}\n{2} vezes".format(
            letra, palavra, num_letras
        )
    )
    nova_palavra = palavra.replace(letra, "")
    return nova_palavra


retorno = remove_letra(palavra_raw, letra)

print("Resultado:", retorno)

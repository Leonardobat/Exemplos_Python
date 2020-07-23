# -*- coding: utf-8 -*-
""" Exemplo 3 da Aula do Mini Curso de Python.

    Neste arquivo estão presente duas funções que serão utilizadas 
    durante a aula do mini curso de python.
    :Author: Leonardo B.
"""
from datetime import datetime, timedelta


def data_do_dia() -> None:
    """Essa função mostra o dia de hoje"""
    print("\t" + datetime.now().strftime("%d/%m/%Y"))
    return


def horario(fuso: int) -> None:
    """ Essa função mostra o horário
        
        Parameters
        ----------
        fuso:
            Fuso horário local.       
    """
    horario = datetime.utcnow()
    horario += timedelta(hours=fuso)
    msg = horario.strftime("%H:%M") + " GMT{0}".format(fuso)
    print("\t" + msg)
    return None


if __name__ == "__main__":
    print("Data Atual:")
    try:
        data_do_dia().upper()
    except AttributeError:
        pass
    horario(-5)

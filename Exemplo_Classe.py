# -*- coding: utf-8 -*-

class aluno():
    def __init__(self, nome):
        self.nome = nome
        self.atributos = {"triste": False, "cansado": False}
        self.curso = "Eng. Elétrica"

    def periodo(self, periodo):
        if periodo > 7:
            self.atributos.update({"triste": True})
            self.atributos.update({"cansado": True})
        elif periodo > 4:
            self.atributos["cansado"] = True
        else:
            pass

    def apresentar_atributos(self):
        if self.atributos["cansado"] and self.atributos["triste"]:
            self.cansado, self.triste = "cansado", "triste"
        elif self.atributos["cansado"] or self.atributos["triste"]:
            if self.atributos["cansado"]:
                self.cansado, self.triste = "cansado", "feliz"
            else:
                self.cansado, self.triste = "motivado", "triste"
        else:
            self.cansado, self.triste = "motivado", "feliz"
        msg = "{0} está {1} e {2}.".format(self.nome, self.cansado, self.triste)
        print(msg)


if __name__ == "__main__":
    milksheykson = aluno("Milksheykson")
    frank = aluno("frank".capitalize())
    joyce = aluno("joyce".upper())
    print(frank.nome)
    milksheykson.periodo(8)
    frank.periodo(2)
    milksheykson.apresentar_atributos()
    frank.apresentar_atributos()
    print(
        "{0} faz {1}, por isso ele está {2}".format(
            milksheykson.nome, milksheykson.curso, milksheykson.triste.upper()
        )
    )
    joyce.apresentar_atributos()

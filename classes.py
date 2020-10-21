class Aluno:

    def __init__(self, codigo, nome,matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("Nome: "+ self.nome)
        print("Codigo: " + self.codigo)
        print("Matricula: " + self.matricula)

    def toAluno(Aluno):
        a = Aluno(Aluno.codigo, Aluno.nome, Aluno.matricula)
        return a

class AlunoEnsinoMedio(Aluno):

    def __init__(self, codigoM, nomeM, matriculaM, anoM):
        Aluno.__init__(self, codigoM, nomeM, matriculaM)
        self.ano = anoM 

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: " + self.ano)

    def toAlunoEnsinoMedio(Aluno):
        b = AlunoEnsinoMedio(Aluno.codigo, Aluno.nome, Aluno.matricula, anoM)
        return b
class AlunoGraduacao(Aluno):

    def __init__(self, codigoG, nomeG, matriculaG, semestreG):
        Aluno.__init__(self, codigoG, nomeG, matriculaG)
        self.semestre = semestreG

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: " + self.semestre)

    def toAlunoGraduacao(Aluno):
        c = AlunoGraduacao(Aluno.codigo, Aluno.nome, Aluno.matricula, semestreG)
        return c


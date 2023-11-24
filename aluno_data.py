import pymysql.cursors
from aluno import Aluno

class AlunoData:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.conexao.cursor()

    def insert(self, aluno: Aluno):
        try:
            sql = 'INSERT INTO alunos VALUES (%s, %s, %s, %s, %s)'
            self.cursor.execute(sql, (aluno.matricula,
                                      aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota))

            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao inserir! Erro: {error}')

    def select(self):
        try:
            sql = 'SELECT * FROM alunos'
            self.cursor.execute(sql)
            alunos = self.cursor.fetchall()
            return alunos
        except Exception as error:
            print(f'Erro ao listar! Erro: {error}')

    def update(self, aluno: Aluno):
        try:
            sql = 'UPDATE alunos SET nome = %s, idade = %s, curso = %s, nota = %s WHERE matricula = %s'
            self.cursor.execute(sql, (aluno.nome,
                                      aluno.idade,
                                      aluno.curso,
                                      aluno.nota,
                                      aluno.matricula))
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao atualizar! Erro: {error}')

    def delete(self, matricula: str):
        try:
            sql = 'DELETE FROM alunos WHERE matricula = %s'
            self.cursor.execute(sql, matricula)
            self.conexao.commit()
        except Exception as error:
            print(f'Erro ao deletar! Erro: {error}')



if __name__ == '__main__':
    ad = AlunoData()
  #  aluno = Aluno('Sarah', 40, 'Psicologia', 9.9)
  #  ad.insert(aluno)
  #  aluno.matricula ='f4ab59a9-8a55-11ee-a7b4-00e04c362c9e'
  #  ad.update(aluno)

  #  ad.delete('cc03507e-8a56-11ee-8145-00e04c362c9e')
    print(ad.select())
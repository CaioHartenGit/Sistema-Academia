from apps.database.conexao import Conectar

class TreinoRepository:
    def inserir_Cadastrar(self, nome, dia_semana, id_aluno):
        conn = Conectar.conectar()
        cursor = conn.cursor()

        try:
            cursor.execute('''

            INSERT INTO treino (nome,dia_semana, id_aluno)
            VALUES (%s, %s, %s)
            RETURNING id,nome,dia_semana, id_aluno
        
        ''',(nome,dia_semana,id_aluno)
        )
            treino = cursor.fetchone()
            conn.commit()
            return treino
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def listar(self):
        conn = Conectar.conectar()
        cursor = conn.cursor()

        try:
            cursor.execute('''

                SELECT * FROM treino

            ''')
            treinos = cursor.fetchall()
            return treinos
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

        
    def buscar_por_id(self,id_aluno):
        conn  = Conectar.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute('''

                SELECT * FROM treino
                WHERE id_aluno = %s

            ''',(id_aluno,)
            )
            treinos = cursor.fetchall()
            return treinos
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def alterar_treino(self, id_aluno, dia_semana, novo_dia_semana):
        conn = Conectar.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE treino
                SET dia_semana = LOWER(%s)
                WHERE id_aluno = %s
                AND LOWER(dia_semana) = LOWER(%s)
                RETURNING id, nome, dia_semana, id_aluno
            ''', (
                novo_dia_semana,
                id_aluno,
                dia_semana
            ))
            treino = cursor.fetchone()
            conn.commit()
            return treino
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()

    def delete_treino(self,id_aluno):
        conn = Conectar.conectar()
        cursor = conn.cursor()
        try:
            cursor.execute('''

            DELETE FROM treino
            WHERE id_aluno = %s
            ''',(id_aluno,)
            )
            conn.commit()
            return True
        except Exception:
            conn.rollback()
            return False 
        finally:
            cursor.close()
            conn.close()

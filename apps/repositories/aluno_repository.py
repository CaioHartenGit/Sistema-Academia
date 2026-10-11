from apps.database.conexao import Conectar
from psycopg.rows import dict_row


class AlunoRepository:

    def inserir(self, nome, idade, plano):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                INSERT INTO aluno (nome, idade, plano)
                VALUES (%s, %s, %s)
                RETURNING id, nome, idade, plano, ativo
                """,
                (nome, idade, plano)
            )

            aluno = cursor.fetchone()

            conn.commit()

            return aluno

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()

    def listar(self):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                SELECT id, nome, idade, plano, ativo
                FROM aluno
                """
            )

            alunos = cursor.fetchall()

            return alunos

        finally:

            cursor.close()
            conn.close()

    def buscar_por_id(self, id_aluno):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                SELECT id, nome, idade, plano, ativo
                FROM aluno
                WHERE id = %s
                """,
                (id_aluno,)
            )

            aluno = cursor.fetchone()

            return aluno

        finally:

            cursor.close()
            conn.close()

    def atualizar(self, nome, idade, plano, id_aluno):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                UPDATE aluno
                SET nome = %s,
                    idade = %s,
                    plano = %s
                WHERE id = %s
                RETURNING id, nome, idade, plano, ativo
                """,
                (nome, idade, plano, id_aluno)
            )

            aluno = cursor.fetchone()

            if aluno is None:
                conn.rollback()
                return None

            conn.commit()

            return aluno

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()

    def deletar(self, id_aluno):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                DELETE FROM aluno
                WHERE id = %s
                RETURNING id, nome, idade, plano, ativo
                """,
                (id_aluno,)
            )

            aluno = cursor.fetchone()

            if aluno is None:
                conn.rollback()
                return None

            conn.commit()

            return aluno

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()

    def ativar(self, id_aluno):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                UPDATE aluno
                SET ativo = TRUE
                WHERE id = %s
                RETURNING id, nome, idade, plano, ativo
                """,
                (id_aluno,)
            )

            aluno = cursor.fetchone()

            if aluno is None:
                conn.rollback()
                return None

            conn.commit()

            return aluno

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()

    def desativar(self, id_aluno):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                UPDATE aluno
                SET ativo = FALSE
                WHERE id = %s
                RETURNING id, nome, idade, plano, ativo
                """,
                (id_aluno,)
            )

            aluno = cursor.fetchone()

            if aluno is None:
                conn.rollback()
                return None

            conn.commit()

            return aluno

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()

    def buscar_por_nome(self, nome):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                SELECT id, nome, idade, plano, ativo
                FROM aluno
                WHERE nome = %s
                """,
                (nome,)
            )

            alunos = cursor.fetchall()

            return alunos

        finally:

            cursor.close()
            conn.close()

    def buscar_por_plano(self, plano):

        conn = Conectar.conectar()
        cursor = conn.cursor(row_factory=dict_row)

        try:

            cursor.execute(
                """
                SELECT id, nome, idade, plano, ativo
                FROM aluno
                WHERE plano = %s
                """,
                (plano,)
            )

            alunos = cursor.fetchall()

            return alunos

        finally:

            cursor.close()
            conn.close()
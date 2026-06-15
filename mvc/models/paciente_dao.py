import sqlite3
import datetime
import os
from mvc.models.paciente import Paciente

class PacienteDAO:
    def __init__(self, db_name="bd/nutricao.db"):
        self.db_name = db_name
        self._criar_tabela()

    def _conectar(self):
        os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
        return sqlite3.connect(self.db_name)

    def _criar_tabela(self):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS pacientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    nascimento TEXT NOT NULL,
                    altura REAL NOT NULL,
                    peso REAL NOT NULL,
                    genero TEXT NOT NULL
                )
            """)
            conn.commit()

    def inserir(self, paciente):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pacientes (nome, nascimento, altura, peso, genero)
                VALUES (?, ?, ?, ?, ?)
            """, (
                paciente.nome,
                paciente.nascimento.strftime('%Y-%m-%d'),
                paciente.altura,
                paciente.peso,
                paciente.genero
            ))
            conn.commit()

    def listar(self):
        pacientes = []
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, nascimento, altura, peso, genero FROM pacientes")
            linhas = cursor.fetchall()
            for linha in linhas:
                ano, mes, dia = map(int, linha[2].split('-'))
                nascimento = datetime.date(ano, mes, dia)
                p = Paciente(
                    id=linha[0],
                    nome=linha[1],
                    nascimento=nascimento,
                    altura=linha[3],
                    peso=linha[4],
                    genero=linha[5]
                )
                pacientes.append(p)
        return pacientes

    def buscar_por_id(self, id_paciente):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, nascimento, altura, peso, genero FROM pacientes WHERE id = ?", (id_paciente,))
            linha = cursor.fetchone()
            if linha:
                ano, mes, dia = map(int, linha[2].split('-'))
                nascimento = datetime.date(ano, mes, dia)
                return Paciente(
                    id=linha[0],
                    nome=linha[1],
                    nascimento=nascimento,
                    altura=linha[3],
                    peso=linha[4],
                    genero=linha[5]
                )
        return None

    def excluir(self, id_paciente):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_paciente,))
            conn.commit()
            return cursor.rowcount > 0

    def atualizar(self, id_paciente, paciente):
        with self._conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE pacientes
                SET nome = ?, nascimento = ?, altura = ?, peso = ?, genero = ?
                WHERE id = ?
            """, (
                paciente.nome,
                paciente.nascimento.strftime('%Y-%m-%d'),
                paciente.altura,
                paciente.peso,
                paciente.genero,
                id_paciente
            ))
            conn.commit()
            return cursor.rowcount > 0

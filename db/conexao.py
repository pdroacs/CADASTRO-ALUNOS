import sqlite3
import os


def conectar():
    caminho = os.path.join('database', 'alunos.db')
    return sqlite3.connect(caminho)

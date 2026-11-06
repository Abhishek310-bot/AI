from pgvector.psycopg import register_vector
from pgvector import Vector

from app.database.postgres import get_connection


def get_vector_connection():

    connection = get_connection()

    register_vector(connection)

    return connection
import logging
import os
from logging.config import dictConfig

import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

from api.logging_config.logger_config import get_logger_config


class MariaDBConnection:
    def __init__(self):
        load_dotenv()
        dictConfig(get_logger_config())

        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")
        self.connection = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_host,
                user=self.db_user,
                password=self.db_password,
                database=self.db_name,
            )
            if self.connection.is_connected():
                logging.info(
                    "Verbindung zur MariaDB-Datenbank erfolgreich hergestellt."
                )
                return self.connection
        except Error as e:
            logging.info(f"Fehler beim Verbinden mit der Datenbank: {e}")
            self.connection = None
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logging.info("Datenbankverbindung geschlossen.")

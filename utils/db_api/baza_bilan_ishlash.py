import sqlite3




class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple= None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection= self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            language varchar(3),
            PRIMARY KEY (id)
                );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += "AND" .join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id : int, name: str, email: str = None, language: str = 'uz'):

        sql = """
        INSERT INTO myfiles_teacher(id, Name, language) VALUES(?,?,?,?)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)
    def select_user(self, **kwargs):
        sql = "SELECT * FROM myfiles_teacher WHERE"
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM myfiles_teacher;", fetchone=True)

    def update_user_email(self, email, id):
        sql = f"""
        UPDATE myfiles_teacher SET email=? WHERE id=?
        """
        return self.execute(sql, parameters=(email, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM WHERE TRUE", commit=True)

    def user_qoshish(self, first_name: str, tg_id: int, user_name: str):

        sql = """
        INSERT INTO userlar( first_name, tg_id, user_name) VALUES(?,?,?)
        """
        self.execute(sql, parameters=(first_name, tg_id, user_name), commit=True)

    def userlar_soni(self):
        return self.execute("SELECT COUNT(*) FROM userlar;", fetchone=True)




def logger(statement):
    print(f"""
-------------------------------------------------------------
Executing:
{statement}
-------------------------------------------------------------
""")
import pyodbc


class InitDatabase:
    def __init__(self, database, username, password, server='tcp:localhost,1433'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password

        self.cursor = self.execution()

        print(f"database initialized with server: '{self.server}', database: '{self.database}' and user: '{self.username}'")

    def make_connection(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        return cnxn

    def execution(self):
        cnxn = self.make_connection()
        cursor = cnxn.cursor()
        return cursor

    def execute_command(self, command):
        self.cursor.execute(command)

    def commit_changes(self):
        self.cursor.commit()

    def fetch(self):
        self.cursor.fetchone()

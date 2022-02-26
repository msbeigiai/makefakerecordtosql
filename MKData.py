import pandas as pd
from CRRecord import ChooseRandomRecord


class MakeFakeData(ChooseRandomRecord):
    def __init__(self, database, table_name, username, password, server='tcp:localhost,1433'):
        super().__init__(database, table_name, username, password, server)
        self.data = self.list_result
        self.table_name = table_name
        self.columns = []

    def return_record_data(self):
        return self.data[1]

    def insert_random_data(self):
        self.fetch_random_record()
        command = ''

    def columns_of_base_database(self):
        # table_name = "N" + self.table_name
        command = "SELECT * FROM " + self.table_name
        df = pd.read_sql(command, self.make_connection())
        self.execute_command(command)
        self.columns = df.columns

    def ingest_one_data(self, column_name):
        pass

    def ingest_random_row(self):
        data = self.roll_down_data()
        print(type(data))
        print(data)
        command = 'insert into ' + self.table_name + " " + "values" + [str(value) for value in data]
        self.execute_command(command)
        # self.commit_changes()

    def roll_down_data(self):
        value = self.return_record_data()
        list_data = []
        for i in range(1, len(value)):
            list_data.append(value[i])
        return list_data

    # def make_insert_command(self, list_value):
    #     list_command = []
    #     for i in range(len(list_value)):


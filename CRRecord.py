import numpy as np
from IDBs import InitDatabase


class ChooseRandomRecord(InitDatabase):
    """ Makes a connection with help of base class """
    def __init__(self, database, table_name, username, password, server='tcp:localhost,1433'):
        super().__init__(database, username, password, server)
        self.list_result = []
        self.table_name = table_name

    def return_number_of_records(self):
        """ Returns number of records exist in the table """
        command = 'select count(*) from ' + self.table_name + ';'
        self.execute_command(command)
        self.return_result()

    def return_result(self):
        """ Append results in a class variable 'list_result' """
        for i in self.cursor:
            self.list_result.append(i)

    def make_random_record(self):
        """ Finds a random record from '0' to 'last record' of table """
        self.return_number_of_records()
        rand_num = np.random.randint(0, self.list_result[0])
        return rand_num

    def find_and_execute_record(self, row_num):
        """ After finding a random record, this function 'executes' that record """

        command = "select * from (select  ROW_NUMBER() over (Order By TRANSACTIONID) as RowNum, * from " + self.table_name +\
                  ") t2 where RowNum = " + str(row_num[0]) + ';'
        self.execute_command(command)
        self.return_result()

    def fetch_random_record(self):
        """ After finding a random record, this function 'fetches' that record """
        rnd_row = self.make_random_record()
        self.find_and_execute_record(rnd_row)

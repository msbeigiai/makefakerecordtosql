class Animal:
    def __init__(self, name):
        self.name = name


from CRRecord import ChooseRandomRecord
from MKData import MakeFakeData
from MCommand import MakeCommand

server = 'tcp:localhost,1433'
database = 'MicrosoftDynamicsAX'
username = 'sa'
password = 'testpassword'
table_name = 'dbo.RETAILTRANSACTIONTABLE'

# choose_random_record = ChooseRandomRecord(database, table_name, username, password)
# choose_random_record.fetch_random_record()
# print(choose_random_record.list_result[1])

make_fake_data = MakeFakeData(database, table_name, username, password)
make_fake_data.fetch_random_record()
make_fake_data.return_record_data()
# make_fake_data.ingest_random_row()

make_command = MakeCommand(make_fake_data)
# print(make_command.query_columns)
# print(make_command.query_values)
# print(make_command.query_len)

print([value for value in make_command.query_values])


# print(make_command.export_string())
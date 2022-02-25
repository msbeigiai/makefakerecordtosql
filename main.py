from faker import Faker
import pyodbc
from MKData import MakeFakeData
import pandas as pd

fake = Faker()

server = 'tcp:localhost,1433'
database = 'MicrosoftDynamicsAX'
username = 'sa'
password = 'testpassword'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

command = 'select * from dbo.RETAILTRANSACTIONTABLE;'

df = pd.read_sql(command, cnxn)

make_data = MakeFakeData(df)
# print(make_data.return_len())
# print(make_data.show_columns())
# make_data.show_type_of_columns()
# info = make_data.show_info()
list_type = make_data.type_of_each_column()
# print(list_type)
# print(list_type[2])
# print(make_data.m)
print(make_data.make_dictionary_fill())

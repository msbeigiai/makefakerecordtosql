class MakeCommand:
    def __init__(self, make_fake_data):
        make_fake_data.columns_of_base_database()
        self.query_columns = make_fake_data.columns
        self.query_len = len(make_fake_data.columns)
        self.query_values = make_fake_data.roll_down_data()
        self.table_name = make_fake_data.table_name
        self.command = self.make_complete_command()

    def export_string(self):
        command = ''
        for i in range(0, self.query_len):
            tag = ", "
            if i == self.query_len - 1:
                tag = ""
            command += str(self.query_columns[i]) + tag
        return command

    def export_value(self):
        pass

    def make_complete_command(self):
        first_command = self.export_string()
        command = ''
        for i in self.query_len:
            command = 'insert into ' + self.table_name + " " + "(" + first_command + ")" + "values" + \
                      "(" + self.query_values[i] + ")"

        return command



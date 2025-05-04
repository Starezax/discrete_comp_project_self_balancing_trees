''''tree sql'''
import argparse
import shlex
from data_manager import DataManager

class TreeSQL:
    """
    TreeSQL -class for parsing and executing SQL-like commands.
    This class provides an interface for creating databases, tables, and performing CRUD operations.
    """
    def __init__(self):
        """
        Initialize the TreeSQL class with a DataManager instance.
        The DataManager is responsible for managing the databases and tables.
        """
        self.data_manager = DataManager()

    def parse_command(self, command):
        """
        Parse the input command and execute the corresponding action.
        The command can be a SQL-like command for creating databases, tables, 
        and performing CRUD operations.

        :param command: str - The SQL-like command to be executed
        :return: str - The result of the command execution or an error message.
        """
        tokens = shlex.split(command)
        if not tokens:
            return "Пуста команда"

        cmd = tokens[0].lower()

        if cmd == "create":
            if len(tokens) >= 2 and tokens[1].lower() == "database":
                return self.data_manager.create_database(tokens[2])
            if len(tokens) >= 2 and tokens[1].lower() == "table":
                return self.create_table_command(tokens[2:])
        if cmd == "use":
            return self.data_manager.use_database(tokens[1])
        if cmd == "insert":
            return self.insert_command(tokens)
        if cmd == "select":
            return self.select_command(tokens)
        if cmd == "update":
            return self.update_command(tokens)
        if cmd == "delete":
            return self.delete_command(tokens)
        return "Невідома команда"

    def create_table_command(self, tokens):
        """
        Create a table in the current database.
        The command should be in the format: CREATE TABLE table_name (column1, column2, ...)
        Optionally, a tree type can be specified using the "USING" keyword.
        The default tree type is "avl".
        
        :param tokens: list - The tokens of the command after splitting
        :return: str - The result of the table creation or an error message.
        """
        table_name = tokens[0]
        tree_type = "avl"

        if "using" in [t.lower() for t in tokens]:
            idx = tokens.index("USING") if "USING" in tokens else tokens.index("using")
            tree_type = tokens[idx + 1]

        col_start = tokens.index("(")
        col_end = tokens.index(")")
        columns_str = ' '.join(tokens[col_start + 1: col_end])
        columns = [col.strip() for col in columns_str.split(",")]

        return self.data_manager.create_table(table_name, columns, tree_type)

    def insert_command(self, tokens):
        """
        Insert a record into a table.
        The command should be in the format: INSERT INTO table_name VALUES (value1, value2, ...)
        The values should be separated by commas and can be strings, integers, or floats.

        :param tokens: list - The tokens of the command after splitting
        :return: str - The result of the insertion or an error message.
        """
        try:
            table_name = tokens[2]
            values_index = tokens.index("VALUES")
            values_str = ' '.join(tokens[values_index + 1:])
            values_str = values_str.strip("()")
            raw_values = [v.strip() for v in values_str.split(",")]
            parsed_values = [self._parse_value(v) for v in raw_values]
            return self.data_manager.insert(table_name, parsed_values)

        except Exception as e:
            return f"Помилка вставки: {e}"

    def select_command(self, tokens):
        """
        Select records from a table.
        The command should be in the format: SELECT * FROM table_name WHERE condition
        The condition is optional and can be used to filter the results.
        
        :param tokens: list - The tokens of the command after splitting
        :return: str - The result of the selection or an error message.
        """
        try:
            from_index = tokens.index("FROM")
            table_name = tokens[from_index + 1]

            condition = None
            if "WHERE" in [t.upper() for t in tokens]:
                where_index = tokens.index("WHERE")
                condition = ' '.join(tokens[where_index + 1:])

            result = self.data_manager.select(table_name, condition)
            return "\n".join(str(r) for r in result)

        except Exception as e:
            return f"Помилка SELECT: {e}"

    def update_command(self, tokens):
        """
        Update records in a table.
        The command should be in the format: UPDATE table_name SET field1=value1, field2=value2
        WHERE condition
        The condition is optional and can be used to filter the records to be updated.

        :param tokens: list - The tokens of the command after splitting
        :return: str - The result of the update or an error message.
        """
        try:
            table_name = tokens[1]
            set_index = tokens.index("SET")
            where_index = tokens.index("WHERE") if "WHERE" in tokens else len(tokens)

            update_tokens = tokens[set_index + 1: where_index]
            updates = {}
            for item in ' '.join(update_tokens).split(','):
                field, value = item.split('=')
                updates[field.strip()] = value.strip().strip("'\"")

            condition = ' '.join(tokens[where_index + 1:]) if "WHERE" in tokens else None

            return self.data_manager.update(table_name, updates, condition)

        except Exception as e:
            return f"Помилка UPDATE: {e}"

    def delete_command(self, tokens):
        """
        Delete records from a table.
        The command should be in the format: DELETE FROM table_name WHERE condition
        The condition is optional and can be used to filter the records to be deleted.

        :param tokens: list - The tokens of the command after splitting
        :return: str - The result of the deletion or an error message.
        """
        try:
            table_name = tokens[2]
            condition = None
            if "WHERE" in [t.upper() for t in tokens]:
                where_index = tokens.index("WHERE")
                condition = ' '.join(tokens[where_index + 1:])

            return self.data_manager.delete(table_name, condition)

        except Exception as e:
            return f"Помилка DELETE: {e}"

    def _parse_value(self, value):
        """
        Helper method to parse a value from the command.
        This method converts the value to its appropriate type (int, float, or string).
        If the value is enclosed in single quotes, it is treated as a string.
        If it can be converted to an integer or float, it is converted accordingly.
        Otherwise, it is returned as a string.

        :param value: str - The value to be parsed
        :return: int, float, or str - The parsed value
        """
        if value.startswith("'") and value.endswith("'"):
            return value.strip("'")
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

def main():
    """
    Main function to run the TreeSQL command line interface.
    This function uses argparse to parse command line arguments and 
    execute the corresponding actions.
    """
    parser = argparse.ArgumentParser(description="Інтерфейс команд для роботи з TreeSQL")
    parser.add_argument("--cmd", type=str, help="SQL-подібна команда")
    args = parser.parse_args()

    sql = TreeSQL()

    if args.cmd:
        result = sql.parse_command(args.cmd)
        print(result)
    else:
        print("Введіть команду або 'exit'):")
        while True:
            try:
                command = input(">>> ")
                if command.strip().lower() in ["exit", "quit"]:
                    break
                result = sql.parse_command(command)
                print(result)
            except KeyboardInterrupt:
                print("\nВихід.")
                break

if __name__ == "__main__":
    main()

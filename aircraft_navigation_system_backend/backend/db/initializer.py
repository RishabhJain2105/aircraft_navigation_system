import mysql.connector as myscon
import os

def execute_sql_file(file_path, cur):
    with open(file_path, 'r') as f:
        raw_data = f.readlines()
        cleaned_data = "".join([line.strip() for line in raw_data])
        table_insertion_commands = cleaned_data.split(';')
    table_insertion_commands = [query.strip() for query in table_insertion_commands if query.strip()]

    for command in table_insertion_commands:
        try:
            cur.execute(command)
        except Exception as e:
            print(f"Error executing command: {command}\nError: {str(e)}")

def dummy_data_insertion(cur):
        data_directory = "./data"
        sql_files = [
            "aircraft.sql",
            "aircraft_navigation.sql",
            "airports.sql",
            "routes.sql",
            "flights.sql"
        ]

        for sql_file in sql_files:
            file_path = os.path.join(data_directory, sql_file)
            if os.path.exists(file_path):
                print(f"Executing {sql_file}...")
                execute_sql_file(file_path, cur)
            else:
                print(f"File {sql_file} does not exist in the directory.")

        print("All data inserted successfully.")

def table_creation(cur):
        cur.execute("DROP DATABASE IF EXISTS AircraftNavigationSystem;")
        print("Deleted Database")
        cur.execute("CREATE DATABASE AircraftNavigationSystem;")
        print("Created Database")
        cur.execute("USE AircraftNavigationSystem;")
        print("Using Database")

        table_creation_commands = []
        with open("schema.sql", 'r') as f:
            raw_data = f.readlines()
            cleaned_data = "".join([line.strip() for line in raw_data])
            table_creation_commands = cleaned_data.split(';')
        table_creation_commands = [query.strip() for query in table_creation_commands if query.strip()]

        for command in table_creation_commands:
            cur.execute(command)

        print("Tables created successfully.")

def show_tables(cur):
        cur.execute("SHOW TABLES;")
        for table in cur.fetchall():
            print(table)
            cur.execute(f"SELECT * FROM {table[0]}")
            print(len(cur.fetchall()))

def main():
    try:
        credentials_file = "credentials.nopush"

        if os.path.isfile(credentials_file):
            with open(credentials_file, "r") as file:
                creds = file.readlines()
                user_host = creds[0].rstrip('\n')
                user_port = creds[1].rstrip('\n')
                user_name = creds[2].rstrip('\n')
                user_pass = creds[3].rstrip('\n')
        else:
            with open(credentials_file, "w") as file:
                user_host = input("Enter user host: ") + '\n'
                user_port = input("Enter user port: ") + '\n'
                user_name = input("Enter user name: ") + '\n'
                user_pass = input("Enter user pass: ")
                file.writelines([user_host, user_port, user_name, user_pass])

        # mysql connection establishing logic
        con = myscon.connect(user=user_name, passwd=user_pass, host=user_host, port=int(user_port))
        print("Successfully established connection!")

        cur = con.cursor()

        # create all the tables and the database
        table_creation(cur)
        con.commit()

        # insert dummy data into all the tables
        dummy_data_insertion(cur)
        con.commit()
        
        # show all tables
        show_tables(cur)
        
        con.close()
        print("Connection closed.")

    except Exception as e:
        print("\nAn exception occurred!")
        print(e, '\n')

if __name__ == "__main__":
    main()

import mysql.connector as myscon

def get_db_connection():
    with open("./db/credentials.nopush", "r") as file:
        creds = file.readlines()
        user_host = creds[0].rstrip('\n')
        user_port = creds[1].rstrip('\n')
        user_name = creds[2].rstrip('\n')
        user_pass = creds[3].rstrip('\n')

    print(user_host, user_name)
    return myscon.connect(
        user=user_name,
        passwd=user_pass,
        host=user_host,
        port=user_port,
        database="AircraftNavigationSystem"
    )
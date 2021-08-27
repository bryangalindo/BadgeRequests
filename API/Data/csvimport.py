from azure.cosmosdb.table.tableservice import TableService
import csv

if __name__ == '__main__':
    CSV_FILE = 'users.csv'
    TABLE = 'users'
    CONNECTION_STRING = ''
    
    table_service = TableService(
        connection_string=CONNECTION_STRING)

    try:
        with open(CSV_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                user = {}
                user['RowKey'] = row[0]
                user['PartitionKey'] = row[1]
                user['Supervisor'] = row[2]
                user['SupervisorGoogleChatID'] = row[3]
                table_service.insert_entity(TABLE, user)

        print('GREAT SUCCESS')
    except Exception as e:
        print(e)

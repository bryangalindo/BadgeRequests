from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from .config import settings
import csv


# USE THIS FILE TO IMPORT THE BADGE CSV TO COSMOS EMULATOR

table_service = TableService(
    connection_string=settings.CONNECTION_STRING)


try:
    with open('E:/badges.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            badge = {}
            badge['RowKey'] = row[0]
            badge['PartitionKey'] = row[1]
            badge['Title'] = row[2]
            badge['Description'] = row[3]
            badge['Exp'] = int(row[4])
            table_service.insert_entity('badges', badge)

    print('GREAT SUCCESS')
except Exception as e:
    print(e)

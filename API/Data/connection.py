from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from .config import settings


class Table:

    # Initialize the Table class with an Azure Table Storage table name (string)
    def __init__(self, table_name: str):
        self.table_service = TableService(
            connection_string=settings.CONNECTION_STRING)
        self.table_name = table_name

    # Create a table with the given name
    def create_table(self):
        self.table_service.create_table(self.table_name)

    # Get a single row by primary key (PartitionKey + RowKey)
    def get(self, partition_key: str, row_key: str):
        return self.table_service.get_entity(self.table_name, partition_key, row_key)

    # Query all rows for a given partition key. Include a subset (column name) to grab only the given column of the initial query.
    def query(self, column: str = None, value: str = None, subset: str = None):
        if column is not None:
            return self.table_service.query_entities(self.table_name, filter=f"{column} eq '{value}'")
        if subset is not None:
            return self.table_service.query_entities(self.table_name, filter=f"{column} eq '{value}'", select=subset)
        else:
            return self.table_service.query_entities(self.table_name)

    # Inserts a new entry into the database
    def insert(self, entity_object: dict):
        self.table_service.insert_entity(self.table_name, entity_object)

    # Updates an existing entry in the database
    def update(self, entity_object: dict):
        self.table_service.update_entity(self.table_name, entity_object)

    # Overwrites an existing entity with a matching PK or inserts if it does not exist
    def overwrite(self, entity_object: dict):
        self.table_service.insert_or_replace_entity(
            self.table_name, entity_object)

    # Delete an existing entry in the database
    def delete(self, partition_key: str, row_key: str):
        self.table_service.delete_entity(
            self.table_name, partition_key, row_key)

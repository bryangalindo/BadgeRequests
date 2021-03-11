badges = [
    {
        "PartitionKey": "Milestone",
        "RowKey": "1",
        "Title": "Belt Buster",
        "Description": "The winner of the Champion Belt",
        "Exp": 1,
    },
    {
        "PartitionKey": "Milestone",
        "RowKey": "2",
        "Title": "Newsletter Newbie",
        "Description": "Be Featured in the Support Newsletter",
        "Exp": 1,
    },
    {
        "PartitionKey": "Projects",
        "RowKey": "14",
        "Title": "HB SQL Conversion - Skywalker",
        "Description": "HeavyBid SQL Conversion in production (apprentice)",
        "Exp": 1,
    },
]

applications = [
    {
        "PartitionKey": "test1@test.com",
        "RowKey": "1"
    },
    {
        "PartitionKey": "test2@test.com",
        "RowKey": "2"
    },
]

users = [
    {
        "PartitionKey": "test1@test.com",
        "RowKey": "1",
        "exptotal": 1,
        "totalbadges": 10,
        "firstname": "Test",
        "lastname": "Person"
    },
    {
        "PartitionKey": "test2@test.com",
        "RowKey": "2",
        "exptotal": 1,
        "totalbadges": 10,
        "firstname": "Testerino",
        "lastname": "Persono"
    }
]

requests = [
    {"PartitionKey": "test1@test.com", "RowKey": "1", "badgeID": "1",
     "category": "Milestone", "approved": False, "approved_by": ""},
    {"PartitionKey": "test1@test.com", "RowKey": "2", "badgeID": "2",
     "category": "Milestone", "approved": True, "approved_by": "Tim Allen"},
    {"PartitionKey": "test2@test.com", "RowKey": "3", "badgeID": "1",
     "category": "Milestone", "approved": True, "approved_by": "Tim Allen"},
    {"PartitionKey": "test2@test.com", "RowKey": "4", "badgeID": "2",
     "category": "Milestone", "approved": False, "approved_by": ""}
]

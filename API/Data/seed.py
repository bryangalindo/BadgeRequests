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
        "firstname": "Test Person"
    },
    {
        "PartitionKey": "test2@test.com",
        "RowKey": "2",
        "exptotal": 1,
        "totalbadges": 10,
        "name": "Testerino Persono"
    }
]

requests = [
    {
        "PartitionKey": "test1@test.com", "RowKey": "1", "ApplicationID": "1",
        "badgeID": "1", "category": "Milestone", "approved": False, "approved_by": ""
    },
    {
        "PartitionKey": "test1@test.com", "RowKey": "2", "ApplicationID": "1",
        "badgeID": "2", "category": "Milestone", "approved": True, "approved_by": "Tim Allen"
    },
    {
        "PartitionKey": "test2@test.com", "RowKey": "3", "ApplicationID": "2",
        "badgeID": "1", "category": "Milestone", "approved": True, "approved_by": "Tim Allen"
    },
    {
        "PartitionKey": "test2@test.com", "RowKey": "4", "ApplicationID": "2",
        "badgeID": "2", "category": "Milestone", "approved": False, "approved_by": ""
    },
]

admins = [
    {
        "PartitionKey": "will.pankonien@hcss.com",
        "RowKey": "1"
    },
    {
        "PartitionKey": "bryan.galindo@hcss.com",
        "RowKey": "2"
    }
]

from Data.connection import Table
import inquirer
from Data.seed import badges, applications, users, requests


def table_prompt():
    questions = [
        inquirer.Checkbox('tables',
                          message="Choose which tables to create",
                          choices=['badges', 'applications', 'users',
                                   'requests'],
                          default=['badges', 'applications', 'users',
                                   'requests']),
    ]
    answers = inquirer.prompt(questions)

    if 'badges' in answers['tables']:
        badge_table = Table('badges')
        try:
            badge_table.create_table()
            print('The badges table has been created.')
        except Exception as e:
            print(e)

    if 'applications' in answers['tables']:
        application_table = Table('applications')
        try:
            application_table.create_table()
            print('The applications table has been created.')
        except Exception as e:
            print(e)

    if 'users' in answers['tables']:
        user_table = Table('users')
        try:
            user_table.create_table()
            print('The users table has been created.')
        except Exception as e:
            print(e)

    if 'requests' in answers['tables']:
        request_table = Table('requests')
        try:
            request_table.create_table()
            print('The requests table has been created.')
        except Exception as e:
            print(e)

    print('Table setup complete!')


def seed_prompt():
    questions = [
        inquirer.Checkbox('seed',
                          message="Choose which tables to seed",
                          choices=['badges', 'applications', 'users',
                                   'requests'],
                          default=['badges', 'applications', 'users',
                                   'requests']),
    ]
    answers = inquirer.prompt(questions)

    if 'badges' in answers['seed']:
        badge_table = Table('badges')
        try:
            for badge in badges:
                badge_table.overwrite(badge)
            print('The badges table has been seeded.')
        except Exception as e:
            print(e)

    if 'applications' in answers['seed']:
        application_table = Table('applications')
        try:
            for application in applications:
                application_table.overwrite(application)
            print('The applications table has been seeded.')
        except Exception as e:
            print(e)

    if 'users' in answers['seed']:
        user_table = Table('users')
        try:
            for user in users:
                user_table.overwrite(user)
            print('The users table has been seeded.')
        except Exception as e:
            print(e)

    if 'requests' in answers['seed']:
        request_table = Table('requests')
        try:
            for request in requests:
                request_table.overwrite(request)
            print('The requests table has been seeded.')
        except Exception as e:
            print(e)

    print('Table seeding complete!')


table_prompt()
seed_prompt()

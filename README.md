# echtiat-be

### Runing the app

To run the application: 
1. Move to the root folder of the app and activate a virtual enviorment:
```bash
source venv/bin/activate
```

2. Start the application
```bash
flask --app app run --debug
```

### DB migration

To create a migration script after changing or adding DB models, execute the following command:
```bash
flask db migrate -m "new table version"
```
A new migration script will be generated in migrations/versions/

To run the migration script:
```bash
flask db upgrade
```

### CLI Commands

To create a database with all defined tables, execute the following command in the app root directory:
```bash
flask cli create_db 
```

To populate the table with test data, execute:
```bash
flask cli populate_db 
```

To drop all tables in the database:
```bash
flask cli drop_db 
```

### Populate requirements file

To populate requirements.txt file with installed packages:
```bash
pip freeze > requirements.txt
```
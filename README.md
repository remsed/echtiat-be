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
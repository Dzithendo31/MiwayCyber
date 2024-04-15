# Setup


## Virtual ENV

```bash
python -m venv myenv
```

## Activate

```sh
 .\myenv\Scripts\Activate.ps1
```


## Changing the Database Connection String
If you need to change the database connection string, you can do so by modifying the .env file. Typically, the connection string is stored in a configuration file like config.py or settings.py. Locate the file where the database connection parameters are defined and update the relevant fields such as the host, port, username, password, and database name.

```python
LOCAL_DATABASE_URL = 'postgresql://username:password@localhost/mydatabase'
```
You would replace username, password, localhost, and mydatabase with the appropriate values for your database server.

Installing Required Packages
To install the required packages for this project, you can use the requirements.txt file. After activating your virtual environment, run the following command:

bash
Copy code
pip install -r requirements.txt
This will install all the packages listed in the requirements.txt file into your virtual environment, ensuring that you have the necessary dependencies to run the project.

Default Values to be Inserted in SQL Form
If you need to insert default values into your SQL database, you can do so using SQL statements or by setting default values in your database schema.

For example, if you have a table named users and you want to insert a default value for the created_at column, you can define it in your SQL schema like this:

sql
Copy code
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
In this example, the created_at column will default to the current timestamp when a new record is inserted if no value is provided explicitly.

Feel free to customize these instructions based on the specifics of your project! Let me know if you need further assistance.







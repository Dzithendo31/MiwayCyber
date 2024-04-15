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

## Installing Required Packages
To install the required packages for this project, you can use the requirements.txt file. After activating your virtual environment, run the following command:

```bash
pip install -r requirements.txt
```
This will install all the packages listed in the requirements.txt file into your virtual environment, ensuring that you have the necessary dependencies to run the project.

## Default Values to be Inserted in SQL Form
You'll need to insert default values into your SQL database, you can do so using SQL statements or by setting default values in your database schema.

For example, if you have a table named users and you want to insert a default value for the created_at column, you can define it in your SQL schema like this:

```sql

insert into policyStatus (name,color,description)
values
	('Under Review','#fedc00','Your policy is currently being looked at by our team. We are making sure everything is in order, and we might reach out if we need any additional information from you. This is a temporary stage, and we aim to move your policy to the next step as swiftly as possible.'),
	('Approved','#01af41','Your policy has been reviewed and meets all our criteria. It is now active, and you are fully covered according to the terms of your policy. You can rest easy knowing you are protected.'),
	('Suspended','#fe8741',' Your policy has been temporarily put on hold. This could be due to several reasons, such as discrepancies in your information, missed payments, or other issues that need resolution. Please check your account for details on how to address this, or contact us directly. We are eager to help get your policy back in good standing.'),
	('Claimed','#0161ad','This status indicates that a claim has been filed against your policy. Our claims department is currently processing it, and we will keep you updated every step of the way. We understand this can be a stressful time, so we are committed to handling your claim as quickly and smoothly as possible.');
```







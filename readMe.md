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

## Project Report


# Problem Statement

Insurance companies face significant challenges in adapting to rapidly changing business needs and customer expectations. Specifically, there is a lack of agile policy management systems that can swiftly incorporate new business requirements and customer insights. Additionally, potential customers often experience difficulties navigating insurance applications on existing platforms, which leads to lower customer satisfaction and reduced policy uptake. The goal is to develop a more intuitive and responsive system that simplifies the process of creating and updating insurance policies and enhances the customer registration and application process on the company’s website and app.

# Solution Design

We have designed a web application-based solution to allow Insurance companies to create and modify their polices based on the business needs for user to browse, view existing policies, update them and also apply for a new one. The solution offers significant features that enable the company to manage their policies and users.

# **Core Features of the Project**

The application that I design is called MiWayCyber, from the MiWay insurance company which is under the Sanlam Group. The basic idea of the MiWay cyber is to offer insurance for digital products like crypto and also protection from loss caused by data breaches and cyber extrusion which we will see a rank of these as the AI era is taking off with a significant impact on cyber security.

1. **User Registration**
    
    The web application allows the user to sign up to be part of the MiWay cyber customers, this does not make them a policy holder in any how, but only a registered customer.
    
    Registering opens up applying for a new policy based on the customer's needs.
    
2. **Registering for a Policy**
    
    New user and registered user can apply for a new policy on the web application, this is a simple process that only requires one form about the policy details, as the user details have already been registered in the web application, the customer has to agree to a declaration based on the policy before they can submit the policy.
    
    A new policy goes through a few steps before it can get approved, ‘In Review’, ‘Approved’, ‘Suspended’ and claimed for after it has been approved and the customer decides to claim for a loss for the policy.
    
    **Under Review**
    
    *‘Your policy is currently being looked at by our team. We are making sure everything is in order, and we might reach out if we need any additional information from you. This is a temporary stage, and we aim to move your policy to the next step as swiftly as possible.’*
    
    **Approved**
    
    *‘Your policy has been reviewed and meets all our criteria. It is now active, and you are fully covered according to the terms of your policy. You can rest easy knowing you are protected.’*
    
    **Suspended**
    
    *‘Your policy has been temporarily put on hold. This could be due to several reasons, such as discrepancies in your information, missed payments, or other issues that need resolution. Please check your account for details on how to address this or contact us directly. We are eager to help get your policy back in good standing.’*
    
    **Claimed**
    
    *‘This status indicates that a claim has been filed against your policy. Our claims department is currently processing it, and we will keep you updated every step of the way. We understand this can be a stressful time, so we are committed to handling your claim as quickly and smoothly as possible.’*
    
    This applies also to claims that user make when it is their time of need, in an event of loss due to for example digital identity fraud.
    
3. **Policy Management by the Admin.**
    
    The admin is allowed to change, approved, delete and update policies that are active above that they can also create new policies based on the business requirements. If a customer that is registered decides to claim an approved policy, then the admin can decline or approve the claim.
    
4. **Policy Management by the User.**
    
    Each user can access their policies and claims in one page, where they can either create a new one or claim an approved policy.
    
5. **Customer Management by Admin:**
    
    Each user can be view by the admin, this is where they can decline and delete the users based on the business background checks and underwriting. The admin page also allows the admin to adda new user, maybe at an intermediary level of an insurance business**.**
    
6. **Claim Processing:**
    
    If a customer’s policy is approved, then they can claim, this is designed to change the policy status as claimed and a new claim is created as ‘*under review’,* this fives the admin a chance to review the claim, decline it or approve it if it makes sense, this allows that not every claim has to be approved. After it has been approved then the status changes to approved allowing the user to visually know that they are claim has been approved and wait for communication from the insurance.
    

### **System Architecture:**

1. **Flask & Flask Framework Overview**:
    
    The application uses flask as a web application framework, allowing us to work on the backend and the frontend of the application. Requests are easily integrated from the backed to the frontend using jinja in html.
    
2. **Flask Routing and Views**:
    
    The application is modularly designed to group routes that are related to each other in one blueprint, this for example all user related route, like user/register, user/login can be found in the userBP.py, this was to improve the DX of the application. Other routes were designed dynamically based on the user input, for example user/<id>, will open a route of the user based on the user that is logged in.
    
3. **Templates and Static Files**:
    
    To continue to improve the DX in the web application source code, static files like images and CSS were grouped in one folder and all dynamic html files that were used in these applications were stored in the templates file, these included the base.html which using jinja it was inherited by almost all the html in the application.
    
4. **Databases and Models**:
    
    Using SQL Alchemy in flask we were able to connect with our SQL server database that was hosted in Azure, allowing use to perform CRUD operation on the table we created. This was made possible by defining Several classes of Models, allowing us to query the database with the python methods available.
    
5. **API Authentication and Authorization**:
    
    in the web application, we used flask login to protect the route and login for the user, meaning not all pages were freely accessed, and some pages needed only the admin rights to be accessed.
    
- Protect API routes using authentication mechanisms suitable for both web and mobile consumers.



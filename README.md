ONLINE BOOKSTORE
To run the program:

open terminal
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/79f91dea-1538-46b1-bfcc-977608056f7d)

By clicking on terminal you will find like this
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/c8239bb2-4073-4245-a809-fcdbfe4de31e)

 
run this below command
py manage.py runserver
you can find this in the terminal
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/87e1e30a-0736-40cb-a0a6-b8ce61d3f4ac)


now open this link in your browser 
http://127.0.0.1:8000/
you will find like this in your browser this is the home page of project
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/6adcb612-d55c-4178-a140-927a66d672fa)

--------------------------------------------------------------------------------------------------------------------------------------
Admin or Superuser privileges:

Now go to admin page by using this link http://127.0.0.1:8000/admin/
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/4329f4e6-32c2-4a70-9360-7c1440f23fec)

 
You will find the admin login page like above

login with admin credentials

What to do if you don’t have a superuseraccount?(No need to follow this section if you already have a superuser)
Open a new terminal in pycharm 
Enter the following command
py manage.py createsuperuser
give username , email, password and re-enter the password.
If it show this line “Bypass password validation and create user anyway? [y/N]:”
Type y and click on enter now you have superuser account and you can continue with the following steps

after successful login you will find like this
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/ba4188bb-e613-47ec-a186-339f47bde53d)

admin account is also called as super user
database is controlled by this super user
you can add, delete and manage users, groups, orders and books 
click on users and you can find all the users 
you can add , delete and manage them  
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/109edb75-5c17-46f6-91d6-ddb1b9bfc885)
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/58066a16-dc54-4ac8-a6ec-1f38cd6b2fe8)

You can similarly find for books and orders also.
You don’t have to open or use groups in this project
To logout from the admin account click on logout option from top right corner

User:

you will be redirected to home page
you can find anonymous user on to left , click on top of that you would find two options signup and login 
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/c4af6e89-9b1e-4160-808b-78cf51b09502)

--------------------------------------------------------------------------------------------------------------------------------------
Signup:

click on signup and you will be redirected to signup page 
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/cc7bd8f0-da80-428a-a396-025b9e050595)

provide the details and create a account


Note : Follow the requirements
 
 Username - 	Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
 
 Password - 	Your password can’t be too similar to your other personal information.
 		Your password must contain at least 8 characters.
 		Your password can’t be a commonly used password.
 		Your password can’t be entirely numeric.
 
 Password confirmation: 
  		Enter the same password as before, for verification.
 


After successful creation of account , you will automatically redirected to the login page

--------------------------------------------------------------------------------------------------------------------------------------
Login:
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/87b06020-f870-4b26-916f-fc89cd52dc08)

provide the username and password 

click on login and you will redirected to the home page

if you click on create account you will be redirected to signup page

--------------------------------------------------------------------------------------------------------------------------------------
Details of the site:
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/09bd9a18-d7b7-4565-bb88-a1a9656b6ab1)


On top right corner you can find a blue circle and when you place the cursor near it you can see the search option
 
 Type the name of book and click enter to find the books
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/9c431d91-fcaf-41a2-a103-4f50bdb66acd)
To go to home page click on the Online Book Store on top left corner
You can find the book title ,price and if the stock is available or not
Click on view button to know more about the book
 
![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/5aaebeb2-7e7a-498a-975c-e6c047c4fb3c)

Here you can find the book front cover, title, author and a little description of the book
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/bb7c319f-170a-4965-bf0a-bf1dc7370e4c)

You can also find a button as Follow author 
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/c23cd729-4d8d-4d79-859e-1ad3ee811140)

You can find the price of the book
 ![image](https://github.com/pavani-1510/OnlineBookStore/assets/158314455/36c3eef4-1a24-45bc-afd3-905a3d7f9497)

You can find a button buy now
When you click on the buy now button you will be redirected to the checkout page

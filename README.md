# OnlineBookStore
To run the program:


open terminal
 
By clicking on terminal you will find like this
 
run this below command
py manage.py runserver
you can find this in the terminal
 

now open this link in your browser 
http://127.0.0.1:8000/
you will find like this in your browser this is the home page of project
 
--------------------------------------------------------------------------------------------------------------------------------------
Admin or Superuser privileges:

Now go to admin page by using this link http://127.0.0.1:8000/admin/
 
You will find the admin login page like above

--------------------------------------------------------------------------------------------------------------------------------------
What to do if you don’t have a superuseraccount?(No need to follow this section if you already have a superuser)
Open a new terminal in pycharm 
Enter the following command
py manage.py createsuperuser
give username , email, password and re-enter the password.
If it show this line “Bypass password validation and create user anyway? [y/N]:”
Type y and click on enter now you have superuser account and you can continue with the following steps
--------------------------------------------------------------------------------------------------------------------------------------
after successful login you will find like this
 
admin account is also called as super user
database is controlled by this super user
you can add, delete and manage users, groups, orders and books 
click on users and you can find all the users 
you can add , delete and manage them  
 
You can similarly find for books and orders also.
You don’t have to open or use groups in this project
To logout from the admin account click on logout option from top right corner
--------------------------------------------------------------------------------------------------------------------------------------
User:

you will be redirected to home page
you can find anonymous user on to left , click on top of that you would find two options signup and login 
 
--------------------------------------------------------------------------------------------------------------------------------------
Signup:

click on signup and you will be redirected to signup page 
 
provide the details and create a account


Note : Follow the requirements
# 
# Username - 	Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
# 
# Password - 	Your password can’t be too similar to your other personal information.
# 		Your password must contain at least 8 characters.
# 		Your password can’t be a commonly used password.
# 		Your password can’t be entirely numeric.
# 
# Password confirmation: 
#  		Enter the same password as before, for verification.
# 


After successful creation of account , you will automatically redirected to the login page

--------------------------------------------------------------------------------------------------------------------------------------
Login:
 
provide the username and password 

click on login and you will redirected to the home page

if you click on create account you will be redirected to signup page

--------------------------------------------------------------------------------------------------------------------------------------
Details of the site:

On top right corner you can find a blue circle and when you place the cursor near it you can see the search option
 
 Type the name of book and click enter to find the books
 
To go to home page click on the Online Book Store on top left corner
You can find the book title ,price and if the stock is available or not
Click on view button to know more about the book
 

Here you can find the book front cover, title, author and a little description of the book
 
You can also find a button as Follow author 
 
You can find the price of the book
 
You can find a button buy now
When you click on the buy now button you will be redirected to the checkout page


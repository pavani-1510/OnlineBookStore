# 📚 Online Book Store

An Online Book Store web application developed using **JSP (JavaServer Pages)**, **Java**, and **MySQL**.  
This project allows users to browse books, manage their cart, and place orders. Admins can manage inventory and orders.

---

## 🌟 Features

- 🧑‍💼 User Registration and Login
- 📖 Browse Available Books
- 🛒 Add Books to Shopping Cart
- 💳 Checkout and Place Orders
- 📦 Admin Panel for Book Management
- 🧾 Order Viewing and Deletion
- 🎨 Clean UI using HTML and CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Frontend | HTML, CSS, JSP |
| Backend | Java (JSP) |
| Database | MySQL |
| Server | Apache Tomcat |

---

## 📁 Project Structure

```
OnlineBookStore-main/
├── book.sql                   # MySQL database script
├── cart.jsp                   # Add/view cart
├── checkout.jsp               # Checkout process
├── connection.jsp             # MySQL DB connection
├── deletecart.jsp             # Remove item from cart
├── deleteorder.jsp            # Admin deletes order
├── deleteproduct.jsp          # Admin deletes product
├── header.jsp                 # Common header
├── index.jsp                  # Homepage
├── login.jsp                  # User login
├── order.jsp                  # User places order
├── orders.jsp                 # Admin views all orders
├── product.jsp                # Admin adds new product
├── register.jsp               # New user registration
├── style.css                  # Frontend styling
├── updateorder.jsp            # Admin updates order
├── updateproduct.jsp          # Admin updates product
├── viewcart.jsp               # Cart overview
├── vieworder.jsp              # View placed orders
├── viewproduct.jsp            # View product catalog
```

---

## 🧑‍💻 Setup Instructions

### 1. Requirements

- Java JDK 8 or above
- Apache Tomcat 8/9
- MySQL Server
- Any IDE (Eclipse / IntelliJ) or text editor

---

### 2. Database Setup

1. Start MySQL server.
2. Import `book.sql` using the MySQL CLI or any GUI like phpMyAdmin:

```bash
mysql -u root -p < path/to/book.sql
```

3. Open `connection.jsp` and configure the connection:

```jsp
<%
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection(
        "jdbc:mysql://localhost:3306/book", "root", "yourpassword"
    );
%>
```

---

### 3. Run the Project

#### Option 1: Deploy on Tomcat Manually

1. Copy the `OnlineBookStore-main` folder to `webapps/` directory of your Tomcat.
2. Start Tomcat server (`startup.bat` or via Eclipse).
3. Open browser and visit:  
   `http://localhost:8080/OnlineBookStore-main/`

#### Option 2: Using Eclipse (Dynamic Web Project)

1. Import the folder as a Dynamic Web Project.
2. Right-click project → Run As → Run on Server.
3. Visit the local server URL in your browser.


-----------------------
## Author
- [R Pavani](https://www.linkedin.com/in/r-pavani/)
- [GitHub](https://github.com/pavani-1510/)

---

© 2025 R Pavani. All rights reserved.

---

<h1 align="center">SellCycle</h1>


[View the live project here](https://sell-app-cycle-f7894996863d.herokuapp.com/)


SellCycle is an online website for buying, selling, and exchanging new and secondhand clothing, accessories, and more. 
It offers users a convenient way to declutter their closets, discover fantastic deals, and give preloved items a new lease on life. With a focus on sustainability, SellCycle promotes an eco-friendly shopping experience that benefits both individuals and the planet.


![](static/images/12.png)



# Index

1. [User Experience (UX)](#user-experience-ux)
2. [Features](#features)
3. [Design](#design)
4. [Planning](#planning)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

# User Experience(UX)

 ### User stories :

*  Navigate site
   - As a **Site User** I can **view the item listed** so that **I can easily access application functionality**
*  View products list
   - As a **Site User** I can **view a list of products** so that **I can select one to access more details or purchase**
*  View item information
   - As a **Site User** I can **click on a product** so that **I can view its full details**
*  Buy a product
   - As a **Site User** I can **see a selection of items** so that **which I can choose from**
*  View the categories section
   - As a **Site User** I can **access a list of categories of items** and purchase the wanted item**
*  Delete/Edit a product listed
   - As a **Site User** I can **cancel a hike I have booked** so that **a place is no longer reserved for me**
*  View likes
   - As a **Site User** I can **view the number of likes on each number** so that **I can see which are most popular**
*  Like / Unlike an item
   - As a **Site User** I can **like or unlike an item** so that **I can increase the product popularity**
*  Contact seller
   - As a **Site User** I can **contact the seller** so that **I can give ask for more information**
*  View past conversations
   - As a **Site User** I can **view past conversations** so that I can stay in contact**with the customers**
*  Approve comments
   - As a **Site Admin** I can **review and then approve or disapprove comments** so that **unsuitable or objectionable content can be filtered out**
*  Account registration and login
   - As a **Site User** I can **add item and description**of the product  **that I want to sell**
*  Manage stock
   - As a **Site Admin** I can **create, read, update and delete items** so that **I can manage site content and  availability**
*  Add items 
   - As a **Site Admin** I can **add items and images** so that **I can finish writing the content later and release once approved**
* Browse items
  - As a **Site User** I can **access a list of items in that past that I added** so that **I can see products I have previously added**



## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used Balsamiq to design my site wireframes.

[Balsamiq](https://balsamiq.com/wireframes) 
  
## Mobile Wireframes

<details>

<summary>
Click here to see the Mobile Wireframes
</summary>

</details>


### Desktop Wireframes

<details>

<summary>
Click here to see the Desktop Wireframes
</summary>

</details>

### Tablet Wireframes

<details>

<summary>
Click here to see the Tablet Wireframes
</summary>
</details>


##  Features
- SellCycle is a comprehensive web application developed using the Django framework, designed to provide a user-friendly platform for individuals looking to buy and sell second-hand items. This project enables users to easily add items for sale, browse available listings, and engage with other users. With an intuitive interface, sellers can efficiently manage their listings  while buyers can search, filter, and find great deals on pre-owned products. Users have the ability to **create**, **read**, **update**, and **delete** their listings, as well as manage their accounts seamlessly.

### Navigation Bar

 - Consistent Design: The navigation bar provides a cohesive design and layout across all pages, ensuring easy access to essential sections of the site.
 - Quick Navigation: It includes the SellCycle logo and a link to the homepage for fast navigation.
 - User Authentication: For users who are not logged in, options to register or log in are clearly displayed. Once logged in, the navigation bar updates to show the 
   Catalogue as well as add products along with a personalized greeting that includes the user’s name and a profile icon.
 - Responsive Design: The navigation bar is optimized for responsiveness, adapting seamlessly to various screen sizes. On mobile devices, it transforms into a compact 'hamburger' menu, allowing effortless navigation without cluttering the interface.
 

### Navigation Bar Views

<details>
<summary>Unregistered User Navigation Bar View</summary>
<img src="static/images/navbar-login.png" alt="Unregistered User Navigation Bar" width="600">
</details>

<details>
<summary>Registered User Navigation Bar View</summary>
<img src="static/images/logout-navbar.png" alt="Registered User Navigation Bar" width="600">
</details>

<details>
<summary>Burger Menu View</summary>
<img src="static/images/mobile-navbar.png" alt="Burger Menu View" width="600">
</details>


### User Authentication (SignUp, Login, Logout)

- User authentication methods have been integrated to ensure that users can only list items for sale if they are logged in. Existing users must log in to access the selling features, while new users can easily register before making a listing request.

Dedicated login and logout pages provide a secure authentication experience. If a user attempts to log in with an incorrect username or password, immediate on-screen feedback is given, prompting them to enter the correct credentials. Additionally, a required feature ensures that users must fill in both the username and password fields, preventing incomplete submissions and enhancing overall security.

<details>
<summary>Sign Up or Login  to be able to add items</summary>
<img src="static/images/add.png"  width="600">
</details>

<details>
<summary>Login/Logout Forms</summary>
<img src="static/images/login-form.png"  width="600">

<img src="static/images/signUp-form.png"  width="600">
</details>

<details>
<summary>Existing user alert</summary>
<img src="static/images/alert.png"  width="600">
</details>



### Landing Page


<details>
<summary>Landing Page</summary>
<img src="static/images/landing-page.png"  width="700">
</details>

 At the top of the landing page, a striking area showcases a vibrant image of diverse products available for buying and selling. This compelling visual communicates SellCycle's purpose as a dynamic platform for facilitating seamless transactions. The branding prominently features the SellCycle name, reinforcing the site's mission to connect users in a convenient and intuitive marketplace experience.


### Add items

<details>
<summary>Add items</summary>
<img src="static/images/add.png"  width="600">
</details>

When an authenticated user logs into their account, they gain access to a streamlined interface that allows them to easily add items they wish to sell. This feature empowers users to list their products quickly, with a user-friendly form guiding them through the process. Users can upload images, provide detailed descriptions, set prices, and manage their listings effortlessly, making it simple to showcase their items to potential buyers.



### Listing Items

Item Listing System
The item listing page features an eye-catching image of the product alongside a detailed description and associated pricing information. When a user wants to list an item for sale, they must provide their Name, Category , Price, and any additional required information about the item they wish to sell.
An  "Add" button is prominently displayed at the bottom of the form, allowing users to finalize their item listing.


###  CRUD Functionality for Listings

The Create, Read, Update, and Delete (CRUD) functionality is crucial for managing user listings on SellCycle. After logging in, users have access to buttons that allow them to edit or delete their listings. They can also view their current listings at any time.

- **Edit Button**: If a user wishes to change the details of their listing, an Edit button is readily available. Upon clicking this button, users can modify the listing information, and once confirmed, the updates are applied immediately.

- **Delete Button**: Users can also easily remove their listings by clicking the Delete button. This functionality ensures that users have full control over their items and can manage their listings efficiently.

This streamlined process enhances user experience by providing intuitive options for managing listings directly from their account dashboard.

### Inbox

<details>
<summary>Message the seller</summary>
<img src="static/images/message.png"  width="600">
</details>

 The **inbox feature** is an essential component of our platform, providing users  the chances to communicate seamlessly regarding their transactions. This feature allows buyers and sellers to send and receive messages, facilitating inquiries about listings, negotiations on prices, and coordination for pick-up or delivery. The inbox is designed with user privacy in mind, allowing for secure communication while enhancing the overall buying and selling experience. 



### Catalogue 

<details>
<summary>Catalogue</summary>
<img src="static/images/catalogue.png"  width="600">
</details>

The **catalogue feature** provides users with an organized and visually appealing way to browse a wide range of second-hand items. It allows buyers to filter and sort listings by categories, price, and more, ensuring a seamless shopping experience. Each item includes detailed descriptions and high-quality images, helping users make informed decisions. Regular updates keep the catalogue fresh, encouraging users to explore the latest offerings and enhancing overall engagement on the platform.




### Browse 

<details>
<summary>See products and their prices listed </summary>
<img src="static/images/browse.png"  width="600">
</details>

The **browse feature** allows users to easily explore a wide variety of second-hand items available for sale. With intuitive navigation and filtering options, buyers can quickly find products that match their interests and needs. This feature supports seamless scrolling through listings, showcasing high-quality images and essential details for each item. By making the discovery process effortless, the browse feature enhances user engagement and encourages more interactions within the marketplace.



### Categories

<details>
<summary>See the available categories  </summary>
<img src="static/images/categories.png"  width="600">
</details>

 The **categories feature** organizes listings into distinct groups, making it easier for users to navigate and find specific types of second-hand items. By categorizing products—such as women, mens, kids, can quickly hone in on their interests. Users can effortlessly explore and discover items that suit their needs.


### SellCycle: PostgreSQL Database & Super User Creation

The admin interface of SellCycle offers a user-friendly graphical user interface (GUI) for managing data related to selling and adding items. Administrators can easily create, read, update, and delete product listings and conversations without needing direct access to the database. They can add new items across categories such as Women, Men, and Kids, complete with relevant details like price, description, and featured images. Additionally, admins can manage conversations between users, modifying or deleting them as necessary.

Non-technical users, such as business managers and customer service representatives, can navigate the Django admin interface without needing to understand the underlying code. The auto-generated forms make it straightforward to add, edit, or remove entries.

### Database Integration:

### SellCycle: Admin Functionality for Managing Listings

The admin user can add and publish items through the admin pages of SellCycle. These pages are accessible either by appending '/admin' to the application URL or by signing in and clicking the Admin link, which appears in the navigation bar only when the admin is logged in.
To add a new item, the admin can click the "+ Add" link next to the table name and then fill in the required data fields. A rich text editor (Summernote) is provided for the item description, allowing for easy formatting. If the admin user does not upload an image, a default image will be used for the item. This functionality streamlines the process of managing listings and ensures a consistent presentation on the platform.

<details>
<summary>User interactions managed through the Django admin panel</summary>
<img src="static/images/admin.png"  width="600">
</details>


<details>
<summary>The admin user can select the category and add items</summary>
<img src="static/images/admin.png"  width="600">
</details>



 <details>
<summary> Admin effectively handling conversations</summary>
<img src="static/images/admin.png"  width="600">
</details>


### SellCycle: Responsive Design with Bootstrap

Responsive design ensures that SellCycle functions seamlessly across all devices, from desktops to smartphones. By leveraging Bootstrap, the website automatically adapts its layout and appearance based on screen size, providing a consistent user experience. Below are key aspects of how Bootstrap enhances responsiveness and builds user trust.

**Navbar**: The navbar-toggler feature collapses the menu on smaller screens, improving usability for mobile users. This ensures that navigation remains straightforward, regardless of device.

**Container-fluid**: This class guarantees that content adjusts fluidly to various screen widths. Bootstrap’s grid system (e.g., col-md-8, offset-md-2) organizes elements effectively, maintaining proper spacing and alignment.

**Form Styling**: User experience and accessibility are prioritized with Bootstrap form controls (form-control, form-group), ensuring that all forms are consistently styled and responsive across devices.

**CSRF Token**: Security is paramount, with Django’s CSRF protection implemented to safeguard forms from malicious attacks.

**Button Styling**: Actionable elements like "Sign in" are styled with Bootstrap's btn classes, making them easily recognizable and engaging.

**Font Awesome Icons**: The use of icons, such as user and social media icons, enhances visual interest and usability throughout the site.

**Branding**: A custom logo and favicon reinforce brand identity, contributing to a cohesive user experience.

**Content Focused on Trust**: Building trust is essential for user engagement. SellCycle fosters trust through:

- **Clear Navigation**: The navbar directs users to vital pages like "Sign in," "Sign Up," and "My Items," promoting transparency and ease of access.
- **Personalized Experience**: Displaying the logged-in user’s name (e.g., Hi, {{ user.username }}) in the navbar reassures users of their secure session.
- **Social Proof**: Links to social media profiles, such as GitHub, LinkedIn, and Twitter, demonstrate the company's connections to reputable networks.
- **Secure Practices**: Implementing user authentication and form validation enhances credibility and user confidence.



### How Existing Features Address User Stories

The User Stories in the User Experience (UX) section of this document are numbered from 1 to 10, while the existing features are labeled as F01 to F07. Below is a traceability matrix that cross-references the user stories with the corresponding features, demonstrating how each feature supports specific stories:


<details>
<summary>Traceability Matrix Graphic</summary>
<img src="static/images/d"  width="600">
</details>


###  Features which could be implemented

*Buy Integration for User Items*
- Implementing a buy integration feature on SellCycle will enable users to purchase items directly through the platform, creating a seamless shopping experience. This feature is essential for facilitating transactions between buyers and sellers efficiently.


*Instant Checkout*

- A streamlined checkout process that minimizes steps, enabling users to complete their purchases swiftly. This includes reviewing item details, confirming shipping information, and selecting payment options.

*Inventory Management*

- Real-time updates to item availability to ensure users can only purchase items that are in stock, reducing the risk of overselling.

*Order Confirmation*

- Automated email or in-app notifications confirming the purchase details, including item description, price, and estimated delivery time, to enhance user trust.


*Like/Unlike Functionality for User Items*

- Implementing a like/unlike feature for items added by users can significantly enhance engagement on SellCycle. This feature would allow users to express their appreciation for items by clicking a "like" button. Each user would have the ability to like or unlike items, with the status being tracked in the database to ensure accurate counts and user interactions.

*Shopping Cart Functionality for User Items*

- Introducing a cart feature for user-added items on SellCycle can enhance the shopping experience significantly. This feature would allow users to save items they’re interested in purchasing, facilitating a smoother transaction process.

*Payment Integration for Users*

- Implementing a payment integration feature for user-added items on SellCycle will streamline the purchasing process and enhance user convenience. This feature would allow users to complete transactions directly through the platform, making it easier to buy items they are interested in.

*Transaction History*

- A section in user profiles where they can view their past purchases and payment history, adding transparency and convenience.

*Loyalty and Referral Programs*

- Introducing loyalty and referral programs on SellCycle can enhance user engagement and encourage repeat transactions. These features would reward users for their activity on the platform, fostering a sense of community and encouraging word-of-mouth promotion.

## Entity-Relationship Diagram (ERD)

<details>
<summary>ER diagram:</summary>
<img src="static/images/diagram.png"  width="600">
</details>


### Notes on the ER diagrams :
- User: Represents the customer who adds the items. This is a foreign key referencing Django's built-in User model.
- Listing: Represents different categories available for selling an item, such as "Women", "Mens", and "Kids". Each item has attributes such as:

  - category: The type of item being sold.
  - price: The cost of the item.
  - description: Details about the item.
  - featured_image: Image associated with the item.
  - image: An optional image 
- Product: Represents a product available for sale. Key attributes include:
  - category: Links the product to a specific category using a foreign key.
  - name: The name of the product.
  - featured_image: An optional image associated with the product, uploaded using Cloudinary.
  - description: Details about the product; this can be blank or null if no description is provided.
  - image: An additional optional image for the product, also uploaded using Cloudinary.
  - price: The cost of the product.
  - is_sold: A boolean indicating whether the product has been sold.
  - created_at: Automatically set to the current date and time when the product is created.
  - created_by: Links the product to the user who created it using a foreign key.

- Relationships
   - User to Product: This is a one-to-many relationship. A user can create multiple products, but each product is associated with one user.

   - Category to Product: This is a one-to-many relationship. A category can have multiple products, but each product belongs to one category.
   Product to Category: one-to-many . Each product is linked to one category via the category foreign key. A single category can have multiple products associated with it. This relationship helps organize products, allowing users to filter and browse items by category. The related_name='products' allows for easy access to all products in a specific category.
  
   - Product to User: one-to-many relathionship. Each product is associated with one user through the created_by foreign key. A user can create multiple products, but each product belongs to a single user. This relationship enables users to manage their own products. The related_name='products' allows access to all products created by a specific user.


- Benefits of This Structure
  - Organization: The relationships and unique constraints create a well-structured database. This organization allows for efficient querying and management of products.

  - Data Integrity: The unique constraint prevents duplicates, ensuring that the product catalog remains clear and easy to navigate.
  The foreign key relationships ensure that the database remains consistent, as deleting a category or user also cleans up associated products.

  - User Management: Linking products to users allows for personalized experiences where users can manage their own products and view their inventory.

  - Foreign Key Constraints:

Description: The foreign keys (category and created_by) ensure that each product must be associated with a valid category and user. If a category or user is deleted, all associated products will also be deleted due to on_delete=models.CASCADE. This maintains referential integrity in the database. Ensures that a product cannot exist without a valid category and creator, preventing orphaned records.

The Product model effectively manages relationships and constraints to ensure data integrity and usability within the application. By linking products to categories and users, it provides a structured way to handle inventory while maintaining referential integrity.
## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

### Technologies Used

- **Google Fonts:** Implemented the Josefin Sans font to enhance the site's typography.
- **Font Awesome:** Incorporated to provide icons that improve both aesthetics and user experience.
- **Git:** Utilized for version control, employing the Gitpod terminal for committing changes and pushing updates to GitHub.
- **GitHub:** Acts as the project's code repository, facilitating agile development through User Stories (GitHub Issues) and tracking progress on a Kanban board.
- **dbdiagram.io:** Used to create Entity Relationship diagrams that represent the application’s data model.
- **Balsamiq:** Applied to design wireframes during the planning phase, aiding in the visual structure of the application.
- **Django:** The framework chosen for its ability to support rapid and secure application development.
- **Bootstrap:** Used to create responsive web pages, ensuring a seamless experience across devices.
- **Gunicorn:** The web server selected to run the Django application on Heroku.
- **dj_database_url:** A library that simplifies the connection to PostgreSQL databases through URL configuration.
- **psycopg2:** The database adapter that enables communication with PostgreSQL databases.
- **Cloudinary:** Utilized for storing and managing images used throughout the application.
- **Summernote:** Integrated for rich text editing capabilities in the "ADDITIONAL TEXT" field when users create or edit bookings.
- **Django Allauth:** Employed to manage user registration and authentication processes effectively.
- **Django Crispy Forms:** Facilitates cleaner and more efficient form rendering.
- **jQuery:** Utilized to enhance user interactions by fading out alert messages smoothly.
- **Django Testing Tools:** Used for testing the application’s Model-View-Template (MVT) architecture to ensure reliability.

### Agile Development with Github

- For the SellCycle project, GitHub Issues served as the Agile management tool. User Stories, complete with acceptance criteria, were defined and tracked through GitHub Issues, while development progress was organized using a Kanban board. Each User Story was linked to a 'parent' Epic issue, illustrating how they contribute to the project's overarching objectives. Acceptance criteria were rigorously tested as each story progressed to the 'Done' column, and they were also included in the comprehensive manual testing outlined in the Testing section of this README.
You can access the Epic, User Stories, and Kanban board here: [Kanban Board](https://github.com/users/Esty-8/projects/9)

### Testing

- HTML Validation

Since this project utilizes Django templates, the HTML has been validated by manually executing the application pages, copying the source of the rendered pages, and then validating this version of the HTML using the [W3C Validator](https://validator.w3.org). The HTML for the Django admin site pages was not edited, so it has not been validated here. The Signup/Registration form, Login, and Logout pages from Django Allauth were remodeled and have been validated, with results provided below.There were a few  issues encountered during the validatotion process which didn't resulted in the code not fully validated.

<details>
<summary> Validation result for foundation.html
</summary>
<img src="static/images/foundation.png"  width="600">
</details>

<details>
<summary>Validation result for login.html</summary>
<img src="static/images/login.png"  width="600">
</details>

<details>
<summary>Validation resign for Sign In Page </summary>
<img src="static/images/signup.png"  width="600">
</details>


<details>
<summary> Validation result for Catalogue  Page</summary>
<img src="static/images/products.png"  width="600">
</details>


<details>
<summary> Validation result for Browse Page</summary>
<img src="static/images/b.png"  width="600">
</details>

<details>
<summary>Validation result for Inbox Page</summary>
<img src="static/images/inbox.png"  width="600">
</details>















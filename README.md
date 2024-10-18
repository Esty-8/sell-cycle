<h1 align="center">SellCycle</h1>


[View the live project here](https://sell-app-cycle-f7894996863d.herokuapp.com/)


SellCycle is an online website for buying, selling, and exchanging new and secondhand clothing, accessories, and more. 
It offers users a convenient way to declutter their closets, discover fantastic deals, and give preloved items a new lease on life. With a focus on sustainability, SellCycle promotes an eco-friendly shopping experience that benefits both individuals and the planet.


![](static/images/Screenshot4.png)



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


#  Features


### Navigation Bar

 - Consistent Design: The navigation bar provides a cohesive design and layout across all pages, ensuring easy access to essential sections of the site.
 - Quick Navigation: It includes the SellCycle logo and a link to the homepage for fast navigation.
 - User Authentication: For users who are not logged in, options to register or log in are clearly displayed. Once logged in, the navigation bar updates to show the 
   Catalogue as well as add products along with a personalized greeting that includes the user’s name and a profile icon.
 - Responsive Design: The navigation bar is optimized for responsiveness, adapting seamlessly to various screen sizes. On mobile devices, it transforms into a compact      'hamburger' menu, allowing effortless navigation without cluttering the interface.
  Desktop

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

### Landing Page
- At the top of the landing page, a striking area showcases a vibrant image of diverse products available for buying and selling. This compelling visual communicates SellCycle's purpose as a dynamic platform for facilitating seamless transactions. The branding prominently features the SellCycle name, reinforcing the site's mission to connect users in a convenient and intuitive marketplace experience.

<details>
<summary>Landing Page</summary>
<img src="static/images/login.png"  width="700">
</details>



**Add items**

- When an authenticated user logs into their account, they gain access to a streamlined interface that allows them to easily add items they wish to sell. This feature empowers users to list their products quickly, with a user-friendly form guiding them through the process. Users can upload images, provide detailed descriptions, set prices, and manage their listings effortlessly, making it simple to showcase their items to potential buyers.

### User Authentication (SignUp, Login, Logout)

- User authentication methods have been integrated to ensure that users can only list items for sale if they are logged in. Existing users must log in to access the selling features, while new users can easily register before making a listing request.

Dedicated login and logout pages provide a secure authentication experience. If a user attempts to log in with an incorrect username or password, immediate on-screen feedback is given, prompting them to enter the correct credentials. Additionally, a required feature ensures that users must fill in both the username and password fields, preventing incomplete submissions and enhancing overall security.

<details>
<summary>Sign Up and Login in to add items</summary>
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


### Listing Items

- Item Listing System
The item listing page features an eye-catching image of the product alongside a detailed description and associated pricing information. When a user wants to list an item for sale, they must provide their Name, , Category , Price, and any additional required information about the item they wish to sell.
- An  "Add" button is prominently displayed at the bottom of the form, allowing users to finalize their item listing.

Key Features:
Custom Input Fields: Tailored fields ensure comprehensive data collection.

### Inbox

<details>
<summary>Message the seller</summary>
<img src="static/images/"  width="600">
</details>


### Catalogue 
<details>
<summary></summary>
<img src="static/images/"  width="600">
</details>


### Browse 
<details>
<summary>See products and their prices listed </summary>
<img src="static/images/"  width="600">
</details>

### Categories
<details>
<summary>See the available categories  </summary>
<img src="static/images/"  width="600">
</details>










### Future Features

 
 - Users will have CRUD functionality and autonomy on their profiles





- **Browse**

 -
 -

- **Dashboard**
 - 
 - To keep track of the items added.

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













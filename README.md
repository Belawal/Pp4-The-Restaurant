# The Restaurant

![Screen Responsive](<assets/images/screen responsive.png>)

Welcome to our restaurant website — a smart and easy way to manage bookings and connect with your customers online.

This website is made to help both the restaurant owner and the customers. Customers can easily check available tables and book their seats online anytime. This saves them time and gives them a smooth experience.

For the restaurant owner, the website helps to keep track of all reservations in one place. You can see which times are busy, which tables are booked, and avoid overbooking. This helps you manage your team and kitchen better, and improves customer service.

Key Features:
Online Table Booking: Customers can book a table through the website, 24/7.

Email Confirmation: After booking, customers get an email to confirm their reservation.

User Accounts: Customers can sign up, log in, and view their past bookings.

Admin Dashboard: The owner can see all bookings, cancel reservations, and update booking settings.

Mobile Friendly: The website works on phones, tablets, and computers.

Benefits:
For Customers: Quick and easy way to book a table, with clear confirmation and less waiting.

For Owner: Save time, reduce booking mistakes, and give better service by planning ahead.

This website helps bring your restaurant online and gives your business a more professional image.



### Visitor Goals
- Learn about the restaurant's menu and offerings.
- Contact the restaurant via the contact form.

### User Goals
- Sign up, log in, and manage their reservations.
- View available menu items.
- Cancel reservations if needed.

### Business Goals
- Simplify the reservation process.
- Manage and track customer reservations efficiently.
- Provide a contact point for customer inquiries.

## Features

- **User Authentication:** Sign up, log in, and log out securely.
- **Reservation System:** Users can book tables and view or cancel their reservations.
- **Admin Panel:** Admins can view all reservations and cancel them.
- **Menu Page:** Displays a sample menu with dishes and prices.
- **Contact Form:** Users can send messages via a contact form.

## User Stories
1. As a, user I want to register an account so that I can book a table.
2. As a user, I want to log in to my account so that I can access my bookings.
3. As a user, I want to log out of my account so that I can securely end my session.
4. As a user, I want to reset my password so that I can regain access to my account.
5. As a user, I want to book a table for a specific date and time so that I can reserve a spot.
6. As a user, I want to view my bookings so that I can manage them.
7. As a user, I want to edit my bookings so that I can update the date, time, or number of guests..
8. As a user, I want to cancel my bookings so that I can free up my reservation.
9. As an admin, I want to log in to an admin dashboard so that I can manage bookings.
10. As an admin, I want to view all bookings so that I can manage them.
11. As an admin, I want to filter bookings by date so that I can view reservations for a specific day.
12. As a developer, I want to test the application so that I can ensure it works as expected.
13. As a developer, I want to deploy the application to a cloud platform so that it is accessible to users.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Pp4-The-Restaurant.git
    cd Pp4-The-Restaurant
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (for admin access):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the app at [http://localhost:8000](http://localhost:8000).

## Deployment Instructions

### Deploying Locally

1. Ensure your virtual environment is active and dependencies are installed.
2. Collect static files:

    ```bash
    python manage.py collectstatic
    ```

3. Update `ALLOWED_HOSTS` in `settings.py` to include your domain or IP address.
4. Run the server:

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

### Deploying to Heroku

**Note:** The deployment to Heroku was unsuccessful due to it not recognizing the student plan and requesting payment.

### Deploying to GitHub Pages

1. Open GitHub and select your repository.
2. Go to **Settings**.
3. Scroll down to **GitHub Pages**.
4. Select the deployment source from "None" to "main" and save.
5. Refresh the page and check the deployment section for the provided link : https://github.com/Belawal/Pp4-The-Restaurant.git

## Main Pages

- Home: `/`
- Sign Up: `/signup/`
- Log In: `/login/`
- Reservation: `/reservation/`
- User Reservations: `/user-reservations/`
- Admin Reservations: `/admin-reservations/`
- Menu: `/menu/`
- Contact: `/contact/`

## Admin Access

- Go to `/admin/` to log in as an admin.
- **Username:** Admin
- **Password:** ADMIN101

## Technologies Used

- Django (Python Web Framework)
- HTML/CSS (Templates and Styling)
- BootStrap

## Color Scheme

- **Background:** Light neutral tones (#F5F5F5)
- **Primary Color:** Deep red (#B22222) for buttons and highlights
- **Secondary Color:** Soft beige (#FAEBD7) for accents
- **Text:** Dark gray (#333333) for better readability

## Responsive Design

This project is responsive and works well on different screen sizes:

- Mobile (up to 768px)
- Tablet (768px - 1024px)
- Desktop (1024px and above)
![Responsive View](assets/images/ScreenshotuiDev.jpg)

## Wireframes
    Wireframe with a basic layout for various screen sizes, also will contain the smae structure fo the enitre webstite

![wireframe](<assets/images/wireframeLayout.jpg>)
![wireframe](<assets/images/wireframeLayout2.jpg>)
![wireframe](<assets/images/wireframeLayout3.jpg>)

## Testing & Validation
- HTML code checked and passed using W3C HTML5 Validator.
- CSS validated with W3C CSS Validator and autoprefixer used.
- All links tested using W3C Link Checker.

## Debugging and Testing
During the setup and initial execution of the Django project, several issues were encountered. This section outlines these issues and their solutions:

**Error #1: Template Context Not Displaying Data**
- **Issue:** Data from `views.py` not showing in HTML templates.
- **Solution:** Ensure you pass context using `render()` and use correct template variable names.

**Error #2: Migration Not Applying**
- **Issue:** Changes in models not reflecting in the database.
- **Solution:**

**Error #3: Form Not Saving Data**
- **Issue:** Form submission doesn't save to the database.
- **Solution:** Ensure `form.is_valid()` is checked, and use `form.save()` method.

**Error #4: Static Files Not Loading**
- **Issue:** CSS/JS files not loading on the page.
- **Solution:** Use `{% load static %}` and correct `{% static 'path/to/file.css' %}` syntax.

**Error #5: Module Not Found Error**
- **Issue:** Django module or package not found.
- **Solution:** Ensure the app is listed in `INSTALLED_APPS` and imports are correct.

**Error #6: IntegrityError (Unique Constraint Failed)**
- **Issue:** Duplicate data causing database constraint failure.
- **Solution:** Check for unique fields and handle duplicates in views.

**Error #7: no such table: booking_reservation**
- **Issue:** Attempt to access a non-existent table in SQLite.
- **Solution:** Ensure migration files are applied:

**Error #8: Login and Signup Pages Not Working**
- **Issue:** Login and signup templates not rendering.
- **Solution:** Ensure templates are in the correct directory and views are defined properly.

## Future Improvements

- Add reservation editing.
- Improve UI/UX.
- Integrate email notifications.

## Deployment
**Github**
1. Push your code to a GitHub repository.
2. Log in to your GitHub account.
3. Go to the repository on GitHub → Settings → Pages.
4. Under "Source," select the branch (`main`) and folder (`root`).
5. Save and wait a few minutes for the site to be live.
6. Site will be available at `https://github.com/Belawal/Pp4-The-Restaurant.git`.

**Heroku**
1. Go to (heroku.com) and log in.
2. Click New → Create new app.
3. Enter an app name and then click Create app.
4. In the app dashboard, go to the Deploy tab.
5. Under Deployment method, select GitHub.
6. Connect your GitHub account and search for your repository.
7. Click Connect next to your repo.
8. Choose the branch you want to deploy (`main`).
9. Click Deploy Branch to start the deployment.

## LINKS
**GITHUB** :https://github.com/Belawal/Pp4-The-Restaurant.git
**HEROKU APP** :https://resturant-pp4-9aa9c2dc0d6f.herokuapp.com/

## License

This project is for educational purposes.


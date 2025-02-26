# The Restaurant

![Screen Responsive](<assets/images/screen responsive.png>)

This is a Django-based web app that lets users make restaurant reservations. Users can sign up, log in, and manage their bookings. Admins can view and cancel any reservation.

## Goals

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

## How It Works

1. Users sign up or log in.
2. Logged-in users can make, view, and cancel their reservations.
3. Admins can view and cancel any reservation through a dedicated panel.

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
![Responsive](<assets/images/screen responsive.png>)

## Wireframes
    Wireframe with a basic layout for various screen sizes
![wireframe](<assets/images/wireframe layout.png>)
![wireframe](<assets/images/wireframe layout 2.png>)
![wireframe](<assets/images/wireframe layout 3.png>)

## Debugging and Testing

During the setup and initial execution of the Django project, several issues were encountered. This section outlines these issues and their solutions:

**Error #1: Template Context Not Displaying Data**
- **Issue:** Data from `views.py` not showing in HTML templates.
- **Solution:** Ensure you pass context using `render()` and use correct template variable names.

**Error #2: Migration Not Applying**
- **Issue:** Changes in models not reflecting in the database.
- **Solution:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

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

    ```bash
    python manage.py migrate booking
    ```

If the error persists, check the migration history:

    ```bash
    python manage.py showmigrations
    ```

Reset migrations if needed:

    ```bash
    python manage.py migrate booking zero
    python manage.py makemigrations booking
    python manage.py migrate booking
    ```

**Error #8: Login and Signup Pages Not Working**
- **Issue:** Login and signup templates not rendering.
- **Solution:** Ensure templates are in the correct directory and views are defined properly.

Restart the server:

    ```bash
    python manage.py runserver
    ```

## Future Improvements

- Add reservation editing.
- Improve UI/UX.
- Integrate email notifications.

## License

This project is for educational purposes.


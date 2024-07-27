# Django Retreats API

This project is a Django-based API for managing retreats, including filtering, searching, and pagination functionalities.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Additional Information](#additional-information)

## Prerequisites

Before setting up the application, ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package installer)
- Virtualenv (optional but recommended for virtual environments)

## Setup Instructions

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/Ekagra/shoonyalife
   cd shoonyalife
   ```

2. **Create and Activate a Virtual Environment:**

  ```sh
  python -m venv .venv
  source .venv/bin/activate  
  # On Windows use `.venv\Scripts\activate`
  ```

3. **Install Dependencies:**

```sh
pip install -r requirements.txt
```

4. **Apply Migrations:**

```sh
python manage.py migrate
```

5. **Start the Development Server:**
```sh
python manage.py runserver
```
## API Endpoints
- **Host:** `https://shoonyalife.onrender.com`

### 1. Retreats

**List Retreats**
- **Endpoint:** `/api/retreats/`
- **Method:** GET
- **Description:** Retrieve a list of all retreats.
- **Example Request:** `GET https://shoonyalife.onrender.com/api/retreats/`
- **Query Parameters:**
  - `location`: Filter retreats by location (e.g., `?location=Pune`)
  - `price`: Filter retreats by price (e.g., `?price=500`)
  - `duration`: Filter retreats by duration (e.g., `?duration=3`)
  - `search`: Search retreats by title or description (e.g., `?search=Wellness`)
  - `page`: Pagination page number (e.g., `?page=1`)
  - `limit`: Number of items per page (e.g., `?limit=5`)

**Retrieve a Single Retreat**

- **Endpoint:** `/api/retreats/{id}/`
- **Method:** GET
- **Description:** Retrieve details of a specific retreat by ID.
- **Example Request:** `GET https://shoonyalife.onrender.com/api/retreats/1/`

### 2. Bookings

**Create a Booking**

- **Endpoint:** `/api/bookings/`
- **Method:** POST
- **Description:** Create a new booking.
- **Request Body:**
  ```json
  {
    "user_id": 123,
    "user_name": "John Doe",
    "user_email": "john.doe@example.com",
    "user_phone": "+1234567890",
    "retreat": 1,
    "retreat_title": "Yoga for Stress Relief",
    "retreat_location": "Goa",
    "retreat_price": 200,
    "retreat_duration": 3,
    "payment_details": "Paid via credit card"
  }

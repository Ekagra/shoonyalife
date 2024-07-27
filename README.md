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
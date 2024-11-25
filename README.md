FastAPI MongoDB Professional Project

Overview
This is a modular and scalable web application built using FastAPI, with MongoDB as the database backend. The project adheres to professional coding practices, ensuring clarity, modularity, and scalability.

Key Features
FastAPI Framework:
High-performance, asynchronous API development.
Interactive API documentation with Swagger UI and ReDoc.
MongoDB Integration:
Uses the motor library for asynchronous database operations.
Professional Project Structure:
Modular design with clear separation of concerns for routes, services, models, and utilities.
Environment Configuration:
Centralized configuration using .env for flexibility across environments.
Custom Logging:
Structured logging for improved monitoring and debugging.
Health Check Endpoint:
Simple / endpoint to verify application status.
Setup Instructions
Clone the Repository:

bash
Copy code
git clone <repository_url>
cd fastapi_mongo_project
Set Up Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables:

Create a .env file in the project root and add:
plaintext
Copy code
MONGO_URI=mongodb://localhost:27017
APP_NAME=FastAPI Professional Project
DEBUG=True
Run the Application:

bash
Copy code
uvicorn app.main:app --reload
Access API Documentation:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Folder Structure
Below is the folder structure and its explanation:

graphql
Copy code
fastapi_mongo_project/
├── .env                      # Environment variables file
├── app/
│   ├── config.py             # Centralized configuration for environment variables
│   ├── db/
│   │   ├── connection.py     # Handles MongoDB connection setup and teardown
│   ├── main.py               # Entry point for the FastAPI application
│   ├── models/
│   │   ├── item_model.py     # Defines MongoDB schema and Pydantic validation models
│   ├── routes/
│   │   ├── items.py          # Defines API endpoints for CRUD operations on items
│   ├── services/
│   │   ├── item_service.py   # Contains business logic for interacting with MongoDB
│   ├── utils/
│   │   ├── logger.py         # Custom logger setup for structured application logging
│   ├── __init__.py           # Indicates that this is a package
├── requirements.txt          # Lists all Python dependencies
├── .gitignore                # Specifies files and folders to ignore in Git
├── README.md                 # Documentation file (this file)
Explanation of Each File/Folder
.env:

Stores environment-specific variables like the MongoDB URI and application name.
Keeps sensitive information out of the source code.
app/:

Main directory containing the application code.
app/config.py:

Centralized configuration using pydantic-settings.
Reads variables from .env and provides default values if not specified.
app/db/connection.py:

Manages the connection to MongoDB using the motor library.
Includes lifecycle methods (connect_to_mongo, close_mongo_connection).
app/main.py:

Entry point of the application.
Sets up the FastAPI app, includes routes, initializes the database, and handles startup/shutdown events.
app/models/item_model.py:

Defines the schema for items using Pydantic.
Validates incoming API requests and ensures proper data serialization.
app/routes/items.py:

Contains API endpoints (routes) for performing CRUD operations on items.
Delegates business logic to the item_service.py file.
app/services/item_service.py:

Handles business logic, such as creating, reading, updating, and deleting items in MongoDB.
Keeps the routes clean by abstracting database interactions.
app/utils/logger.py:

Configures a structured logger for consistent logging throughout the app.
requirements.txt:

Lists all Python dependencies for the project, including FastAPI, Motor, and Pydantic.
.gitignore:

Specifies files and directories to exclude from version control (e.g., venv/, .env, __pycache__).
README.md:

Documentation file (this file) describing the project, setup instructions, and folder structure.

Endpoints:

Base URL: http://127.0.0.1:8000
Method	Endpoint	Description
GET	/	Health Check
GET	/api/items/	Fetch all items
GET	/api/items/{id}	Fetch a single item by ID
POST	/api/items/	Create a new item
DELETE	/api/items/{id}	Delete an item by ID

Future Enhancements:

Add JWT-based authentication and role-based access control.
Implement unit and integration tests using pytest.
Add Docker support for easy deployment.
Create CI/CD pipelines for automated builds, testing, and deployment.

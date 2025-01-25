# Employee Management System

## Project Overview
The Employee Management System is a web-based application built with Flask to manage employee records. It allows users to create, read, update, and delete employee information in a user-friendly interface.

## Features
- Add new employees with name, department, and email.
- View a list of employees.
- Update employee details.
- Delete employees with confirmation.
- Responsive and modern UI with CSS styling.

## Project Structure
```
employee-management/
│-- app/
│   ├── static/
│   │   ├── styles.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── add_employee.html
│   │   ├── update_employee.html
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── config.py
│-- requirements.txt
│-- run.py
│-- README.md
```

## Prerequisites
Before running this project, ensure you have the following installed:
- Docker
- Python 3.9+

## Setup Instructions

### Running Locally (Without Docker)
1. Clone the repository:
   ```bash
   git clone https://github.com/stwins60/employee-management.git
   cd employee-management
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate    # For Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.py
   ```
5. Open `http://localhost:5000` in your browser.


## CRUD Operations
- **Add Employee:** Navigate to `/add` and fill out the form.
- **Update Employee:** Click on the "Edit" button next to an employee to update details.
- **Delete Employee:** Click on the "Delete" button next to an employee (requires confirmation).

<!-- ## Deployment to Production
1. Push the Docker image to Docker Hub:
   ```bash
   docker tag employee-management your-dockerhub-username/employee-management:latest
   docker push your-dockerhub-username/employee-management:latest
   ```
2. Deploy to a cloud platform such as AWS ECS or Azure App Services. -->

<!-- ## Future Enhancements
- Implement authentication and authorization.
- Replace SQLite with PostgreSQL for production.
- Deploy using Kubernetes for better scalability. -->

<!-- ## License
This project is licensed under the MIT License.

## Contact
For any inquiries or contributions, contact [your-email@example.com](mailto:your-email@example.com).
 -->

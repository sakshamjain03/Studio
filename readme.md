# IDR Studio

## Project 1 - Internal Full-Stack Website

### Project Objective
The aim of IDR Studio is to create an internal platform to showcase the project portfolio of Tech Mahindra Maker’s Lab. The website helps present previous company projects to potential clients, enhancing engagement and streamlining the process of displaying project details.

### Technologies Used
- Frontend: HTML, CSS, JavaScript
- Backend: Django, SQLite

### Features
- Browse and view project details such as name, description, technologies used, and resource links.
- User authentication for authorized personnel to manage and update project information.
- Responsive design with interactive project galleries and contact options using jQuery.

### Methodology
#### Frontend Development
- HTML & CSS: Developed a responsive structure and design to ensure an accessible and engaging user interface.
- JavaScript & jQuery: Added interactivity to the website with project galleries and contact features.

#### Backend Development
- Django: Created a robust backend using Django, handling the logic for serving project data and user management.
- SQLite: Configured and used an SQLite database to store and manage project details efficiently.

### Integration and Testing
- Integrated the frontend and backend using Django’s templating engine and AJAX for asynchronous interactions.
- Implemented user authentication to ensure only authorized users can modify project details.

### Setup Instructions
Follow these steps to run the project locally:

#### Prerequisites
- Python (>= 3.6)
- Django (>= 3.2)
- SQLite (comes pre-installed with Python)
- Git

#### Steps to Get Started
1. Clone the Repository
```
git clone https://github.com/your-username/idr-studio.git
cd idr-studio
```
2. Set Up a Virtual Environment (Optional but recommended)
```
python -m venv env
source env/bin/activate   # For Linux/macOS
env\Scripts\activate      # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up the Database
```
python manage.py migrate
```
5. Create a Superuser (Admin) Account
```
python manage.py createsuperuser
```
6. Run the Development Server
```
python manage.py runserver
```
7. Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

### Usage
- Admin Panel: Access the admin panel at /admin/ to add or edit project details.
- Browse Projects: The main interface allows users to view and browse the company’s project portfolio.

### Contributing
If you'd like to contribute to IDR Studio, feel free to submit a pull request or open an issue.

### License
This project is licensed under the MIT License.
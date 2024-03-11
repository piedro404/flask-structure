# Flask-Structure - Base Structure for API Projects 🧱
[![Licença](https://img.shields.io/badge/Licença-MIT-blue.svg)](https://github.com/piedro404/flask-structure/blob/main/LICENSE.md)

A Python library dedicated to exemplify and facilitate the start of Flask projects for APIs 💫. Download flask-structure and streamline the "start" of your projects with ease 🚀.

##### Organized and Scalable Structure. 😎📱

### Structure
<img width="221" alt="2024-03-09_17h53_25" src="https://github.com/piedro404/flask-structure/assets/88720549/47491b5a-0b36-4b5c-870c-3edfa321a4b3">

#### Details
- Controllers: Contains controllers that manage the application logic, connecting routes to specific operations.
- Drivers: Stores the drivers and libraries necessary to connect and operate with other services or hardware.
- Errors: Defines specific error types and custom exceptions that can be triggered during code execution.
- Main: The main entry point of the application. Within this folder, "Routes" manages API routes, and "Server" is responsible for starting and managing the web server.
- Models: Contains data models, usually classes representing tables in the database.
- Static: Stores static files such as CSS, JS, images, etc., needed to render front-end web pages.
- Templates: Maintains HTML templates and documentation related to the structure or usage of the API.
- Validators: Includes scripts or modules to validate input data or API requests.
- Views: Defines different types of HTTP responses and views associated with presentation logic.

# API Structure Features 🔨
- Info: Welcomes users and provides relevant information about the API and contacts.
- Docs: A place to learn about the API and how to use it interactively and dynamically.
- Favicon.ico: Icon to be displayed in the website window.

# Key Technologies Used 🌐
- Flask: Framework used for web application development, providing a flexible and efficient structure for creating APIs and user interfaces.
- Python: Primary programming language chosen for its versatility, simplicity, and large developer community.
- Cerberus: Python data validation library, used to ensure the integrity and consistency of data manipulated by the application.
- Other Libraries: The rest of the libraries can be found in requirements.txt, including various tools and utilities that complement and enhance the application's functionality.

# Documentation 📃

### API:
An API (Application Programming Interface) is a set of rules and definitions that allows communication between different software. It enables applications and services to exchange information and functionality efficiently and standardized.

### Key Uses in Development:
1. Service Integration:
   APIs facilitate integration between different services and platforms, allowing applications to share data and functionality.
2. Mobile Application Development:
   APIs are essential for mobile app development, providing access to resources such as location, camera, notifications, among others.
3. Access to External Data:
   Used to obtain data from external sources, such as social networks, databases, third-party services, providing up-to-date information.
4. Integration with Web Platforms:
   APIs are crucial for integrating web applications, enabling efficient communication between the front-end and back-end.
5. Microservices Development:
   In microservices architectures, APIs are essential for communication between the various distributed components of an application.
6. Task Automation:
   APIs allow the automation of routine tasks, optimizing processes and improving operational efficiency.
7. Plugin and Extension Development:
   Used to create plugins and extensions in various platforms, expanding the functionalities of existing software.
8. Resource Economy:
   Facilitate development by allowing the reuse of already implemented functionalities, saving time and resources.

# How to Run the Library Locally 🛠️
1. Virtual Environment (Optional)
For organization and ease of running the project, I suggest creating a virtual environment. To do this, use the following command:
```Bash
  python -m venv .venv
```
```Bash
  .venv\Scripts\activate
```

2. Download the library:
```bash
   pip install flask-structure
```

3. Run the command to create the project structure
```Bash
  flask-structure create
```

4. Install dependencies:
```bash
   pip install -r requirements.txt
```
   
5. Run the application:
```bash
   python run.py
```

6. Use the structure your way ;)

## Demonstrated Features of the Generated Structure 💻
1. Main Route ("/"): Returns a template that renders Swagger documentation. <br>(http://127.0.0.1:3000)

<img width="930" alt="2024-03-09_18h21_55" src="https://github.com/piedro404/flask-structure/assets/88720549/db073d7d-9b59-4dac-8b54-d008a6c9f27b">

2. API Information Route ("/info"): Returns a JSON with information about the API. <br>(http://127.0.0.1:3000/info)
```bash
{
    "status": True,
    "message": "Welcome to the Structure Flask API!",
    "version": "1.0v",
    "endpoints": {
        "docs": "/",
        "info": "/info",
    },
    "documentation": "/",
    "contact": {
        "email_personal": "pedro.henrique.martins404@gmail.com",
        "email_academic": "pedro.borges@alu.unibalsas.edu.br",
        "github": "piedro404",
        "linkedin": "pedrohenrique404"
    }
}
```

# License 
This project is licensed under the MIT License - see the [LICENSE](https://github.com/piedro404/flask-structure/blob/main/LICENSE.md) file for details.

# About 📒
Thanks to everyone, I wish you great studies. If you want, contact me at pedro.henrique.martins404@gmail.com.

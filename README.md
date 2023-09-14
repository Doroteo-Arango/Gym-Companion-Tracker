# Gym Guide & Tracker using Flask
## Introduction:
In the age of heart disease, chronic illnessses, & lack of exercise, staying active is essential for the prolonging of human life. In this Flask web-application, fitness enthusiasts are given a tool to track their progress, learn about muscle hypertrophy, and calculate their Body Mass Index (BMI). This web-application focuses on one of the larger niches of the exercise community, those who train for strength, & hypertrophy. This application is very user-friendly whether the user is a novice, or adept-lifter. By providing users with an easy-to-use fitness companion, this web-application aims to be an indispensible companion to exercise training.
## Features:
User Registration: A personal user account must be created to personalise experiences in private, ensuring progress & data are securely stored for future usage.

Muscular Hypertrophy Guidance: Access a comprehensive guide on training each major muscle group in tandem for peak hypertrophy. In this web-application, one can learn how to effectively train antagonistic muscle pairs (bicep & triceps) in order to maximise muscle gain & strength gain while minimising risk of injury due to overtraining without the necessary rest.

Progress Tracking: Keep track of daily gym sessions using an integrated notes app. Keeping consistent logs of progress ensures a user keeps track of their goals.

BMI Calculation: Calculate your BMI using the built-in calculator. Although not a concrete form of self-judgement, the BMI scale still persists to be a solid proof of progress. Learn the fundamentals needed to obtain a better version of yourself.

Challenges: Try out various fitness-related challenges in order to keep your body in the best shape possible.
## Technology & Skills:
In this web-application, the Flask framework for web-design was used. The core logic & functionality of the application was implemented using Python. Python is an excellent language for web development. User authentication, data processing & database management was aided massively by Python's clear syntax. Flask was used because it is a beginner-friendly framework, allowing for routing & dynamic content generation in conjunction with HTML & CSS. Flask's capability also suited the scope of this project perfectly. Jinja syntax allowed for a quick repitition of HTML pages while maintaining efficient projct progression.

Dark mode was chosen as the theme for the web-application because it is the nicest on the eye stylistically. A layout page in HTML was created including every basic necessity that each subsequent HTML page included, such as all metadata, such as bootstrap imports & stylesheet imports. A navigation bar was used for each webpage to further improve ease-of-usage.

HTML & CSS were used heavily to design the user interface. HTML was used for structuring, CSS was used for visual design. The result is a clean & intuitive user experience.

Javascript was used to design the animation features of this web-application. The note deletion feature & the BMI calculation was implemented using Javascript.

## Files Included in Submission:
In the Python file '__init__.py', lays the foundation for a Flask web application according to the scope of this project. Flask-Login was imported for user authentication. SQLAlchemy was imported for database management, to store user information & user data. A function called 'create_app' was defined. In this function, the primary components regarding security & database initialisation were set up. A user loader function retrieves users from the data base to manage user sessions.

The script 'app.py' initialises the Flask application & was the go-to executable to start the local server, although the command 'flask run' is also acceptable. The app is ran in debug mode at each execution. This ensures that the website is dynamically updated automatically whenever a change is made to the code while the server is still running.

In 'views.py' the standard routes for the website were clarified. Throughout this website, multiple routes were used. For each situation in the user interface in which a post or get request was submitted, the user would be redirected to any of a selection of HTML pages. This would be implemented in 'views.py'. The home route was redirected to, whenever a login failure would occur or any other similar issue. The operation of the notes section of this website was added via this file. For example, in the code it can be viewed clearly that upon 'POST' request, in the notes (/log) page, the note would be added to the database. A similar process would occur for the deletion of a note.

Routes for user authentication were defined in 'auth.py' using blueprints. Functions for the sign-up, log-in & log-out are defined here. Prompts for each required user information step are defined (username, password, e.t.c.). In each step, the database is queried for information pertaining to each route. For example, when logging into an account, the database is queried to check if passwords match. If successfull, the user will be redirected to the homepage. The requirements when creating an account can be set in the 'sign_up' function. For the scope of this project, the length of the email must be greater than 4 characters, the length of the name of the account must be greater than 2. Then the user is added to the database.

Database models are created utilising SQLAlchemy, in 'models.py'. Two databases are used in this project. All users are stored a schema within a 'User' class containing attributes for identification, email, password, first name, and note. The 'Note' class represents tracked gym data, with attributes for identification, data, date, & user identification. A one-to-many relationship is utilised for the note system, where one single parent object (i.e. the user) can have multiple children objects associated with them.

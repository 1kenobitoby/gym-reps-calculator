# Gym reps calculator
A web app that allows people who are into weight training to calculate the correct combination of weight and number of repetitions for an exercise.

# Project description
This is a Streamlit web app written in Python 3.8.10. It allows a user to enter a weight lifted and number of repetitions they can complete for a weight training exercise. By linear regression it then calculates a table of suggested weights and repetitions to help them achieve various training goals.<br>
It defaults to a linear relationship between weights and reps which is widely published online and in subject-specific printed matter. Optionally the user has the chance to override the default relationship and create a bespoke relationship for themselves based on inputs entered from their own experience. The bespoke relationship is also calculated by linear regression of their inputs.<br>
The project has been built in Streamlit V1.27 and distributed as a public app on the Streamlit Community Cloud.<br>
There are no plans to develop or update the app (except for bug fixes). Users have the option to contact the authors to suggest changes or improvements which we might implement if we think they are a good idea and it\'s worth our while. But probably not.<br>

# How to run the project
Open the URL [https://gym-reps-calculator.streamlit.app](https://gym-reps-calculator.streamlit.app)

# Dependencies
streamlit V1.27<br>
numpy (for user input handling)<br>
scikit-learn (for linear regression of user inputs)<br>

# Licence
The code is copyrighted and no specific licence for its use or distribution is granted. That said, users are welcome to inspect the code, clone the repository and copy code snippets if doing so would help them solve problems with their own projects. But don\'t rip it off wholesale.


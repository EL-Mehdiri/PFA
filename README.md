
# TaskZenith Task Manager

TaskZenith is a powerful and intuitive web-based task manager designed to streamline your workflow and help you stay organized. With its user-friendly interface and robust features, TaskZenith empowers individuals and teams to efficiently manage tasks, prioritize projects, and achieve their goals with ease. 
It is a feature-rich and user-friendly web-based task manager that revolutionizes the way individuals and teams manage their tasks and projects. With its comprehensive set of tools and intuitive interface, TaskZenith empowers users to stay organized, collaborate effectively, and accomplish their goals with ease.


## Key Features
- Task Management: Create, track, and organize tasks effortlessly. Assign due dates, set priorities, and categorize tasks to stay on top of your workload.
- Collaborative Workspaces: Collaborate seamlessly with your team members by creating shared workspaces. Delegate tasks, discuss project details, and keep everyone in the loop.
- Flexible Project Views: Customize your task views based on your preferences. Choose between list or calendar views to visualize your tasks and projects in a way that suits your workflow. The list view provides a straightforward task list, while thecalendar view allows users to view tasks and deadlines in a familiar calendar format.
- Task creation: Users can create new tasks by providing a title, description, due date, and possibly other relevant details. This allows users to capture all the necessary information about a task.
- Calendar: Task managers often provide options to set due dates and lay down the time to complete tasks. This allows users to track deadlines and and always keep them updated to ensure timely completion
- Task editing: Users can click on this option to open a task creation form where they can input the task title, description, due date, priority, and other relevant information. 
- Task Organization: Users can organize their tasks and categorize them and assigning tags, labels or comments . These features help users by structuring their tasks based on their preferences or project requirements.
- Task tracking: To know users task status and progress, the manager often use visual cues or status indicators. Such as color-coded labels for priority levels, or icons denoting task completion. As of a search bar that makes it easy to find your tasks.
- Task grouping: Designed for team collaboration often include features that facilitate communication among team members. This may include commenting on tasks and sharing updates.


## Installation and Usage
To install and set up TaskZenith on your local machine, please follow the instructions below. Make sure you have Python 3.11.1 installed before proceeding.

### Prerequisites

- Python 3.11.1
- Flask-Admin==1.6.1
- Flask-Bcrypt==1.0.1
- Flask-Login==0.6.2
- Flask-Session==0.5.0
- Flask-SQLAlchemy==3.0.3
- Flask-WTF==1.1.1

### Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the TaskZenith repository.
3. Run the following command to clone the repository:
git clone [https://github.com/your-username/taskzenith.git](https://github.com/EL-Mehdiri/PFA.git)
Replace `your-username` with your GitHub username.

### Install Dependencies

1. Navigate to the cloned TaskZenith directory: cd taskzenith
2. Create a virtual environment (optional but recommended): python3 -m venv env

3. Activate the virtual environment:
- On macOS and Linux:
  ```
  source env/bin/activate
  ```
- On Windows:
  ```
  .\env\Scripts\activate
  ```

4. Install the required dependencies: pip install -r requirements.txt

### Configure the Application


1. Configure the database connection by setting the `DATABASE_URI` variable. For example: DATABASE_URI = 'sqlite:///database.db'


### Run the Application

1. Run the following command to start the application: fpython main.py
---

Happy task management with TaskZenith!

## Authors

- [Ridmani Mehdi](https://github.com/EL-Mehdiri)
- [Essahli Sara](https://github.com/Asurite)
- [Bouikhef Anwar](https://github.com/777Anwar)
- [Idmahou Hafid]()

## Acknowledgments

We would like to express our heartfelt gratitude to our school, eWA, for providing us with the necessary resources and opportunities to develop TaskZenith. We are grateful for the support and encouragement we received.

We would also like to extend our appreciation to our professors for their guidance, expertise, and invaluable feedback throughout the development process. Their mentorship and encouragement have been instrumental in shaping TaskZenith.

We are indebted to eWA School and our professors for their contribution to our learning journey and the realization of this project.

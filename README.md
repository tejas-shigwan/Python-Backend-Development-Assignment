Project Description
Task Management Web App

This web application allows users to effectively manage their tasks by adding, editing, deleting, and marking them as completed. The application is built using .NET Core for the backend, HTML/CSS for the front end, and jQuery for client-side interactivity.

Key Features:

Task Creation: Users can add new tasks with a name, due date, and priority.
Task Editing: Existing tasks can be modified to update their name, due date, or priority.
Task Deletion: Tasks can be removed from the list if they are no longer necessary.
Task Completion: Tasks can be marked as completed to indicate that they have been finished.
Responsive Design: The application is designed to be responsive, ensuring a good user experience on different screen sizes.
Technologies Used:

Backend: ASP.NET Core Web API, Entity Framework Core, SQLite (or SQL Server)
Frontend: HTML, CSS, jQuery
Project Structure:

TaskManagementApp/
├── TaskManagementApp.API
│   ├── Controllers
│   ├── Data
│   ├── Models
│   ├── Program.cs
│   └── Startup.cs
├── TaskManagementApp.UI
│   ├── index.html
│   ├── script.js
│   └── style.css
└── README.md
Steps to Run the Application:

Clone the repository:
Bash
git clone https://github.com/your-username/TaskManagementApp.git
Use code with caution.

Restore NuGet packages:
Bash
cd TaskManagementApp.API
dotnet restore
Use code with caution.

Run the database:
For in-memory database: The database will be created automatically when the application starts.
For SQLite: Create a todo.db file in the TaskManagementApp.API directory.
For SQL Server: Configure the connection string in appsettings.json and ensure SQL Server is running.
Start the application:
Bash
dotnet run
Use code with caution.

Access the application: Open a web browser and navigate to http://localhost:5000 to use the task management app.
Additional Notes:

You can customize the application's appearance and functionality by modifying the HTML, CSS, and JavaScript code.
For more advanced features, consider adding features like task filtering, sorting, and reminders.
You can replace SQLite with SQL Server by configuring the connection string in appsettings.json

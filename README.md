# softwareplanningtool
This is a project planning tool implemented in Python. It allows the user to create a new project, add tasks to it, assign the tasks to team members, and generate a Gantt chart to visualize the project timeline.
## Requirements
The following Python packages are required to run the tool:
pandas
datetime
plotly
## Classes
The tool defines two classes:
Project
This class represents a project and contains the following attributes:
name: the name of the project
team_members: a list of team members working on the project
start_date: the start date of the project
end_date: the end date of the project
tasks: a list of tasks associated with the project
The class also contains the following methods:
add_task: adds a new task to the project
calculate_total_effort: calculates the total estimated effort for all tasks in the project
assign_tasks_to_team_members: assigns tasks to team members based on estimated effort
get_project_details: prompts the user for project details
get_task_details: prompts the user for task details
Task
This class represents a task and contains the following attributes:
name: the name of the task
description: a description of the task
estimated_effort: the estimated effort required to complete the task
due_date: the due date of the task
assigned_to: the team member assigned to the task
## Gantt Chart
The tool generates a Gantt chart using the plotly package. The chart displays the timeline of each task, with different colors representing different team members. The chart also includes the project start and end dates.
## Usage
To use the tool, simply run the planningtool.py file using Python
The tool will prompt the user for project details, such as project name, team members, start date, and end date. The user can then add tasks to the project and assign them to team members. Once all tasks have been assigned, the tool will generate a Gantt chart to visualize the project timeline.

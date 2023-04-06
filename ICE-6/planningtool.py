import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

# Define a class for the project
class Project:
    def __init__(self, name, team_members, start_date, end_date):
        self.name = name
        self.team_members = team_members
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.tasks = []

    def add_task(self, name, description, estimated_effort, due_date):
        task = Task(name, description, estimated_effort, due_date)
        self.tasks.append(task)

    def calculate_total_effort(self):
        total_effort = sum(task.estimated_effort for task in self.tasks)
        return total_effort

    def assign_tasks_to_team_members(self):
        num_members = len(self.team_members)
        if num_members == 0:
            print('There are no team members for this project')
            return

        total_effort = self.calculate_total_effort()
        if total_effort == 0:
            print('There are no tasks for this project')
            return

        avg_effort_per_member = total_effort / num_members
        assigned_effort = [0] * num_members

        for task in self.tasks:
            min_index = assigned_effort.index(min(assigned_effort))
            assigned_effort[min_index] += task.estimated_effort
            task.assigned_to = self.team_members[min_index]

        print('Tasks assigned successfully')

# Define a class for the tasks
class Task:
    def __init__(self, name, description, estimated_effort, due_date):
        self.name = name
        self.description = description
        self.estimated_effort = estimated_effort
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.assigned_to = []
    def assign_to_team_member(self, team_member):
        self.assigned_to.append(team_member)


# Define a function to prompt the user for project details
def get_project_details():
    name = input('Enter project name: ')
    team_members = input('Enter names of team members separated by commas: ').split(',')
    start_date = input('Enter project start date (YYYY-MM-DD): ')
    end_date = input('Enter project end date (YYYY-MM-DD): ')
    return Project(name, team_members, start_date, end_date)

# Define a function to prompt the user for task details
def get_task_details():
    name = input('Enter task name: ')
    description = input('Enter task description: ')
    estimated_effort = int(input('Enter estimated effort in hours: '))
    due_date = input('Enter task due date (YYYY-MM-DD): ')
    return (name, description, estimated_effort, due_date)

# Get project details from user
project = get_project_details()

# Prompt user for tasks and add them to project
while True:
    add_task = input('Do you want to add a task to this project? (y/n): ')
    if add_task.lower() == 'n':
        break
    task_details = get_task_details()
    project.add_task(*task_details)

# Assign tasks to team members
project.assign_tasks_to_team_members()

# Print project details
print('\nProject Name:', project.name)
print('Team Members:', ', '.join(project.team_members))
print('Start Date:', project.start_date.strftime('%Y-%m-%d'))
print('End Date:', project.end_date.strftime('%Y-%m-%d'))
print('Total Effort:', project.calculate_total_effort())

# Print task details
print('\nTasks:')
for task in project.tasks:
    print('Name:', task.name)
    print('Description:', task.description)
    print('Estimated Effort:', task.estimated_effort)
    print('Due Date:', task.due_date.strftime('%Y-%m-%d'))
    print('Assigned To:', task.assigned_to)
    print()

# Generate Gantt chart
task_df = []
for task in project.tasks:
    task_df.append({
        'Task': task.name,
        'Start': task.due_date.strftime('%Y-%m-%d'),
        'Finish': (task.due_date + timedelta(hours=task.estimated_effort)).strftime('%Y-%m-%d'),
        'Assigned To': task.assigned_to
    })
task_df = pd.DataFrame(task_df)
project_duration = (project.end_date - project.start_date).days
fig = px.timeline(task_df, x_start='Start', x_end='Finish', y='Task', color='Assigned To')
fig.update_layout(title=f'{project.name} Gantt Chart', xaxis_title='Date', yaxis_title='Task', yaxis=dict(autorange="reversed"))
fig.update_yaxes(autorange="reversed")
fig.update_xaxes(range=[project.start_date.strftime('%Y-%m-%d'), project.end_date.strftime('%Y-%m-%d')], tickformat='%Y-%m-%d', 
                 nticks=project_duration+1)
fig.show()

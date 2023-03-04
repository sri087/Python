#
# Purpose: Script to access Todoist through APIs and compute
#          progress metrics for each project
#
# Constraints: 
#          1. The free plan of Todoist allows only 5 projects.
#          2. Workaround is to use labels starting with 'Project_' to indicate projects
#          3. All tasks will reside in the Todoist inbox 
#          4. The free plan does not provide a REST API call to access completed tasks
#          5. Workaround is to use the SYNC API call
#
# Method: 
#          1. Collect a list of completed and not completed tasks
#             along with their labels
#          2. Each task in a project is assigned the same label 
#          3. Count the number of labels in each of completed and not completed groups
#             and compute completion percentages
#
# Sample Output:
# -----------------------------------------------------------
# Project                                 Progress Indicator
# -----------------------------------------------------------
# Project_IncreaseServerUtilization            25% **--------
# Project_ManningLiveProjects                  10% *---------
# Project_Taxes2022                            33% ***-------
# -----------------------------------------------------------
#

import requests
import json

from collections import Counter

params = {
    "project_id": "INBOX PROJ ID" # project id of Inbox
}

headers = {
    "Authorization" : "Bearer <API TOKEN>"
}

def get_active_tasks():
    url = "https://api.todoist.com/rest/v2/tasks"
    result = requests.get(url=url,headers=headers,params=params)
    tasks = json.loads(result.text)
    return [label for task in tasks for label in task['labels'] ]
 

def get_completed_tasks(yr="2023"):
    url = "https://api.todoist.com/sync/v9/completed/get_all"
    result = requests.get(url=url,headers=headers,params=params)
    tasks = json.loads(result.text)
    return [task["content"] for task in tasks['items'] if task["completed_at"][:4]==yr]


def print_line(character='-',count=30):
    print(character*count)


def format_print(my_dict):

    print_line(count=59)
    print(f'{"Project":<40}{"Progress":<9}{"Indicator"}')
    print_line(count=59)

    for key, value in my_dict.items():

        complete = int(value * 10)
        todo = 10 - complete
        print(f'{key:<40} {round(value,2):>7.0%} {complete * "*"}{todo *"-"}')

    print_line(count=59)


def main():
 
    active_tasks = get_active_tasks()
    completed_tasks = get_completed_tasks()

    active_task_counter = Counter(active_tasks)
    # Completed tasks are returned with the label appended to them
    # the labels are prefixed by @ symbol. so extract all after the @ symbol
    done_task_counter = Counter([done_task.split('@')[-1] for done_task in completed_tasks])
 
    pct_comp_dict = {}

    for key,value  in done_task_counter.items():
        if key in active_task_counter.keys():
            # Project in progress
            pct_comp_dict[key] = done_task_counter[key] / (value + active_task_counter[key])
        else:
            pct_comp_dict[key] = 1 # Project 100% complete

    for key in active_task_counter.keys():
        if key not in pct_comp_dict.keys():
            pct_comp_dict[key] = 0 # Project Not started 
    
    format_print(pct_comp_dict)

if __name__ == '__main__':
    main()

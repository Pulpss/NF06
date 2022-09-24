tasks2 = [
    {
        "name": "A",
        "duration": 3,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": [],
        "tasks_after": ["C"],
    },
    {
        "name": "B",
        "duration": 2,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": [],
        "tasks_after": ["C", "D"],
    },
    {
        "name": "C",
        "duration": 1,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["A", "B"],
        "tasks_after": ["G"],
    },
    {
        "name": "D",
        "duration": 2,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["B"],
        "tasks_after": ["F"],
    },
    {
        "name": "E",
        "duration": 1,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["F", "G"],
        "tasks_after": [],
    },
    {
        "name": "F",
        "duration": 3,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["D"],
        "tasks_after": ["E"],
    },
    {
        "name": "G",
        "duration": 2,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["C"],
        "tasks_after": ["E"],
    },
]

tasks = [
    {
        "name": "A",
        "duration": 2,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": [],
        "tasks_after": ["C", "G"],
    },
    {
        "name": "B",
        "duration": 8,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": [],
        "tasks_after": ["D", "E"],
    },
    {
        "name": "C",
        "duration": 5,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["A"],
        "tasks_after": [],
    },
    {
        "name": "D",
        "duration": 2,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["B"],
        "tasks_after": ["G"],
    },
    {
        "name": "E",
        "duration": 6,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["B"],
        "tasks_after": ["F"],
    },
    {
        "name": "F",
        "duration": 5,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["E"],
        "tasks_after": [],
    },
    {
        "name": "G",
        "duration": 3,
        "min_start_date": 0,
        "max_start_date": 0,
        "tasks_before": ["A", "D"],
        "tasks_after": [],
    },
]


def get_min_start_date(task):
    tasks_before = [t for t in tasks if task["name"] in t["tasks_after"]]
    if tasks_before:
        return max([get_min_start_date(t) for t in tasks_before]) + task["duration"]
    else:
        return task["duration"]

def get_max_start_date(task):
    tasks_after = [t for t in tasks if t["name"] in task["tasks_after"]]
    if tasks_after != []:
        return min([t['min_start_date'] for t in tasks_after]) - task["min_start_date"]
    else:
        return max([t['min_start_date'] for t in tasks]) - task["min_start_date"]

def get_task_level(task):
    if task["tasks_before"] == []:
        return 0
    else:
        sum = 0
        for task_before in [t for t in tasks if task["name"] in t["tasks_after"]]:
            sum += get_task_level(task_before)
        return sum + 1

def find_critical_path(tasks):
    path = []
    max_dur = max([t['min_start_date']+t['duration'] for t in tasks])
    critcal_last_task = [t for t in tasks if t['min_start_date']+t['duration'] == max_dur][0]
    path.append(critcal_last_task['name'])
    while critcal_last_task['tasks_before'] != []:
        critcal_last_task = [t for t in tasks if t['name'] in critcal_last_task['tasks_before']][0]
        path.append(critcal_last_task['name'])
    return list(reversed(path))


def sort_tasks_by_level(tasks):
        for i in range(len(tasks)):
            for j in range(len(tasks) - 1):
                if tasks[j]["level"] > tasks[j + 1]["level"]:
                    tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]

def get_chart(tasks=[]):
    for task in tasks:
        task["min_start_date"] = get_min_start_date(task) - task["duration"]
        task["level"] = get_task_level(task)
    for task in tasks:
        task["max_start_date"] = get_max_start_date(task)
        print(task["name"], task["level"], task["min_start_date"], task["duration"], task["max_start_date"])
    print(find_critical_path(tasks))




get_chart(tasks)

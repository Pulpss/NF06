import ctypes as ct
import os

DLL_BASE_NAME = "C_lib"

if os.name == "nt":
    path = os.path.join(
        os.path.abspath(os.path.dirname(__file__) + "/../"),
        DLL_BASE_NAME + ".dll",
    )
    dll = ct.CDLL(path)
else:
    """!
    For other file systems, we use files ending in .so
    """
    dll = ct.CDLL(f"{os.path.abspath(os.curdir)}/../" + DLL_BASE_NAME + ".so")


class Task(ct.Structure):
    """Task structure for C
    fields:
    - name: name of the task
    - description: description of the task
    - duration: duration of the task
    - min_start_date: minimum start date of the task
    - max_start_date: maximum start date of the task
    - tasks_before: array of tasks that must be completed before this task
    - tasks_before_amount: amount of tasks that must be completed before this task
    - tasks_after: array of tasks that must be completed after this task
    - tasks_after_amount: amount of tasks that must be completed after this task
    - completed: 1 if the task is completed, 0 otherwise
    - level: level of the task in the critical path
    """

    _fields_ = [
        ("name", ct.c_char_p),
        ("description", ct.c_char_p),
        ("duration", ct.c_int),
        ("min_start_date", ct.c_int),
        ("max_start_date", ct.c_int),
        ("tasks_before", ct.POINTER(ct.c_char_p)),
        ("tasks_before_amount", ct.c_int),
        ("tasks_after", ct.POINTER(ct.c_char_p)),
        ("tasks_after_amount", ct.c_int),
        ("completed", ct.c_int),
        ("level", ct.c_int),
    ]


class Pygantt(ct.Structure):
    """Pygantt structure for C
    fields:
    - project_name: name of the project
    - project_description: description of the project
    - start_date: start date of the project
    - background_image: path to the background image of the project
    - tasks_amount: amount of tasks in the project
    - tasks: array of tasks in the project
    """

    _fields_ = [
        ("project_name", ct.c_char_p),
        ("project_description", ct.c_char_p),
        ("start_date", ct.c_char_p),
        ("background_image", ct.c_char_p),
        ("tasks_amount", ct.c_int),
        ("tasks", ct.POINTER(Task)),
    ]


class TasksResponse(ct.Structure):
    """TasksResponse structure for C
    fields:
    - tasks: array of tasks
    - amount: amount of tasks
    """

    _fields_ = [
        ("tasks", ct.POINTER(Task)),
        ("amount", ct.c_int),
    ]


"""Here we define the input and output types of the functions"""
dll.findTasksBefore.argtypes = [Pygantt, Task]
dll.findTasksBefore.restype = TasksResponse
dll.findTasksAfter.argtypes = [Pygantt, Task]
dll.findTasksAfter.restype = TasksResponse
dll.getTaskLevel.argtypes = [Pygantt, Task]
dll.getTaskLevel.restype = ct.c_int
dll.findCriticalPath.argtypes = [Pygantt]
dll.findCriticalPath.restype = TasksResponse
dll.getMinStartDate.argtypes = [Pygantt, Task]
dll.getMinStartDate.restype = ct.c_int


def createPointerArrayTasksName(array):
    """!
    Create a pointer array of tasks name ready for C

    @param array: array of tasks name

    @return: pointer array of tasks name
    """
    arr = (ct.c_char_p * len(array))()
    arr[:] = [name.encode("utf-8") for name in array]
    return arr


def createTaskStruct(task):
    """!
    Create a task structure ready for C

    @param task: task

    @return: task structure
    """
    task_struct = Task()
    task_struct.name = task["name"].encode("utf-8")
    task_struct.description = task["description"].encode("utf-8")
    task_struct.duration = task["duration"]
    task_struct.tasks_before = createPointerArrayTasksName(task["tasks_before"])
    task_struct.tasks_before_amount = len(task["tasks_before"])
    task_struct.tasks_after = createPointerArrayTasksName(task["tasks_after"])
    task_struct.tasks_after_amount = len(task["tasks_after"])
    task_struct.completed = task["completed"]
    """This is just for the temporary variables in order not to freak out C with no value"""
    try:
        task_struct.level = task["level"]
    except KeyError:
        task_struct.level = -1
    try:
        task_struct.min_start_date = task["min_start_date"]
    except KeyError:
        task_struct.min_start_date = -1
    try:
        task_struct.max_start_date = task["max_start_date"]
    except KeyError:
        task_struct.max_start_date = -1
    return task_struct


def createTaskFromStruct(task_struct):
    """!
    Create a task from a task structure from C for python

    @param task_struct: task structure from C

    @return: task
    """
    task = {
        "name": task_struct.name.decode("utf-8"),
        "description": task_struct.description.decode("utf-8"),
        "duration": task_struct.duration,
        "min_start_date": task_struct.min_start_date,
        "max_start_date": task_struct.max_start_date,
        "tasks_before": [
            task_struct.tasks_before[i].decode("utf-8")
            for i in range(task_struct.tasks_before_amount)
        ],
        "tasks_after": [
            task_struct.tasks_after[i].decode("utf-8")
            for i in range(task_struct.tasks_after_amount)
        ],
        "completed": task_struct.completed,
        "level": task_struct.level,
    }
    return task


def createFileFromStruct(file_struct):
    """!
    Create a file from a file structure from C for python

    @param file_struct file_struct: file structure from C

    @return dict: file
    """
    file = {
        "project_name": file_struct.project_name.decode("utf-8"),
        "project_description": file_struct.project_description.decode("utf-8"),
        "start_date": file_struct.start_date.decode("utf-8"),
        "background_image": file_struct.background_image.decode("utf-8"),
        "tasks": [
            createTaskFromStruct(file_struct.tasks[i])
            for i in range(file_struct.tasks_amount)
        ],
    }
    return file


def createPointerArrayTasks(tasks):
    """!
    Create a pointer array of tasks ready for C

    @param tasks tasks: array of tasks

    @return ct.POINTER(Task): pointer array of tasks
    """
    arr = (Task * len(tasks))()
    struct_array = ct.cast(arr, ct.POINTER(Task))
    for i in range(len(tasks)):
        struct_array[i] = createTaskStruct(tasks[i])
    return struct_array


def createPyganttFile(data):
    """!
    Create a Pygantt structure ready for C

    @param data data: data from the global variable

    @return Pygantt_file: Pygantt structure ready for C
    """
    Pygantt_file = Pygantt(
        project_name=data["project_name"].encode("utf-8"),
        project_description=data["project_description"].encode("utf-8"),
        start_date=data["start_date"].encode("utf-8"),
        background_image=data["background_image"].encode("utf-8"),
        tasks_amount=len(data["tasks"]),
        tasks=createPointerArrayTasks(data["tasks"]),
    )
    return Pygantt_file


def getTaskLevel(data, task):
    """!
    Get the level of a task via the C function

    @param data data: data from the global variable
    @param task task: target task to get the level of

    @return level: level of the task as an int
    """
    return dll.getTaskLevel(createPyganttFile(data), createTaskStruct(task))


def findCriticalPath(data):
    """!
    Find the critical path via the C function

    @param data data: data from the global variable

    @return tasks: array of tasks
    """
    tasks = []
    res = dll.findCriticalPath(createPyganttFile(data))
    for i in range(res.amount):
        tasks.append(createTaskFromStruct(res.tasks[i]))
    return tasks


def getMinStartDate(data, task):
    """!
    Get the minimum start date of a task via the C function

    Here we have to subtract the duration of the task to get a usable value

    @param data data: data from the global variable
    @param task task: target task to get the minimum start date of

    @return min_start_date: minimum start date of the task as an int
    """
    return (
        dll.getMinStartDate(createPyganttFile(data), createTaskStruct(task))
        - task["duration"]
    )


def getMaxStartDate(data, task):
    """!
    Get the maximum start date of a task via the C function
    It is used in the pessimistic version of the Gantt diagramm and the PERT chart

    @param data data: data from the global variable
    @param task task: target task to get the maximum start date of

    @return max_start_date: maximum start date of the task as an int
    """
    return dll.getMaxStartDate(createPyganttFile(data), createTaskStruct(task))

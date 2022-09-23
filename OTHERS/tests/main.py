from ctypes import *
import oslib
import sys
import json

DLL_BASE_NAME = "ctypes"

class Task(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("description", c_char_p),
        ("duration", c_int),
        ("min_start_date", c_int),
        ("max_start_date", c_int),
        ("tasks_before", POINTER(c_char_p)),
        ("tasks_before_amount", c_int),
        ("tasks_after", POINTER(c_char_p)),
        ("tasks_after_amount", c_int),
        ("completed", c_int),
        ("level", c_int),
    ]


class Pygantt(Structure):
    _fields_ = [
        ("project_name", c_char_p),
        ("project_description", c_char_p),
        ("start_date", c_char_p),
        ("background_image", c_char_p),
        ("tasks_amount", c_int),
        ("tasks", POINTER(Task)),
    ]


class TasksResponse(Structure):
    _fields_ = [
        ("tasks", POINTER(Task)),
        ("amount", c_int),
    ]

def main(*argv):
    dll_name = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        (argv[0] if argv else DLL_BASE_NAME) + ".dll",
    )
    lib = CDLL(dll_name)

    # read zuu.pygantt file as json
    with open("zuu.pygantt", "r") as f:
        file = json.load(f)

    def createPointerArrayTasksName(array):
        arr = (c_char_p * len(array))()
        arr[:] = [name.encode("utf-8") for name in array]
        return arr

    def createTaskStruct(task):
        task_struct = Task()
        task_struct.name = task["name"].encode("utf-8")
        task_struct.description = task["description"].encode("utf-8")
        task_struct.duration = task["duration"]
        task_struct.min_start_date = task["min_start_date"]
        task_struct.max_start_date = task["max_start_date"]
        task_struct.tasks_before = createPointerArrayTasksName(task["tasks_before"])
        task_struct.tasks_before_amount = len(task["tasks_before"])
        task_struct.tasks_after = createPointerArrayTasksName(task["tasks_after"])
        task_struct.tasks_after_amount = len(task["tasks_after"])
        task_struct.completed = task["completed"]
        task_struct.level = task["level"]
        return task_struct

    def createPointerArrayTasks(tasks):
        arr = (Task * len(tasks))()
        struct_array = cast(arr, POINTER(Task))
        for i in range(len(tasks)):
            struct_array[i] = createTaskStruct(tasks[i])
        return struct_array

    Pygantt_file = Pygantt(
        project_name=file["project_name"].encode("utf-8"),
        project_description=file["project_description"].encode("utf-8"),
        start_date=file["start_date"].encode("utf-8"),
        background_image=file["background_image"].encode("utf-8"),
        tasks_amount=len(file["tasks"]),
        tasks=createPointerArrayTasks(file["tasks"]),
    )

    lib.findTasksBefore.argtypes = [Pygantt, Task]
    lib.findTasksBefore.restype = TasksResponse
    lib.findTasksAfter.argtypes = [Pygantt, Task]
    lib.findTasksAfter.restype = TasksResponse
    lib.getTaskLevel.argtypes = [Pygantt, Task]
    lib.getTaskLevel.restype = c_int
    lib.findCriticalPath.argtypes = [Pygantt]
    lib.findCriticalPath.restype = TasksResponse
    lib.getMinStartDate.argtypes = [Pygantt, Task]
    lib.getMinStartDate.restype = c_int



    for i in range(len(file["tasks"])):
        print(Pygantt_file.tasks[i].name)
        print(lib.getTaskLevel(Pygantt_file, Pygantt_file.tasks[i]))
        print(lib.getMinStartDate(Pygantt_file, Pygantt_file.tasks[i]) - Pygantt_file.tasks[i].duration)
    print("done")

    res = lib.findCriticalPath(Pygantt_file)
    for i in range(res.amount):
        print(res.tasks[i].name)




rc = main(*sys.argv[1:])
sys.exit(rc)

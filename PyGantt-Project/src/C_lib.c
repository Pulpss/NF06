#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct task
{
    char *name;
    char *description;
    int duration;
    int min_start_date;
    int max_start_date;
    char **tasks_before;
    int tasks_before_amount;
    char **tasks_after;
    int tasks_after_amount;
    int completed;
    int level;
} task;

typedef struct pygantt
{
    char *project_name;
    char *project_description;
    char *start_date;
    char *background_image;
    int tasks_amount;
    task *tasks;
} pygantt;

typedef struct tasksResponse
{
    task *tasks;
    int amount;
} tasksResponse;


task findTaskWithName(pygantt file, char *name)
/*
 * This function is used to find a task in a pygantt file by its name
 * Pretty explicit you might say...
*/
{
    for (int i = 0; i < file.tasks_amount; i++)
    {
        if (strcmp(file.tasks[i].name, name) == 0)
        {
            return file.tasks[i];
        }
    }
}

__declspec(dllexport) tasksResponse findTasksBefore(pygantt file, task target)
/*
 * This function is used to find all the tasks before a given task
 * It returns a tasksResponse struct which contains an array of tasks and the amount of tasks
*/
{
    tasksResponse res;
    task *tasks = (task *)malloc(sizeof(task));
    int index = 0;
    // iterate through all the tasks in the file
    for (int i = 0; i < file.tasks_amount; i++)
    {
        // iterate through all the tasks before the target task
        for (int j = 0; j < target.tasks_before_amount; j++)
        {
            // if the names match add it to the list
            if (strcmp(file.tasks[i].name, target.tasks_before[j]) == 0)
            {
                tasks = realloc(tasks, sizeof(task) * (index + 1));
                tasks[index] = file.tasks[i];
                index += 1;
            }
        }
    }
    res.tasks = tasks;
    res.amount = index;
    return res;
}

__declspec(dllexport) tasksResponse findTasksAfter(pygantt file, task target)
/*
 * This function is used to find all the tasks after a given task
 * It returns a tasksResponse struct which contains an array of tasks and the amount of tasks
*/
{
    tasksResponse res;
    task *tasks = (task *)malloc(sizeof(task));
    int index = 0;
    // iterate through all the tasks in the file
    for (int i = 0; i < file.tasks_amount; i++)
    {
        // iterate through all the tasks after the target task
        for (int j = 0; j < target.tasks_after_amount; j++)
        {
            // if the names match add it to the list
            if (strcmp(file.tasks[i].name, target.tasks_after[j]) == 0)
            {
                tasks = realloc(tasks, sizeof(task) * (index + 1));
                tasks[index] = file.tasks[i];
                index += 1;
            }
        }
    }
    res.tasks = tasks;
    res.amount = index;
    return res;
}

__declspec(dllexport) int getTaskLevel(pygantt file, task target)
/*!
 * To find the level of a task, we take the maximum level of the tasks before
 * and we add 1 to it
 * If the task has no tasks before, we return 0
 */
{
    int max = 0;
    // if there is no task before then the level is just 0
    if (target.tasks_before_amount == 0)
    {
        return 0;
    }
    else
    {
        task *tasks_before = findTasksBefore(file, target).tasks;
        // we take the highes level of the tasks before and we add 1 to it
        for (int i = 0; i < target.tasks_before_amount; i++)
        {
            if (getTaskLevel(file, tasks_before[i]) > max)
            {
                max = getTaskLevel(file, tasks_before[i]);
            }
        }
        return max + 1;
    }
}

__declspec(dllexport) tasksResponse findCriticalPath(pygantt file)
/*!
 * To find the critical path, we start at the tasks that has the maximum end duration
 * and we go back until we find a task with no tasks before
 */
{
    tasksResponse res;
    task *path = (task *)malloc(sizeof(task));
    int max_dur = 0;
    int index = 0;
    // we initialize the maximum duration as the maximum end duration
    for (int i = 0; i < file.tasks_amount; i++)
    {
        if (file.tasks[i].min_start_date + file.tasks[i].duration > max_dur)
        {
            max_dur = file.tasks[i].min_start_date + file.tasks[i].duration;
        }
    }
    // Initialize the first critical last task
    task critical_last_task;
    for (int i = 0; i < file.tasks_amount; i++)
    {
        if (file.tasks[i].min_start_date + file.tasks[i].duration == max_dur)
        {
            critical_last_task = file.tasks[i];
        }
    }
    path[index] = critical_last_task;
    index += 1;
    // Iterate until we find a task with no tasks before
    while (critical_last_task.tasks_before_amount != 0)
    {
        tasksResponse res = findTasksBefore(file, critical_last_task);
        // find the tasks which has the maximum end duration
        int max_dur = 0;
        for (int i = 0; i < res.amount; i++)
        {
            if (res.tasks[i].min_start_date + res.tasks[i].duration > max_dur)
            {
                max_dur = res.tasks[i].min_start_date + res.tasks[i].duration;
                critical_last_task = res.tasks[i];
            }
        }
        path = realloc(path, sizeof(task) * (index + 1));
        path[index] = critical_last_task;
        index += 1;
    }
    // Invert the path
    task *path_inverted = malloc(sizeof(task) * index);
    for (int i = 0; i < index; i++)
    {
        path_inverted[i] = path[index - i - 1];
    }
    res.tasks = path_inverted;
    res.amount = index;
    return res;
}

__declspec(dllexport) int getMinStartDate(pygantt file, task target)
/*!
 * To find the minimum start date of a task, we take the maximum start date of the tasks before
 * and we add the duration of the task to it
 * If the task has no tasks before, we return the duration of the task
 */
{
    int min = 0;
    // if there is no task before then the minimum start date is just the duration of the task
    if (target.tasks_before_amount == 0)
    {
        return target.duration;
    }
    else
    {
        task *tasks_before = findTasksBefore(file, target).tasks;
        // we take the highest start date of the tasks before and we add the duration of the task to it
        for (int i = 0; i < target.tasks_before_amount; i++)
        {
            if (getMinStartDate(file, tasks_before[i]) + tasks_before[i].duration > min)
            {
                min = getMinStartDate(file, tasks_before[i]);
            }
        }
        return min + target.duration;
    }
}

__declspec(dllexport) int getMaxStartDate(pygantt file, task target)
/*!
 * To find the maximum start date of a task, we take the minimum start date of the tasks after
 * and we subtract the duration of the task to it
 * If the task has no tasks after, we return the maximum start date of all the tasks
 */
{
    tasksResponse res = findTasksAfter(file, target);
    if (res.amount != 0)
    {
        // initialize
        int min = res.tasks[0].min_start_date;
        // we take the lowest start date of the tasks after and we subtract the duration of the task to it
        for (int i = 0; i < res.amount; i++)
        {
            if (res.tasks[i].min_start_date < min)
            {
                min = res.tasks[i].min_start_date;
            }
        }
        return min - target.duration;
    }
    else
    {
        int max = 0;
        // if there is no task after then the maximum start date is just the maximum start date of all the tasks
        for (int i = 0; i < file.tasks_amount; i++)
        {
            if (file.tasks[i].min_start_date > max)
            {
                max = file.tasks[i].min_start_date;
            }
        }
        return max;
    }
}
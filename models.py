from datetime import datetime


def get_next_valid_id():
    if 'uid' not in get_next_valid_id.__dict__:
        get_next_valid_id.uid = 0

    get_next_valid_id.uid += 1
    return get_next_valid_id.uid


class Task:
    TASK_IMPORTANT = 3
    TASK_MILD = 2
    TASK_NORMAL = 1

    def __init__(self, name=None, deadline=None, est_size=1, priority=TASK_NORMAL):
        self.id = get_next_valid_id()
        self.name = name or 'New Task'
        self.deadline = deadline or datetime(2015, 11, 29)
        self.est_size = est_size
        self.priority = priority

    def __str__(self):
        return '({2}) {0} @ {1}'.format(self.name, self.deadline, self.est_size)

week_free_times = [
    4, 4, 2, 3, 4, 4, 4
]

tasks = [
    Task('CoOpt HW 2', datetime(2015, 11, 17), 3),
    Task('CoOpt HW 3', datetime(2015, 11, 19), 4),
    Task('DSD Midterm', datetime(2015, 11, 23), 6),
    Task('ESP TA', datetime(2015, 11, 22), 2),
    Task('Helli', datetime(2015, 11, 19), 1),
]


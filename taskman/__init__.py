__appname__ = 'taskman'
__version__ = '0.0.1'
__author__ = 'Matthias Gilch'


def project_add(name: str):
    """
    Save a new project

    :param name: Name of the project
    """
    pass


def project_select(name: str):
    """
    Select the current project

    :param name: Name of the project to select
    """
    pass


def task_add(name: str, priority: int=5, project: str=None, description: str=None):
    """
    Save a new task

    :param name: Name/Title of the task
    :param priority: Priority of the task between 0 and 10
    :param project: Name of the project to add to
    :param description: Description of the task
    """
    pass


def task_show(pk: int):
    pass


def task_summary(project: str=None):
    pass



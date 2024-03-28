todo_list = {
    "Faire les courses" : True,
    "Ranger le garage" : False,
    "Compléter l'exercice 4" : False,
}

def get_not_finished(todo:dict):
    tasks = []
    for task in todo: 
        if not todo[task] : tasks.append(task)
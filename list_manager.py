def insert_end(a_list, an_object):
    '''(list, object) -> None

    Inserts an_object into the end of a_list.
    '''
    a_list.append(an_object)

def insert_start(a_list, an_object):
    '''(list, object) -> None

    Inserts an_obect into the start of a_list.
    '''
    a_list.insert(0, an_object)

def insert_center(a_list, an_object):
    '''(list, object) -> None

    Inserts an_obect into the center of a_list.
    '''
    x = round((len(a_list)-0.5)/2)
    a_list.insert(x, an_object)

def remove_end(a_list):
    '''(list) -> None

    Removes an object in the end of the line.
    '''
    a_list.pop(-1)

def remove_start(a_list):
    '''(list) -> None

    Removes an object in the start of the line.
    '''
    a_list.pop(0)
    
def remove_center(a_list):
    '''(list) -> None

    Removes an object in the center of the line.
    '''
    x = round((len(a_list)-0.5)/2)
    print(x)
    a_list.pop(x)



    
def test_insert_end():
    names = []
    print("Inserting in the end:")
    insert_end(names, "Mary")
    print(names)
    insert_end(names, "John")
    print(names)
    insert_end(names, "Rambo")
    print(names)

def test_insert_start():
    names = []
    print("Inserting in the start:")
    insert_start(names, "Mary")
    print(names)
    insert_start(names, "John")
    print(names)
    insert_start(names, "Rambo")
    print(names)

def test_insert_center():
    names = []
    print("Inserting in the center:")
    insert_center(names, "Mary")
    print(names)
    insert_center(names, "John")
    print(names)
    insert_center(names, "Rambo")
    print(names)
    
def test_remove_end():
    names = ["James", "Mary", "Rambo"]
    print("Removing from the end:")
    print(names)
    remove_end(names)
    print(names)


def test_remove_start():
    names = ["James", "Mary", "Rambo"]
    print("Removing from the start:")
    print(names)
    remove_start(names)
    print(names)


def test_remove_center():
    names = ["James", "Mary", "Rambo",'asd','asdf','asdfg','asdfgh','zxc','qwe','qwer']
    print("Removing from the center:")
    print(names)
    remove_center(names)
    print(names)


    


def run_all_tests():
    test_insert_end()
    test_insert_start()
    test_insert_center()
    test_remove_end()
    test_remove_start()
    test_remove_center()

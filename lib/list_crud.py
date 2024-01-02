def create_an_empty_list():
    return []


l = [1, 2, 3, 4]

def create_a_list():
    print(l)

create_a_list()

def add_element_to_end_of_list(l, element):
    l.append(element)
    print(l)

add_element_to_end_of_list(l, 5)

def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    print(l)

add_element_to_start_of_list(l, 0)

def remove_element_from_end_of_list(l):
    l.pop()
    print(l)

remove_element_from_end_of_list(l)

def remove_element_from_start_of_list(l):
    del l[0]
    print(l)

remove_element_from_start_of_list(l)

def retrieve_first_element_from_list(l):
    print(l[0])
    
retrieve_first_element_from_list(l)

def retrieve_element_from_index(l, index):
    if 0 < len(l):
        return l[index]
    else:
        return None
    
print(retrieve_element_from_index(l, 2))

def retrieve_last_element_from_list(l):
    print(l[-1])

retrieve_last_element_from_list(l)
    

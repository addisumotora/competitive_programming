def has_cycle(head):
    listset = []
    
    current = head
    
    while current:
        if current.data in listset:
            return 1
        listset.append(current.data)
        current = current.next
    
    return 0
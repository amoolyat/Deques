from Deque_Generator import get_deque

class Queue:

    def __init__(self):
        self.__dq = get_deque()

    def __str__(self):
    # Orients string from front (left) to back (right).
        return str(self.__dq)

    def __len__(self):
        return len(self.__dq)

    def enqueue(self, val):
        self.__dq.push_back(val) 

    def dequeue(self):
        return self.__dq.pop_front()

    def peek(self):
        return self.__dq.peek_front()


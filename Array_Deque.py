from Deque import Deque

class Array_Deque(Deque):

    def __init__(self):
        self.__capacity = 1
        self.__contents = [None] * self.__capacity
        self.__size = 0
        self.__front = None
        self.__back = None
        
    
    def __str__(self):
        if self.__size == 0:
            return "[ ]"
        first = self.__front
        i = 0
        val = ""
        while first < self.__capacity and i < self.__capacity:
            if self.__contents[first] != " ": 
                val += str(self.__contents[first]) + ", "
            first = (first + 1) % self.__capacity
            i+=1
        val = val.strip(", ")
        return "[ " + val + " ]"
    
    def __len__(self):
        return self.__size

    def __grow(self):
        old_capacity = self.__capacity
        self.__capacity *= 2
        old_list = self.__contents
        self.__contents = [" "] * self.__capacity
        first = self.__front
        for i in range(len(old_list)):
            self.__contents[i] = old_list[first]
            if first == self.__back:
                self.__back = i
            first = (first + 1) % old_capacity
            #print("i: " + str(i) + " first " + str(first) + " self contents " + str(self.__contents))
        #self.__contents[len(old_list)] = old_list[self.__back]
        self.__front = 0
        #print(" back index " + str(self.__back) + "     " + str( self.__contents[self.__back]))
    
    def push_front(self, val):
        if self.__size == 0:
            self.__contents[0] = val
            self.__front = 0 
            self.__back = 0
        elif self.__size <= self.__capacity:
            if self.__size == self.__capacity:
                self.__grow()
            f = ((self.__front - 1 + self.__capacity) % self.__capacity)
            self.__contents[f] = val
            self.__front = f
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            return None
        first = self.__contents[self.__front]
        self.__contents[self.__front] = " "
        self.__front = ((self.__front + 1) % self.__capacity)
        self.__size -= 1
        return first
        
    def peek_front(self):
        if self.__size == 0:
            return None
        return self.__contents[self.__front]
    
    def push_back(self, val): 
        if self.__size == 0:
            self.__contents[0] = val
            self.__front = 0 
            self.__back = 0
        elif self.__size <= self.__capacity:
            if self.__size == self.__capacity:
                self.__grow()
            b = ((self.__back + 1) % self.__capacity)
            self.__contents[b] = val
            self.__back = b
        self.__size += 1
       
    def pop_back(self):
        if self.__size == 0:
            return None
        last = self.__contents[self.__back]
        self.__contents[self.__back] = " "
        self.__back = ((self.__back - 1 + self.__capacity) % self.__capacity)
        self.__size -= 1
        return last

    def peek_back(self):
        if self.__size == 0:
            return None
        return self.__contents[self.__back]
    


class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.__header = self.__Node(None)
        self.__trailer = self.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0
        self.__curr = None
        self.__iter_index = 0

    def __len__(self):
        return self.__size


    def append_element(self, val):
        node = Linked_List.__Node(val)
        node.prev = self.__trailer.prev
        node.prev.next = node
        node.next = self.__trailer
        self.__trailer.prev = node
        self.__size += 1

    def insert_element_at(self, val, index):
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        node = Linked_List.__Node(val)
        if index == 0:
            node.next = self.__header.next
            self.__header.next = node
            node.prev = self.__header
            node.next.prev = node 
        else:
            curr = self.__header
            count = 0
            while curr is not None and curr.next is not None and count < index:
                curr = curr.next
                count += 1
            
            nextNode = curr.next
            node.prev = curr
            node.next = nextNode
            nextNode.prev = node
            curr.next = node
        self.__size += 1

    def remove_element_at(self, index):
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        if index == 0:
            temp = self.__header.next.val
            self.__header.next = self.__header.next.next
            self.__header.next.prev = self.__header
            self.__size -= 1
            return temp
    
        else:
            curr = self.__header
            count = 0
            
            while curr is not None and curr.next is not None and count < index:
                curr = curr.next
                count += 1
            
            node = curr.next
            afterNode = node.next
            curr.next = afterNode
            afterNode.prev = curr
            node.prev = None
            node.next = None
            self.__size -= 1
            return node.val

    def get_element_at(self, index):
        if self.__size == 0 or index >= self.__size or index < 0:
            raise IndexError
        count = 0 
        curr = self.__header
        while curr.next is not None and count <= index:
            curr = curr.next
            count += 1
        return curr.val

    def rotate_left(self):
        if self.__size != 0:
            curr = self.__header.next
            self.__header.next = curr.next
            curr.next.prev = self.__header

            curr.prev = self.__trailer.prev
            curr.next = self.__trailer   
            self.__trailer.prev.next = curr
            self.__trailer.prev = curr
        
    def __str__(self):
        val = ""
        curr = self.__header.next
        while curr and curr != self.__trailer:
            val += str(curr.val) + ", "
            curr = curr.next
        val = val.strip(", ")
        if len(val):
            return "[ " + val + " ]"
        else:
            return "[ ]"

    def __iter__(self):
        self.__curr = self.__header.next
        self.__iter_index = 0
        return self

    def __next__(self):
        if self.__curr == self.__trailer:
            raise StopIteration
        to_return = self.__curr.val
        self.__curr = self.__curr.next
        self.__iter_index += 1
        return to_return

    def __reversed__(self):
        ll = Linked_List()
        ll_curr = ll.__header
        curr = self.__trailer.prev
        
        while curr is not None and curr != self.__header:
            n = Linked_List.__Node(curr.val)
            ll.__size +=1
            ll_curr.next = n
            ll_curr.next.prev = ll_curr
            ll.__trailer.prev = n
            ll.__trailer.prev.next = ll.__trailer
            curr = curr.prev
            ll_curr = ll_curr.next
        return ll
    
    def insert_increasing(self,val):
        current = self.__trailer
        newest = Linked_List.__Node(val)
        while current.prev is not self.__header:
            if current.prev.val < val:
                break
            current = current.prev
        print(current.val)
        current.prev.next = newest
        newest.prev = current.prev
        newest.next = current
        current.prev = newest
        self.__size = self.__size +1

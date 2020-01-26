
class Node:
    def __init__(self ,key ,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class HashTable:

    def __init__(self ,capacity):
        self.size = 0
        self.capacity = capacity  # Initial_capacity
        self.buckets = [None] * self.capacity

    def _hash_func(self, key):
        hash_sum = 0

        for indx ,char in enumerate(key):

            hash_sum += (indx + len(key)) ** ord(char)

            hash_sum = hash_sum % self.capacity # uniformly index distribute karne ke lye

        return hash_sum

    def Insert(self, key, value):
        self.size += 1

        index = self._hash_func(key)

        node = self.buckets[index]

        if node == None:
            self.buckets[index] = Node(key, value)

        else: # collision #  key ---> [n]-[n]-[n]
            x = self.buckets[index]
            while x:
                if x.next == None:
                    break
                x = x.next

            newnode = Node(key ,value)
            x.next = newnode
            newnode.previous = x


    def find(self, key):
        index = self._hash_func(key)

        node = self.buckets[index]


        while node != None and node.key != key:
            node = node.next

        if node == None:
            return 343
        else:

            return node.value

    def Delete(self ,key):

        index = self._hash_func(key)

        node = self.buckets[index]
        # prev = None

        while node != None and node.key != key: # node tak pohonchjayen """[ BG ]"""
            # prev = node
            node = node.next

        if node == None:
            return None

        elif self.buckets[index].key == key: # means that item is at first to be deleted
            vlaueofdeleted = self.buckets[index].value
            temp = self.buckets[index]
            self.buckets[index] = temp.next
            temp = None
            self.size -= 1
            return vlaueofdeleted

        elif node.next == None: # item is atlast
            self.size -= 1
            vlaueofdeleted = node.value
            prev = node.previous
            prev.next = None
            return vlaueofdeleted

        else: # item is in middle
            self.size -= 1
            # from [BG] we have traced the target node
            bckup = node.value
            aage_wala = node.next # node ke aage wala node
            peeche_wala = node.previous

            #linking the nodes
            peeche_wala.next = aage_wala
            aage_wala.previous = peeche_wala
            # deleting the node
            node = None

            return bckup # value of deleted node



    def print_HashTable(self):
        for i in self.buckets:
            if i != None and i.next == None:
                print(i.value)

            if i != None and i.next != None:
                x = i
                while x != None:
                    print(x.value)
                    x = x.next

    def getvalue(self,key): # all fine in here

        index = self._hash_func(key)
        node = self.buckets[index]

        while node.key != key:
            node = node.next

        return node.value

# print check
# ht = HashTable(10)
# obj = HashTable(10)
# obj.Insert('A', 5)
# obj.Insert('B', 10)
# obj.Insert('Ball', 'hello')
# obj.Insert('5656', 'kapcha')
# obj.Insert('2352', '23ooppe')
# obj.Insert('967sdsg', '12abs98jack')
# print("Print1")
# obj.print_HashTable()



# testing
# print("get")
# print(obj.getvalue('B'))
# print(obj.size)
#
# print(5 ,'==' ,obj.Delete('A'))
# print(obj.size)
# print(None ,'==' ,obj.Delete('A'))
# print(obj.size)
# print(None ,'==' ,obj.Delete('A'))
# print(obj.size)
#
# print(None ,'==' ,obj.Delete('A'))
#
# print(obj.find('A'))

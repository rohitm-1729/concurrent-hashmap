from data_structures.linked_list import LinkedList

class LinkedListEntry:

  def __init__(self) -> None:
    self.list = LinkedList()

  def add(self, item) -> None:
    self.list.add(item)

  def get(self, key: int) -> None:
    return self.list.search(key)

  def debug(self):
    head = self.list.head
    if head is None:
      print(None)
    else:
      tmp = head
      output = []
      while tmp:
        output.append("(% s, % s)" % (tmp.item.key, tmp.item.val))
        tmp = tmp.next
      print('->'.join(output))

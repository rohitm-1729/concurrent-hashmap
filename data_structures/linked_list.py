class LinkedListNode:
  def __init__(self, item) -> None:
    self.item = item
    self.next = None

class LinkedList:

  def __init__(self) -> None:
    self.head = None
    self.end = None

  def add(self, item) -> None:
    if self.end:
      self.end.next = LinkedListNode(item)
      self.end = self.end.next
    else:
      self.head = self.end = LinkedListNode(item)

  def search(self, key):
    tmp = self.head
    while tmp is not None:
      if tmp.item.key == key:
        return tmp.item.val
      tmp = tmp.next

    return 'No Value Found'

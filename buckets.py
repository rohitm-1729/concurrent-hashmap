from bucket.linked_list_entry import LinkedListEntry
from bucket.bucket_item import BucketItem

class Buckets:

  def __init__(self, size: int) -> None:
    self.buckets = [LinkedListEntry() for i in range(size)]
    self.size = size

  def add(self, hash: int, key: str, value: str) -> None:
    index = hash%self.size
    item = BucketItem(key,value)
    self.buckets[index].add(item)

  def get(self, hash: int, key: str) -> str:
    index = hash%self.size
    return self.buckets[index].get(key)

  def debug(self):
    for bucket in self.buckets:
      bucket.debug()

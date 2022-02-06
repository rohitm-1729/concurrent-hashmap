from hashing_strategy import HashingStrategy
from buckets import Buckets

class HashTable:
  def __init__(self, size: int) -> None:
    self.strategy = HashingStrategy()
    self.buckets = Buckets(size)

  def get(self, key: str) -> str:
    hash = self.strategy.generate_hash(key)
    return self.buckets.get(hash, key)

  def put(self, key: str, val: str) -> None:
    hash = self.strategy.generate_hash(key)
    self.buckets.add(hash, key, val)

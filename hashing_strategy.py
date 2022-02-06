from strategies.simple_hashing_strategy import SimpleHashingStrategy
from strategies.bad_hashing_strategy import BadHashingStrategy

class HashingStrategy:

  def __init__(self) -> None:
    self.strategy = BadHashingStrategy()

  def generate_hash(self, key: str) -> int:
    return self.strategy.generate_hash(key)

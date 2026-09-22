
class GlobalBudget:
    """
    One shared marketing budget across the system.
    """
    _instance = None


    def __new__(cls, initial_amount: float = 0.0):
      # TODO: Singleton pattern implementation
      if cls._instance is None:
         instance = super().__new__(cls) #interesting, so you don´t need to hardcode the object directly (could use object, that's the root class every other class in Python ultimately derives from)
         instance._balance = initial_amount
         cls._instance = instance
      return cls._instance
    #now the class atribute no longer points to None but to the actual GlobalBudget instance.
      

    def allocate(self, amount: float) -> None:
      # TODO: Allocate amount from the budget
      if amount <= 0:
         raise ValueError("Allocation amount must be larger thn 0.")
      if amount > self._balance:
          raise ValueError("Insufficient funds in the budget.")
      self._balance -= amount

    def remaining(self) -> float:
        return self._balance

    def __repr__(self) -> str:
        return f"<GlobalBudget remaining={self._balance}>"

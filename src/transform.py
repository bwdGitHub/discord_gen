from abc import ABC, abstractmethod

class Transform(ABC):

    @abstractmethod
    def transform(self,str):
        pass

class Test_Transform(Transform):

    def transform(self,str):
        # simple transform - just reverse the input string.
        return str[::-1]

"""
The Adapter design pattern is a structural design pattern that allows objects with incompatible interfaces to work
together. It wraps an existing class with a new interface so that it becomes compatible with the client's interface.
"""

from abc import ABC, abstractmethod
from pathlib import Path


#%% 3rd Party
class AmazingFilter:
    def __init__(self):
        print('Setting up filter')

    def transform(self, content: bytes) -> bytes:
        print('Making your phot amazing')
        return content


#%% Abstract
class Filter(ABC):
    @abstractmethod
    def apply(self, content: bytes) -> bytes:
        ...


#%% Implementation
class SepiaFilter(Filter):
    def apply(self, content: bytes) -> bytes:
        print('Making photo in sepia')
        return content


class SharpenFilter(Filter):
    def apply(self, content: bytes) -> bytes:
        print('Making photo sharp')
        return content


#%% Adapter
class AmazingFilterAdapter(Filter):
    filter: AmazingFilter

    def __init__(self):
        self.filter = AmazingFilter()

    def apply(self, content: bytes) -> bytes:
        self.filter.__init__()
        return self.filter.transform(content)


#%% Main
class Image:
    path: Path
    content: bytes

    def __init__(self, path):
        self.path = Path(path)
        self.content = self.path.read_bytes()

    def apply(self, filter: Filter) -> None:
        self.content = filter.apply(self.content)


if __name__ == '__main__':
    img = Image('some_imgs_path.png')
    img.apply(SepiaFilter())
    img.apply(SharpenFilter())
    img.apply(AmazingFilterAdapter())

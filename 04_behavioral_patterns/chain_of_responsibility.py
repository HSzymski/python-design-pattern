"""
The Chain of Responsibility design pattern is a behavioral design pattern that allows an object to pass the request
along the chain of potential handlers until an object handles it. It simplifies your code and allows you to skip
explicit sender-receiver bindings.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class HttpRequests:
    username: str
    password: str

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password


@dataclass
class Handler(ABC):
    next: 'Handler'

    @abstractmethod
    def do_handle(self, request: HttpRequests) -> bool:
        pass

    def handle(self, request: HttpRequests) -> None:
        if self.do_handle(request):
            return
        if self.next:
            self.next.handle(request)


class Authenticator(Handler):
    def do_handle(self, request: HttpRequests) -> bool:
        is_valid: bool = (request.get_username() == 'admin' and
                          request.get_password() == 'myVoiceIsMyPassword')
        print('Authentication')
        return not is_valid


class Compressor(Handler):
    def do_handle(self, request: HttpRequests) -> bool:
        print('Compress')


class Logger(Handler):
    def do_handle(self, request: HttpRequests) -> bool:
        print('Log')


@dataclass
class WebServer:
    handler: Handler

    def handle(self, request: HttpRequests) -> None:
        self.handler.handle(request)


if __name__ == '__main__':
    # authenticator -> logger -> compressor
    compressor: Compressor = Compressor(None)
    logger: Logger = Logger(compressor)
    authenticator: Authenticator = Authenticator(logger)
    server = WebServer(authenticator)
    server.handle(HttpRequests('admin', 'myVoiceIsMyPassword'))
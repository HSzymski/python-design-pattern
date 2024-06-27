"""
The Proxy design pattern is a structural design pattern that provides a surrogate or placeholder for another object to
control access to it. This pattern is used when you need to create a wrapper to cover the main object’s complexity.
"""


class RealSubject:
    def request(self) -> str:
        return "RealSubject: Handling request."


class Proxy:
    _real_subject: RealSubject = None

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> str:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")


real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
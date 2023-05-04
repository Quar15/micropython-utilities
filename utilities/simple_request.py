import urequests as requests
# import requests
from utilities.threads import SECOND_THREAD_LOCK, start_thread


def get(url: str):
    return requests.get(url)


def post(url: str, data: str):
    return requests.post(url, data=data)


def put(url: str, data: str):
    return requests.put(url, data=data)


def delete(url: str, data: str):
    return requests.delete(url, data=data)


class ThreadRequest:
    req = None

    @staticmethod
    def wait_for_last_request():
        SECOND_THREAD_LOCK.acquire()
        SECOND_THREAD_LOCK.release()


    def _get(self, url):
        req = requests.post(url)


    def get(self, url: str):
        start_thread(self._get, (self, url, ))


    def _get(self, url):
        req = requests.post(url)


    def post(self, url: str, data: str):
        start_thread(self._get, (self, url, data ))


    def put(self, url: str, data: str):
        start_thread(self._get, (self, url, data ))


    def delete(self, url: str, data: str):
        start_thread(self._get, (self, url, data ))
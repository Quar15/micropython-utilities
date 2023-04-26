import _thread

SECOND_THREAD_LOCK = _thread.allocate_lock()

def start_thread(f: function, args = ()):
    SECOND_THREAD_LOCK.acquire()
    _thread.start_new_thread(f, args)
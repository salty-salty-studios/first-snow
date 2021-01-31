init python:
    import time
    import threading

    class ExtendableEvent(NoRollback):
        def __init__(self, interval, stop_func, start_func=None):
            self.ends_at = None
            self.timer = None
            self.interval = interval
            self.start_func = start_func
            self.stop_func = stop_func

        def trigger(self):
            now = time.time()
            if now < self.ends_at:
                self.timer = threading.Timer(self.ends_at - now, self.trigger)
                self.timer.run()
            else:
                self.timer = None
                self.stop_func()

        def start(self, run_start=True):
            self.ends_at = time.time() + self.interval
            self.timer = threading.Timer(self.interval, self.trigger)
            self.timer.start()
            if run_start and self.start_func:
                self.start_func()

        def cancel(self):
            self.timer.cancel()

        def extend(self, interval):
            new_ends = time.time() + interval
            self.interval = interval
            if new_ends < self.ends_at:
                self.cancel()
                self.start(run_start=False)
            else:
                self.ends_at = new_ends

        def has_ended(self):
            return self.timer is None

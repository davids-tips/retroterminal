import time
import sys

def delay_print(s, delay: int = None):
    if delay == None:
        delay = .25
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()
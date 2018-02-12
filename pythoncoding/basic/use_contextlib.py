from contextlib import contextmanager, closing
from urllib.request import urlopen

class Query(object):
    def __init__(self, name):
        self.name = name
        
    def query(self):
        print('Query info about %s...' % self.name)
        
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
    
with create_query('Bob') as q:
    q.query()
    
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
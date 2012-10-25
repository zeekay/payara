from os.path import join, dirname, abspath

GIT_HOST      = 'git@github.com'
ACCESS_KEY    = 'your AWS access key'
ACCESS_SECRET = 'your AWS access secret'
IGNORED_FILES = []
IGNORED_EXTS  = ['.pyc']
REPOS_ROOT    = join(dirname(abspath(__file__)), 'repos')
HOST          = '127.0.0.1'
PORT          = 8000
SERVER        = 'wsgiref'
SERVER_OPTS   = {}

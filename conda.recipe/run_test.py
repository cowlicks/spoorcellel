import sys
from os import environ, path

import pytest


out = pytest.main(['-vv', path.join(environ['SRC_DIR'], 'spoorcellel')])
sys.exit(out)

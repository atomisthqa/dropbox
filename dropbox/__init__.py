# -*- coding: utf-8 -*-
import logging
try:
    from logging import NullHandler
except ImportError:
    from logging import Handler

    class NullHandler(Handler):
        def emit(self, record):
            pass


__version__ = '0.1.0'
__doc__ = """
My new project
"""

logging.getLogger('dropbox').addHandler(NullHandler())


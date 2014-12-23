"""
Settings used by spire project.

This consists of the general production settings, with an optional import of any local
settings.
"""

# Import production settings.
from spire.settings.production import *

# Import optional local settings.
try:
    from spire.settings.local import *
except ImportError:
    pass

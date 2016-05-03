import collections

from .output import Output
from .graphviz import GraphvizOutput
from .gephi import GephiOutput
from .ubigraph import UbigraphOutput
from .pickle import PickleOutput
from .text import TextOutput


outputters = collections.OrderedDict([
    ('graphviz', GraphvizOutput),
    ('gephi', GephiOutput),
    ('text', TextOutput),
    # ('ubigraph', UbigraphOutput),
])

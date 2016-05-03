from .output import Output


class TextOutput(Output):
    def __init__(self, **kwargs):
        self.fp = None
        self.output_file = 'pycallgraph.txt'
        Output.__init__(self, **kwargs)

    @classmethod
    def add_arguments(cls, subparsers, parent_parser, usage):
        defaults = cls()

        subparser = subparsers.add_parser(
            'text', help='Text generation',
            parents=[parent_parser], usage=usage,
        )

        cls.add_output_file(
            subparser, defaults, 'The generated text file'
        )

    def done(self):
        f = open(self.output_file, 'w')
        edges = ['%s -> %s (%d, %f)' % (e.src_func, e.dst_func, e.calls.value, e.time.value) for e in self.processor.edges()]
        f.write('\n'.join(edges))
        f.close()

    def update(self):
        pass

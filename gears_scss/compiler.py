import os
import sass
from gears.compilers import BaseCompiler


class SCSSCompiler(BaseCompiler):

    result_mimetype = 'text/css'

    def __call__(self, asset):
        asset.processed_source = self.run(asset.processed_source)

    def run(self, source):
        return sass.compile_string(source.encode('utf-8')).decode('utf-8')

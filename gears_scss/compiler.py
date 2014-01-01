import os
import sys
import sass
from gears.compilers import BaseCompiler


class SCSSCompiler(BaseCompiler):

    result_mimetype = 'text/css'

    def __call__(self, asset):
        include_folder = os.path.dirname(asset.absolute_path)
        asset.processed_source = self.run(asset.processed_source, include_folder)

    def run(self, source, include_folder):
        source = bytes(source, encoding='utf-8')
        include_folder = include_folder.encode(sys.getfilesystemencoding())
        return sass.compile_string(source, include_folder).decode('utf-8')

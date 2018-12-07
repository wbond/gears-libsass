import os
import sys
import sass
import re
from gears.compilers import BaseCompiler


class LibsassCompiler(BaseCompiler):

    result_mimetype = 'text/css'

    def __call__(self, asset):
        include_folder = os.path.dirname(asset.absolute_path)
        asset.processed_source = self.run(asset.processed_source, include_folder)
        for path in self.find_imports(asset.absolute_path):
            asset.dependencies.add(path)

    def run(self, source, include_folder):
        source = bytes(source, encoding='utf-8')
        return sass.compile(string=source, include_paths=[include_folder])

    def find_imports(self, path):
        dirname = os.path.dirname(path)
        with open(path, 'rb') as f:
            contents = f.read().decode('utf-8')

        output = []
        for match in re.findall(r'^\s*@import\s+("[^"]+"|\'[^\']+\')\s*;', contents, re.I | re.M):
            # Figure out what folder it should be in first. If the import
            # includes a folder name:
            #
            # @import "foo/example"
            #
            # Then we will get something like:
            #
            # /path/to/scss/foo/example
            temp_path = os.path.join(dirname, match[1:-1])
            temp_path = os.path.normpath(temp_path)
            # However, we need to then add the _ prefix and .scss suffix in
            # order to get a result like:
            #
            # /path/to/scss/foo/_example.scss
            import_dirname = os.path.dirname(temp_path)
            import_filename = '_%s.scss' % os.path.basename(temp_path)
            import_path = os.path.join(import_dirname, import_filename)

            output.append(import_path)
            output.extend(self.find_imports(import_path))

        # Clean up the list to be minimal
        output = set(output)
        output.discard(path)

        return list(output)

# Copyright (C) 2024 Mike Pento
#
# This file is part of Versionbump.
#
# Versionbump is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# Versionbump is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this Versionbump.  If not, see <http://www.gnu.org/licenses/>.

import logging
from versionbump import utils
from versionbump.version import Version

from versionbump.exception import InvalidPathName


class Process:
    '''
    This is a class that processes bump requests.
    '''
    dirty_files = 0

    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(cls)

    def __init__(self, path, version, replace, field, increment):
        if not path.is_dir():
            raise InvalidPathName('Invalid path name.')

        if increment <= 0:
            raise ValueError(
                'Increment must be a positive number, greater than zero.'
                )

        self.path = path
        self.version = version
        self.replace = replace
        self.field = field
        self.increment = increment

        # get bumped version
        self.bumped_version = Version(self.version).bump(field, increment)
        
        if self.replace != None:
            self.bumped_version = Version(self.replace).replace()
        else:
            self.bumped_version = Version(self.version).bump(field, increment)

    def do_process(self):
        if self.replace != None:
            logging.info(
                'Replacing version \'%s\' with version \'%s\'.',
                self.version,
                self.replace)
        else:
            logging.info(
                'Bumping field \'%s\' of version %s by an increment of %d.',
                self.field,
                self.version,
                self.increment)

        logging.info('The new version will be %s.', self.bumped_version)

        # get file list
        files = list(utils.get_files(self.path))

        for file in files:
            logging.info('Processing File: %s', utils.get_parent(file))

            # if the file is not binary, process it.
            if utils.is_binary(file):
                logging.info('File %s is binary, skipping.',
                             utils.get_parent(file))
            else:
                # get file content
                content = list(utils.load_file(file))

                # copy file content to buffer
                buffer = content.copy()

                for i, line in enumerate(content):
                    if self.version in line:
                        content[i] = line.replace(self.version,
                                                  self.bumped_version)

                # if file has been changed, save it
                if self.is_dirty(buffer, content):
                    utils.save_file(file, content)

        # done
        logging.info('Modified %d out of %d files.',
                     Process.dirty_files,
                     len(files))

    def is_dirty(self, buffer, content):
        if set(buffer) != set(content):
            Process.dirty_files += 1
            return True
        return False

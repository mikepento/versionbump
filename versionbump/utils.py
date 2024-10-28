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

import os
import io
import errno
import logging
from pathlib import Path
from versionbump.config import Config

BLOCK_SIZE = 1024


def get_files(path):
    ''' Return a list of files matching a search pattern. '''
    config = Config()

    files = [file for pattern in config.get_patterns()
             for file in Path(path).glob('**/**/' + pattern)]

    if not len(files) > 0:
        raise SystemExit('No matching files found, nothing to do.')
    logging.info('Found %d files matching search criteria.',
                 len(files))
    return files


def load_file(file):
    ''' Load file and return content. '''
    try:
        with io.open(file, 'r', encoding='utf-8', errors='ignore') as fp:
            return fp.readlines()
    except IOError as ex:
        raise IOError(errno.EIO, os.strerror(errno.EIO), file) from ex


def save_file(file, content):
    ''' Save file. '''
    try:
        with io.open(file, 'w', encoding='utf-8') as fp:
            fp.writelines(content)
    except IOError as ex:
        raise IOError(errno.EIO, os.strerror(errno.EIO), file) from ex


def get_parent(path, levels=1):
    ''' Return current path with levels number of parents. '''
    common = path
    for i in range(levels + 1):
        common = os.path.dirname(common)
    return os.path.relpath(path, common)


def is_binary(file):
    ''' Binary file check. '''
    try:
        with open(file, mode='rb') as fp:
            while 1:
                block = fp.read(BLOCK_SIZE)
                if b'\0' in block:
                    return True
                if len(block) < BLOCK_SIZE:
                    break
    except IOError as ex:
        raise IOError(errno.EIO, os.strerror(errno.EIO), file) from ex
    return False

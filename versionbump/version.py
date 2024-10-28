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

import re
from versionbump.exception import MalformedVersionString


class Version:
    """
    This is a class that provides methods for validating version
    string format and data, and bumping specific field values by
    specific increments.
    """

    def __init__(self, version):
        if not re.match(r'^(\d+)\.(\d+)\.(\d+)$', version):
            raise MalformedVersionString(
                f'The string \"{version}\" is not a valid version string.'
                )
        self.version = version

    def bump(self, field, increment=1):
        ''' Bump the version field value by increment. '''
        # split version fields to integer vars
        major, minor, patch = map(int, self.version.split('.'))

        # bump rules by field
        # NOTE: "noqa" ignores line during code analysis
        match field: # noqa
            case 'major':
                major += increment
                minor = 0
                patch = 0
            case 'minor':
                minor += increment
                patch = 0
            case 'patch':
                patch += increment

        return '.'.join(map(str, (major, minor, patch)))

    def replace(self):
        ''' Returns replacement version, for format verification purposes. '''
        return self.version

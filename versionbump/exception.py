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


class VersionBumpException(Exception):
    """ Base Class for versionbump exceptions """


class MalformedVersionString(VersionBumpException):

    def __init__(self, message):
        self.message = message


class WrongPythonVersion(VersionBumpException):

    def __init__(self, message):
        self.message = message


class InvalidPathName(VersionBumpException):

    def __init__(self, message):
        self.message = message

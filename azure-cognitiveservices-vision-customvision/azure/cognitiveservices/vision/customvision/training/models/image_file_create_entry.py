# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageFileCreateEntry(Model):
    """ImageFileCreateEntry.

    :param name:
    :type name: str
    :param contents:
    :type contents: bytearray
    :param tag_ids:
    :type tag_ids: list[str]
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'contents': {'key': 'Contents', 'type': 'bytearray'},
        'tag_ids': {'key': 'TagIds', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ImageFileCreateEntry, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.contents = kwargs.get('contents', None)
        self.tag_ids = kwargs.get('tag_ids', None)

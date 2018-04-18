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


class ImageCreateSummary(Model):
    """ImageCreateSummary.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar is_batch_successful:
    :vartype is_batch_successful: bool
    :ivar images:
    :vartype images:
     list[~azure.cognitiveservices.vision.customvision.training.models.ImageCreateResult]
    """

    _validation = {
        'is_batch_successful': {'readonly': True},
        'images': {'readonly': True},
    }

    _attribute_map = {
        'is_batch_successful': {'key': 'IsBatchSuccessful', 'type': 'bool'},
        'images': {'key': 'Images', 'type': '[ImageCreateResult]'},
    }

    def __init__(self, **kwargs):
        super(ImageCreateSummary, self).__init__(**kwargs)
        self.is_batch_successful = None
        self.images = None

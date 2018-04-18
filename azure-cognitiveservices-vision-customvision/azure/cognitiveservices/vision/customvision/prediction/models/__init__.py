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

try:
    from .image_url_py3 import ImageUrl
    from .image_tag_prediction_model_py3 import ImageTagPredictionModel
    from .image_prediction_result_model_py3 import ImagePredictionResultModel
except (SyntaxError, ImportError):
    from .image_url import ImageUrl
    from .image_tag_prediction_model import ImageTagPredictionModel
    from .image_prediction_result_model import ImagePredictionResultModel

__all__ = [
    'ImageUrl',
    'ImageTagPredictionModel',
    'ImagePredictionResultModel',
]

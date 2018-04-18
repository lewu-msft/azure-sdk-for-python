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

from enum import Enum


class SkuName(Enum):

    f0 = "F0"
    s1 = "S1"


class SkuTier(Enum):

    free = "Free"
    standard = "Standard"


class Kind(Enum):

    sdk = "sdk"
    designer = "designer"
    bot = "bot"
    function = "function"


class ChannelName(Enum):

    facebook_channel = "FacebookChannel"
    email_channel = "EmailChannel"

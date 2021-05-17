#!/usr/bin/env python
# encoding: utf-8
#
#
# Monday, April 12, 2021, 6:11 PM
#

"""Common settings."""

from __future__ import unicode_literals
import os
import random
from workflow import Workflow3, ICON_WARNING

wf = Workflow3()


BEEUSER = os.path.expanduser(os.getenv('BEEUSER', ''))
TOKEN = os.path.expanduser(os.getenv('BEETOKEN', ''))
BEECOMMENT = os.path.expanduser(os.getenv('BEECOMMENT', ''))

    

	

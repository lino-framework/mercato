# -*- coding: UTF-8 -*-
# Copyright 2017-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, rt, _
from django.db import models
from django.conf import settings

from lino.utils import join_elems
from etgen.html import E
from lino.core.fields import IncompleteDateField
from lino.mixins import CreatedModified, BabelDesignated
from lino.core.roles import Explorer





# encoding: utf-8
#
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http:# mozilla.org/MPL/2.0/.
#
# Contact: Kyle Lahnakoski (kyle@lahnakoski.com)
#

"""
# NOTE:

THE self.lang[operator] PATTERN IS CASTING NEW OPERATORS TO OWN LANGUAGE;
KEEPING Python AS# Python, ES FILTERS AS ES FILTERS, AND Painless AS
Painless. WE COULD COPY partial_eval(), AND OTHERS, TO THIER RESPECTIVE
LANGUAGE, BUT WE KEEP CODE HERE SO THERE IS LESS OF IT

"""
from __future__ import absolute_import, division, unicode_literals

from jx_base.expressions._utils import simplified
from jx_base.expressions.expression import Expression
from jx_base.expressions.false_op import FALSE
from mo_json import BOOLEAN

NotOp = None


class ExistsOp(Expression):
    data_type = BOOLEAN

    def __init__(self, term):
        Expression.__init__(self, [term])
        self.field = term

    def __data__(self):
        return {"exists": self.field.__data__()}

    def vars(self):
        return self.field.vars()

    def map(self, map_):
        return self.lang[ExistsOp(self.field.map(map_))]

    def missing(self):
        return FALSE

    def exists(self):
        return TRUE

    @simplified
    def partial_eval(self):
        return self.lang[NotOp(self.field.missing())].partial_eval()

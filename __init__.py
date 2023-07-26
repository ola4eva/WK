# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2016 Webkul Software Pvt. Ltd.
# Author : www.webkul.com
#
##############################################################################

from . import models
from . import wizard
from . import report

def pre_init_check(cr):
    from odoo.service import common
    from odoo.exceptions import UserError
    version_info = common.exp_version()
    server_serie = version_info.get('server_serie')
    if not 14 < float(server_serie) <= 16.0:
        raise UserError(
            'Module support Odoo series 16.0 found {}.'.format(server_serie))
    return True


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

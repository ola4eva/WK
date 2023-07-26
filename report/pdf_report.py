
# -*- coding: utf-8 -*-
###############################################################################
#
#  Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
###############################################################################

from odoo import api, fields, models
from odoo import tools, _

class SendPayslipReport(models.AbstractModel):
    _name = 'report.employee_payslip_send_email.report_send_payslip'
    _description = "Payslip Pdf Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        employee_id = self.env.context.get('employee_id')
        date_from = self.env.context.get('date_from')
        date_to = self.env.context.get('date_to')
        payslips = self.env['wk.hr.payslip'].search(
            [
                '|','&',('date_from', '>=', date_from),
                ('date_from', '<=', date_to),'&',
                ('date_to', '>=', date_from),
                ('date_to', '<=', date_to),
                ('employee_id', '=', employee_id)
            ], order="date_from asc")
        docargs = {
            'doc_ids': data.get('ids', payslips),
            'doc_model': 'wk.hr.payslip',
            'docs': payslips,
            'data': dict(
                data,
                records=payslips,
            ),
        }
        return docargs

# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2016 Webkul Software Pvt. Ltd.
# Author : www.webkul.com
#
##############################################################################

from odoo import api, fields, models, tools, _

class HrPayslip(models.Model):
    _inherit = 'wk.hr.payslip'

    def action_payslip_sent(self):
        template = self.env.ref('employee_payslip_send_email.payslip_send_template_single', raise_if_not_found=False)
        for obj in self:
            if template and obj.payslip_count!=0:
                template.sudo().send_mail(obj.id, force_send=True)
                return self.env['wizard.message'].generated_message("Email sent successfully!!")
            else:
                return self.env['wizard.message'].generated_message("First, create payslip lines for this record!!")
        return True        

        

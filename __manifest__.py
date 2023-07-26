# -*- coding: utf-8 -*-
##########################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
##########################################################################
{
    "name":  "Employee Payslip Send By Email",
    "summary":  '''Hassle-free way to send payslips to employees in Odoo!''',
    "category":  "Human Resources",
    "version":  "1.0.0",
    "sequence":  15,
    "license":  "Other proprietary",
    "author":  "Webkul Software Pvt. Ltd.",
    "website":  "https://store.webkul.com/Odoo-Employee-Payslip-Send-By-Email.html",
    "description":  """https://store.webkul.com""",
    "live_test_url":  "http://odoodemo.webkul.com/?module=employee_payslip_send_email",
    "depends":  [
        'wk_hr_payroll',
    ],
    "data":  [
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'report/report_template.xml',
        'report/report.xml',
        'data/mail_template_data.xml',
        'views/payslip_send_employee_view.xml',
        'wizard/payslip_send_view.xml',
    ],
    "images":  ['static/description/Banner.gif'],
    "application":  True,
    "installable":  True,
    "auto_install":  False,
    "price":  25,
    "currency":  "USD",
    "pre_init_hook":  "pre_init_check",
}

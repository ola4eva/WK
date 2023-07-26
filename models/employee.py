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

from odoo import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _description = 'Employee'

    medic_exam = fields.Date(string='Medical Examination Date', groups='base.group_user')
    vehicle = fields.Char(string='Company Vehicle', groups='base.group_user')
    first_contract_date = fields.Date(compute='_compute_first_contract_date', groups="base.group_user")

    # from core

    address_home_id = fields.Many2one(
        'res.partner', 'Address', help='Enter here the private address of the employee, not the one linked to your company.',
        groups="base.group_user", tracking=True,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    private_email = fields.Char(related='address_home_id.email', string="Private Email", groups="base.group_user")
    country_id = fields.Many2one(
        'res.country', 'Nationality (Country)', groups="base.group_user", tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], groups="base.group_user", tracking=True)
    marital = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('cohabitant', 'Legal Cohabitant'),
        ('widower', 'Widower'),
        ('divorced', 'Divorced')
    ], string='Marital Status', groups="base.group_user", default='single', tracking=True)
    spouse_complete_name = fields.Char(string="Spouse Complete Name", groups="base.group_user", tracking=True)
    spouse_birthdate = fields.Date(string="Spouse Birthdate", groups="base.group_user", tracking=True)
    children = fields.Integer(string='Number of Children', groups="base.group_user", tracking=True)
    place_of_birth = fields.Char('Place of Birth', groups="base.group_user", tracking=True)
    country_of_birth = fields.Many2one('res.country', string="Country of Birth", groups="base.group_user", tracking=True)
    birthday = fields.Date('Date of Birth', groups="base.group_user", tracking=True)
    ssnid = fields.Char('SSN No', help='Social Security Number', groups="base.group_user", tracking=True)
    sinid = fields.Char('SIN No', help='Social Insurance Number', groups="base.group_user", tracking=True)
    identification_id = fields.Char(string='Identification No', groups="base.group_user", tracking=True)
    passport_id = fields.Char('Passport No', groups="base.group_user", tracking=True)
    bank_account_id = fields.Many2one(
        'res.partner.bank', 'Bank Account Number',
        domain="[('partner_id', '=', address_home_id), '|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        groups="base.group_user",
        tracking=True,
        help='Employee bank salary account')
    permit_no = fields.Char('Work Permit No', groups="base.group_user", tracking=True)
    visa_no = fields.Char('Visa No', groups="base.group_user", tracking=True)
    visa_expire = fields.Date('Visa Expire Date', groups="base.group_user", tracking=True)
    additional_note = fields.Text(string='Additional Note', groups="base.group_user", tracking=True)
    certificate = fields.Selection([
        ('graduate', 'Graduate'),
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
        ('doctor', 'Doctor'),
        ('other', 'Other'),
    ], 'Certificate Level', default='other', groups="base.group_user", tracking=True)
    study_field = fields.Char("Field of Study", groups="base.group_user", tracking=True)
    study_school = fields.Char("School", groups="base.group_user", tracking=True)
    emergency_contact = fields.Char("Emergency Contact", groups="base.group_user", tracking=True)
    emergency_phone = fields.Char("Emergency Phone", groups="base.group_user", tracking=True)
    km_home_work = fields.Integer(string="Home-Work Distance", groups="base.group_user", tracking=True)
    phone = fields.Char(related='address_home_id.phone', related_sudo=False, readonly=False, string="Private Phone", groups="base.group_user")
    category_ids = fields.Many2many(
        'hr.employee.category', 'employee_category_rel',
        'emp_id', 'category_id', groups="hr.group_hr_manager",
        string='Tags')
    notes = fields.Text('Notes', groups="base.group_user")
    color = fields.Integer('Color Index', default=0, groups="base.group_user")
    barcode = fields.Char(string="Badge ID", help="ID used for employee identification.", groups="base.group_user", copy=False)
    pin = fields.Char(string="PIN", groups="base.group_user", copy=False,
        help="PIN used to Check In/Out in Kiosk Mode (if enabled in Configuration).")
    departure_reason = fields.Selection([
        ('fired', 'Fired'),
        ('resigned', 'Resigned'),
        ('retired', 'Retired')
    ], string="Departure Reason", groups="base.group_user", copy=False, tracking=True)
    departure_description = fields.Text(string="Additional Information", groups="base.group_user", copy=False, tracking=True)
    departure_date = fields.Date(string="Departure Date", groups="base.group_user", copy=False, tracking=True)
    message_main_attachment_id = fields.Many2one(groups="base.group_user")
    contract_warning = fields.Boolean(string='Contract Warning', store=True, compute='_compute_contract_warning', groups="base.group_user")

    payslip_count = fields.Integer(
        compute='_compute_payslip_count',
        string='Payslip Count',
        groups="base.group_user")

    def _compute_payslip_count(self):
        for employee in self:
            employee.payslip_count = len(employee.slip_ids)

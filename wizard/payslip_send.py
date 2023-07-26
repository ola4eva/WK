# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2016 Webkul Software Pvt. Ltd.
# Author : www.webkul.com
#
##############################################################################

from odoo import api, fields, models, tools, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class PayslipSend(models.TransientModel):
	_name = 'payslip.send'
	_description = "Payslip Send Wizard"
	
	date_from = fields.Date(string='Date From', required=True, default=lambda self: fields.Date.to_string(date.today().replace(day=1)))
	date_to = fields.Date(string='Date To', required=True, default=lambda self: fields.Date.to_string((datetime.now() + relativedelta(months=+1, day=1, days=-1)).date()))
	
	def send_payslips(self):
		txt1 = ""
		employee_ids = self.env.context.get('active_ids')
		rec = self.env['wk.hr.payslip'].search([('employee_id','in',employee_ids),('date_from','=',self.date_from),('date_to','=',self.date_to)])
		template = self.env.ref('employee_payslip_send_email.payslip_send_template', raise_if_not_found=False)
		for count in range(len(employee_ids)):
			for record in rec:
				if template and employee_ids[count]==record.employee_id.id and record.payslip_count!=0:
					template.sudo().with_context(employee_id=employee_ids[count], date_from=self.date_from, date_to=self.date_to).send_mail(employee_ids[count], force_send=True)
					txt1 += str(record.employee_id.name) + ", "		
		if txt1 != "":
			txt1 = "Email sent successfully, to the employee(s): " + txt1
		else:
			txt1 = "Create payslip of the employee(s) for " +str(self.date_from.strftime("%B")) + " first!!"	
		return self.env['wizard.message'].generated_message(txt1)
		
		
class WizardMessage(models.TransientModel):
	_name = "wizard.message"
	_description = "Message Wizard"
	
	text = fields.Text(string='Message')
	
	def generated_message(self,message,name='Message/Summary'):
		partial_id = self.create({'text':message}).id
		return {
			'name':name,
			'view_mode': 'form',
			'view_id': False,
			'view_type': 'form',
			'res_model': 'wizard.message',
			'res_id': partial_id,
			'type': 'ir.actions.act_window',
			'target': 'new',
			'domain': '[]',
		}

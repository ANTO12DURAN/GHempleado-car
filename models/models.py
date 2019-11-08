# -*- coding: utf-8 -*-

from odoo import models, fields


class CarRequest(models.Model):
    _name = "car.request"  # tabla de bd => car_request
    _description = "Car Resquet"

    name = fields.Char(string="Request", required=True, )
    date_form = fields.Datetime(string="Starting Date", default=fields.Datetime.now(), )
    date_to = fields.Datetime(string="End Date", required=False, )
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required=True, )
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required=True, )

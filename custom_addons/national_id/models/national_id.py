# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models


class NationalId(models.Model):
    _name = "national.id"
    _description ="National Id Application records"

    surname = fields.Char(string="Surname", required=True)
    lastname = fields.Char(string="Lastname", required=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender")
    age = fields.Integer(string="Age", required=True)
    district = fields.Char(string="District", required=True)
    sub_county = fields.Char(string="Sub_county", required=True)
    parish = fields.Char(string="Parish", required=True)
    village = fields.Char(string="Village", required=True)
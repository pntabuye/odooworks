# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cdw_inherit_odoo_credentials = fields.Boolean("Inherit Odoo Credentials")
    cdw_login = fields.Char()
    cdw_password = fields.Char()
    cdw_xmlapi_baseurl = fields.Char()

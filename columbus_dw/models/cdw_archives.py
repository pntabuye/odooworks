# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ColumbusDWArchives(models.Model):
    _name = 'cdw.archives'
    _description = 'Columbus DW Archives'

    name = fields.Char()
    webexpress = fields.Char(compute='_compute_webexpress_url')
    archive = fields.Selection([
        ('documents\\phone bills\\all documents', 'Phone Bills'),
        ('documents\\phone bills\\all documents', 'Phone Bills1'),
        ('documents\\phone bills\\all documents', 'Phone Bills2'),
        ], string='Archive selection', default='documents\\phone bills\\all documents'
    )

    @api.onchange('archive')
    def _compute_webexpress_url(self):
        self.webexpress  = 'http://37.187.240.107/columbusdw/index.htm"'
        self.webexpress += '?username=salesforce'
        self.webexpress += '&amp;autologin=1&amp;showtoolbars=1&amp;showtree=0&amp;dockedview=1&amp;'
        self.webexpress += 'startuppath=' + self.archive

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

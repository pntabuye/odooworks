# -*- coding: utf-8 -*-
{
    'name': "Columbus DW for Odoo",
    'summary': """Columbus DW connector for Odoow""",
    'version': '13.0.0.0.1',
    'category': 'Document Management',
    "license": "LGPL-3",
    'website': "http://www.planbweb.com",
    'author': "Paul Ntabuye Butera",
    "contributors": [
        "Paul Ntabuye Butera <pntabuye@planbweb.com>",
    ],
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings.xml',
        'views/columbusdw_archives_views.xml',
        'views/columbusdw_views.xml',
        # 'views/columbusdw_templates.xml',
    ],
    'description': """
        This connector allows to connect Columbus DW from Macro4 with Odoo
    """,
    "images": [
        'static/description/banner.png'
    ],
    'demo': [
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}

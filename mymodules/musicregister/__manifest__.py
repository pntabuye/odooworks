# -*- coding: utf-8 -*-
{
    'name': 'Music Label',
    'summary': 'Manage a record company music portfolio',
    'description': """
        Manage record company:
        - released albums,
        - released singles
        - signed artists
    """,
    'author': 'Paul Ntabuye Butera',
    'website': "http://www.planbweb.com",
    'category': 'Project',
    'version': '0.1',
    'depends': ['base'],
    'installable': True,
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}

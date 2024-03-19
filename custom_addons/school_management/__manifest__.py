{
    'name': "School Management",
    'summary': "Manage school information",
    'description': "This module helps in managing school details like students, classes, and divisions.",
    'author': "Jinay Shah",
    'website': "https://www.yourwebsite.com",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/school.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

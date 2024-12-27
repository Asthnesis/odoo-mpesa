{
    'name':'Mpesa Transactions',
    'description': '',
    'licence': '',
    'author': 'Edward R',
    'website': 'https://softiqtechnologies.co.ke',
    'license': 'AGPL-3',
    'depends': ['analytic','sale'],  
    'data': [
        'views/pos_config.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
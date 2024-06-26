{
    'name': 'Payment Manager',
    'version': '1.0',
    'description': 'Módulo de registro de proyectos',
    'summary': 'Módulo de registro de proyectos',
    'author': 'Digilab Soluciones S.A.C',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'menus/menu.xml',
        'views/dl_project_view.xml', 
        'views/dl_payment_view.xml',
        'views/dl_company_view.xml',
        # 'views/dl_employee_view.xml',
        'views/dl_deliverable_view.xml',
        'security/ir_model_access.xml',
    ],
    'demo': [
        
    ],
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'dl_payment_manager/static/src/js/gridstack-all.js',
            'dl_payment_manager/static/src/xml/dl-dashboard.xml',
            'dl_payment_manager/static/src/js/dl-dashboard.js',
            'dl_payment_manager/static/src/css/gridstack.css',
            'dl_payment_manager/static/src/css/gridstack-extra.css',            
        ]
    }
}
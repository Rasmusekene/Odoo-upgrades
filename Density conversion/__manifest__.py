{
    'name': 'Purchase UoM Conversion through density',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Converts product quantity from L to g based on product density',
    'depends': ['purchase', 'stock'],
    'data': [
        'views/product_template_views.xml'
        'views/purchase_order_line.xml'
             ],
    'installable': True,
    'auto_install': False,
}

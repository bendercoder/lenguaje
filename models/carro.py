# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class carro(osv.osv):
    _name='lenguaje.carro'
    _rec_name='carro'
    
    _columns={
        'color':fields.char('Color',size=80,required=True,help='Aquí va el color del carro'),
        'active':fields.boolean('Active',help='Si esta activo el motor lo incluira en la vista')
    }

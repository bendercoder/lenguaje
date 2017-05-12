# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class marca(osv.osv):
    _name='lenguaje.marca'
    _rec_name='marca'
    
    _columns={
        'marca':fields.char('Marca',size=80,required=True,help='Aquí va la marca del carro'),
        'active':fields.boolean('Active',help='Si esta activo el motor lo incluira en la vista')
    }

class modelo(osv.osv):
    _name='lenguaje.modelo'
    _rec_name='modelo'
    
    _columns={
        'modelo':fields.char('Modelo',size=80,required=True,help='Aquí va el modelo del carro'),
        'active':fields.boolean('Active',help='Si esta activo el motor lo incluira en la vista')
    }

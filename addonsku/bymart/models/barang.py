from odoo import api, fields, models


class barang(models.Model):
    _name = 'bymart.barang'
    _description = 'New Description'

    name = fields.Char(string='Product')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    kelompok_id = fields.Many2one(comodel_name='bymart.kelompok', string='Kategori', ondelete='cascade')

    supplier_id = fields.Many2many(comodel_name='bymart.supplier', string='Supplier')
    
    
    
    
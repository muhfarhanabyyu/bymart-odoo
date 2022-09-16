from odoo import api, fields, models


class supplier(models.Model):
    _name = 'bymart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telpon = fields.Char(string='No. Telpon')
    barang_id = fields.Many2many(comodel_name='bymart.barang', string='Product')
    
    

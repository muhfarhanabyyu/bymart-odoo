from odoo import api, fields, models


class person(models.Model):
    _name = 'bymart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date('Tanggal Lahir')
    

class kasir(models.Model):
    _name = 'bymart.kasir'
    _inherit = 'bymart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')


class cleaningservice(models.Model):
    _name = 'bymart.cleaningservice'
    _inherit = 'bymart.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')

    

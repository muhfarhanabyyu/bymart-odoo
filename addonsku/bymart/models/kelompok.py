from odoo import api, fields, models


class kelompok(models.Model):
    _name = 'bymart.kelompok'
    _description = 'New Description'

    name = fields.Selection([
        ('laptop', 'Laptop'),('laptop gaming', 'Laptop Gaming'),('smartphone', 'Smartphone'),
        ('printer', 'Printer')
    ], string='Kategori')
    kode_kategori = fields.Char(string='Kode Kategori')
    
    @api.onchange('name')
    def _kode_kategori(self):
        if (self.name == 'laptop'):
            self.kode_kategori = "lap01"
        elif (self.name == 'laptop gaming'):
            self.kode_kategori = 'lap02'
        elif (self.name == 'smartphone'):
            self.kode_kategori = 'hp01'
        elif (self.name == 'printer'):
            self.kode_kategori = 'pr01'

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='bymart.barang', inverse_name='kelompok_id', string='Product')
    
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['bymart.barang'].search([('kelompok_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
    
    
    

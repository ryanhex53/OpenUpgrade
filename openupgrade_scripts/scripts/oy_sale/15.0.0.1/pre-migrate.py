import logging
_logger = logging.getLogger(__name__)

from openupgradelib import openupgrade

@openupgrade.migrate()
def migrate(env, version):
  _logger.warning('Migrating version %s of oy_sale', version)
  openupgrade.rename_models(env.cr, [('qx.sale.code', 'oy.sale.sale.code')])
  openupgrade.rename_tables(env.cr, [('qx_sale_code', 'oy_sale_sale_code')])
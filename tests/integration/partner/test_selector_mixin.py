from django.test import TestCase

from izi.apps.partner import strategy
from izi.test import factories


class TestUseFirstStockRecordMixin(TestCase):

    def setUp(self):
        self.product = factories.create_product()
        self.mixin = strategy.UseFirstStockRecord()

    def test_selects_first_stockrecord_for_product(self):
        stockrecord = factories.create_stockrecord(self.product)
        selected = self.mixin.select_stockrecord(self.product)
        self.assertEqual(selected.id, stockrecord.id)

    def test_returns_none_when_no_stock_records(self):
        self.assertIsNone(self.mixin.select_stockrecord(self.product))

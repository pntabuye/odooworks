class TestMRArtiste(common.TransactionCase):
    def test_some_action(self):
        record = self.env['model.a'].create({'field': 'value'})
        record.some_action()
        self.assertEqual(
            record.field,
            expected_field_value)
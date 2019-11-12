import unittest
import pandas as pd
import kuma


class TestSeriesAccessor(unittest.TestCase):
    def test_apply_with(self):
        df = pd.DataFrame(dict(input=[0, 1]))
        df['result'] = df['input'].kuma.apply(lambda x: x + 1)
        self.assertListEqual(df['result'].tolist(), [1, 2])

    def test_apply_with_empty_df(self):
        df = pd.DataFrame(columns=['input'])
        df['result'] = df['input'].kuma.apply(lambda x: x + 1)
        self.assertEqual(len(df['result']), 0)

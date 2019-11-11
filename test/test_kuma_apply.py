import unittest

import pandas as pd

import kuma

kuma.pandas()


class TestKumaApply(unittest.TestCase):
    def test_with_empty(self):
        df = pd.DataFrame(columns=['input'])
        df['result'] = df['input'].kuma_apply(lambda x: x + 1)
        self.assertEqual(len(df['result']), 0)

    def test_with_not_empty(self):
        df = pd.DataFrame(dict(input=[0, 1]))
        df['result'] = df['input'].kuma_apply(lambda x: x + 1)
        self.assertEqual(len(df['result']), 2)


import pandas as pd


class KumaSeries(object):
    """To make IDE intellisense work well, functions are defined as staticmethod and named with `kuma_` prefix.
    """
    @staticmethod
    def kuma_apply(data: pd.Series, func, **kwargs):
        return data.apply(func=func, **kwargs) if not data.empty else []


def kuma_pandas():
    pd.Series.kuma_apply = KumaSeries.kuma_apply

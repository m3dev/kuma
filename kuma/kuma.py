import pandas as pd


@pd.api.extensions.register_series_accessor('kuma')
class SeriesAccessor(object):
    def __init__(self, pandas_obj: pd.Series) -> None:
        self._obj = pandas_obj

    def apply(self, func, **kwargs):
        return self._obj.apply(func=func, **kwargs) if not self._obj.empty else []

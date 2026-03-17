import contextlib

with contextlib.suppress(ImportError):
    import pandas as pd

    pd.set_option("display.max_rows", 999999)
    pd.set_option("display.max_columns", 999999)
    pd.set_option("display.max_colwidth", 999999)

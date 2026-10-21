import pandas as pd

def reduce_memory(df):
    """
    returns DataFrame with smaller memory size by downcasting integers and floats and converting certain objects to category type.
    input is edited inplace
    """
    int_cols = df.select_dtypes(include="int64").columns
    for col in int_cols:
        df[col] = pd.to_numeric(df[col], downcast="integer")

    float_cols = df.select_dtypes(include="float64").columns
    for col in float_cols:
        df[col] = pd.to_numeric(df[col], downcast="float")

    object_cols = df.select_dtypes(include=["object", "string"]).columns
    obj_cols = []
    for col in object_cols:
        if df[col].memory_usage(deep=True) > df[col].astype("category").memory_usage(deep=True):
            obj_cols.append(col)
    for col in obj_cols:
        df[col] = df[col].astype("category")
    return df
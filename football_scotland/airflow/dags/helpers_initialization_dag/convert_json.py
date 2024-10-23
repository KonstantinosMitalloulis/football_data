import json
import pandas as pd
def safe_json_dumps(x):
    if pd.isna(x):  # Check if the value is NaN
        return None  # or return a default JSON value like '{}'
    try:
        return json.dumps(x)
    except:
        return None  # Handle other potential serialization errors
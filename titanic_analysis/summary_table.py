import pandas as pd

def create_summary_table(df):

    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
     # Implement the logic here
    
    summary = {
        "Feature Name": df.columns.tolist(),
        "Data Type":[df[col].dtype for col in df.columns.tolist()],
        "Unique Values": [df[col].nunique() for col in df.columns.tolist()],
        "Missing Values": [df[col].isnull().any() for col in df.columns.tolist()]
    }

    return pd.DataFrame(summary, columns=["Feature Name", "Data Type", "unique Values", "Missing Values"])
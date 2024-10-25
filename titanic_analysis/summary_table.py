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
        "Feature Name": [],
        "Data Type": [],
        "Unique Values": [],
        "Missing Values": []

    }
    for column in df.columns:
        summary["Feature Name"].append(column)
        summary["Data Type"].append(df[column].dtype)
        summary["Unique Values"].append(df[column].nunique())
        summary["Missing Values"].append(df[column].isnull().any())
    
    
    return pd.DataFrame(summary)

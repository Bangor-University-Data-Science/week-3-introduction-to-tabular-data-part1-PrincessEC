def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
     # Implement the logic here
    
    summary = pd.DataFrame({
        "Feature Name": df.colunms,
        "Data Type": df.dtypes.values,
        "Unique Values": df.unique().values,
        "Has Missing Values": df.isnull().any().values

    })  
    
    
    return pd.DataFrame(summary)

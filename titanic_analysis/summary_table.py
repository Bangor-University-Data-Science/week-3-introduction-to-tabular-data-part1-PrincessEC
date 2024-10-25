def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
     # Implement the logic here
    
    summary ={}

    for column in df.columns:
        summary[column] = {
            "Data Type": df[column].dtype,
            "Unique Values": df[column].nunique(),
            "Missing Values": df[column].isnull().any()
        }
    return summary
       

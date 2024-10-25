def create_summary_table(df):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values, and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
     # Implement the logic here
    
    summary_dict = {"Feature Name": df.column.to-list(),
                 "Data Type": df.dtypes.values,
                 "Has missing Values": df.isna().summary().values,
                "Number of Unique Values": df.nunique().values
                 }
    summary_df = pd.DataFrame(summary_dict)
    return summary_df

       

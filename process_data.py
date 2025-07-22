def clean_data(df):
         # Remove rows with any missing values
            df = df.drop('timestamp', axis=1)
            return df


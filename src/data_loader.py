import pandas as pd

def get_nav_data(nav_csv_path: str) -> pd.DataFrame:
    """
    Load NAV data from the specified CSV path and return a cleaned DataFrame.
    Assumes:
    - Index is date
    - '$-Adjusted' column needs to be dropped
    """
    NAV_df = pd.read_csv(nav_csv_path, index_col=0, parse_dates=True)

    if '$-Adjusted' in NAV_df.columns:
        NAV_df.drop('$-Adjusted', axis=1, inplace=True)

    NAV_df['scheme_code'] = '122639'
    NAV_df.columns = NAV_df.columns.str.strip()
    columns = NAV_df.columns.tolist()
    if len(columns) >= 2:
        NAV_df.rename(columns={columns[0]: 'NAV', columns[1]: 'Nifty500_TRI'}, inplace=True)
    else:
        raise ValueError("Expected at least two columns to rename, found: " + str(columns))
    return NAV_df
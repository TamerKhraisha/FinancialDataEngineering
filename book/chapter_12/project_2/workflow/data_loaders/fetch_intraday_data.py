import io
import pandas as pd
import io
import os
import pandas as pd
import requests
from datetime import datetime
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loads Intraday Time Series data
    """
    api_key = os.environ['ALPHAVINTAGE_API_KEY']

    output_df = pd.DataFrame()

    for symbol in ['IBM', 'MSFT', 'GOOG']:

        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&outputsize=full&datatype=csv&adjusted=true&apikey={api_key}'
        request_result = requests.get(url)
        df = pd.read_csv(io.StringIO(request_result.text), sep=',')
        df['symbol'] = symbol
        output_df = pd.concat([output_df, df], axis=0)

    output_df['ingestion_timestamp']= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output_df = output_df.rename(columns={'timestamp': 'price_timestamp', 'open': 'open_price', 'close': 'close_price'})
    return output_df


@test
def test_output(df) -> None:
    """
    Test the API output.
    """
    assert df is not None, 'The output is undefined'

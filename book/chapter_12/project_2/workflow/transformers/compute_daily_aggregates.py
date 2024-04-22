from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.AVERAGE

    Docs: https://docs.mage.ai/guides/transformer-blocks#aggregation-actions
    """

    df['price_date'] = df['price_timestamp'].astype('datetime64[ns]').dt.strftime('%Y-%m-%d')

    action = build_transformer_action(
        df,
        action_type=ActionType.AVERAGE,
        action_code='',  # Enter filtering condition on rows before aggregation
        arguments=['open_price', 'close_price', 'high', 'low', 'volume'],  # Enter the columns to compute aggregate over
        axis=Axis.COLUMN,
        options={'groupby_columns': ['price_date', 'symbol']},  # Enter columns to group by
        outputs=[
            # The number of outputs below must match the number of arguments
            {'uuid': 'daily_open', 'column_type': 'number_with_decimals'},
            {'uuid': 'daily_close', 'column_type': 'number_with_decimals'},
            {'uuid': 'daily_high', 'column_type': 'number_with_decimals'},
            {'uuid': 'daily_low', 'column_type': 'number_with_decimals'},
            {'uuid': 'daily_volume', 'column_type': 'number_with_decimals'},
        ],
    )

    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

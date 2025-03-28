import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)


def is_dataframe(dataframe: pd.DataFrame) -> bool:
    return isinstance(dataframe, pd.DataFrame)

def exist_column_in_dataframe(dataframe: pd.DataFrame, column: str) -> bool:
    if column in dataframe.columns:
        return True
    return False

def column_type_is_float(dataframe: pd.DataFrame, column: str) -> bool:
    if dataframe[column].dtype == 'float64':
        return True
    return False

def estatistical_describe_dataframe(
        df: pd.DataFrame, numeric_column: str, string_column: str) -> None:
    if not is_dataframe(df):
        print('Data is not a dataframe.')
        return None
    
    if not exist_column_in_dataframe(df, numeric_column):
        print('Column does not exist in dataframe.')
        return None
    
    if not column_type_is_float(df, numeric_column):
        print('Column type is not float.')
        return None

    if not exist_column_in_dataframe(df, string_column):
        print('Column does not exist in dataframe.')
        return None
    
    print(df.describe())
    print()

    print(df[numeric_column].sum())
    print()

    print(df[df[numeric_column] == df[numeric_column].max()])
    print()

    print(df[df[numeric_column] == df[numeric_column].min()])
    print()

    print(df.value_counts(string_column))
    print()

    return None


if __name__ == '__main__':
    dataframe_uc_br: pd.DataFrame = pd.read_excel(
        'dadosgeoestatisticos_ucs_27fev2025.xlsx', engine='openpyxl',
        skiprows=2, nrows=341)

    # print(dataframe.tail())

    # remove unuseful columns
    print(dataframe_uc_br.columns)
    dataframe_uc_br.drop(columns=['Unnamed: 0', 'Código CNUC (MMA)'], inplace=True)

    # Statistical area analysis uc in Brazil
    estatistical_describe_dataframe(
        dataframe_uc_br,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    print(dataframe_uc_br.value_counts('Gerência Regional'))
    print()

    # Separate data by brazilian region instead of 'Gerência Regional' column
    northern_regional_management: pd.DataFrame = dataframe_uc_br[
        dataframe_uc_br['Gerência Regional'] == 'GR1']
    northeast_regional_management: pd.DataFrame = dataframe_uc_br[
        dataframe_uc_br['Gerência Regional'] == 'GR2']
    midwest_regional_management: pd.DataFrame = dataframe_uc_br[
        dataframe_uc_br['Gerência Regional'] == 'GR3']
    southeast_regional_management: pd.DataFrame = dataframe_uc_br[
        dataframe_uc_br['Gerência Regional'] == 'GR4']
    southern_regional_management: pd.DataFrame = dataframe_uc_br[
        dataframe_uc_br['Gerência Regional'] == 'GR5']

    # Data analysis for northern region
    estatistical_describe_dataframe(
        northern_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    # Data analysis for northeast region
    estatistical_describe_dataframe(
        northeast_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    # Data analysis for midwest region
    estatistical_describe_dataframe(
        midwest_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    # Data analysis for southeast region
    estatistical_describe_dataframe(
        southeast_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    # Data analysis for southeast region
    estatistical_describe_dataframe(
        southern_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

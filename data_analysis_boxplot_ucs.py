import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

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

def ensure_directory_exists(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        return None
    return None

def dataframe_boxplot_graphic(
        df: pd.DataFrame, numeric_column: str,
        boxplot_title: str, boxplot_file_name: str) -> None:
    if not is_dataframe(df):
        print('Data is not a dataframe.')
        return None
    
    if not exist_column_in_dataframe(df, numeric_column):
        print(f'Column does not exist in dataframe.')
        return None
    
    if not column_type_is_float(df, numeric_column):
        print('Column type is not float.')
        return None
    
    ensure_directory_exists('boxplot_images')
    
    regional_names_br: dict[str, str] = {
        'northern_regional_management': 'região_norte',
        'northeast_regional_management': 'região_nordeste',
        'midwest_regional_management': 'região_centro_oeste',
        'southeast_regional_management': 'região_sudeste',
        'southern_regional_management': 'região_sul',
        'outliers_northern_regional_management': 'outliers_região_norte',
        'outliers_northeast_regional_management': 'outliers_região_nordeste',
        'outliers_midwest_regional_management': 'outliers_região_centro_oeste',
        'outliers_southeast_regional_management': 'outliers_região_sudeste',
        'outliers_southern_regional_management': 'outliers_região_sul',
        'dataframe_uc_br': 'Brasil'}
    
    plt.figure(figsize=(10, 6))
    plt.title(boxplot_title, loc='center', fontsize=20, fontweight='bold')
    sns.boxplot(x=df[numeric_column], color='green')
    plt.ticklabel_format(style='plain', axis='x')
    name_boxplot_file: str = (
        f"boxplot_images/{numeric_column[:4].lower()}_"
        f"{regional_names_br.get(boxplot_file_name, 'Key not found.')}.jpg")
    plt.savefig(name_boxplot_file, dpi=300, bbox_inches="tight")
    return None

if __name__ == '__main__':
    dataframe_uc_br: pd.DataFrame = pd.read_excel(
            'dadosgeoestatisticos_ucs_27fev2025.xlsx', engine='openpyxl',
            skiprows=2, nrows=341)

    # print(dataframe.tail())

    # remove unuseful columns
    print(dataframe_uc_br.columns)
    dataframe_uc_br.drop(
        columns=['Unnamed: 0', 'Código CNUC (MMA)'], inplace=True)

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
    print()
    
    print(northern_regional_management['Área (em hectares)**'].describe())
    print()
    print(northeast_regional_management['Área (em hectares)**'].describe())
    print()
    print(midwest_regional_management['Área (em hectares)**'].describe())
    print()
    print(southeast_regional_management['Área (em hectares)**'].describe())
    print()
    print(southern_regional_management['Área (em hectares)**'].describe())
    print()
    
    dataframe_boxplot_graphic(
        northern_regional_management, 'Área (em hectares)**',
        'Área das UCs na região Norte', 'northern_regional_management')
    dataframe_boxplot_graphic(
        northeast_regional_management, 'Área (em hectares)**',
        'Área das UCs na região Nordeste', 'northeast_regional_management')
    dataframe_boxplot_graphic(
        midwest_regional_management, 'Área (em hectares)**',
        'Área das UCs na região Centro-Oeste', 'midwest_regional_management')
    dataframe_boxplot_graphic(
        southeast_regional_management, 'Área (em hectares)**',
        'Área das UCs na região Sudeste', 'southeast_regional_management')
    dataframe_boxplot_graphic(
        southern_regional_management, 'Área (em hectares)**',
        'Área das UCs na região Sul', 'southern_regional_management')
    dataframe_boxplot_graphic(
        dataframe_uc_br, 'Área (em hectares)**',
        'Área das UCs no Brasil', 'dataframe_uc_br')

    # Outliers UCs region by area
    SUPERIOR_LIMIT_BOXPLOT_NORTHERN: float = 1_502_697.93
    SUPERIOR_LIMIT_BOXPLOT_NORTHEAST: float = 240_061.07
    SUPERIOR_LIMIT_BOXPLOT_MIDWEST: float = 458_332.11
    SUPERIOR_LIMIT_BOXPLOT_SOUTHEAST: float = 136_529.85
    SUPERIOR_LIMIT_BOXPLOT_SOUTHERN: float = 89_398.28

    outliers_northern_regional_management: pd.DataFrame = \
        northern_regional_management.loc[northern_regional_management[
            'Área (em hectares)**'] >= SUPERIOR_LIMIT_BOXPLOT_NORTHERN]
    outliers_northeast_regional_management: pd.DataFrame = \
        northeast_regional_management.loc[northeast_regional_management[
            'Área (em hectares)**'] >= SUPERIOR_LIMIT_BOXPLOT_NORTHEAST]
    outliers_midwest_regional_management: pd.DataFrame = \
        midwest_regional_management.loc[midwest_regional_management[
            'Área (em hectares)**'] >= SUPERIOR_LIMIT_BOXPLOT_MIDWEST]
    outliers_southeast_regional_management: pd.DataFrame = \
        southeast_regional_management.loc[southeast_regional_management[
            'Área (em hectares)**'] >= SUPERIOR_LIMIT_BOXPLOT_SOUTHEAST]
    outliers_southern_regional_management: pd.DataFrame = \
        southern_regional_management.loc[southern_regional_management[
            'Área (em hectares)**'] >= SUPERIOR_LIMIT_BOXPLOT_SOUTHERN]
    
    print('Número de UCs outliers na região Norte: '
        f'{len(outliers_northern_regional_management)}')
    print('Número de UCs outliers na região Nordeste: '
        f'{len(outliers_northeast_regional_management)}')
    print('Número de UCs outliers na região Centro-Oeste: '
        f'{len(outliers_midwest_regional_management)}')
    print('Número de UCs outliers na região Sudeste: '
        f'{len(outliers_southeast_regional_management)}')
    print('Número de UCs outliers na região Sul: '
        f'{len(outliers_southern_regional_management)}')
    print()

    # UCs outliers region by area
    print(outliers_northern_regional_management[
        ['Nome da Unidade de Conservação',
         'Atos legais (Criação ou redefinição)',
         'Área (em hectares)**',
         'UF de Abrangência']])
    print()
    print(outliers_northeast_regional_management[
        ['Nome da Unidade de Conservação',
         'Atos legais (Criação ou redefinição)',
         'Área (em hectares)**',
         'UF de Abrangência']])
    print()
    print(outliers_midwest_regional_management[
        ['Nome da Unidade de Conservação',
         'Atos legais (Criação ou redefinição)',
         'Área (em hectares)**',
         'UF de Abrangência']])
    print()
    print(outliers_southeast_regional_management[
        ['Nome da Unidade de Conservação',
         'Atos legais (Criação ou redefinição)',
         'Área (em hectares)**',
         'UF de Abrangência']])
    print()
    print(outliers_southern_regional_management[
        ['Nome da Unidade de Conservação',
         'Atos legais (Criação ou redefinição)',
         'Área (em hectares)**',
         'UF de Abrangência']])
    print()

    # UCs outliers region by area boxplot
    dataframe_boxplot_graphic(outliers_northern_regional_management,
        'Área (em hectares)**',
        'Área das UCs outliers na região Norte',
        'outliers_northern_regional_management')
    dataframe_boxplot_graphic(outliers_northeast_regional_management,
        'Área (em hectares)**',
        'Área das UCs outliers na região Nordeste',
        'outliers_northeast_regional_management')
    dataframe_boxplot_graphic(outliers_midwest_regional_management,
        'Área (em hectares)**',
        'Área das UCs outliers na região Centro-Oeste',
        'outliers_midwest_regional_management')
    dataframe_boxplot_graphic(outliers_southeast_regional_management,
        'Área (em hectares)**',
        'Área das UCs outliers na região Sudeste',
        'outliers_southeast_regional_management')
    dataframe_boxplot_graphic(outliers_southern_regional_management,
        'Área (em hectares)**',
        'Área das UCs outliers na região Sul',
        'outliers_southern_regional_management')

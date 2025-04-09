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

def generate_bar_chart_plot_top5_max(
        df: pd.DataFrame, numeric_column: str, string_column: str,
        bar_chart_title: str, name_image: str) -> None:
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
    
    ensure_directory_exists('readme_images')

    regional_names_br: dict[str, str] = {
        'northern_regional_management': 'top5_ucs_região_norte',
        'northeast_regional_management': 'top5_ucs_região_nordeste',
        'midwest_regional_management': 'top5_ucs_região_centro_oeste',
        'southeast_regional_management': 'top5_ucs_região_sudeste',
        'southern_regional_management': 'top5_ucs_região_sul',
        'dataframe_uc_br': 'top5_ucs_Brasil'}

    df_top5 = df.sort_values(by=numeric_column, ascending=False).head(5)

    plt.figure(figsize=(15, 6))  
    sns.barplot(x=numeric_column, y=string_column, data=df_top5,
                palette='viridis', hue=string_column, legend=False)
    plt.title(bar_chart_title, loc='center', fontsize=20, fontweight='bold')
    plt.xlabel(numeric_column)
    plt.tight_layout() 
    name_image_file: str = (
        f"readme_images/{numeric_column[:4].lower()}_maior_"
        f"{regional_names_br.get(name_image, 'Key not found.')}.jpg")
    plt.savefig(name_image_file, dpi=300, bbox_inches="tight")
    
    return None

def generate_bar_chart_plot_top5_min(
        df: pd.DataFrame, numeric_column: str, string_column: str,
        bar_chart_title: str, name_image: str) -> None:
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
    
    ensure_directory_exists('readme_images')

    regional_names_br: dict[str, str] = {
        'northern_regional_management': 'top5_ucs_região_norte',
        'northeast_regional_management': 'top5_ucs_região_nordeste',
        'midwest_regional_management': 'top5_ucs_região_centro_oeste',
        'southeast_regional_management': 'top5_ucs_região_sudeste',
        'southern_regional_management': 'top5_ucs_região_sul',
        'dataframe_uc_br': 'top5_ucs_Brasil'}

    df_top5 = df.sort_values(by=numeric_column, ascending=True).head(5)

    plt.figure(figsize=(15, 6))  
    sns.barplot(x=numeric_column, y=string_column, data=df_top5,
                palette='Set2', hue=string_column, legend=False)
    plt.title(bar_chart_title, loc='center', fontsize=20, fontweight='bold')
    plt.xlabel(numeric_column)
    plt.tight_layout() 
    name_image_file: str = (
        f"readme_images/{numeric_column[:4].lower()}_menor_"
        f"{regional_names_br.get(name_image, 'Key not found.')}.jpg")
    plt.savefig(name_image_file, dpi=300, bbox_inches="tight")
    
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
    
    # statistical area analysis uc in Brazil by region
    estatistical_describe_dataframe(
        northern_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    estatistical_describe_dataframe(
        northeast_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    estatistical_describe_dataframe(
        midwest_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    estatistical_describe_dataframe(
        southeast_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')

    estatistical_describe_dataframe(
        southern_regional_management,
        'Área (em hectares)**',
        'Bioma* (IBGE 1:250mil). Para as UCs que ocorrem em mais de um bioma, é considerado apenas o bioma que abrange 50% ou mais de seu território')
    
    # Generate bar chart plot top 5 max area by region
    generate_bar_chart_plot_top5_max(
        northern_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs na região Norte',
        'northern_regional_management')
    
    generate_bar_chart_plot_top5_max(
        northeast_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs na região Nordeste',
        'northeast_regional_management')
    
    generate_bar_chart_plot_top5_max(
        midwest_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs na região Centro-Oeste',
        'midwest_regional_management')
    
    generate_bar_chart_plot_top5_max(
        southeast_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs na região Sudeste',
        'southeast_regional_management')
    
    generate_bar_chart_plot_top5_max(
        southern_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs na região Sul',
        'southern_regional_management')
    
    generate_bar_chart_plot_top5_max(
        dataframe_uc_br, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 maiores UCs no Brasil',
        'dataframe_uc_br')
    
    # Generate bar chart plot top 5 min area by region
    generate_bar_chart_plot_top5_min(
        northern_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs na região Norte',
        'northern_regional_management')
    
    generate_bar_chart_plot_top5_min(
        northeast_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs na região Nordeste',
        'northeast_regional_management')
    
    generate_bar_chart_plot_top5_min(
        midwest_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs na região Centro-Oeste',
        'midwest_regional_management')
    
    generate_bar_chart_plot_top5_min(
        southeast_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs na região Sudeste',
        'southeast_regional_management')
    
    generate_bar_chart_plot_top5_min(
        southern_regional_management, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs na região Sul',
        'southern_regional_management')
    
    generate_bar_chart_plot_top5_min(
        dataframe_uc_br, 'Área (em hectares)**',
        'Nome da Unidade de Conservação', '5 menores UCs no Brasil',
        'dataframe_uc_br')
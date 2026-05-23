#Importación de paquetes
#Importamos pandas
import pandas as pd 
#Importamos numpy
import numpy as np 
#Importamos datetime 
import datetime as dt 

#Importación de visualizaciones
import seaborn as sns
import matplotlib.pyplot as plt


def visualizacion_1 (df):
    """Función que permite realizar una visualización inicial del data frame con el que 
        vamos a trabajar.
    variables: 
    df (dataframe.pd): Dataframe de pandas a analizar
    """
    print ("DATOS GENERALES:")
    forma = df.shape
    print (f'El dataframe está compuesto por {forma[0]} filas y {forma[1]} columnas')
    print ("-----------------------")
    print ("Las columnas que conforman el dataframe son:")
    print (df.columns)
    print ("-----------------------")
    print ("Las columnas del df tienen la siguiente información")
    print("--")
    df.info()

def renombrar_columnas (df, old_name, new_name):
    """Función para renombrar columnas de un dataframe de pandas

    Args:
        df (pandas dataframe): Dataframe de pandas sobre el que realizaremos el cambio.
        old_name (str): Nombre de la columna que queremos cambiar.
        new_name (str): Nuevo nombre que tendrá la columna.
    """    
    df = df.rename(columns= {old_name : new_name})
    print (f"Nombre de la columna cambiado de {old_name} a {new_name}")
    return df

def nulos (columna):
    """Función para visualizar los nulos en una columna de un dataframe 

    Args:
        columna (columna de Df): Columna de un dataframe en pandas a analizar.
    """
    nulos = sum(pd.isna(columna))
    print(f"La columna tiene {nulos} valores nulos")

def convertir_numero_entero (columna):
    """Función para convertir columnas con números decimales innecesarios a numeros enteros

    Args:
        columna (columna de df pandas): Columna de un dataframe en formato pandas
    """    
    columna = columna.apply(lambda x: int(x) if pd.notnull(x) else np.nan)
    columna = columna.astype('Int64')
    return(columna)

def binario_to_bool (column):
    """Función que convierte valores binarios en float a valores booleanos respetando los nulos de una columna

    Args:
        column (pandas column): Columna de un df de pandas.

    Returns:
        pandas column: Columna modificada
    """    
    resultados = [] #Creamos una lista vacía sobre la que volcaremos resultados.
    for x in column: #Creamos un bucle que recorra la columna y aplique los cambios
        if pd.isna(x): 
            resultados.append(np.nan)
        elif x == 0.0:
            resultados.append('no')
        else: 
            resultados.append('yes')
    column = resultados #Copiamos los resultados en la columna original y los devolvemos
    return column

def segundos_a_minutos (column): 
    """Función que convierte segundos a minutos en una columna de un df de pandas

    Args:
        column (pandas column): Columna de un dataframe en pandas

    Returns:
        col.pd: Columna convertida a minutos
    """    
    minutos = [] #Creamos una lista vacía en la que volcaremos el resultado en minutos
    for x in column: 
        minutos.append(x/60)
    column = minutos
    return column

def comas_por_puntos (column):
    """Función para convertir las comas a puntos en una columna de tipo O de un df pandas. Además
    la convierte a columna de tipo float. 

    Args:
        column (pd.col): Columna que queremos cambiar

    Returns:
        pd.col: Columna modificada
    """    
    column = column.apply(lambda x: x.replace(',', '.'))
    return column

def eda_inicial (df):
    """Función para la creación de un análisis inicial durante un EDA que nos permita entender los datos

    Args:
        df (pandas dataframe): Dataframe de pandas sobre el que ejecutaremos el análisis.
    """       
    #Extraemos las columnas numéricas
    numerical_cols = df.select_dtypes(include = 'number').columns

    #Extraemos las columnas categóricas 
    category_cols = df.select_dtypes(include= ['object', 'category']).columns 
    #Describimos las variables numéricas para entender como funcionan:
    description_num = df.describe().T.round(4)

    #Describimos las variables categóricas para entender como funcionan:
    description_cat = df.describe(include= ['object', 'category']).T

    #Hacemos un print para comprender que columna es cada una 
    print("Variables numéricas: \n", numerical_cols)
    print(" ")
    print(description_num)
    print(" ")
    print("Variables categóricas: \n", category_cols)
    print(" ")
    print(description_cat)

def cat_analysis (variables):
    """Función para realizar un análisis inicial de variables categóricas contra una variable objetivo.

    Args:
        variables (pandas dataframe): Dataframe en el que incluimos solo las variables categóricas 
        variable_objetivo (pandas column): Variable contra la que realizaremos el análisis.
    """    
    for var in variables:
        #Introducimos el encabezado para ver que variable analizamos cada vez 
        print(f"VARIABLE: {var}")
        print(" ")
        #Vamos a ver el número de categorías que hay por cada variable 
        unicos = variables[var].nunique()
        print(f"Número de categorías: {unicos}")
        print(" ")

        #Observamos la distribución de frecuencias de las variables
        print("Distribución de frecuencias")
        distribution_freq = variables[var].value_counts()
        print (distribution_freq)
        print(" ")

        #Por último se analiza el porcentaje que ocupa cada una de las categorías dentro de la variable
        print("Porcentajes")
        porcentajes = variables[var].value_counts(normalize=True).round(4)*100
        print (porcentajes)

        #Incluimos también un gráfico que refleje este porcentaje 
        plt.figure(figsize= (12, 10))
        plt.pie(porcentajes, labels = porcentajes.index, autopct= '%1.1f%%', startangle= 90)
        plt.title (var)
        plt.axis('equal')
        plt.show()

        print("\n" * 3)

def num_analysis(df):
    """
    Realiza el análisis univariante de las variables numéricas de un DataFrame.
    Muestra las estadísticas descriptivas y un histograma y boxplot por cada variable.

    Args:
        df (pd.DataFrame): Dataframe de pandas que vamos a analizar.
    """
    # Seleccionamos las columnas numéricas
    columnas_numericas = df.select_dtypes(include=np.number).columns

    # Recorremos cada columna numérica
    for columna in columnas_numericas:

        print(f"VARIABLE: {columna}")
        print (" ")
        # Estadísticas descriptivas
        print ("ESTADÍSTICAS DESCRIPTIVAS")
        print (" ")
        print(df[columna].describe().round(2))

        # Creamos la figura con dos gráficos: histograma y boxplot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        # Histograma
        df[columna].hist(ax=ax1, bins=20, color='steelblue', edgecolor='white')
        ax1.set_title(f'Histograma - {columna}')
        ax1.set_xlabel(columna)
        ax1.set_ylabel('Frecuencia')

        # Boxplot
        df[columna].plot.box(ax=ax2, color='steelblue')
        ax2.set_title(f'Boxplot - {columna}')

        plt.suptitle(columna, fontsize=14, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
def corr_fig (df,columns):
    """Función para obtener una matriz de correlación entre variables y un posterior heat map.

        Args:
        df (pandas dataframe): Dataframe en el que se encuentran las columnas 
        columuns (list): lista que contine las variables de pandas.
    """
    #Obtenemos la matriz de correlación 
    corr_matrix = df[columns].corr()
    #Creamos el heatmap plasmando la matriz de correlación
    plt.figure(figsize = (10,8))
    #Aquí creamos el gráfico con su paleta de colores e incluyendo los valores en cada celda del mapa. 
    sns.heatmap(corr_matrix, annot= True, cmap= 'YlOrRd')
    plt.show()  

def initial_exploration (df):
    """ Función para realizar una exploración inicial de un set de datos que permita entender como está formado el mismo así como
    las columnas y tipos de datos que lo conforman.

    Args:
    df (pandas datafram): Dataframe de pandas sobre el cuál buscamos realizar la exploración inicial. 
    """  
    #En primer lugar, miramos el número de registros y de columnas que tiene el dataframe.
    shape = df.shape
    print (f'El dataframe tiene {shape[0]} registros y {shape[1]} columnas')
    print ("")

    #En segundo lugar, miramos las columnas que forman el dataframe y el tipo de datos de cada columna
    columns = df.columns
    print("El Df está formado por las siguientes columnas:")
    print(columns)
    print("")

    #En tercer lugar miramos el tipo de datos que conforma nuestro dataframe:
    datos = df.dtypes
    print ("Los tipos de datos que forman las columnas son los siguientes:")
    print (datos)
    print ("")

    #A continuación miramos los valores iniciales del dataframe
    header = df.head
    print("Los registros iniciales del dataframe son los siguientes:")
    print(header)
    print("")


def nulos_tabla(df):
    """Función para averiguar el porcentaje de nulos por columna del DF

    Args:
        df (pandas datafram): Dataframe de pandas sobre el que trabajaremos.

    Returns:
        _type_: _description_
    """    
    #Creamos una lista vacía en la que añadiremos los resultados.
    resultados = []

    #Creamos un bucle para que aplique a toda la función el siguiente cálculo
    for columna in df.columns:

        #Hacemos el cálculo del total de nulos en cada columna
        nulos = sum(pd.isna(df[columna]))   

        #Empezamos a añadir todos los resultados la lista vacía 
        resultados.append({

            #Añadimos el nombre de la columna 
            "columna":     columna,

            #Añadimos el total de nulos por columna
            "total_nulos": nulos,

            #Por último calculamos el porcentaje de nulos dividiendo el total de nulos entre el total de registros
            "porcentaje":  round((nulos / len(df)) * 100, 2)
        })

    #Creamos un nuevo dataframe con los resultados en formato tabla
    tabla = pd.DataFrame(resultados)

    #Ordenamos los valores de mayor a menor de acuerdo al porcentaje
    tabla = tabla.reset_index(drop=True)
    return tabla

def precombine_registers (df, col1, col2):
    """Función que devuelve la cantidad de filas con registros en dos columnas, en ambas y en ninguna columna.

    Args:
        df (pandas df): Dataframe de pandas
        col1 (str): Columna del dataframe
        col2 (str): Columna del dataframe
    """    
    #Registramos el número de nulos en cada columna
    registros_x = df[col1].notnull().sum()
    registros_y = df[col2].notnull().sum()
    #Registramos la cantidad de columnas que tienen información en ambas columnas
    ambas = len(df[df[col1].notnull() & df[col2].notnull()])
    #Registramos la cantidad de columnas sin registros en ninguna columna
    ninguna = len(df[df[col1].isnull() & df[col2].isnull()])
    #Volcamos todos los resultados
    print (f'{col1} tiene {registros_x} registros')
    print (f'{col2} tiene {registros_y} registros')
    print (f'Hay {ambas} columnas con registros en ambas columnas')
    return (f'{ninguna} carecen de registros')

def eliminar_nulos(df, columna):
    """
    Elimina las filas que contienen valores nulos en una columna específica de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame de pandas sobre el que se aplicará el filtrado.
        columna (str): Nombre de la columna en la que se detectarán y eliminarán los valores nulos.
    """    
    #Obtenemos la forma del dataframe antes del borrado
    forma_inicial = df.shape
    print (f'El dataframe tiene la siguiente forma {forma_inicial}')

    #Eliminamos los registros en los que hay nulos 
    df = df.dropna(subset = [columna])
    print ("Se han eliminado los registros")

    #Obtenemos la forma del dataframe de nuevo para ver que no haya errores.
    forma_despues = df.shape
    print(f'El dataframe tiene la siguiente forma tras el borrado {forma_despues}')
    return df

def convertir_altura (col):
    """Función que convierte pulgadas y pies a centimetros

    Args:
        col (columna dataframe pandas): Columna en la que vamos a realizar la conversión.
    """    
    #Gestionamos los nulos 
    if pd.isna(col):
        return np.nan
    #Tratamos el string para separar los valores en pies y pulgadas
    numeros = str(col).replace("'", " ").replace('"', " ").split()

    #Guardamos los valores en dos listas transitorias
    pies = int(numeros[0])
    pulgadas = int(numeros[1])

    #Convertimos los valores a centimetros 
    altura_cm = (pies*30.48) + (pulgadas*2.54)

    #Redondeamos el resultado a 2 decimales
    return round(altura_cm, 2)


def analisis_duplicados (df):
    """Devuelve dos tablas:
    - Tabla 1: duplicados por columna
    - Tabla 2: filas duplicadas y porcentaje

    Args:
        df (pd.DataFrame): Dataframe de pandas que vamos a analizar.
    """  

    #-----TABLA 1: DUPLICADOS POR COLUMNA-----  
    print ("-----DUPLICADOS POR COLUMNA-----")
    #Creamos una lista vacía en la que volcaremos los resultados
    resultados_columna = []

    #Creamos un bucle para que analice todas las columnas
    for columna in df.columns: 
        
        #Calculamos los duplicados por columna
        duplicados = df[columna].duplicated().sum()

        #Calculamos el porcentaje de duplicados por columna
        porcentaje = round((duplicados/len(df))*100, 2)

        #Añadimos los resultados a la lista
        resultados_columna.append({
            'columna' : columna, 
            'duplicados': duplicados,
            'porcentaje': porcentaje
        })
    #Devolvemos el resultado en formato dataframe 
    print (pd.DataFrame(resultados_columna))

    #-----TABLA 2: FILAS DUPLICADAS-----
    print("-----FILAS DUPLICADAS-----")
    #Creamos una lista vacía en la que volcaremos los resultados
    tablas_filas = []

    #Calculamos las filas duplicadas y el porcentaje 
    filas_duplicadas = df.duplicated().sum()
    porcentaje_filas = round((filas_duplicadas/len(df))*100, 2)

    #Añadimos los resultados a la lista
    tablas_filas.append({
        'total filas' : len(df),
        'filas_duplicadas': filas_duplicadas,
        'porcentaje': porcentaje_filas
    })
    print (pd.DataFrame(tablas_filas))

def duplicados_columna (df, col): 
    """Devuelve la cantidad de registros y el porcentaje individualmente
       por columna

    Args:
        df (pd.Dataframe): Dataframe de pandas del que obtenemos los duplicados
        col (pd.column): Columna que queremos analizar
    """    
    numero = df[col].duplicated().sum()
    porcentaje = (numero/len(df[col]))*100

    print (f'Duplicados: {numero} Porcentaje: {porcentaje}')
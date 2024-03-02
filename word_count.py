"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""

    filenames = glob.glob(f"{input_directory}/*.txt") ##extrae los nombres de los documentos
    dataframes = [
        pd.read_csv(filename,sep="\t",header=None,names=["text"])
        for filename in filenames
    ] ##comprenhension para listas, tuplas y diccionarios, no es necesario el : para el ciclo for
    concatenated_df = pd.concat(dataframes,ignore_index=True)
    return concatenated_df
    

 
def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe=dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()
    dataframe["text"] = dataframe["text"].str.replace(".","") #reemplaza por vacio
    dataframe["text"] = dataframe["text"].str.replace(",","")

    return dataframe


def count_words(dataframe):
    """Word count"""
    dataframe=dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split() 
    dataframe = dataframe.explode("text")
    dataframe["count"] = 1
    dataframe = dataframe.groupby("text").agg({"count":"sum"})

    return dataframe

def count_words_(dataframe):
    """Word count"""
    dataframe=dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split() 
    dataframe = dataframe.explode("text")
    dataframe = dataframe["text"].value_counts()
    return dataframe





def save_output(dataframe, output_filename):
    """Save output to a file."""
    dataframe.to_csv(output_filename,sep="\t",index=True,header=False)



#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""

    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words_(df)
    save_output(df,output_filename)
    print(df)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )

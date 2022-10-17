import pandas as pd
import lxml


def write_table(noten):
    # list to data frame
    df_list = pd.read_html(noten)
    df = df_list[-1]

    # save in csv data
    df.to_csv('transcript_of_records.csv')

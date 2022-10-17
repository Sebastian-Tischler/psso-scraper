import pandas as pd


def clear_table():
    # save csv data as data frame
    data = pd.read_csv("transcript_of_records.csv")

    # clear data
    for x in data["Note"]:
        data["note_adjusted"] = data["Note"].apply(lambda x: x/10)

    # save cleared data frame in csv data
    data.to_csv('transcript_of_records.csv')

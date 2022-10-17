import pandas as pd


def new_subjects():
    new = pd.read_csv("transcript_of_records.csv")
    old = pd.read_csv("transcript_of_records_old.csv")

    count_new = 0
    count_old = 0

    for _ in new.iterrows():
        count_new += 1


    for _ in old.iterrows():
        count_old += 1

    if count_new == count_old:
        return True
    else:
        return False

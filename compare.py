import pandas as pd
import math


def compare():
    new = pd.read_csv("transcript_of_records.csv")
    old = pd.read_csv("transcript_of_records_old.csv")

    list_new = []
    list_old = []

    for index, row in new.iterrows():
        if math.isnan(row["note_adjusted"]):
            list_new.append("-")
        else:
            list_new.append(row["note_adjusted"])

    for index, row in old.iterrows():
        if math.isnan(row["note_adjusted"]):
            list_old.append("-")
        else:
            list_old.append(row["note_adjusted"])

    changes_index = []
    index = 0
    for x in range(len(list_new)):
        if list_new[index] == list_old[index]:
            index += 1
        else:
            changes_index.append(index)
            index += 1

    changes = []
    for x in changes_index:
        idx = 0
        for index, row in new.iterrows():
            if idx == x:
                changes.append(f"You got a grade of {row['note_adjusted']} in {row['Prüfungstext']}.")
            idx += 1

    if len(changes) > 0:
        data = pd.read_csv("transcript_of_records.csv")
        data.to_csv('transcript_of_records_old.csv')

    return changes

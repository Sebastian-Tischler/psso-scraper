import open
import write_table
import clear_table
import compare
import telegram_bot
import new_subjects

noten = open.open_psso()
write_table.write_table(noten)
clear_table.clear_table()
subjects = new_subjects.new_subjects()
if not subjects:
    change = compare.compare()
    telegram_bot.send(change)

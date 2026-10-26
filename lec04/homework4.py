
def next_birthday(date, birthdays):
    birthday = (1,1)
    list_of_names = []
    upcoming_birthdays = [b_date for b_date in birthdays if b_date > date]
    if upcoming_birthdays:
        next_date = min(upcoming_birthdays)
    else:
        next_date = min(birthdays.keys())
    
    return next_date, birthdays[next_date]
    
birthday = {
    (1,10): ["Alice"],
	(5,15): ["Bob", "Charlie"],
	(10,20): ["David"],
	(12,25): ["Eve"]
}
current_date = (1,10)
next_date, names = next_birthday(current_date, birthday)
print("Next birthday after ", current_date, "is ", next_date, "\n")
print("People with this birth date are", names)
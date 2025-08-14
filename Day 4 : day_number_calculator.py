def main():SS
    try:
        day = int(input('Enter day: '))
        month = int(input('Enter month: '))
        year = int(input('Enter year: '))
    except ValueError:
        print('Invalid input. Please enter numbers only.')
        return
    if year <= 0:
        print('Invalid year.')
        return
    if not (1 <= month <= 12):SS
        print('Invalid month.')
        return
    is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    month_lengths = [0,
        31, 29 if is_leap else 28, 31, 30, 31, 30,
        31, 31, 30, 31, 30, 31
    ]
    if not (1 <= day <= month_lengths[month]):
        print('Invalid day.')
        return
    month_names = (
        '', 'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    )
    day_number = sum(month_lengths[:month]) + day
    total_days_in_year = 366 if is_leap else 365
    remaining_days = total_days_in_year - day_number
    print(f"{day} {month_names[month]} {year} is day number {day_number}.")
    print(f"There are {remaining_days} days remaining in this year.")
if __name__ == "__main__":
    main()

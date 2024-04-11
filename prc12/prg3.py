import calendar

def display_calendar(year, month):
    cal = calendar.month(year, month)
    print("Calendar:")
    print(cal)

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))
    display_calendar(year, month)

if __name__ == "__main__":
    main()

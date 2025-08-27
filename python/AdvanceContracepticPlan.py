def advance_contraceptic_plan():
    recap = 'yes'

    while recap.lower().trim() == 'yes':
        print("Enter your preferred Menstrual Cycle plan")

        day = int(input("Enter last period day (1-31): "))
        month = int(input("Enter last period month (1-12): "))
        year = int(input("Enter last period year: "))
        cycle_length = int(input("Enter cycle length in days: "))
        period_duration = int(input("Enter period duration in days: "))

       
        next_day = day + cycle_length
        next_month = month
        next_year = year

        while next_day > 30:
            next_day -= 30
            next_month += 1
            if next_month > 12:
                next_month = 1
                next_year += 1

        ovulation_day = day + (cycle_length / 2)
        ovulation_month = month
        ovulation_year = year

        while ovulation_day > 30:
            ovulation_day -= 30
            ovulation_month += 1
            if ovulation_month > 12:
                ovulation_month = 1
                ovulation_year += 1

        fertile_start = ovulation_day - 2
        fertile_end = ovulation_day + 2

    
        print(f"Next Period: {next_day}/{next_month}/{next_year}")
        print(f"Ovulation Date: {ovulation_day}/{ovulation_month}/{ovulation_year}")
        print(f"Fertile Window: {fertile_start} to {fertile_end}")
        print("Safe Periods:")
        print(f"  After Period: Day {day + period_duration} to {fertile_start - 1}")
        print(f"  Before Next Period: Day {fertile_end + 1} to {next_day - 1}")

        recap = input("\nDo you want to calculate again? (Y/N): ")

    print("\nYour consultation has ended. Stay sharp,")
    print("May we not be victims of unwanted pregnancy.")
    print("Dr. Adedeji Fareed Cares!")
advance_contraceptic_plan()
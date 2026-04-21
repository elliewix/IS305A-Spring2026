import datetime as dt

start_date = dt.date(2015, 1, 1).isoformat()
end_date = dt.date(2015, 3, 31).isoformat()


years = [year for year in range(2015, 2026)]
start_month = 1
end_month = 3
start_day = 1 # always constant
end_day = 31 # varies by month

dates = []
for year in years:
    if end_month < 13: # ensure that we don't go out of bounds for months. At the end, the end month should move from 12 to 15 and this will no longe run
        if end_month == 6 or end_month == end_month == 9: # accounts for the month of June and September where the last day is on the 30th and not 31st
            end_day = 30
            start_date = dt.date(year, start_month, start_day)
            end_date = dt.date(year, end_month, end_day)

            date = (start_date.isoformat(), end_date.isoformat()) # converts it to the format used by the api which is YYYY-MM-DD
            dates.append(date)

        else:
            end_day = 31 # every other end month I can have the end day as 31st
            start_date = dt.date(year, start_month, start_day)
            end_date = dt.date(year, end_month, end_day)
            

            date = (start_date.isoformat(), end_date.isoformat())
            dates.append(date)

    # increment to the next chunk of 3 months
    start_month += 3 
    end_month += 3
    

print(dates) # dates look good
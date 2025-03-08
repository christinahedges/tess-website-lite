def main(today_date_decimal):
    from datetime import datetime
    import pandas as pd

    fn_ = 'https://tess.mit.edu/public/files/TESS_orbit_times.csv'
    df = pd.read_csv(fn_, header = 0, delimiter=",", engine='python', na_filter=True).values
    sector = df[0:-1,0]
    orbit = df[0:-1,1]
    start_sector = df[0:-1,2]
    end_sector = df[0:-1,3]
    
    for ii in zip(start_sector, end_sector, sector, orbit):     
        start_date = datetime.strptime(str(ii[0][0:10]), "%Y-%m-%d")
        end_date = datetime.strptime(str(ii[1][0:10]), "%Y-%m-%d")
        
        start_date_decimal = start_date.year + (start_date.timetuple().tm_yday - 1) / 365.2425
        end_date_decimal = end_date.year + (end_date.timetuple().tm_yday - 1) / 365.2425

        if (today_date_decimal >= start_date_decimal) and (today_date_decimal <= end_date_decimal):
            return ii[2], ii[3]

if __name__ == "__main__":
    main()
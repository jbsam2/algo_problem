T = int(input())
  
for test_case in range(1, T + 1):
    days_31 = ['01', '03', '05', '07', '08', '10', '12']
    days_30 = ['04', '06', '09', '11']
    date_input = input()
    year = date_input[0:4]
    month = date_input[4:6]
    day = int(date_input[6:])
    if month == '02':
        if day > 28:
            print(f'#{test_case} -1')
        else:
            if day > 10:
                print(f'#{test_case} {year}/{month}/{day}')
            else:
                print(f'#{test_case} {year}/{month}/0{day}')
    elif month in days_31:
        if day > 31:
            print(f'#{test_case} -1')
        else:
            if day > 10:
                print(f'#{test_case} {year}/{month}/{day}')
            else:
                print(f'#{test_case} {year}/{month}/0{day}')
    elif month in days_30:
        if day > 30:
            print(f'#{test_case} -1')
        else:
            if day > 10:
                print(f'#{test_case} {year}/{month}/{day}')
            else:
                print(f'#{test_case} {year}/{month}/0{day}')
    else:
        print(f'#{test_case} -1')
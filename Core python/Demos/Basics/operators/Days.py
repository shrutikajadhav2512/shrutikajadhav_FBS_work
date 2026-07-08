#take days
days=int(input('enter days:'))
# calculations
years=days//365
remaining_days=days%365
weeks=remaining_days//7
day=remaining_days%7
# Display result
print(f'days is:{days}')
print(f'years is:{years}')
print(f'remaining days is:{remaining_days}')
print(f'weeks is:{weeks}')
print(f'day is:{day}')
print(f'days is:{days},years:{years},ramaining days:{remaining_days},weeks:{weeks},days is:{day}')
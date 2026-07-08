# WAP to conver days into years,week,days.
days=int(input('Enter days:'))
# calculations
years=days//365
remaining_days=days%365
week=remaining_days//7
remain_days=remaining_days%7
# display
print(f'years:{years},remaining_days:{remaining_days},weeks:{week},remaining_days:{remain_days}')

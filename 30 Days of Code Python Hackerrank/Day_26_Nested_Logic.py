# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date
return_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))

return_date = date(day=return_date[0], month=return_date[1], year=return_date[2])
due_date = date(day=due_date[0], month=due_date[1], year=due_date[2])

fine = 0

if return_date > due_date:
    if return_date.year == due_date.year:
        if return_date.month == due_date.month:
            fine = 15 * (return_date.day - due_date.day)
        else:
            fine = 500 * (return_date.month - due_date.month)
    else:
        fine = 10000

print(fine)

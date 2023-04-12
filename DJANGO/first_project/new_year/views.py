from django.shortcuts import render

from datetime import datetime

# Create your views here.

def index(request):
    if is_new_year_today(): check = 'YES'
    else: check = 'NO'
    return render(request, 'is_new_year/index.html', {
        'check': check,  
    })

def is_new_year_today() -> bool:
    now = datetime.now()
    data = (now.day, now.month)
    if data == (1, 1): return True
    else: return False



def test():
    if is_new_year_today(): check = 'YES'
    else: check = 'NO'
    print(check)


if __name__ == '__main__':
    test()

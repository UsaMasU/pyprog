from django.shortcuts import render
import pyodbc


def index(request):
    template = 'mssql/index.html'

    if request.method == 'POST':
        print('post')
    else:  # request.method == 'GET'
        area = request.GET.get('area')
        get_area = lambda: f'WHERE [DeviceArea] = {area}' if area is not None else ""

        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=ES01\WINCC;DATABASE=STATISTIC;UID=vertek;PWD=dbtest')
        cursor = cnxn.cursor()

        cursor.execute("\
                SELECT TOP 1000 \
                [DeviceID], [DeviceName], [DeviceCode], [DeviceArea] \
                FROM [STATISTIC].[dbo].[Device] \
                " + get_area() + " \
                ORDER BY DeviceArea")

        rows = cursor.fetchall()

        context = {
            'rows': rows,
            'text': 'MS SQL',
        }
    return render(request, template, context)


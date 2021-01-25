from django.shortcuts import render
from geopy.geocoders import Nominatim
from tkinter import *
import pyodbc
import pgeocode
import itertools
import ctypes 

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



def updateAgentsDistance(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select * from Agents')
    result=cursor.fetchall()

    cursor.execute('select * from Agents_Distance')
    result1=cursor.fetchall()

    if not result1:
        for r in result:
            loc=pgeocode.GeoDistance('us')
            NYdist=loc.query_postal_code('10007',str(r.Zipcode))
            Bostondist=loc.query_postal_code('02111',str(r.Zipcode))
            LAdist=loc.query_postal_code('90001',str(r.Zipcode))
            Chicagodist=loc.query_postal_code('60007',str(r.Zipcode))
            Austindist=loc.query_postal_code('73301',str(r.Zipcode))
            Columbusdist=loc.query_postal_code('43004',str(r.Zipcode))
            Hustondist=loc.query_postal_code('77001',str(r.Zipcode))
            Pheonixdist=loc.query_postal_code('85035',str(r.Zipcode))
            SanDiegodist=loc.query_postal_code('78384',str(r.Zipcode))
            SanJosedist=loc.query_postal_code('95130',str(r.Zipcode))
            Dallasdist=loc.query_postal_code('77001',str(r.Zipcode))

           
            sqeury="INSERT INTO [Agents_Distance]([Id],[NewYork],[Boston],[LA],[Chicago],[Austin],[Columbus],[Huston],[Phonix],[SanDiego],[SanJose],[Dallas]) VALUES("+str(r.Id)+","+str(NYdist)+","+str(Bostondist)+","+str(LAdist)+","+str(Chicagodist)+","+str(Austindist)+","+str(Columbusdist)+","+str(Hustondist)+","+str(Pheonixdist)+","+str(SanDiegodist)+","+str(SanJosedist)+","+str(Dallasdist)+")"
            cursor.execute(sqeury)
            conn.commit()
            Mbox('Message', 'Agents distance is now upto-date...!!!', 1)
             
    elif len(result) != len(result1):
        cursor.execute('select * from Agents where Id not in (select Id from Agents_Distance)')
        result=cursor.fetchall()

        for r in result:
            loc=pgeocode.GeoDistance('us')
            NYdist=loc.query_postal_code('10007',str(r.Zipcode))
            Bostondist=loc.query_postal_code('02111',str(r.Zipcode))
            LAdist=loc.query_postal_code('90001',str(r.Zipcode))
            Chicagodist=loc.query_postal_code('60007',str(r.Zipcode))
            Austindist=loc.query_postal_code('73301',str(r.Zipcode))
            Columbusdist=loc.query_postal_code('43004',str(r.Zipcode))
            Hustondist=loc.query_postal_code('77001',str(r.Zipcode))
            Pheonixdist=loc.query_postal_code('85035',str(r.Zipcode))
            SanDiegodist=loc.query_postal_code('78384',str(r.Zipcode))
            SanJosedist=loc.query_postal_code('95130',str(r.Zipcode))
            Dallasdist=loc.query_postal_code('77001',str(r.Zipcode))

           
            sqeury="INSERT INTO [Agents_Distance]([Id],[NewYork],[Boston],[LA],[Chicago],[Austin],[Columbus],[Huston],[Phonix],[SanDiego],[SanJose],[Dallas]) VALUES("+str(r.Id)+","+str(NYdist)+","+str(Bostondist)+","+str(LAdist)+","+str(Chicagodist)+","+str(Austindist)+","+str(Columbusdist)+","+str(Hustondist)+","+str(Pheonixdist)+","+str(SanDiegodist)+","+str(SanJosedist)+","+str(Dallasdist)+")"
            cursor.execute(sqeury)
            conn.commit()
            Mbox('Message', 'Agents distance is now upto-date...!!!', 1)
    else:
        #alert_popup("Message", "Updated...!!!", "agents disatnce is updated...")
        Mbox('Message', 'Agents distance is already upto-date...!!!', 1)  

    cursor.close()
    
    conn.close()

    return render(request,'Main.html')
        



def getAgents(request):
    
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, NewYork from Agents_Distance order by NewYork) b on a.Id =b.id order by b.NewYork')
    result=cursor.fetchall()
    

    cursor.close()
    conn.close()
    return render(request,'Index.html',{'res':result})
  
   


def mainpage(request):
    return render(request,'Main.html')

def getAgentsofBoston(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Boston from Agents_Distance order by Boston) b on a.Id =b.id order by b.Boston')
    result=cursor.fetchall()
    

    cursor.close()
    conn.close()
    return render(request,'boston.html',{'res':result})

def getAgentsofLA(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, LA from Agents_Distance order by LA) b on a.Id =b.id order by b.LA')
    result=cursor.fetchall()
    

    cursor.close()
    conn.close()
    return render(request,'la.html',{'res':result})

def getAgentsofChicago(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Chicago from Agents_Distance order by Chicago) b on a.Id =b.id order by b.Chicago')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'Chicago.html',{'res':result})


def getAgentsofColumbus(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Columbus from Agents_Distance order by Columbus) b on a.Id =b.id order by b.Columbus')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'Columbus.html',{'res':result})


def getAgentsofAustin(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Austin from Agents_Distance order by Austin) b on a.Id =b.id order by b.Austin')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'Austin.html',{'res':result})


def getAgentsofHuston(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Huston from Agents_Distance order by Huston) b on a.Id =b.id order by b.Huston')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'Huston.html',{'res':result})


def getAgentsofPheonix(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Phonix from Agents_Distance order by Phonix) b on a.Id =b.id order by b.Phonix')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'pheonix.html',{'res':result})


def getAgentsofSanDiego(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, SanDiego from Agents_Distance order by SanDiego) b on a.Id =b.id order by b.SanDiego')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'SanD.html',{'res':result})


def getAgentsofSanJose(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, SanJose from Agents_Distance order by SanJose) b on a.Id =b.id order by b.SanJose')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'SanJ.html',{'res':result})


def getAgentsofDallas(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=shubham;'
                        'Trusted_Connection=yes;')

    cursor=conn.cursor()
    
    cursor.execute('select a.Id,a.Name,a.Address,a.City,a.Zipcode,a.State from Agents a inner join (select top 100 Id, Dallas from Agents_Distance order by Dallas) b on a.Id =b.id order by b.Dallas')
    result=cursor.fetchall()

    cursor.close()
    conn.close()
    return render(request,'Dallas.html',{'res':result})


def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()
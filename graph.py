import csv
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import datetime

#csv in format of date,distance,steps and must be in the same directory as this file

file = 'stats.csv'
data = []
current_month = str(datetime.datetime.now().month)
current_year = str(datetime.datetime.now().year)
convert_month = {'01':'Jan','02':'Feb','03':'Mar','04':'Apr','05':'May','06':'Jun','07':'Jul','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}

with open(file) as f:
    for line in f:
        line = line.strip()
        if line.split(',')[0] != 'date':
            data.append([line.split(',')[0],line.split(',')[1],line.split(',')[2]])




############



def stats(data):
    total_steps = 0
    total_distance = 0
    total_days = 0
    end_date = ''
    for entry in data:
        if total_days == 0:
            d = datetime.datetime.strptime(entry[0], '%Y%m%d')
            start_date = datetime.date.strftime(d,"%d/%m/%Y")
            
        total_steps += int(entry[2])
        total_distance += float(entry[1])
        total_days += 1
        end_date = entry[0]
        
    d = datetime.datetime.strptime(end_date, '%Y%m%d')
    end_date = datetime.date.strftime(d,"%d/%m/%Y")
    date_format = "%d/%m/%Y"
    a = datetime.datetime.strptime(start_date, date_format)
    b = datetime.datetime.strptime(end_date, date_format)
    total_elapsed = (b - a).days
    print('Total Steps:',total_steps)
    print('Total Kilometres:',round(total_distance,2),'km')
    print('Achieved in',total_days,'active days and a total period of',total_elapsed,'days.')
    print('That results in being active about',str(round(total_days/total_elapsed,2)*100)+'%'+' of the time.')



############


    
def steps_vs_date(data,month=current_month,year=current_year,scale=1):
    dates = []
    steps = []
    
    for entry in data: #format date
        steps.append(int(int(entry[2])*scale))
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
    removal = []
    for date in dates:
        if date[3:6] != convert_month[month] or date[-4:] != year:
            removal.append(dates.index(date)-len(removal))

    for n in removal:
        del dates[n]
        del steps[n]
        
    plt.bar([x for x in range(len(dates))],steps)
    plt.xticks([x for x in range(len(dates))],dates,rotation=45)
    for a,b in zip([x for x in range(len(dates))],steps):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Number of Steps')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Steps vs Date - with scale factor of' + ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()


    
############


    
def distance_vs_date(data,month=current_month,year=current_year,scale=1):
    dates = []
    distances = []
    
    for entry in data: #format date
        distances.append(float(entry[1])*scale)
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
       
    removal = []
    for date in dates:
        if date[3:6] != convert_month[month] or date[-4:] != year:
            removal.append(dates.index(date)-len(removal))

    for n in removal:
        del dates[n]
        del distances[n]
        
    plt.bar([x for x in range(len(dates))],distances)
    plt.xticks([x for x in range(len(dates))],dates,rotation=45)
    for a,b in zip([x for x in range(len(dates))],distances):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Distance (km)')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Distance vs Date - with scale factor of'+ ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()



############



def distance_vs_steps(data,month=current_month,year=current_year,scale=1):
    dates = []
    distances = []
    steps = []
    
    for entry in data: #format date
        distances.append(float(entry[1])*scale)
        steps.append(float(entry[2])*scale)
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
       
    removal = []
    for date in dates:
        if date[3:6] != convert_month[month] or date[-4:] != year:
            removal.append(dates.index(date)-len(removal))

    for n in removal:
        del dates[n]
        del distances[n]
        del steps[n]

    plt.scatter(distances,steps)
    plt.ylabel('Steps')
    plt.xlabel('Distance')
    mng = plt.get_current_fig_manager()
    t = 'Distance vs Steps - with scale factor of'+ ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()



############



def steps_summary(data,year=current_year,scale=1):
    dates = []
    steps = []
    
    for entry in data: #format date
        steps.append(int(int(entry[2])*scale))
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
    removal = []
    for date in dates:
        if date[-4:] != year:
            removal.append(dates.index(date)-len(removal))

    for n in removal:
        del dates[n]
        del steps[n]
        
    plt.bar([x for x in range(len(dates))],steps)
    plt.xticks([x for x in range(len(dates))],dates,rotation=45)
    for a,b in zip([x for x in range(len(dates))],steps):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Number of Steps')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Steps Summary - with scale factor of' + ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()



############




def distance_summary(data,year=current_year,scale=1):
    dates = []
    distances = []
    
    for entry in data: #format date
        distances.append(float(entry[1])*scale)
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
       
    removal = []
    for date in dates:
        if date[-4:] != year:
            removal.append(dates.index(date)-len(removal))

    for n in removal:
        del dates[n]
        del distances[n]
        
    plt.bar([x for x in range(len(dates))],distances)
    plt.xticks([x for x in range(len(dates))],dates,rotation=45)
    for a,b in zip([x for x in range(len(dates))],distances):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Distance (km)')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Distance Summary - with scale factor of'+ ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()




########



def all_time_steps(data,scale=1):
    dates = []
    steps = []
    
    for entry in data: #format date
        steps.append(int(int(entry[2])*scale))
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
    
    plt.bar([x for x in range(len(dates))],steps)
    plt.xticks([x for x in range(len(dates))],dates,rotation=90)
    for a,b in zip([x for x in range(len(dates))],steps):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Number of Steps')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Steps Summary - with scale factor of' + ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()



########



def all_time_distance(data,scale=1):
    dates = []
    distances = []
    
    for entry in data: #format date
        distances.append(float(entry[1])*scale)
        d = datetime.datetime.strptime(entry[0], '%Y%m%d')
        dates.append(datetime.date.strftime(d,"%d/%b/%Y"))
        
    plt.bar([x for x in range(len(dates))],distances)
    plt.xticks([x for x in range(len(dates))],dates,rotation=90)
    for a,b in zip([x for x in range(len(dates))],distances):
        plt.text(a,b,str(b),color='red',va='bottom',ha='center')
        
    plt.ylabel('Distance (km)')
    plt.xlabel('Date')
    mng = plt.get_current_fig_manager()
    t = 'Distance Summary - with scale factor of'+ ' ' + str(scale)
    mng.set_window_title(title=t)
    mng.window.state('zoomed')
    plt.show()



########



def graph_help():
    print('Functions of fitness module include:')
    print('steps_vs_date - params:data,month,year,scale')
    print('distance_vs_date - params:data,month,year,scale')
    print('distance_vs_steps - params:data,month,year,scale')
    print('steps_summary - params:data,year,scale')
    print('distance_summary - params:data,year,scale')
    print('all_time_steps - params:data,scale')
    print('all_time_distance - params:data,scale')
    print('stats - params:data')

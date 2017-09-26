from html.parser import HTMLParser

is_event_ul, is_events_li, is_events_title, is_events_time, is_events_location = 0, 0, 0, 0, 0
event_list=[]
event_data={}

class MyHTMLparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global is_event_ul, is_events_li, is_events_title, is_events_time, is_events_location
        if tag=='ul' and len(attrs)>0:
            for x in attrs:
                if x[0]=='class' and 'list-recent-events' in x[1]:
                    is_event_ul=1
                    break

        if is_event_ul==1 and tag=='li':
            is_events_li=1
        if is_events_li==1 :
                if tag=='a':
                    is_events_title=1
                if tag=='time':
                    is_events_time = 1
                    event_data['datetime'] = attrs[0][1][:10]
                if tag == 'span' and attrs[0][1]=='event-location':
                    is_events_location = 1


        #print(' handle_starttag: ',attrs)
    def handle_endtag(self, tag):
        global is_event_ul, is_events_li, is_events_title, is_events_time, is_events_location
        if tag=='ul' and is_event_ul==1:
            is_event_ul=0
        if tag=='li' and is_events_li == 1:
            is_events_li = 0
        if  tag=='a' and is_events_title == 1:
            is_events_title = 0
        if tag=='time' and is_events_time == 1:
            is_events_time = 0
        if tag=='span' and is_events_location == 1:
            is_events_location = 0
        #print(' handle_endtag: ',tag)

    def handle_startendtag(self, tag, attrs):
        pass
        #print('------------------- handle_startendtag: ',tag)

    def handle_data(self, data):
        global event_list,event_data
        if is_events_title==1:
            event_data['title']=data
        if is_events_time==1:

            event_data['time']=data
        if is_events_location==1:
            event_data['location']=data
            event_data_copy=event_data.copy()
            event_list.append(event_data_copy)

    def handle_comment(self, data):
        pass
        #print(' handle_comment: ',data)
    def handle_charref(self, name):
        pass
        #print(' handle_charref: ',name)

    def handle_entityref(self, name):
        pass
        #print(' handle_entityref: ',name)

parser = MyHTMLparser()
str1='''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
str=''
with open('d:/learn/pythonOrg.html','r') as f:
        str=f.read()
print(str)
parser.feed(str)

for index,value in  enumerate(event_list):
    print('index ,',index+1)
    for key in value:
        print('%s ..  %s'  % (key,value[key]))
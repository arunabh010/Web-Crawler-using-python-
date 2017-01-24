from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import MySQLdb


def index(request):
    context = RequestContext(request)

    context_dict = {'boldmessage': "I am bold font from the context"}

    # return HttpResponse("Hey world wasssupp !!")
    return render_to_response('rango/index.html', context_dict)




def search(request):
    if request.POST:
         print request.POST['term']
         return HttpResponseRedirect("/")
    else:
         return render_to_response("search.html")



def index(request):
    # context = RequestContext(request)

    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="123456",
                           db="ratings")
    cursor = conn.cursor()
    if conn.open:
        print "dude SQL DB is connected"
        #   context_dict= {'boldmessage':"dude its connected"}
    else:
        print "huh! U r not connected"
        #  context_dict= {'boldmessage':"huh! U r not connected"}

    Search_str = "CapitaLand"
    # cursor.execute('SELECT * FROM Name_copy where Name = ?', Search_str)
    cursor.execute('SELECT * FROM Name_copy where Name = "CapitaLand"')
    names = [row[0] for row in cursor.fetchall()]
    # row=cursor.fetchone()
    html = "<html><body>" \
           "COMPANY NAME is %s.<br> " \
           "RATING TYPE = %s.<br>" \
           "RATING      = %s.<br>" \
           "RATING DATE = %s<br>" \
           " </body></html>" % (row[0], row[1], row[2], row[3])

    # PRINTING IN TABLE FORMAT
    html = "<!DOCTYPE html>" \
           "<html>THIS  IS TABLE for SEARCH STRING from SQL <br><br><body>" \
           "<table style>" \
           "<tr>" \
           "<td>%s</td>&nbsp" \
           "<td>%s</td>" \
           "<td>%s</td>" \
           "<td>%s</td>" \
           "</tr>" \
           "</table>" \
           "</body></html>" % (row[0], row[1], row[2], row[3])

    conn.close()
    return HttpResponse(html)

# Create your views here.

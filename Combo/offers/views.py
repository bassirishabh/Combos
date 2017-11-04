from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import MyModelForm
import os
from django.conf import settings
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.
def offer(request):

    return render(request,'offers/home.html')
def sendmail(receiver, dirname):
    fromaddr = "kapil0806@gmail.com"
    toaddr = receiver

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ML model run results"

    body = "download attachment for results"

    msg.attach(MIMEText(body, 'plain'))

    filename = str(dirname) + '/combo1.txt'
    print(dirname)
    print(filename)
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % 'result.txt')

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "gemini0806")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
def AddList(request) :
        form=MyModelForm(request.POST,request.FILES)
        print(form.data)

        context={
            "form":form,
        }
        combo1=open("combo1.txt",'w')
        if form.is_valid():
            print("Hello")
            ll=int(form.cleaned_data['lower_limit'])
            ul = int(form.cleaned_data['upper_limit'])
            email=form.cleaned_data['email']
            print(email)
            print(ll)
            print(ul)
            form.save(commit=False)
            file=request.FILES['file1']
            path = settings.MEDIA_ROOT
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            path_name = os.path.join(path, filename)
            print(path_name)
            f=open(path_name,'r')
            d = {}
            for l in f:
                if not l.strip(): continue
                l = l.strip()
                key, val = l.split(" ")
                d[(key)] = val
            l1=[]

            ResultList=set()
            for key in d:
                l1.append(int(d[key]))
            print(len(l1))
            for i in range(10000):
                SetSize = random.randint(2,len(l1)-1)
                z = random.sample(l1,SetSize)

                z.sort()
                Chromosome = tuple(z)
                if ((sum(Chromosome) >ll)and(sum(Chromosome) <ul)) :
                    l2 = []
                    for i in Chromosome:
                        for key in d:
                            if (int(d[key]) == int(i)):
                                l2.append(key)
                                break
                    t = tuple(l2)
                    ResultList.add((t))
            for r in ResultList:
                combo1.write(str(r)+"\n")
            combo1.close()
            dir=os.getcwd()
            sendmail(email, dir)
            print("\nTotal Sets: ", len(ResultList))




            return render(request,'offers/home.html')
        return render(request,'offers/home1.html',context)

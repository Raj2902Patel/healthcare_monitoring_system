from django.shortcuts import render

import requests

# Create your views here.

def raj(request):
    records = {}
    url = "http://localhost/RaJ/fetch.php"
    response = requests.get(url=url)
    appo_api = response.json()
    records['appodata'] = appo_api


    return render(request,'raj.html',records)

def ecg(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-ecg.php"
    response = requests.get(url=url)
    ecg_api = response.json()
    records['ecgdata'] = ecg_api

    print(records)
    return render(request,'ecg2.html',records)

def pulse(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-pulse.php"
    response = requests.get(url=url)
    pulse_api = response.json()
    records['pulsedata'] = pulse_api

    return render(request,'pulse2.html',records)

def oxygen(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-oxygen.php"
    response = requests.get(url=url)
    oxy_api = response.json()
    records['oxydata'] = oxy_api

    return render(request,'oxygen.html',records)

def datatables(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-temp.php"
    response = requests.get(url=url)
    temp_api = response.json()
    records['tempdata'] = temp_api

    return render(request,'datatables.html',records)

def index(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/Data.php"
    response = requests.get(url=url)
    data_ecg = response.json()
    records['Data'] = data_ecg

    url1 = "https://healthcaregls.000webhostapp.com/API/datao.php"
    response = requests.get(url=url1)
    data_oxygen = response.json()
    records['OxygenD'] = data_oxygen

    url2 = "https://healthcaregls.000webhostapp.com/API/Datap.php"
    response = requests.get(url=url2)
    data_pulse = response.json()
    records['PulseD'] = data_pulse

    url3 = "https://healthcaregls.000webhostapp.com/API/datat.php"
    response = requests.get(url=url3)
    data_temp = response.json()
    records['TempD'] = data_temp

    return render(request,'index2.html',records)

def patient(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/Data.php"
    response = requests.get(url=url)
    data_ecg = response.json()
    records['Data'] = data_ecg

    url1 = "https://healthcaregls.000webhostapp.com/API/datao.php"
    response = requests.get(url=url1)
    data_oxygen = response.json()
    records['OxygenD'] = data_oxygen

    url2 = "https://healthcaregls.000webhostapp.com/API/Datap.php"
    response = requests.get(url=url2)
    data_pulse = response.json()
    records['PulseD'] = data_pulse

    url3 = "https://healthcaregls.000webhostapp.com/API/datat.php"
    response = requests.get(url=url3)
    data_temp = response.json()
    records['TempD'] = data_temp

    lasttempdata = data_temp["Data"][0]["temp_value"]
    lastoxydata = data_oxygen["Data"][0]["oxygen_value"]
    lastpulsedata = data_pulse["Data"][0]["pulse_value"]
    lastecgdata = data_ecg["Data"][0]["ecg_value"]

    lastpulsedata1 = int(lastpulsedata)
    lastecgdata1 = int(lastecgdata)
    lastoxydata1 = int(lastoxydata)
    lasttempdata1 = int(lasttempdata)


    if (lastpulsedata1 > 100 or lastpulsedata1 < 60) or (lastecgdata1 > 100 or lastecgdata1 < 60) or (
            lastoxydata1 < 90) or (lasttempdata1 > 100):

        msg = "Patient Name : ""Joshi Shashank Rushikbhai" "\n\nECG Value : " + lastecgdata + "\nOxygen Value : " + lastoxydata + "\nPulse Value : " + lastpulsedata + "\nTemperature Value : " + lasttempdata
        # this variable will be passed as message in mail
        

        from django.core.mail import send_mail

        send_mail(
            'Alert Message From HealthCare',
            msg,
            'healthcare.info2023@gmail.com',
            ['dr.jayeshpatel2580@gmail.com'],
            fail_silently=False,
        )
    else:
        pass

    return render(request,'patient.html',records)

def pecg(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-ecg.php"
    response = requests.get(url=url)
    ecg_api = response.json()
    records['ecgdata'] = ecg_api

    return render(request,'pecg.html',records)

def poxygen(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-oxygen.php"
    response = requests.get(url=url)
    oxy_api = response.json()
    records['oxydata'] = oxy_api

    return render(request,'poxygen.html',records)

def ppulse(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-pulse.php"
    response = requests.get(url=url)
    pulse_api = response.json()
    records['pulsedata'] = pulse_api

    return render(request,'ppulse.html',records)

def ptemp(request):
    records = {}
    url = "https://healthcaregls.000webhostapp.com/API/fetchapi-temp.php"
    response = requests.get(url=url)
    temp_api = response.json()
    records['tempdata'] = temp_api

    return render(request,'ptemp.html',records)
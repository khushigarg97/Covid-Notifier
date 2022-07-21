from plyer import notification
import requests
from bs4 import BeautifulSoup 
import time

# function used to give the notification
def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon ="C:\Covid-19 Notification System\img1.ico",
        timeout = 10
    )

# function used to take the data from the site 
def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":

        #notifyMe("Hey Khushi! Let's checkout the Covid cases")
        htmlData = getData('https://www.mohfw.gov.in/')
        #print(htmlData)
        soup = BeautifulSoup(htmlData, 'html.parser')
        # print(soup.prettify())

        active_cases = soup.find("li", {'class': 'bg-blue'}).find_all('strong',{'class' : 'mob-hide'})
        active_cases = active_cases[1].get_text()

        Discharged_cases = soup.find("li",{'class': 'bg-green'}).find_all('strong',{'class' : 'mob-hide'})
        Discharged_cases = Discharged_cases[1].get_text()

        Death_cases = soup.find("li",{'class': 'bg-red'}).find_all('strong',{'class' : 'mob-hide'})
        Death_cases = Death_cases[1].get_text()

        Total_vaccination=soup.find("span",{'class' : 'coviddata'})
        Total_vaccination=Total_vaccination.get_text()

        # Total_cases = int(active_cases) + int(Discharged_cases) + int(Death_cases)
        # print(Total_cases)

        notification_title = "Covid-19 Notification System"
        notification_text= f"Active Cases : {active_cases}\nDischarged Cases : {Discharged_cases}\nDeath Cases : {Death_cases}\nTotal Vaccination : {Total_vaccination} "
        notifyMe(notification_title,notification_text)
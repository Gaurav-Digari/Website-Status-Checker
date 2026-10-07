import requests as req
up=0
not_up=0
total=0

def design():
    with open("report.txt","a") as file :
        file.write("WEBSITE STATUS REPORT \n")
        file.write("=====================\n")
        file.write(f"{'URL':<20} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")

def write(url):
    try:
        response=req.get(url,timeout=5)
    except req.exceptions.Timeout:
        Label="TimeOut"
        not_up+=1
    except req.exceptions.ConnectionError:
        Label="UNREACHABLE"
        not_up+=1
    except req.exceptions.MissingSchema:
        Label="Invalid Url"
        not_up+=1

    
    
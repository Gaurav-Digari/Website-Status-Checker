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
        result="TimeOut"
        not_up+=1
    except req.exceptions.ConnectionError:
        result="UNREACHABLE"
        not_up+=1
    except req.exceptions.MissingSchema:
        result="INVALID URL"
        not_up+=1

    status=response.status_code
    time=response.elapsed.total_seconds()*1000

    if response.is_redirect:
        redirect="Yes"
    else :
        redirect="No"

    if 200 <= status <=  299:
        result="UP" 
        up+=1
    elif 400 <= status <= 499:
        result="CLIENT ERROR" 
        not_up+=1
    elif 500 <= status <= 599:
        result="SERVER ERROR" 
        not_up+=1

    if result == "TimeOut" or result=="INVALID URL" or result=="UNREACHABLE":
        status,time,redirect,result=0

    

    
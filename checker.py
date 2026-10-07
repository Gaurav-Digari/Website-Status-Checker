import requests as req

total=0

def design():
    with open("report.txt","a") as file :
        file.write("WEBSITE STATUS REPORT \n")
        file.write("=====================\n")
        file.write(f"{'URL':<20} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")

def write(url):
    up=0
    not_up=0
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

    with open ("report.txt","a") as file :
        file.write(f"{url:<20} {status:<8} {time:<10} {redirect:<12} {result}\n")

    return up,not_up

with open ("sites.txt","r")as file:
    for url in file :
        if url == '\n':
            continue
        else:
            total+=1
            write(url)


    with open ("report.txt","a") as file :
      file.write("SUMMARY\n")
      file.write("-------\n")
      file.write("TOTAL SITES CHECKED {total:<20}\n")
      file.write(f"UP {up:<20}\n")
      file.write(f"NOT UP {not_up:<20}\n")

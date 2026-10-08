import requests as req

total=0
up=0
not_up=0

def design():
    with open("report.txt","a") as file :
        file.write("WEBSITE STATUS REPORT \n")
        file.write("=====================\n")
        file.write(f"{'URL':<41} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")

def write(url):
    result = ""
    global not_up
    global up

    try:
        response = req.get(url, timeout=5)

    except req.exceptions.Timeout:
        result = "TimeOut"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "No"

    except req.exceptions.ConnectionError:
        result = "UNREACHABLE"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "No"

    except req.exceptions.MissingSchema:
        result = "INVALID URL"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "No"

    else:
        status = response.status_code
        time =round(response.elapsed.total_seconds() *1000,2)

        if response.is_redirect:
            redirect = "Yes"
        else:
            redirect = "No"

        if 200 <= status <= 299:
            result = "UP"
            up += 1

        elif 400 <= status <= 499:
            result = "CLIENT ERROR"
            not_up += 1

        elif 500 <= status <= 599:
            result = "SERVER ERROR"
            not_up += 1

    with open("report.txt", "a") as file:
        file.write(
            f"{url:<41} {status:<8} {time:<10} "
            f"{redirect:<12} {result}\n"
        )
design()
with open ("sites.txt","r")as file:
    for url in file :
        if url == '\n':
            continue
        else:
            total+=1
            url=url.strip()
            # write(url)


with open ("report.txt","a") as file :
    file.write("\n \nSUMMARY\n")
    file.write("---------\n")
    file.write(f"TOTAL SITES CHECKED {total:<21}\n")
    file.write(f"{'UP':<20}{up}\n")
    file.write(f"{'NOT UP':<20}{not_up}\n")

import requests as req

total=0
up=0
not_up=0

open("report.txt", "w").close()

def design():
    with open("report.txt","a") as file :
        file.write(f"*****************************         WEBSITE STATUS REPORT           *****************************\n\n")
        file.write(f"{'URL':<41} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")

print(f"*****************************         WEBSITE STATUS REPORT           *****************************\n\n")
print(f"{'URL':<41} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")
def write(url):
    result = ""
    global not_up
    global up

    try:
        response = req.get(url, timeout=5)

    except req.exceptions.Timeout:
        result = "TIMEOUT"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "-"

    except req.exceptions.ConnectionError:
        result = "UNREACHABLE"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "-"

    except (req.exceptions.MissingSchema, req.exceptions.InvalidSchema, req.exceptions.InvalidURL):
        result = "INVALID URL"
        not_up += 1
        status ="-"
        time ="-"
        redirect = "-"

    else:
        status = response.status_code
        time =round(response.elapsed.total_seconds() *1000)

        if response.history:
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
    print(f"{url:<41} {status:<8} {time:<10} {redirect:<12} {result}\n")
design()
with open ("sites.txt","r")as file:
    for url in file :
        if url == '\n':
            continue
        else:
            total+=1
            url=url.strip()
            write(url)

print(f"*****************************         SUMMARY           *****************************\n\n")
print(f"TOTAL SITES CHECKED {total:<21}\n")
print(f"{'UP':<20}{up}\n")
print(f"{'NOT UP':<20}{not_up}\n")

with open ("report.txt","a") as file :
    file.write(f"\n*****************************         SUMMARY           *****************************\n\n")
    file.write(f"TOTAL SITES CHECKED {total:<21}\n")
    file.write(f"{'UP':<20}{up}\n")
    file.write(f"{'NOT UP':<20}{not_up}\n")

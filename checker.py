up=0
not_up=0
total=0

def design():
    with open("report.txt","a") as file :
        file.write("WEBSITE STATUS REPORT \n")
        file.write("=====================\n")
        file.write(f"{'URL':<20} {'STATUS':<8} {'TIME(ms)':<10} {'REDIRECTED':<12} {'RESULT'}\n")

design()
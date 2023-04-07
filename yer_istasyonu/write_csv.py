import csv
telemetri_paketi = []

def write_csv(data):
            global telemetri_paketi
            with open('telemetri_verileri', 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([data]) 
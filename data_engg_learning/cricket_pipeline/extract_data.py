import requests
import csv

url = "https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen"

querystring = {"formatType":"test"}

headers = {
	"x-rapidapi-key": "b3fc19b4d2msh3d427e9a1bb6268p144febjsnb5817fc25b94",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    data = response.json().get('rank', {}) # to extract the rank data
    csv_filename = 'test_batsmen_ranking.csv'

    if data:
        field_names = ['rank','name','country','rating','points','lastUpdatedOn'] #specifying the col names

        #write data to csv
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            #header
            for entry in data:
                writer.writerow({field: entry.get(field) for field in field_names})
            
        print(f"Data fetched successfully and written to '{csv_filename}'")
    else:
        print("No data available from the api")
    
else:
    print("failed to fetch the data:", response.status_code)


import common.job_util as util
import requests
import json
import time

s = requests.Session()
data=[]
# update headers
s.headers.update({
    'Accept': 'application/json',
    'x-api-key': 'kXlFFTjuqWgABx3nXj5oXZn2VWW9ql93mURt'
})

page_cntr = 1
while True:
    time.sleep(1)
    params = {"year": "2021","p":page_cntr}
    response = s.get('https://api.setlist.fm/rest/1.0/search/setlists', params=params)
    output=json.loads(response.content.decode("utf-8"))
    print(output)
    print("Total records:" + str(output["total"]))
    print("Page no:" + str(output["page"]))
    if len(output["setlist"])>0:
        data.extend(output["setlist"])
    else:
        break
    page_cntr+=1

util.convert_output_to_file_type(
    data, "Output.json", "json"
)

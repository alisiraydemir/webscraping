from bs4 import BeautifulSoup
import requests
n_pages = 10
for n in range(2, n_pages):
    print(n)
    html_text = requests.get('https://www.kariyer.net/is-ilanlari/?kw=python&cp='+ str(n)).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("div", class_ = "list-items")
    for job in jobs:
        company_name = job.find("div", class_ = "k-text small").text.strip()
        job_name = job.find("h3", class_ = "kad-card-title").text.strip()
        print(f'''
        Company Name: {company_name}
        Job Name: {job_name}
        ''')

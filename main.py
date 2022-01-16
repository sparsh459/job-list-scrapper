from bs4 import BeautifulSoup
import requests
import time

print('Unfamiliar skills')
unfamiliar_skills = input('>')
print(f'filtering out by unfamiliar skills {unfamiliar_skills}')

def find_jobs():
    resp = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=&cboWorkExp1=0')
    # print(resp.text)

    html_text = resp.text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # print(jobs)
    for index, job in enumerate(jobs):
        date_posted = job.find('span', class_='sim-posted').text
        if 'few' in date_posted:
            company = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Comapny: {company.strip()} \n')
                    f.write(f'Required skills: {skills.strip()} \n')
                    f.write(f'more info: {more_info} \n')
                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting...{time_wait}...minutes')
        time.sleep(time_wait*60)
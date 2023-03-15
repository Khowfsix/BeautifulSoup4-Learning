# Get all job in page 1 of
# https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=

from bs4 import BeautifulSoup
import requests

getPage = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text

soup = BeautifulSoup(markup=getPage, features='lxml')

jobLists = soup.find_all(name='li', class_='clearfix job-bx wht-shd-bx')

for job in jobLists:
    jobName = job.find(name='h2').text
    jobName = ' '.join(jobName.split())
    jobName = jobName.replace('"', '')

    companyName = job.find(
        name='h3', class_='joblist-comp-name').contents[0].text
    companyName = companyName.strip()

    skills = job.find(name='span', class_='srp-skills').text
    skills = ' '.join(skills.split()).replace('"', '')
    skills = skills.replace(" , ", ", ")

    dayPosted = job.find(name='span', class_='sim-posted')
    dayPosted = dayPosted.findAll(name='span')[-1].text

    print(f'''
Job name: {jobName}
Company name: {companyName}
Skills: {skills}
Published date: {dayPosted}
''')

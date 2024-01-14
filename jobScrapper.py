from bs4 import BeautifulSoup;
import requests
import time;
print('Put some skill that you are not familiar with')
unfimaliarSkills = "debugging"
print(f'Filtering out {unfimaliarSkills}')
# we use the .text method to get the html text.
# we use the .content method to get the html content.
# print(html_text) #This outputs a success code of 200 which means that the request was successful.
def findJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobPosts = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, jobpost in enumerate(jobPosts):
        jobPostedDate = jobpost.find('span', class_ = 'sim-posted').span.text
        if 'few' in jobPostedDate:
            companyName = jobpost.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            keySkills = jobpost.find('span', class_='srp-skills').text.replace(' ', '') 
            moreInfo = jobpost.header.h2.a['href']
            # print("The Company Name: " + companyName)
            # print("Key Skills Required: " +  keySkills)
            if unfimaliarSkills not in keySkills:
               with open(f'JobPosts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {companyName.strip()} \n')
                    f.write(f'Required Skills: {keySkills.strip()} \n')
                    f.write(f'More Info: {moreInfo} \n')
                    print(f'File saved with the index {index}')

                #  print(f'Company Name: {companyName.strip()}')
                #     print(f'Required Skills: {keySkills.strip()}')
                #     print(f'More Info: {moreInfo}')
                # print('***********************************************************************************************')

if __name__ == '__main__':
   while True:
    findJobs()
    timewait = 10
    print(f'Waiting for {timewait} minutes...')
    time.sleep(timewait * 60)
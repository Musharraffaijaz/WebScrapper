import requests;
from bs4 import BeautifulSoup;

def extract_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    job_listings = []
  
    job_elements = soup.find_all('div', class_='job-listing')  

    for job_element in job_elements:
        title = job_element.find('h2').text.strip()
        link = job_element.find('a')['href']
        platform = url.split('/')[2] 
        job_listings.append({'title': title, 'link': link, 'platform': platform})

    return job_listings

def search_company_jobs(company_name):
    platforms = ['linkedin.com', 'indeed.com', 'monster.com', 'google.com/jobs'] 

    all_job_listings = []
    for platform in platforms:
        base_url = f"https://www.{platform}/jobs"  
        search_url = f"{base_url}?q={company_name}"  

        try:
            platform_job_listings = extract_job_listings(search_url)
            all_job_listings.extend(platform_job_listings)
        except Exception as e:
            print(f"Error fetching jobs from {platform}: {e}")

    return all_job_listings

company_name = input("Enter company name: ")
job_listings = search_company_jobs(company_name)

for job in job_listings:
    print(f"Title: {job['title']}")
    print(f"Platform: {job['platform']}")
    print(f"Link: {job['link']}")
    print("-" * 50)

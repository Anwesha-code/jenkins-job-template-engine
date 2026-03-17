import yaml
import requests
from jinja2 import Template

JENKINS_URL = "http://localhost:8080"
USERNAME = "AnweshaSingh"
API_TOKEN = "110d63401eb9d9937b6df043e73363cd6b"


def load_template():
    with open("../templates/job_template.xml") as f:
        return Template(f.read())


def load_jobs():
    with open("../configs/jobs.yaml") as f:
        return yaml.safe_load(f)["jobs"]


def create_job(job_name, config_xml):
    crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
    crumb_response = requests.get(crumb_url, auth=(USERNAME, API_TOKEN))

    if crumb_response.status_code != 200:
        print("Crumb fetch failed:", crumb_response.text)
        return

    crumb_data = crumb_response.json()
    crumb_header = {crumb_data['crumbRequestField']: crumb_data['crumb']}

    headers = {
        "Content-Type": "application/xml",
        **crumb_header
    }

    check_url = f"{JENKINS_URL}/job/{job_name}/api/json"
    check = requests.get(check_url, auth=(USERNAME, API_TOKEN))

    if check.status_code == 200:
        url = f"{JENKINS_URL}/job/{job_name}/config.xml"
        response = requests.post(
            url,
            data=config_xml,
            headers=headers,
            auth=(USERNAME, API_TOKEN)
        )
        action = "updated"
    else:
        url = f"{JENKINS_URL}/createItem?name={job_name}"
        response = requests.post(
            url,
            data=config_xml,
            headers=headers,
            auth=(USERNAME, API_TOKEN)
        )
        action = "created"

    if response.status_code in [200, 201]:
        print(f"{job_name} {action} successfully")
    else:
        print(f"Failed {job_name} (Status: {response.status_code})")
        print(response.text)


def main():
    template = load_template()
    jobs = load_jobs()

    for job in jobs:
        config_xml = template.render(**job)
        print("GENERATED XML")
        print(config_xml)
        create_job(job["name"], config_xml)


if __name__ == "__main__":
    main()
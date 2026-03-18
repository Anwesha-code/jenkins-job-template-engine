Here are step-by-step instructions for using the Jenkins Job Template Engine.

## Software Requirements
- Python 3.10 or above
- Jenkins installed and running 
- Git installed and configured
- Install required libraries using: pip install requests pyyaml jinja2

## Project Structure
jenkins-template-engine/
    - src/scripts/      --> Python automation script
    - templates/        --> Jenkins XML template 
    - configs/      --> YAML job configurations 
    - docs/         --> Documentation files 
    - pipelines/        -->Jenkinsfile (CI pipeline definition) 
    - presentations/        -->Demo and project ppt
    - README.md

## Steps
- Start Jenkins (http://localhost:8080)
- Generate API Token: Open Jenkins Dashboard; Go to Manage Jenkins -> Manage Users -> Your User -> Configure; Generate an API Token; Copy and save it securely
- Update API token in generate_jobs.py, and username

    JENKINS_URL = "http://localhost:8080"

    USERNAME = "your_username" 

    API_TOKEN = "your_api_token"
- Configure Jobs in configs/jobs.yaml
- To run the project
    - cd src/scripts
    - py generate_jobs.py
    - Verify job creation on console and Jenkins dashboard
- To execute jobs
    - http://localhost:8080
    - Select job
    - Click 'Build with Parameters'
    - Provide input (branch name)
    - Build
    - View output in console output

## Pipeline Execution
- Clone: Fetches repository code
- Install: Prepares environment
- Build: Executes build commands
- Test: Runs test commands

## Failure
- Invalid Branch: Pipeline fails at Clone stage; Error message displayed in console; Remaining stages are skipped.

## Troubleshooting
- Jobs not created: 
    possible causes:
        -Incorrect API token (Verify credentials)
        -Jenkins not running (Restart Jenkins)
- Git authentication error
    Private repository or incorrect URL
Configuring CI pipelines manually in tools such as Jenkins can be repetitive, time-consuming, and prone to inconsistencies.

## Design Goals
- To automate Jenkins job creation using REST API
- To make project reusable through templated pipeline definitions
- Dynamic configuration using YAML
- Parameterized execution at runtime
- Fail-fast for incorrect configurations

## System Architecture
Automated model using pipeline.

Each component has a specific responsinility
- User Input (jobs.yaml): Job definitions in structured format. Defines job specific parameters. Allows separation between data and the logic.
- Python Script (generate_jobs.py): Core component responsible for orchestrating the system.
    - Load YAML configuration
    - Render template using Jinja2
    - Communicate with Jenkins via REST API
    - Handle authentication and CSRF protection
    - Create or update jobs
- Template Engine and XML Configuration (Jinja2, job_template.xml): A reusable Jenkins pipeline template written in XML with embedded placeholders. Defines CI pipeline structure. Maintains consistency in jobs. Parameterized (Branch variable) Multistage pipeline: Clone, Install, Build, Test
- Jenkins REST API 
- Jenkins Job Creation 
- Pipeline Execution (CI Stages)

## Workflow
- User defines job configurations in jobs.yaml
- Python script reads and starts parsing the YAML file
- Jinja2 template is loaded and rendered with job-specific values
- Generated XML is sent to Jenkins via REST API
- Jenkins creates or updates jobs accordingly
- User triggers job execution (manual or parameterized) on jenkins dashboard
- Pipeline executes defined stages

## Pipeline Design
Structured multi-stage pipeline:
1. Clone Stage
    - Fetches source code from Git repository
    - Uses dynamic branch parameter

2. Install Stage
    - Installs dependencies or prepares environment

3. Build Stage
    - Executes build commands

4. Test Stage
    - Runs test scripts

## Parameterization Design
The pipeline includes runtime parameters: string(name: 'BRANCH', defaultValue: 'main')
- Allows user to select branch during execution
- Enhances flexibility without modifying code

## Error Handling Strategy
Basic error handling mechanisms:
- API Errors: Validates response status codes and prints error messages for debugging
- SCM Errors: Detects invalid repository or branch and stops execution at clone stage
- Fail-Fast Behaviour: If any stage fails, subsequent stages are skipped, hence prevents unnecessary resource usage
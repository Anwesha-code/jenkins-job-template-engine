# Jenkins Job Template Engine

Automating CI pipeline creation using Templates, YAML, and Jenkins API

## Overview
Manually creating and maintaining multiple Jenkins jobs can become repetitive, error-prone, and difficult to scale.

This project automates Jenkins job creation using reusable templates and dynamic configuration.

This project introduces a template-based approach where a single job template is reused with different parameters, allowing automated and scalable CI job creation. The system leverages Python, Jinja2 templating, and Jenkins REST API to generate CI pipelines using programming.

## Objectives
- To eliminate repetitive manual configuration of Jenkins jobs
- To enable reusability using templates

## System Architecture
- generate_jobs.yaml (Configuration)
- Python Script (Template Engine)
- Jinja2 Template (XML Pipeline)
- Jenkins REST API
- Auto-generated Jenkins Jobs
- CI Pipeline Execution

## Tech Stack
- Jenkins (CI/CD automation server)
- Python (scripting and automation)
- Jinja2 (templating engine)
- YAML (job configuration)
- GitHub (source code repository)
- Jenkins REST API (job creation)

## Key Features
- Reusable Job Templates
- YAML-driven Job Configuration
- Automated Job Creation
- Multi-stage CI Pipeline (Clone repo, install dependencies, build applications, run tests)
- Parameterized Pipelines

## How to Run
1. Start Jenkins
2. Generate API Token
3. Install Dependecies (pip install requests pyyaml jinja2)
4. Run:
   py generate_jobs.py
5. Verify Jobs in Jenkins
6. Execute Pipeline
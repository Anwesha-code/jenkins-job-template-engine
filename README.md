# Jenkins Job Template Engine

## Overview
This project automates Jenkins job creation using reusable templates and YAML configuration.

In large DevOps systems, creating multiple Jenkins jobs manually is repetitive and error-prone. 
This project introduces a template-based approach where a single job template is reused with different parameters, allowing automated and scalable CI/CD job creation.

## Features
- Template-based job creation
- Dynamic variable substitution (Jinja2)
- Jenkins REST API integration
- Supports multiple jobs

## Tech Stack
- Jenkins
- Python
- Jinja2
- YAML

## How to Run
1. Start Jenkins
2. Generate API Token
3. Run:
   py generate_jobs.py
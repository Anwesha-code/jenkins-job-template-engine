## 1 – Requirement Analysis and Environment Setup
Understanding problem statement and setting up development enviroments (installing and downloading resources required)
- Install and configure Jenkins locally
- Explore Jenkins UI and manually create sample job
- Understood limitations of manual job creation
- Identified need for automation

## 2 – Template Design and Configuration Setup
Designing a reusable pipeline template and defining external configurations.
- Design XML-based Jenkins job template using Jinja2 placeholders
- Create YAML configuration file (jobs.yaml) to define job parameters
- Define variables such as: repo_url, branch, build_command, test_command

## 3 – API integration and Automation
Implementing the core automation logic using Python and integrating with Jenkins REST API.
- Develop Python script to:Load YAML configuration; Render XML using Jinja2; Interact with Jenkins API
- Implement CSRF crumb handling for secure API communication
- Automate job creation process

## 4 – Feature Enhancement and Testing
Improving the system and validating its functionality.
- Multi-stage pipeline structure: Clone, Install, Build
- Implement parameterized pipelines (runtime branch selection)
- Test success and failure scenarios

## Development Approach
Modular and iterative development approach:
- Started with basic manual jenkins job
- The templating used for reusability
- Automation through API
- Enhancements

## Deliverables
- Working Jenkins Job Template Engine
- Automated job creation 
- YAML-based configuration 
- Reusable pipeline template
- Documentation (README, design, user guide)
- Final demo
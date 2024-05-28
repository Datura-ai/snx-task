# Task Description: Python API Development with FastAPI

## Overview
We are embarking on a project to develop a Python API using FastAPI, designed to interact with client-side requests for managing and executing tasks. This initiative requires the creation of a system capable of dynamically allocating resources and executing code within Docker containers, tailored to the specific needs of each task.

## Task Objectives

### 1. Task Management
- **Task Type & Execution**: Central to this project is the ability to process tasks that include executable code. The system must execute this code and return the output.
- **Code Execution**: The API should accept code snippets from the client, securely execute them, and return the results.

### 2. Resource Requirements
Tasks will detail their resource needs, including:
- CPU
- GPU
- RAM
- Storage

Your solution must dynamically configure a Docker container with these specified resources to create an optimized environment for the code execution.

### 3. Execution and Response
Upon task receipt, the system is expected to:
    - Determine the necessary resources.
    - Set up a Docker container with these resources.
    - Run the code within this container.
    - Return the execution outcomes through the API.

## Project Goals

The aim here is not a fully operational product but to evaluate your solution strategy. We're interested in your:
- Interpretation and application of the business logic.
- Planning and architecture of the API and resource management.
- Problem-solving approach, especially in resource allocation and isolation with Docker.

## Submission Guidelines

- **Time Allocation**: You have 5 hours to work on this task. Focus on delivering the core functionality within this timeframe.
- **Submission**: Upon completion, submit a Pull Request to this repository. Please include a detailed description of your solution.
- **JSON Parameter Example**: To aid in understanding the expected client-side input, below is an example of a JSON parameter object. This includes a simple Python 
code snippet and other parameters:

Example 1: 
```json
{
  "task_type": "execute_code",
  "code": "print('Hello, World!')",
  "resources": {
    "cpu": "2",
    "gpu": "0",
    "ram": "512MB",
    "storage": "1GB"
  }
}
```

Example 2: 
```json
{
  "task_type": "execute_code",
  "code": "for i in range(5): print(f'Count {i}')",
  "resources": {
    "cpu": "1",
    "gpu": "0",
    "ram": "256MB",
    "storage": "500MB"
  }
}
```
This JSON object exemplifies the structure and type of data your API will receive from clients. It outlines the task type, the code to be executed, and the resource requirements.


## Additional Instructions

### Version Control and Commit Strategy

- **Initial Commit**: Immediately after setting up your project structure, make an initial commit to the repository. This serves as a timestamp to help track the time spent on the task.
- **Regular Commits**: Aim to commit your changes at least once every hour. This demonstrates your progress and helps in maintaining a good version control practice.
- **Commit Messages**: Ensure your commit messages are descriptive and reflect the changes made or features added. This is a key part of good GitHub practices.
- **Well-Commented Code**: Your code should be well-commented, explaining the logic and decisions made. This is crucial for maintainability and understanding by others.

### Time Management and Submission

- **Work Duration**: Do not work more than 5 hours on this task. It's important to manage your time effectively and focus on delivering the core functionality within the allocated timeframe.
- **Final Submission**: After 5 hours, or upon completion, submit a Pull Request (PR) to this repository with your final results. The PR description should provide a detailed account of your solution, highlighting any assumptions, challenges faced, and how you addressed them.
- **Video recording**: Please record and upload a video recording (using loom or some other tool) that shows you running and executing your code, as well explaining your comments about the code and your process, your blockers if any, and what you would focus on next if you had more time.

### Emphasis on Quality

- **Code Quality**: Strive for clean, efficient, and readable code. The quality of your code is just as important as the functionality.
- **GitHub Practices**: Use branches for development and merge them into the main branch via Pull Requests. This not only helps in organizing your work but also in incorporating code reviews.
- **Feedback Incorporation**: Be open to feedback on your PR and ready to make adjustments as necessary. This is a part of the collaborative development process.

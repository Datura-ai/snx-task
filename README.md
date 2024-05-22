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
- **JSON Parameter Example**: To aid in understanding the expected client-side input, below is an example of a JSON parameter object. This includes a simple Python code snippet and other parameters:

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

This JSON object exemplifies the structure and type of data your API will receive from clients. It outlines the task type, the code to be executed, and the resource requirements.

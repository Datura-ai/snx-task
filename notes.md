# Candidate Nodes: Python API Development for Task Executor

## Interpretation Ultimate Goal of the Project

The ultimate goal of the project is to create a platform where customers can easily run AI training processes by uploading their training code. The platform will accept code submissions, such as zipped files containing the training code, and execute the training process within dynamically created and isolated Docker containers. Customers will have the flexibility to specify the resources (CPU, RAM, Storage, and GPU) required to run their code. Based on these resource specifications, customers will be charged accordingly for platform usage.

## How to Run Application

### Build Task Executor Docker image

Run command: 
```
make build-task-executor
```

### Setup env file. 

Copy `.env.example` to `.env` and change the environment variables as you want. 

### Run docker compoase. 

```
docker-compose up -d
```

### Other commands

- Generate migrations
```
make generate-migrations message="...."
```

## Implementation Overview

### Current Implementation 

In the current implementation, we've established a dedicated directory for the task executor. Within this directory resides a straightforward Python file responsible for reading a code string from the environment and executing it. We've encapsulated this functionality into a Docker image tailored for the task executor, which we utilize when creating Docker containers from the backend code.

### Proposed Improvement for Future Reality Project

In the future, as we expand our platform's capabilities, we aim to provide customers with the flexibility to upload either individual code files or entire projects for tasks like AI training. Users will have the option to upload their code in zipped format. To facilitate this, we'll establish a dedicated volume within our system to mount the uploaded code into the task container.

This expansion will necessitate the development of our own SDK or API, enabling users to trigger the execution of tasks and specify resource allocations according to their requirements.

e.g.
```python
# This will be our SDK/API package 
import snx_task

... 

def start_training():
    ...

# This will trigger the running of the task inside the dynamcially created docker container.
# We should build our SDK/API and provide the documents that customers can integrate into their project to deploy. 
syx_task.start({ handler: start_training })
````

## Project Structure  & Tech Stacks

### 1. Backend

#### API Designs

- `POST /tasks`     
    
    This endpoint serves to create a task instance, initiate the creation of a Docker container, and execute the provided code. However, we opt not to wait for task completion, a decision driven by considerations of user experience and system scalability.

    The execution of provided code may potentially require significant time, or in the worst case, it might involve malicious code submissions resulting in infinite waiting. Such scenarios could overload the API server and disrupt its functionality.

    As a solution, we opt to trigger the task execution as a background process. This approach allows us to swiftly return a task ID to the user without awaiting the task's output. To maintain simplicity within our time constraints, we've leveraged FastAPI's built-in background task functionality instead of implementing a more robust solution like Celery. However, the concept and necessity of employing background tasks remain crucial, and in a production environment, integrating with Celery would be preferable for scalability and task management

- `GET /tasks/{taskId}`     
    This endpoint retrieves the result of a task using the task ID obtained from the `POST /tasks` API endpoint. Upon creating a task record in the database, we promptly return it to the user while simultaneously initiating the task execution in the background. Once the task is completed, we update the corresponding database record accordingly.

    This approach enables frontend clients to periodically check the status of their tasks. Additionally, we have the option to integrate email notifications or other forms of notifications to inform users when their tasks have finished executing in the background.

#### Security Best Practices 

- Due to time constraints, authentication, authorization, and comprehensive monitoring for malicious code submissions have not been implemented. However, the system does provide a mechanism to track potentially malicious tasks or code through specific columns in the model. The `container_id`, `task_status`, and `elapsed_time` columns within the model can be utilized to detect any suspicious activities or aberrations in task execution. These columns serve as valuable indicators for monitoring and identifying potential security threats within the 

- I implemented secure validation logics for resources. 

#### Migrations & ORM
- Used SQLite for Database.

- I installed alembic for migrations. You can generate migrations automatically using the command in `Makefile`. 

- I used SQLModel(based on `SQLAlchemy` and `Pydantic`) to implement ORM and define DB models. 

#### Dependency Injection, Services, DAO, and Validators

- **Dependency Injection for DRY Principle**: Dependency injection is employed throughout the system to adhere to the DRY (Don't Repeat Yourself) principle. By injecting dependencies rather than hardcoding them within components, we ensure that functionality is reused efficiently across the application. 
- **Services**: Within the router modules, service classes are injected to encapsulate business logic. These services abstract away the implementation details and provide a clear interface for handling various operations. 
- **DAO**: DAO classes are responsible for database operations and are directly utilized by the services. This separation of concerns ensures a clean and modular architecture, allowing for easier maintenance and scalability. 
- Validation: Take advantage of `Pydantic` library to define the schema and implement custom validation. (e.g. resource validation)

#### Missing Points

- Due to time constraint, I didn't write tests for models, services, daos, and routers. 
- I only implemented essential APIs for task management. But we can build more such as getting all tasks, deleting task, rerun task, stop task, etc. If you give more timeframe, I am happy to implement that. 

### 2. Task Executor

This include the python script to read the code string from enviornment and run that code. 
We build this docker image and use it in backend code in creating docker container. 

### 3. Code Quality and Formatting 

- Setup `pre-commit` for formatting and linting commiting code. 

### 4. Package Management 

Used `Poetry` for package management. 
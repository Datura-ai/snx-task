import os

def main():
    # Read Python code from an environment variable
    code = os.getenv('PYTHON_CODE')
    
    # Execute the Python code
    exec(code)

if __name__ == "__main__":
    main()
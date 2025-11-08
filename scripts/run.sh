#!/bin/bash

cd .. # Navigate to the parent directory
source venv/bin/activate # Activate the virtual environment
gunicorn -b 127.0.0.1:5000 app:app # Run the Flask app using Gunicorn on localhost port 5000
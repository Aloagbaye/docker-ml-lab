# Base image with Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install common ML libraries
RUN pip install --no-cache-dir \
    numpy pandas scikit-learn psycopg2-binary SQLAlchemy jupyterlab

# Expose port for JupyterLab
EXPOSE 8888

# Default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

FROM python:3.11-slim
WORKDIR /app

# Install core ML + tracking libraries
RUN pip install --no-cache-dir \
    numpy pandas scikit-learn mlflow psycopg2-binary matplotlib seaborn jupyterlab

EXPOSE 8888
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]

# MLOps Sentiment Analysis API

A production-ready, containerized machine learning API for sentiment analysis, built with Flask, scikit-learn, and Docker. This project demonstrates best practices in local MLOps, including testing, containerization, and CI/CD.

---

## Features

- **Sentiment Analysis**: Predicts sentiment (positive/negative) from text.
- **REST API**: Flask-based endpoints for health check and prediction.
- **Automated Testing**: Pytest suite for API and model.
- **Containerization**: Dockerfile and docker-compose for reproducible environments.
- **CI/CD**: GitHub Actions for automated testing and Docker image builds.

---

## Project Structure

```
mlops/
├── app/
│   ├── __init__.py
│   ├── model/
│   │   ├── train.py
│   │   └── saved/
│   └── api/
│       └── main.py
├── tests/
│   └── test_api.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
├── README.md
└── info.txt
```

---

## Getting Started (Local Development)

### 1. Clone the Repository

```bash
git clone https://github.com/Sunilk240/mlops.git
cd mlops
```

### 2. Set Up Python Virtual Environment

```bash
# Create virtual environment (using uv or python -m venv)
uv venv
# or
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
# or
pip install -r requirements.txt
```

---

## Model Training

Before running the API, train the sentiment analysis model:

```bash
python app/model/train.py
```

This will generate `model.joblib` and `vectorizer.joblib` in `app/model/saved/`.

---

## Running the API Locally

```bash
python app/api/main.py
```

- The API will be available at: `http://localhost:5000`

### Endpoints

- **Health Check:**  
  `GET /health`  
  Response: `{"status": "healthy"}`

- **Version:**  
  `GET /version`  
  Response: `{"version": "1.0.0"}`

- **Prediction:**  
  `POST /predict`  
  Body: `{"text": "Your text here"}`  
  Response:  
  ```json
  {
    "prediction": 1,
    "sentiment": "positive",
    "confidence": 0.95
  }
  ```

---

## Testing

Run the test suite with:

```bash
pytest tests/
```

---

## Docker Usage

### Build and Run with Docker Compose

```bash
# Build and start the container
docker-compose up --build

# Or run in detached mode (background)
docker-compose up -d --build

# To stop the container
docker-compose down

# To view logs
docker-compose logs -f

# To rebuild and restart
docker-compose up --build
```

- The API will be available at `http://localhost:5000` inside the container.

---

## CI/CD

- Automated tests and Docker builds are run on every push via GitHub Actions.
- Docker images can be pushed to DockerHub (see workflow and secrets setup).

### GitHub Actions Secrets Setup

To enable automated Docker builds and security scanning in CI/CD, you must add the following secrets to your GitHub repository:

1. **DOCKERHUB_USERNAME**  
   Your DockerHub username.

2. **DOCKERHUB_TOKEN**  
   A DockerHub access token (not your password).  
   [Create a token here.](https://hub.docker.com/settings/security)

3. **SNYK_TOKEN** (optional, for security scan)  
   Your Snyk API token.  
   [Find your token here.](https://app.snyk.io/account)

**How to add secrets:**
- Go to your repository on GitHub
- Click on `Settings` > `Secrets and variables` > `Actions`
- Click `New repository secret` and add each secret above

---

## Troubleshooting

- **Model file not found?**  
  Run `python app/model/train.py` before starting the API.
- **Port already in use?**  
  Stop other processes using port 5000 or change the port in `main.py` and `docker-compose.yml`.
- **Docker build fails?**  
  Ensure Docker Desktop is running and you have enough resources.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)

---

## Author

Sunilk240 
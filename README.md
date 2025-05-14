# ML Model API Project

## Local Development Setup

### 1. Python Environment Setup
```bash
# Create virtual environment (already done with uv)
uv venv 

# Activate virtual environment
# On Windows:
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
```

### 2. Project Structure
```
project/
├── app/
│   ├── model/
│   │   ├── train.py
│   │   └── saved/
│   └── api/
│       └── main.py
├── tests/
│   └── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md
```

### 3. Running the Application
```bash
# Train the model
python app/model/train.py

# Run the API
python app/api/main.py
```

### 4. Testing
```bash
pytest tests/
```

## Future Docker Setup

### 1. Build and Run with Docker
```bash
# Build the Docker image
docker build -t ml-api .

# Run the container
docker run -p 5000:5000 ml-api
```

### 2. Test the API
- The API will be available at `http://localhost:5000`
- Use Postman or curl to test endpoints:
  ```bash
  curl http://localhost:5000/health
  curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d '{"text": "This is a great product!"}'
  ```

## API Endpoints

### 1. Health Check
- **URL**: `/health`
- **Method**: GET
- **Response**: `{"status": "healthy"}`

### 2. Predict
- **URL**: `/predict`
- **Method**: POST
- **Body**: `{"text": "your text here"}`
- **Response**: 
  ```json
  {
    "prediction": 1,
    "sentiment": "positive",
    "confidence": 0.95
  }
  ``` 
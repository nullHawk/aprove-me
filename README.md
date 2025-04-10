# Loan Approval Prediction System

This project is a **Loan Approval Prediction System** developed as part of my **University Assignment for MLOps**. It consists of a backend API built with Flask and a frontend interface built with Streamlit.

## Features
- **Frontend**: A user-friendly interface to input loan application details and view predictions.
- **Backend**: A Flask-based API that uses a pre-trained machine learning model to predict loan approval status.



## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the application:
    ```bash
    python app.py
3. Access the frontend at `httpp://localhost:7860`

## Docker Support
Build and run the application using Docker:
```bash
docker build -t loan-approval .
docker run -p 7860:7860 loan-approval
```

## Note
This project is for educational purposes only and is part of my MLOps University Assignment.
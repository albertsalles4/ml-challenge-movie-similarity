# ML Challenge – Deployment Guide

## Docker Compose

You can run the entire application with Docker Compose:

```bash
docker-compose up
```

This will start the following containers:

- FastAPI app (API endpoint) at http://localhost:8000
- Streamlit app (Frontend) at http://localhost:8501

## AWS

### Prerequisites

1. Create an AWS account if you don't have one already.
2. Install the AWS CLI and configure it with your credentials.
3. Install Docker.

### Setup

1. Create an ECR repository in your AWS account.
2. Configure your AWS credentials with the AWS CLI.
3. Build and push the Docker images to your ECR repository:

```bash
docker build -t {AWS_ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{MY_REPOSITORY}:latest .
docker push {AWS_ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{MY_REPOSITORY}:latest
```

### AWS Lambda

1. Create a new Lambda function in your AWS account.
2. Choose `Container Image` as the execution environment.
3. Select the Docker image from your ECR repository.

#### Use Function URL (For testing)

4. Once created, go to the `Configuration` tab and enable a `Function URL`.

#### AWS API Gateway (For production – recommended)

Use an API Gateway to expose your Lambda function.

### AWS EC2

1. Create a new EC2 instance.
2. Choose an Amazon Machine Image (AMI) that has Docker installed.
3. Launch the instance and connect to it using SSH.
4. Pull and Run the Docker image from your ECR repository:

```bash
docker pull {AWS_ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{MY_REPOSITORY}:latest
docker run -p 8000:8000 {AWS_ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{MY_REPOSITORY}:latest
```

4. Otherwise, clone the repository and run the application locally:

```bash
git clone https://github.com/albertsalles4/ml-challenge-movie-similarity.git
cd ml-challenge-movie-similarity
docker compose up
```

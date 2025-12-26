# 🚀 Automated Container Deployment Platform

**AWS ECS (Fargate) · Amazon ECR · Application Load Balancer · GitHub Actions**


## 📌 Project Overview

This project demonstrates a **production-style automated container deployment platform** built on AWS.

A **Dockerized Flask application** is deployed on **Amazon ECS (Fargate)**, exposed through an **Application Load Balancer**, and delivered via a **GitHub Actions CI/CD pipeline**.

The project focuses on **real-world cloud engineering practices**, including secure networking, container orchestration, CI/CD automation, and cost-aware cloud operations.


## 🏗️ Architecture Overview

The platform follows a **standard modern containerized application architecture** commonly used in cloud-native environments.

### 🔁 Request Flow

User
→ Application Load Balancer (Public)
→ Target Group (IP mode)
→ ECS Fargate Service (Private Subnets)
→ Dockerized Flask Application


### Key Characteristics

- The Application Load Balancer is the **only public entry point**
- ECS tasks run in **private subnets**
- Traffic routing is controlled by **health checks**
- Container images are stored securely in **Amazon ECR**


## 🖼️ Architecture Diagram

The diagram below illustrates the **high-level architecture and CI/CD workflow** of the platform.

![Architecture Diagram](assets/architecture.png)


## 🧰 Technology Stack

### ☁️ Cloud Services

- **Amazon ECS (Fargate)** – Serverless container orchestration  
- **Amazon ECR** – Secure Docker image registry  
- **Application Load Balancer** – Layer-7 HTTP traffic routing  
- **Amazon VPC** – Network isolation and security  
- **AWS IAM** – Identity and access management  

### 🔧 DevOps Tools

- **Docker** – Application containerization  
- **GitHub Actions** – CI/CD automation  

### 🐍 Application Stack

- **Python**
- **Flask**


## 🧠 Key Design Decisions

### 🚢 Amazon ECS (Fargate)

- No EC2 instance management
- Fully serverless container execution
- Built-in scalability and isolation

### ⚖️ Application Load Balancer

- Layer-7 (HTTP) routing
- Native ECS integration
- Health-check-based traffic forwarding

### 📦 Amazon ECR

- AWS-native container registry
- Secure image storage
- IAM-based authentication

### 🔁 GitHub Actions

- Git-driven CI/CD automation
- No additional CI infrastructure required
- Seamless AWS integration


## 🔐 Security Implementation

### 🌐 Networking Security

- ECS tasks are **not directly accessible from the internet**
- ALB acts as the **only public endpoint**
- Security groups enforce **least-privilege access**:
  - ALB allows HTTP (80) from the internet
  - ECS allows application traffic **only from the ALB security group**

### 🪪 IAM Security

- ECS **Task Execution Role** is used to pull images from ECR
- No credentials are hard-coded in source code
- AWS credentials for CI/CD are stored securely in **GitHub Secrets**


## 🔄 CI/CD Pipeline

### ⚡ Trigger

- Any push to the `main` branch

### 🛠️ Pipeline Flow

1. Code is pushed to GitHub  
2. GitHub Actions pipeline is triggered  
3. Docker image is built from source  
4. Image is pushed to Amazon ECR  
5. ECS service is redeployed automatically  

### ✅ Result

- Fully automated and repeatable deployments
- Zero manual AWS Console interaction for application deployments


## 🧪 Application Details

- Lightweight Flask web application
- Exposes a single HTTP endpoint
- Listens on port **5000**
- Binds to `0.0.0.0` for container compatibility


## ✅ Deployment Validation

Deployment success was validated using the following checks:

- ECS service running with active tasks
- Target group reporting **healthy targets**
- Application accessible via ALB DNS endpoint
- Docker image successfully stored in Amazon ECR

These checks confirm **end-to-end deployment success**.


## 💸 Cost Management

To prevent unnecessary cloud costs, the following actions were taken after validation:

- ECS service scaled down or deleted
- Application Load Balancer removed
- Unused Elastic IPs released
- NAT Gateway removed when not required

This demonstrates **cost-aware cloud engineering practices**.


## 📊 Project Status

- ✅ Completed and validated  
- ✅ CI/CD automation implemented  
- ✅ Cost optimization applied  


## 🏁 Summary

This project showcases a **production-grade container deployment workflow** using AWS-managed services and GitHub Actions. It emphasizes **security, automation, scalability, and cost control**, reflecting real-world cloud engineering practices.

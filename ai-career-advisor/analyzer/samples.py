"""
Pre-loaded Sample Resumes, Sample Job Descriptions, and Career Interests
for instant 1-click testing and demonstration.
"""

SAMPLE_RESUMES = {
    "junior_fullstack": {
        "title": "Alex Chen – Junior Full-Stack Developer",
        "description": "2 years experience with React, Node.js, Express, JavaScript, and MongoDB.",
        "text": """Alex Chen
San Francisco, CA | alex.chen@email.com | (555) 234-5678
linkedin.com/in/alexchen-dev | github.com/alexchen-code

PROFESSIONAL SUMMARY
Passionate Full-Stack Developer with 2+ years of experience building modern web applications using React, Node.js, Express, and MongoDB. Proven track record of optimizing page load times by 40% and delivering scalable RESTful APIs. Enthusiastic about TypeScript, cloud deployments, and clean UI engineering.

TECHNICAL SKILLS
Languages: JavaScript, TypeScript, Python, HTML5, CSS3, SQL
Frameworks & Libraries: React, Next.js, Node.js, Express.js, Tailwind CSS, Redux, Bootstrap
Databases: MongoDB, PostgreSQL, SQLite
Tools & DevOps: Git, GitHub, Docker, Postman, Jest, Vite, Linux
Concepts: RESTful APIs, Agile/Scrum, Responsive Design, State Management

EXPERIENCE
Frontend Developer Intern | Nova Tech Labs
June 2023 - Present | San Francisco, CA
* Architected and deployed 15+ responsive React components using Tailwind CSS, increasing user engagement by 28%.
* Refactored client-side data fetching using custom React hooks, reducing bundle size by 35% and improving Core Web Vitals.
* Collaborated with backend engineers to integrate RESTful endpoints and secure JWT authentication.
* Implemented unit and integration test suites using Jest and React Testing Library, achieving 82% code coverage.

Junior Web Developer | Apex Digital Solutions
January 2022 - May 2023 | San Jose, CA
* Developed internal dashboard tools using JavaScript, Node.js, and Express, automating weekly customer reporting.
* Optimized MongoDB aggregation pipelines and indexing, decreasing database query response times by 45%.
* Spearheaded migration of legacy CSS codebase to modern responsive Tailwind CSS architecture.

PROJECTS
DevPulse – Developer Portfolio & Project Showcase
* Built full-stack platform using React, Node.js, Express, and MongoDB serving 1,200+ monthly active developers.
* Integrated GitHub API to dynamically render repository statistics, contribution graphs, and tech stack tags.
* Deployed application using Docker containers on a Linux VPS with automated GitHub Actions CI/CD pipeline.

E-Commerce FastCart
* Developed shopping platform with shopping cart state management using Redux Toolkit and Stripe checkout integration.
* Built responsive UI with Tailwind CSS supporting mobile, tablet, and desktop viewports.

EDUCATION
Bachelor of Science in Computer Science | San Jose State University (2019 - 2023)
GPA: 3.7 / 4.0
"""
    },
    "data_science_graduate": {
        "title": "Priya Sharma – Data Science & ML Graduate",
        "description": "Recent graduate with strong Python, Pandas, Scikit-Learn, SQL, and Data Visualization skills.",
        "text": """Priya Sharma
New York, NY | priya.sharma@email.com | (555) 987-6543
linkedin.com/in/priyasharma-ds | github.com/priyasharma-data

PROFESSIONAL SUMMARY
Aspiring Data Scientist with strong foundational background in statistical modeling, machine learning, and exploratory data analysis. Proficient in Python, SQL, Pandas, NumPy, and Scikit-Learn. Passionate about applying predictive analytics and NLP techniques to solve real-world business challenges.

TECHNICAL SKILLS
Languages: Python, SQL, R, Bash
ML & Data Libraries: Scikit-Learn, Pandas, NumPy, SciPy, Matplotlib, Seaborn, PyTorch
Databases & Tools: PostgreSQL, MySQL, Tableau, Jupyter Notebooks, Git, Docker
Concepts: Supervised Learning, Unsupervised Learning, Regression, Classification, Feature Engineering, A/B Testing, Statistics

EXPERIENCE
Machine Learning Intern | DataSphere Analytics
June 2023 - August 2023 | New York, NY
* Developed customer churn prediction model using Python, Scikit-Learn, and XGBoost, achieving 86% ROC-AUC.
* Engineered 18 novel behavioral features from raw transactional logs containing over 250,000 user records.
* Created interactive Tableau dashboards to present model insights and feature importances to executive stakeholders.

DATA SCIENCE PROJECTS
Customer Segmentation & Lifetime Value Engine
* Applied K-Means clustering and RFM (Recency, Frequency, Monetary) analysis on 100k+ retail customer transactions.
* Visualized cluster distributions using PCA and Seaborn, identifying high-value customer personas representing 62% of revenue.

Medical Image Classification using PyTorch
* Trained Convolutional Neural Network (CNN) in PyTorch to classify chest X-ray scans with 91.4% test accuracy.
* Implemented data augmentation pipelines and transfer learning with ResNet-50.

Automated Stock Market Sentiment Analyzer
* Scraped 50,000+ financial news articles and calculated sentiment polarity scores using NLP.
* Correlated sentiment indices against S&P 500 volatility indices with a 0.72 statistical correlation coefficient.

EDUCATION
Master of Science in Data Science | Columbia University (2022 - 2024)
Bachelor of Technology in Information Technology | Delhi Technological University (2018 - 2022)
"""
    },
    "devops_intern": {
        "title": "David Miller – Cloud & DevOps Enthusiast",
        "description": "Background in Linux administration, Docker, AWS fundamentals, CI/CD, and Python scripting.",
        "text": """David Miller
Austin, TX | david.miller@email.com | (555) 345-6789
linkedin.com/in/davidmiller-cloud | github.com/davidmiller-ops

PROFESSIONAL SUMMARY
Cloud & DevOps Engineer with hands-on experience configuring AWS cloud infrastructure, Docker containerization, CI/CD automated deployment pipelines, and Linux server administration. Eager to master Kubernetes orchestration and Infrastructure as Code using Terraform.

TECHNICAL SKILLS
Cloud & Infrastructure: AWS (EC2, S3, RDS, IAM, VPC), Linux, Ubuntu, Nginx
DevOps & CI/CD: Docker, Docker Compose, GitHub Actions, Jenkins, Git, Bash Scripting
Languages: Python, Bash, YAML, SQL
Monitoring & Security: Prometheus, Grafana, SSL/TLS, SSH, OWASP basics

EXPERIENCE
Cloud Operations Intern | CloudScale Systems
May 2023 - December 2023 | Austin, TX
* Automated server provisioning scripts in Bash and Python, reducing staging environment setup time from 4 hours to 15 minutes.
* Built GitHub Actions CI/CD workflows that automatically linted, tested, and containerized Docker images on every pull request.
* Configured Prometheus and Grafana dashboards to monitor CPU, memory, and disk usage across 20+ EC2 instances.

PROJECTS
Multi-Container Microservices Deployment with Docker
* Containerized a 3-tier web application (React frontend, Node.js API, PostgreSQL database) using Docker Compose.
* Configured Nginx reverse proxy with SSL certificate termination and automated load balancing.

Automated AWS Backup & Disaster Recovery Bot
* Engineered a serverless Python AWS Lambda function triggered by CloudWatch events to automate daily EBS snapshot backups.
* Implemented lifecycle policies that automatically pruned backups older than 30 days, saving 25% on AWS storage costs.

EDUCATION
Bachelor of Science in Computer Information Systems | University of Texas at Austin (2020 - 2024)
AWS Certified Cloud Practitioner (2023)
"""
    }
}

SAMPLE_JOB_DESCRIPTIONS = {
    "senior_fullstack": {
        "title": "Full Stack Engineer (React, Node.js, PostgreSQL, Docker, AWS)",
        "company": "ScaleUp Tech",
        "text": """Job Title: Full Stack Engineer
Location: Remote / Hybrid

About the Role:
We are looking for a skilled Full Stack Engineer to join our growing product team. You will be responsible for building robust web applications, crafting intuitive user interfaces, and designing scalable backend APIs.

Key Responsibilities:
- Architect and implement features across our modern React and Node.js stack.
- Design normalized relational database schemas in PostgreSQL and optimize complex queries.
- Build and maintain RESTful and GraphQL APIs with robust authentication and error handling.
- Containerize services using Docker and collaborate with DevOps to deploy onto AWS infrastructure.
- Write unit, integration, and end-to-end tests using Jest to maintain high quality standards.
- Participate in code reviews, sprint planning, and agile team ceremonies.

Requirements & Qualifications:
- 2+ years of professional experience in full-stack web development.
- Strong proficiency in JavaScript, TypeScript, React, and Node.js.
- Solid experience with PostgreSQL or MySQL, including indexing and schema design.
- Familiarity with Redis caching, Docker containerization, and Git version control.
- Knowledge of cloud platforms like AWS (S3, EC2, ECS) or GCP.
- Excellent problem-solving, communication, and team collaboration skills.
"""
    },
    "ai_ml_engineer": {
        "title": "Machine Learning / AI Engineer (Python, PyTorch, LLMs, RAG)",
        "company": "Nexus AI Labs",
        "text": """Job Title: Machine Learning & Generative AI Engineer
Location: San Francisco, CA / Remote

About Nexus AI:
Nexus AI is pioneering enterprise generative intelligence platforms. We are seeking an ML/AI Engineer to build, evaluate, and deploy state-of-the-art machine learning models and LLM agentic systems.

Responsibilities:
- Build and fine-tune machine learning and deep learning models using Python, PyTorch, and Hugging Face.
- Develop Retrieval-Augmented Generation (RAG) pipelines utilizing Vector Databases (Pinecone/ChromaDB).
- Implement production-grade APIs using FastAPI and containerize services with Docker.
- Conduct feature engineering, model evaluation, and A/B testing on multi-million record datasets.
- Implement MLOps best practices for model monitoring, latency optimization, and continuous retraining.

Qualifications:
- Bachelor's or Master's in Computer Science, Data Science, or related quantitative field.
- High proficiency in Python, NumPy, Pandas, Scikit-Learn, and PyTorch.
- Experience with Large Language Models (LLMs), LangChain/LlamaIndex, and Prompt Engineering.
- Hands-on experience with Vector Databases (ChromaDB, Pinecone, or Milvus).
- Strong mathematical foundation in linear algebra, statistics, and optimization.
"""
    },
    "devops_cloud_engineer": {
        "title": "Cloud & DevOps Engineer (AWS, Kubernetes, Terraform, CI/CD)",
        "company": "CloudForge Infrastructure",
        "text": """Job Title: Cloud & DevOps Engineer
Location: Remote

Overview:
CloudForge is looking for an infrastructure engineer passionate about automation, Kubernetes, and cloud reliability. You will design, provision, and maintain resilient cloud infrastructure.

Key Responsibilities:
- Design and provision cloud environments using Infrastructure as Code (Terraform) on AWS.
- Manage and maintain Kubernetes clusters (EKS), configuring Helm charts and Ingress controllers.
- Build reliable CI/CD pipelines in GitHub Actions to automate testing, build, and zero-downtime deployments.
- Implement comprehensive observability using Prometheus, Grafana, and ELK stack.
- Champion security best practices, IAM policy enforcement, and vulnerability assessments.

Required Skills:
- Hands-on experience with AWS cloud services (VPC, EC2, EKS, RDS, S3).
- Deep knowledge of Docker and Kubernetes container orchestration.
- Proficiency with Terraform for Infrastructure as Code.
- Experience with Linux administration and Bash/Python scripting.
- Solid understanding of GitOps, CI/CD, and networking protocols (TCP/IP, DNS, SSL).
"""
    }
}

INTEREST_OPTIONS = [
    "Full-Stack Web Development",
    "Artificial Intelligence & LLMs",
    "Cloud Computing & DevOps",
    "Data Science & Analytics",
    "Backend & Microservices",
    "Frontend & UI/UX Engineering",
    "Cybersecurity & Ethical Hacking",
    "Mobile App Development",
    "Distributed Systems & Database Internals",
    "FinTech & High-Frequency Systems"
]

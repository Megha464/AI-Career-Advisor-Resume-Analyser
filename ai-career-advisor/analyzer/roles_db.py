"""
Comprehensive Database of Career Roles & Industry Taxonomies.
Contains role requirements, salary insights, demand, interview questions, and project templates.
"""

CAREER_ROLES = {
    "full_stack_developer": {
        "title": "Full Stack Developer",
        "category": "Software Engineering",
        "match_keywords": ["react", "node.js", "javascript", "typescript", "full stack", "web development", "api", "sql", "html", "css", "mongodb", "postgresql", "frontend", "backend"],
        "core_skills": ["JavaScript", "TypeScript", "React", "Node.js", "PostgreSQL", "RESTful APIs", "Git", "HTML5", "CSS3"],
        "secondary_skills": ["Docker", "Next.js", "Redis", "Tailwind CSS", "CI/CD", "AWS", "GraphQL", "Jest"],
        "salary_range": {"us": "$85,000 - $140,000", "in": "₹7 - ₹18 LPA"},
        "market_demand": "Very High",
        "demand_score": 95,
        "description": "Designs and builds client-facing user interfaces and scalable server-side systems, handling end-to-end web applications.",
        "why_it_fits": "Requires versatile abilities spanning frontend UI/UX component design and backend RESTful API architecture.",
        "roadmap_phases": [
            {"phase": "1. Modern Frontend & State", "duration": "Weeks 1-3", "topics": ["React 19 / Next.js App Router", "TypeScript typing & generics", "State management (Zustand/Redux)", "Tailwind CSS styling"], "goal": "Build dynamic, responsive web interfaces with clean component architectures."},
            {"phase": "2. Robust Backend & Databases", "duration": "Weeks 4-6", "topics": ["Node.js / Express or FastAPI", "PostgreSQL schema design & Prisma/Drizzle ORM", "JWT authentication & OAuth2", "REST & GraphQL APIs"], "goal": "Develop production-ready APIs with relational data models and secure authentication."},
            {"phase": "3. Caching & Cloud Deployment", "duration": "Weeks 7-9", "topics": ["Redis caching & rate limiting", "Docker containerization", "AWS (S3, EC2/ECS) or Vercel/Render", "CI/CD with GitHub Actions"], "goal": "Containerize full-stack services and deploy automated continuous delivery pipelines."},
            {"phase": "4. System Design & Interview Drills", "duration": "Weeks 10-12", "topics": ["Full-stack system design (URL shortener, E-commerce)", "Web security (OWASP Top 10)", "Frontend performance optimization", "Mock technical interviews"], "goal": "Master end-to-end full stack architecture and ace live coding drills."}
        ],
        "project_templates": [
            {
                "title": "Multi-Tenant SaaS Collaboration Platform",
                "summary": "Full-stack real-time workspace with rich-text docs, team channels, role-based access control, and automated billing.",
                "tech_stack": ["Next.js 14", "TypeScript", "Tailwind CSS", "Node.js", "PostgreSQL", "Prisma", "WebSockets", "Docker"],
                "key_features": ["Real-time collaborative editing using WebSockets", "Role-Based Access Control (RBAC) & OAuth2", "Stripe subscription webhooks integration", "Dockerized deployment pipeline with CI/CD"],
                "resume_bullet": "Architected a full-stack SaaS workspace using Next.js, Node.js, and PostgreSQL, enabling 100+ concurrent users with real-time WebSocket syncing and sub-100ms response times."
            },
            {
                "title": "High-Throughput E-Commerce & Inventory Engine",
                "summary": "Scalable e-commerce store with Redis caching, transactional database locks, and resilient order fulfillment queues.",
                "tech_stack": ["React", "TypeScript", "FastAPI / Node.js", "PostgreSQL", "Redis", "Docker", "Stripe"],
                "key_features": ["Distributed inventory locking to avoid race conditions", "Redis caching reducing database query load by 65%", "Cart state persistence and instant checkout flow", "Full unit and integration test coverage with Jest"],
                "resume_bullet": "Developed an e-commerce platform handling catalog queries with Redis caching, reducing DB load by 65% and implementing robust ACID transaction guarantees for checkout."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "How do you manage client-side state in a complex React application, and when would you choose server state tools like React Query over global state like Redux?",
                "key_points": ["Client state vs Server state distinction", "Caching, deduping, and background refetching", "Bundle size and boilerplate comparison"]
            },
            {
                "category": "System Design",
                "question": "Design a scalable Notification System that delivers push notifications, SMS, and emails with rate limiting and priority queues.",
                "key_points": ["Message broker (Kafka/RabbitMQ/Redis)", "Worker pool and delivery microservices", "Idempotency keys and user preference management"]
            },
            {
                "category": "Behavioral",
                "question": "Describe a scenario where you faced a critical production bug. How did you triage, resolve, and prevent it from recurring?",
                "key_points": ["STAR framework", "Root cause analysis (RCA)", "Telemetry logging, rollback strategy, and post-mortem documentation"]
            }
        ]
    },
    "frontend_engineer": {
        "title": "Frontend Software Engineer",
        "category": "Software Engineering",
        "match_keywords": ["react", "vue", "angular", "javascript", "typescript", "css", "html", "next.js", "frontend", "ui", "ux", "responsive", "web"],
        "core_skills": ["JavaScript", "TypeScript", "React", "Next.js", "HTML5", "CSS3", "Tailwind CSS", "Git"],
        "secondary_skills": ["Redux", "GraphQL", "Jest", "Playwright", "Web Performance", "Accessibility (a11y)", "Vite"],
        "salary_range": {"us": "$80,000 - $135,000", "in": "₹6 - ₹16 LPA"},
        "market_demand": "High",
        "demand_score": 88,
        "description": "Crafts accessible, high-performance, and pixel-perfect interactive web interfaces for modern web applications.",
        "why_it_fits": "Aligns with strong foundations in user interface engineering, web component design, and responsive styling.",
        "roadmap_phases": [
            {"phase": "1. Advanced JS & TypeScript", "duration": "Weeks 1-3", "topics": ["Event loop, closures, prototypes", "TypeScript strict typing, utility types", "Modern DOM APIs & web workers"], "goal": "Deepen core language fluency."},
            {"phase": "2. Modern Framework Patterns", "duration": "Weeks 4-6", "topics": ["React Server Components (RSC)", "Hydration & SSR/SSG/ISR", "State management & custom hooks"], "goal": "Master Next.js and modern React patterns."},
            {"phase": "3. Performance & Testing", "duration": "Weeks 7-9", "topics": ["Core Web Vitals (LCP, CLS, INP)", "Code splitting, lazy loading, bundle analysis", "Unit & E2E testing with Vitest and Playwright"], "goal": "Achieve 95+ Lighthouse scores and bulletproof tests."},
            {"phase": "4. Design Systems & Micro-frontends", "duration": "Weeks 10-12", "topics": ["Building reusable design systems with Storybook", "Accessibility compliance (WCAG 2.1 AA)", "Micro-frontends & Module Federation"], "goal": "Prepare for Senior Frontend engineering expectations."}
        ],
        "project_templates": [
            {
                "title": "Accessible Design System & UI Component Library",
                "summary": "Enterprise-grade design system built with Radix UI primitives, Storybook docs, dark mode, and 100% WCAG accessibility.",
                "tech_stack": ["React", "TypeScript", "Tailwind CSS", "Storybook", "Radix UI", "npm package"],
                "key_features": ["30+ accessible components with keyboard navigation", "Automated visual regression testing", "Published npm package with tree-shaking support", "Interactive documentation with live code playground"],
                "resume_bullet": "Built and open-sourced an accessible React design system with 30+ components, automated visual regression tests, and zero-accessibility violations (WCAG 2.1 AA)."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "Explain how React reconciles the Virtual DOM and what triggers re-renders. How do you identify and eliminate unnecessary renders?",
                "key_points": ["Fiber architecture, diffing algorithm", "React.memo, useMemo, useCallback trade-offs", "React DevTools Profiler"]
            },
            {
                "category": "System Design",
                "question": "Design an infinite scroll image gallery like Pinterest or Unsplash optimized for mobile devices and slow networks.",
                "key_points": ["Virtualization / windowing", "IntersectionObserver API", "Skeleton loaders and progressive image decoding"]
            }
        ]
    },
    "backend_engineer": {
        "title": "Backend / API Engineer",
        "category": "Software Engineering",
        "match_keywords": ["python", "java", "node.js", "golang", "go", "sql", "postgresql", "backend", "api", "microservices", "docker", "redis", "fastapi", "django", "spring boot"],
        "core_skills": ["Python", "Java", "Go", "PostgreSQL", "RESTful APIs", "Docker", "Git", "Linux"],
        "secondary_skills": ["Redis", "Kafka", "Microservices", "Kubernetes", "AWS", "CI/CD", "System Design", "gRPC"],
        "salary_range": {"us": "$90,000 - $150,000", "in": "₹8 - ₹20 LPA"},
        "market_demand": "Very High",
        "demand_score": 93,
        "description": "Constructs reliable, scalable server backends, database architectures, microservices, and high-volume data pipelines.",
        "why_it_fits": "Suits candidates with a passion for logic, data integrity, concurrency, network protocols, and distributed systems.",
        "roadmap_phases": [
            {"phase": "1. Advanced Backend Frameworks & Clean Code", "duration": "Weeks 1-3", "topics": ["FastAPI / Spring Boot / Go Gin", "Dependency injection & domain-driven design", "RESTful standards and OpenAPI specs"], "goal": "Build modular, clean API backends."},
            {"phase": "2. Database Deep-Dive & Indexing", "duration": "Weeks 4-6", "topics": ["PostgreSQL indexing, EXPLAIN ANALYZE, query planning", "Transaction isolation levels & connection pooling", "Redis caching patterns"], "goal": "Optimize relational queries and handle concurrency."},
            {"phase": "3. Asynchronous Messaging & Microservices", "duration": "Weeks 7-9", "topics": ["Message queues (RabbitMQ / Apache Kafka)", "Background jobs (Celery / BullMQ)", "Docker, container networking, and gRPC"], "goal": "Decouple monolithic logic into event-driven services."},
            {"phase": "4. Distributed Systems & Reliability", "duration": "Weeks 10-12", "topics": ["Distributed locking, idempotency, circuit breakers", "Observability (Prometheus, Grafana, OpenTelemetry)", "System design interviews"], "goal": "Design resilient systems handling millions of requests."}
        ],
        "project_templates": [
            {
                "title": "High-Volume Distributed URL Shortener & Analytics API",
                "summary": "Distributed service handling millions of redirects with Redis Bloom filters, Kafka clickstream analytics, and PostgreSQL storage.",
                "tech_stack": ["Go / Python FastAPI", "PostgreSQL", "Redis", "Kafka", "Docker", "Prometheus"],
                "key_features": ["Base62 encoding with distributed unique ID generation", "Redis Bloom filter to eliminate DB lookups for non-existent links", "Asynchronous Kafka analytics pipeline for click tracking", "Stress tested up to 10,000 RPS using k6"],
                "resume_bullet": "Engineered an ultra-fast URL shortening engine supporting 10,000+ requests/sec using Redis Bloom filters and Kafka asynchronous event streaming."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "How do database indexes work internally (B-Trees vs Hash indexes), and what are the trade-offs of adding multiple indexes to a table?",
                "key_points": ["B-Tree range searches vs Hash exact match", "Write overhead during INSERT/UPDATE/DELETE", "Clustered vs non-clustered indexes"]
            },
            {
                "category": "System Design",
                "question": "Design a Distributed Rate Limiter that can operate across multiple server instances in a distributed cluster.",
                "key_points": ["Token Bucket / Leaky Bucket / Sliding Window Log", "Centralized Redis store with Lua scripts", "Local in-memory cache fallback during partition"]
            }
        ]
    },
    "ai_ml_engineer": {
        "title": "Machine Learning / AI Engineer",
        "category": "Artificial Intelligence & Data",
        "match_keywords": ["python", "machine learning", "deep learning", "pytorch", "tensorflow", "llm", "nlp", "ai", "pandas", "numpy", "scikit-learn", "generative ai", "langchain", "rag"],
        "core_skills": ["Python", "Machine Learning", "Deep Learning", "PyTorch", "Scikit-Learn", "Pandas", "NumPy", "Git"],
        "secondary_skills": ["Large Language Models (LLMs)", "Generative AI", "RAG", "LangChain", "Vector DB", "Docker", "MLOps", "FastAPI"],
        "salary_range": {"us": "$105,000 - $175,000", "in": "₹10 - ₹25 LPA"},
        "market_demand": "Extremely High",
        "demand_score": 98,
        "description": "Develops machine learning models, neural networks, and generative AI systems, moving algorithms into production.",
        "why_it_fits": "Leverages Python computational prowess, mathematical intuition, and passion for artificial intelligence & LLMs.",
        "roadmap_phases": [
            {"phase": "1. ML Foundations & Data Prep", "duration": "Weeks 1-3", "topics": ["Pandas/NumPy vectorization", "Feature engineering & imputation", "Supervised/unsupervised algorithms with Scikit-Learn", "Model evaluation metrics (ROC-AUC, F1, PR curves)"], "goal": "Build a solid baseline in tabular ML workflows."},
            {"phase": "2. Deep Learning & Computer Vision / NLP", "duration": "Weeks 4-6", "topics": ["PyTorch tensors, autograd, and training loops", "CNNs & Transformers architecture", "Hugging Face transformers fine-tuning"], "goal": "Train and fine-tune modern neural networks."},
            {"phase": "3. Generative AI & RAG Architectures", "duration": "Weeks 7-9", "topics": ["LLMs, Prompt Engineering, Structured Outputs", "RAG with Vector DBs (Chroma/Pinecone)", "LangChain / LlamaIndex agentic workflows"], "goal": "Create enterprise-grade RAG applications with real knowledge grounding."},
            {"phase": "4. MLOps & Production Serving", "duration": "Weeks 10-12", "topics": ["Model quantization (GGUF/AWQ)", "Serving via vLLM / FastAPI", "Docker containerization & latency monitoring", "ML system design"], "goal": "Deploy and monitor ML models with low latency."}
        ],
        "project_templates": [
            {
                "title": "Enterprise RAG Intelligence System with Hybrid Search",
                "summary": "Full Retrieval-Augmented Generation engine querying 10,000+ technical PDF documents with hybrid dense/sparse search and hallucination guardrails.",
                "tech_stack": ["Python", "FastAPI", "LangChain", "PyTorch", "ChromaDB / Pinecone", "Streamlit / React", "Docker"],
                "key_features": ["Hybrid BM25 + dense embedding vector search", "Re-ranking pipeline using cross-encoders", "Source citation with page-level confidence scores", "Evaluated against Ragas framework for faithfulness"],
                "resume_bullet": "Developed an enterprise RAG knowledge engine supporting hybrid vector search over 10k documents, improving retrieval precision by 38% and reducing hallucination to under 2%."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "How does the Self-Attention mechanism in the Transformer architecture work, and what is the computational complexity relative to sequence length?",
                "key_points": ["Query, Key, Value matrices", "Softmax(QK^T / sqrt(d_k)) * V", "O(N^2) complexity and FlashAttention optimizations"]
            },
            {
                "category": "System Design",
                "question": "Design a real-time recommendation feed for a video streaming platform that serves personalized recommendations within 50ms.",
                "key_points": ["Two-stage architecture: Candidate generation (retrieval) + Heavy ranking", "Feature store and vector embeddings", "A/B testing and caching frequently viewed items"]
            }
        ]
    },
    "cloud_devops_engineer": {
        "title": "Cloud & DevOps Engineer",
        "category": "Infrastructure & Cloud",
        "match_keywords": ["aws", "azure", "docker", "kubernetes", "terraform", "ci/cd", "devops", "linux", "jenkins", "ansible", "cloud", "bash", "prometheus"],
        "core_skills": ["AWS", "Docker", "Kubernetes", "Linux", "Terraform", "CI/CD", "GitHub Actions", "Bash"],
        "secondary_skills": ["Python", "Ansible", "Helm", "Prometheus", "Grafana", "Nginx", "Cybersecurity", "ArgoCD"],
        "salary_range": {"us": "$95,000 - $160,000", "in": "₹8 - ₹22 LPA"},
        "market_demand": "Very High",
        "demand_score": 94,
        "description": "Automates cloud infrastructure, manages container orchestration, and builds continuous integration and continuous deployment pipelines.",
        "why_it_fits": "Fits individuals interested in automation, cloud architectures, infrastructure as code, and system reliability.",
        "roadmap_phases": [
            {"phase": "1. Linux Internals & Containerization", "duration": "Weeks 1-3", "topics": ["Linux system administration, processes, networking", "Docker multi-stage builds & image optimization", "Docker Compose microservices orchestration"], "goal": "Master foundational Linux OS and container patterns."},
            {"phase": "2. Infrastructure as Code (IaC) & AWS", "duration": "Weeks 4-6", "topics": ["AWS VPC, EC2, IAM, S3, RDS, ALB", "Terraform state management & modular IaC", "Automated provisioning of multi-tier cloud environments"], "goal": "Provision reproducible cloud infrastructure via code."},
            {"phase": "3. Kubernetes & GitOps", "duration": "Weeks 7-9", "topics": ["K8s Pods, Deployments, Services, Ingress", "Helm charts for package management", "ArgoCD / Flux for GitOps automated rollouts"], "goal": "Deploy and manage resilient distributed clusters."},
            {"phase": "4. Observability & SRE Principles", "duration": "Weeks 10-12", "topics": ["Prometheus metrics collection & PromQL", "Grafana dashboards and alerting rules", "Disaster recovery, SLIs/SLOs/SLAs, and chaos engineering"], "goal": "Attain production monitoring excellence."}
        ],
        "project_templates": [
            {
                "title": "Zero-Downtime Multi-Region Kubernetes & GitOps Platform",
                "summary": "Production-grade automated GitOps deployment pipeline with Terraform AWS provisioning, Helm charts, and automated canary rollouts.",
                "tech_stack": ["Terraform", "AWS (EKS)", "Kubernetes", "Helm", "ArgoCD", "GitHub Actions", "Prometheus"],
                "key_features": ["100% Infrastructure as Code with modular Terraform", "Automated canary deployments with automated rollback triggers", "Prometheus & Grafana alerting with Slack notifications", "Secret management via HashiCorp Vault or AWS Secrets Manager"],
                "resume_bullet": "Automated multi-tier AWS infrastructure using Terraform and deployed an EKS GitOps pipeline with ArgoCD, cutting deployment lead times from hours to under 4 minutes."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "What is the difference between a Kubernetes Pod, Service, and Ingress? How does traffic flow from the internet to a specific container?",
                "key_points": ["Ingress controller routing rules", "ClusterIP / NodePort / LoadBalancer service types", "Kube-proxy and iptables/IPVS packet routing"]
            },
            {
                "category": "System Design",
                "question": "How would you design a highly available, disaster-resilient cloud architecture across two geographical cloud regions?",
                "key_points": ["Multi-region DNS routing (Route 53 latency/failover)", "Active-Active vs Active-Passive database replication", "State management, backups, and RTO/RPO objectives"]
            }
        ]
    },
    "data_scientist": {
        "title": "Data Scientist / Analytics Specialist",
        "category": "Artificial Intelligence & Data",
        "match_keywords": ["python", "sql", "data science", "statistics", "pandas", "machine learning", "tableau", "power bi", "analytics", "r", "data visualization", "a/b testing"],
        "core_skills": ["Python", "SQL", "Pandas", "NumPy", "Scikit-Learn", "Data Visualization", "Statistics"],
        "secondary_skills": ["Tableau", "Power BI", "A/B Testing", "Feature Engineering", "Data Modeling", "BigQuery", "Git"],
        "salary_range": {"us": "$90,000 - $155,000", "in": "₹7 - ₹20 LPA"},
        "market_demand": "High",
        "demand_score": 89,
        "description": "Extracts actionable strategic insights and predictive intelligence from complex datasets using statistical modeling and machine learning.",
        "why_it_fits": "Capitalizes on analytical thinking, exploratory data analysis, business metric translation, and storytelling through data.",
        "roadmap_phases": [
            {"phase": "1. Advanced SQL & Exploratory Analysis", "duration": "Weeks 1-3", "topics": ["Window functions, CTEs, self-joins", "Statistical distributions, hypothesis testing", "Data cleaning & outlier detection in Pandas"], "goal": "Gain mastery in data extraction and statistical validation."},
            {"phase": "2. Predictive Modeling & Classification", "duration": "Weeks 4-6", "topics": ["Linear & Logistic Regression, Decision Trees", "Ensemble methods (Random Forest, XGBoost, LightGBM)", "Hyperparameter tuning with Optuna"], "goal": "Build robust predictive models with proper cross-validation."},
            {"phase": "3. Business Analytics & Dashboards", "duration": "Weeks 7-9", "topics": ["A/B test experimental design and sample size calculation", "Interactive dashboards in Tableau or Power BI", "Cohort analysis and customer lifetime value (LTV) modeling"], "goal": "Connect raw models to tangible revenue and operational metrics."},
            {"phase": "4. Model Deployment & Storytelling", "duration": "Weeks 10-12", "topics": ["Streamlit / Gradio web deployment", "Executive presentations and stakeholder communications", "Portfolio case studies"], "goal": "Present high-impact findings to executive leaders."}
        ],
        "project_templates": [
            {
                "title": "Customer Churn Prediction & Revenue Retention Dashboard",
                "summary": "End-to-end ML classification model predicting user churn risk with SHAP explainability and an interactive executive dashboard.",
                "tech_stack": ["Python", "Scikit-Learn", "XGBoost", "SHAP", "Streamlit", "PostgreSQL"],
                "key_features": ["Engineered 25+ behavioral engagement features from transactional data", "XGBoost classifier reaching 89% ROC-AUC", "SHAP values explaining individual churn drivers to account managers", "Actionable retention simulation dashboard"],
                "resume_bullet": "Developed an XGBoost customer churn model with 89% ROC-AUC and SHAP explainability, identifying high-risk enterprise accounts representing $1.2M in annual recurring revenue."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "How do you handle severe class imbalance in a classification problem (e.g., fraud detection with 0.1% positive rate)?",
                "key_points": ["Evaluation metrics: PR curves / F1 over Accuracy", "Resampling: SMOTE, undersampling", "Class weights and threshold tuning"]
            }
        ]
    },
    "data_engineer": {
        "title": "Data Engineer",
        "category": "Artificial Intelligence & Data",
        "match_keywords": ["python", "sql", "spark", "airflow", "kafka", "etl", "data pipelines", "data warehousing", "snowflake", "bigquery", "dbt", "data engineering"],
        "core_skills": ["Python", "SQL", "Data Pipelines", "ETL", "PostgreSQL", "Data Warehousing", "Git"],
        "secondary_skills": ["Apache Spark", "Airflow", "Kafka", "Snowflake", "BigQuery", "dbt", "Docker", "AWS"],
        "salary_range": {"us": "$95,000 - $160,000", "in": "₹8 - ₹22 LPA"},
        "market_demand": "Very High",
        "demand_score": 92,
        "description": "Constructs scalable data pipelines, automated ETL workflows, and centralized data warehouse architectures.",
        "why_it_fits": "Suits candidates strong in database systems, distributed compute engines, and foundational pipeline automation.",
        "roadmap_phases": [
            {"phase": "1. Advanced SQL & Data Modeling", "duration": "Weeks 1-3", "topics": ["Dimensional modeling (Star & Snowflake schemas)", "Slowly Changing Dimensions (SCD Type 1 & 2)", "Analytical SQL performance tuning"], "goal": "Design performant warehouse schemas."},
            {"phase": "2. Orchestration & Modern Data Stack", "duration": "Weeks 4-6", "topics": ["Apache Airflow DAGs & task scheduling", "dbt transformations and automated data testing", "Cloud warehouses (Snowflake or BigQuery)"], "goal": "Automate reliable batch ETL workflows."},
            {"phase": "3. Distributed Processing with Spark", "duration": "Weeks 7-9", "topics": ["PySpark DataFrames & transformations", "Partitioning, shuffling, and memory tuning", "Delta Lake / Parquet columnar storage"], "goal": "Process multi-gigabyte datasets with distributed compute."},
            {"phase": "4. Real-Time Streaming & Observability", "duration": "Weeks 10-12", "topics": ["Apache Kafka streaming", "Data quality frameworks (Great Expectations)", "Pipeline monitoring and alerting"], "goal": "Build near-real-time streaming pipelines."}
        ],
        "project_templates": [
            {
                "title": "Automated Batch & Streaming Crypto Market Data Pipeline",
                "summary": "Real-time streaming pipeline ingesting live crypto market ticks into Kafka, processed via Spark, and transformed in Snowflake using dbt.",
                "tech_stack": ["Python", "Apache Kafka", "Apache Spark", "Snowflake", "dbt", "Airflow", "Docker"],
                "key_features": ["Ingests 5,000+ real-time tick events/sec via WebSockets", "Structured streaming transformations and aggregation in Spark", "Automated hourly dbt data quality checks with Great Expectations", "Modular Airflow DAG orchestration"],
                "resume_bullet": "Built an automated end-to-end data pipeline processing 5,000+ events/sec using Kafka, Spark, and Snowflake, reducing downstream reporting latency from 24 hours to 5 minutes."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "What is the difference between Star Schema and Snowflake Schema, and which would you choose for an analytical data warehouse?",
                "key_points": ["Denormalization vs Normalization trade-offs", "Query performance vs storage efficiency", "Dim vs Fact table joins in OLAP systems"]
            }
        ]
    },
    "cybersecurity_analyst": {
        "title": "Cybersecurity Analyst / Engineer",
        "category": "Security & Infrastructure",
        "match_keywords": ["cybersecurity", "security", "network security", "penetration testing", "vulnerability", "firewall", "soc", "owasp", "encryption", "siem"],
        "core_skills": ["Cybersecurity", "Network Security", "Linux", "Authentication", "OWASP", "Vulnerability Assessment"],
        "secondary_skills": ["Python", "Bash", "Penetration Testing", "Cryptography", "OAuth2", "Cloud Security", "Docker"],
        "salary_range": {"us": "$85,000 - $145,000", "in": "₹7 - ₹18 LPA"},
        "market_demand": "Very High",
        "demand_score": 91,
        "description": "Protects systems, networks, and applications against vulnerabilities, malicious intrusions, and unauthorized breaches.",
        "why_it_fits": "Appeals to analytical problem solvers focused on security compliance, ethical hacking, and threat mitigation.",
        "roadmap_phases": [
            {"phase": "1. Networking & Linux Security", "duration": "Weeks 1-3", "topics": ["TCP/IP, Wireshark packet analysis, DNS", "Linux hardening, user permissions, iptables", "Identity & Access Management (IAM)"], "goal": "Build robust network security foundations."},
            {"phase": "2. Application Security (AppSec)", "duration": "Weeks 4-6", "topics": ["OWASP Top 10 vulnerabilities (SQLi, XSS, SSRF)", "Secure authentication (JWT, OAuth2, MFA)", "Static and Dynamic application security testing (SAST/DAST)"], "goal": "Identify and remediate web vulnerabilities."},
            {"phase": "3. Threat Detection & SIEM", "duration": "Weeks 7-9", "topics": ["Log analysis with Splunk / ELK stack", "Snort / Suricata IDS/IPS configuration", "Incident response playbooks"], "goal": "Monitor and respond to real-time security events."},
            {"phase": "4. Cloud Security & Compliance", "duration": "Weeks 10-12", "topics": ["AWS/Azure security benchmarks", "CIS controls & SOC 2 compliance", "Security audit preparation"], "goal": "Achieve enterprise security readiness."}
        ],
        "project_templates": [
            {
                "title": "Automated Vulnerability Scanner & OWASP Auditor",
                "summary": "CLI and web tool that scans target web applications for common OWASP Top 10 vulnerabilities and exports comprehensive remediation reports.",
                "tech_stack": ["Python", "FastAPI", "Docker", "OWASP ZAP API", "Nmap", "PostgreSQL"],
                "key_features": ["Automated port scanning and SSL cipher verification", "Crawling and vulnerability detection for SQLi and XSS", "CVSS scoring and actionable remediation steps in markdown/PDF", "Scheduled automated CI/CD pipeline security gates"],
                "resume_bullet": "Developed an automated vulnerability scanner integrating OWASP ZAP and Nmap, identifying 15+ high-risk security flaws across staging environments."
            }
        ],
        "interview_questions": [
            {
                "category": "Technical",
                "question": "How does Cross-Site Scripting (XSS) work, what are the differences between Stored, Reflected, and DOM-based XSS, and how do you protect against them?",
                "key_points": ["Content Security Policy (CSP)", "Input sanitization and output encoding", "HttpOnly and SameSite cookie flags"]
            }
        ]
    }
}

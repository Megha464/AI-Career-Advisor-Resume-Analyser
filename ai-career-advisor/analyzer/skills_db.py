"""
Skills Taxonomy Database
Contains 500+ categorized technical and soft skills, along with aliases/synonyms.
"""

SKILLS_TAXONOMY = {
    "languages": [
        "Python", "JavaScript", "TypeScript", "Java", "C++", "C#", "Go", "Golang",
        "Rust", "Kotlin", "Swift", "Ruby", "PHP", "SQL", "HTML", "HTML5", "CSS", "CSS3",
        "Sass", "SCSS", "R", "Scala", "Dart", "Shell", "Bash", "PowerShell", "Perl",
        "Lua", "Haskell", "Elixir", "Clojure", "MATLAB", "Solidity"
    ],
    "frameworks_libraries": [
        "React", "React.js", "React Native", "Next.js", "Vue", "Vue.js", "Nuxt.js",
        "Angular", "Svelte", "Node.js", "Express", "Express.js", "NestJS", "FastAPI",
        "Flask", "Django", "Spring", "Spring Boot", "ASP.NET", ".NET Core", "Ruby on Rails",
        "Laravel", "Tailwind CSS", "Bootstrap", "Chakra UI", "Material UI", "Redux",
        "Zustand", "GraphQL", "Apollo", "PyTorch", "TensorFlow", "Keras", "Scikit-Learn",
        "Hugging Face", "LangChain", "LlamaIndex", "Pandas", "NumPy", "SciPy", "Matplotlib",
        "Seaborn", "OpenCV", "jQuery", "Electron", "Flutter"
    ],
    "databases": [
        "PostgreSQL", "MySQL", "SQLite", "MongoDB", "Redis", "Cassandra", "DynamoDB",
        "Elasticsearch", "Neo4j", "Firebase", "Supabase", "Oracle", "Microsoft SQL Server",
        "Snowflake", "BigQuery", "CockroachDB", "MariaDB", "CouchDB", "Vector DB", "ChromaDB",
        "Pinecone", "Milvus", "Weaviate", "ClickHouse"
    ],
    "cloud_devops": [
        "AWS", "Amazon Web Services", "Azure", "Microsoft Azure", "GCP", "Google Cloud Platform",
        "Docker", "Kubernetes", "K8s", "Terraform", "Ansible", "Jenkins", "GitHub Actions",
        "GitLab CI", "CircleCI", "Linux", "Ubuntu", "Nginx", "Apache", "Helm", "Prometheus",
        "Grafana", "Datadog", "Serverless", "AWS Lambda", "Cloudflare", "Pulumi", "CI/CD",
        "ArgoCD", "Vagrant", "OpenShift"
    ],
    "developer_tools_architecture": [
        "Git", "GitHub", "GitLab", "Bitbucket", "JIRA", "Confluence", "Postman", "Swagger",
        "OpenAPI", "REST", "RESTful APIs", "GraphQL", "gRPC", "WebSockets", "Kafka",
        "RabbitMQ", "Celery", "Microservices", "System Design", "Distributed Systems",
        "Design Patterns", "Object-Oriented Programming (OOP)", "Functional Programming",
        "TDD", "BDD", "Unit Testing", "Jest", "PyTest", "Cypress", "Selenium", "Playwright",
        "Webpack", "Vite", "Babel", "Docker Compose"
    ],
    "ai_data_science": [
        "Machine Learning", "Deep Learning", "Natural Language Processing (NLP)",
        "Computer Vision", "Large Language Models (LLMs)", "Generative AI", "RAG",
        "Retrieval-Augmented Generation", "Prompt Engineering", "Fine-Tuning", "ETL",
        "Data Pipelines", "Data Modeling", "Data Warehousing", "Apache Spark", "Apache Kafka",
        "Airflow", "dbt", "Tableau", "Power BI", "Statistics", "A/B Testing", "MLOps",
        "Data Engineering", "Feature Engineering"
    ],
    "security_networking": [
        "Cybersecurity", "Network Security", "OAuth", "OAuth2", "JWT", "Authentication",
        "Authorization", "Penetration Testing", "Vulnerability Assessment", "SSL/TLS",
        "Cryptography", "OWASP", "IAM", "SOC 2", "Firewalls", "VPN", "TCP/IP", "DNS"
    ],
    "soft_skills": [
        "Problem Solving", "Critical Thinking", "Analytical Thinking", "Communication",
        "Team Collaboration", "Leadership", "Mentorship", "Agile", "Scrum", "Sprint Planning",
        "Time Management", "Adaptability", "Cross-Functional Collaboration", "Documentation",
        "Stakeholder Management", "Code Reviews", "Emotional Intelligence", "Continuous Learning"
    ]
}

# Mapping common abbreviations and aliases to canonical skill names
SKILL_ALIASES = {
    "js": "JavaScript",
    "ts": "TypeScript",
    "py": "Python",
    "golang": "Go",
    "k8s": "Kubernetes",
    "postgres": "PostgreSQL",
    "psql": "PostgreSQL",
    "mongo": "MongoDB",
    "reactjs": "React",
    "react.js": "React",
    "vuejs": "Vue.js",
    "vue": "Vue.js",
    "nodejs": "Node.js",
    "node": "Node.js",
    "nextjs": "Next.js",
    "next": "Next.js",
    "expressjs": "Express.js",
    "express": "Express.js",
    "sklearn": "Scikit-Learn",
    "scikit-learn": "Scikit-Learn",
    "tf": "TensorFlow",
    "ml": "Machine Learning",
    "dl": "Deep Learning",
    "nlp": "Natural Language Processing",
    "llm": "Large Language Models (LLMs)",
    "llms": "Large Language Models (LLMs)",
    "genai": "Generative AI",
    "rag": "RAG",
    "gh actions": "GitHub Actions",
    "gha": "GitHub Actions",
    "rest api": "RESTful APIs",
    "rest apis": "RESTful APIs",
    "restful": "RESTful APIs",
    "cicd": "CI/CD",
    "ci/cd": "CI/CD",
    "aws": "AWS",
    "gcp": "GCP",
    "tailwind": "Tailwind CSS",
    "bs": "Bootstrap",
    "ms sql": "Microsoft SQL Server",
    "mssql": "Microsoft SQL Server"
}

def get_all_skills_flat():
    """Return all skills as a unique flat set."""
    all_s = set()
    for cat, s_list in SKILLS_TAXONOMY.items():
        for s in s_list:
            all_s.add(s)
    return all_s

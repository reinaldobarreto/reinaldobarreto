<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="440" alt="Python (official logo)" />
</div>

<h1 align="center">Reinaldo Barreto</h1>

<p align="center">
  <strong>Python Backend Engineer | Automation &amp; Data Analytics</strong>
</p>

<p align="center">
  Backend Engineer focused on REST APIs, automation workflows, data processing, SQL optimization,
  ETL pipelines and scalable systems built with clean architecture principles.
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=23&pause=1000&color=4C8CCB&center=true&vCenter=true&width=980&lines=Python+Backend+Engineer;FastAPI+%7C+Django+%7C+SQL+%7C+Automation;ETL%2C+Data+Analysis+and+Scalable+APIs;Business+Automation+for+real+operations;Python-powered+systems+ready+for+production" alt="Animated professional headline" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Backend_Engineer-3776AB?style=for-the-badge&logo=python&logoColor=FFD343" alt="Python Backend Engineer" />
  <img src="https://img.shields.io/badge/FastAPI-Production_APIs-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Django-Scalable_Backend-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/SQL-Analytics_%26_Optimization-D9AC13?style=for-the-badge&logo=postgresql&logoColor=0D1117" alt="SQL and Analytics" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Automation-Business_Process_Engineering-1D9E7A?style=flat-square" alt="Business process automation" />
  <img src="https://img.shields.io/badge/Data-Analysis_%26_Statistics-4C8CCB?style=flat-square" alt="Data analysis and statistics" />
  <img src="https://img.shields.io/badge/Architecture-Clean_%7C_DDD_%7C_SOLID-1A365D?style=flat-square" alt="Software architecture" />
  <img src="https://img.shields.io/badge/Focus-Scalable_Backend_Systems-FFD343?style=flat-square&logoColor=0D1117" alt="Scalable backend systems" />
</p>

<table>
  <tr>
    <td width="66%" valign="top">
      <h2>Building scalable Python solutions</h2>
      <p>
        I design and deliver Python-powered backend systems for production environments, combining
        API engineering, automation, analytics and database design to solve real business workflows.
        My current focus is building robust services with FastAPI, Django, SQLAlchemy, queues,
        ETL pipelines, data processing jobs and SQL-first architectures that are maintainable,
        observable and ready to scale.
      </p>
      <p>
        I also use Python to automate office and enterprise operations such as spreadsheet processing,
        PDF extraction, reporting, file conversion, system integrations, scheduled jobs, internal bots
        and repetitive task automation. JavaScript and TypeScript remain part of my toolkit, but now
        as a complementary stack around a Python backend core.
      </p>
    </td>
    <td width="34%" align="center" valign="top">
      <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="260" alt="Python (official logo)" />
    </td>
  </tr>
</table>

## `whoami.py`

```python
from typing import Iterable


PRIMARY_STACK = (
    "Python",
    "FastAPI",
    "Django",
    "SQL",
    "Automation",
    "Data Analysis",
)

DATA_TOOLKIT = ["Pandas", "NumPy", "Polars", "Jupyter", "DuckDB"]
BACKEND_TOOLKIT = ["DRF", "SQLAlchemy", "Pydantic", "Celery", "Redis"]
COMPLEMENTARY_STACK = ["Node.js", "NestJS", "Next.js", "React", "TypeScript"]

ZEN_OF_PYTHON = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Readability counts.",
    "Now is better than never.",
]


def build_focus(stack: tuple[str, ...], extras: Iterable[str]) -> dict:
    return {
        "role": "Python Backend Engineer",
        "main_stack": stack,
        "specialties": [
            "REST APIs",
            "ETL Pipelines",
            "Business Automation",
            "SQL Optimization",
            "Scalable Backend Systems",
        ],
        "toolkit": [*stack[1:], *extras],
    }


def choose_style(principles: list[str]) -> str:
    if "Readability counts." in principles and "Simple is better than complex." in principles:
        return "clean, explicit and production-ready"
    return "pragmatic and scalable"


reinaldo = build_focus(PRIMARY_STACK, BACKEND_TOOLKIT + DATA_TOOLKIT)
reinaldo["engineering_style"] = choose_style(ZEN_OF_PYTHON)
reinaldo["also_works_with"] = COMPLEMENTARY_STACK
reinaldo["favorite_python_truths"] = tuple(ZEN_OF_PYTHON[:3])
```

## The Zen of Python

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Complex is better than complicated.  
> Flat is better than nested.  
> Sparse is better than dense.  
> Readability counts.  
> Special cases aren't special enough to break the rules.  
> Although practicality beats purity.  
> Errors should never pass silently.  
> Unless explicitly silenced.  
> In the face of ambiguity, refuse the temptation to guess.  
> There should be one, and preferably only one, obvious way to do it.  
> Although that way may not be obvious at first unless you're Dutch.  
> Now is better than never.  
> Although never is often better than right now.  
> If the implementation is hard to explain, it's a bad idea.  
> If the implementation is easy to explain, it may be a good idea.  
> Namespaces are one honking great idea, let's do more of those!

```ts
type StackFocus = "primary" | "complementary";

type Profile = {
  focus: StackFocus;
  backend: string[];
  web: string[];
  mobile: string[];
  notes: string[];
};

const complementary: Profile = {
  focus: "complementary",
  backend: ["Node.js", "NestJS", "Express"],
  web: ["Next.js", "React", "TypeScript"],
  mobile: ["React Native", "Expo"],
  notes: [
    "JavaScript/TypeScript remain part of my toolkit",
    "Python is my primary stack for backend, automation and data",
  ],
};
```

## Python-powered systems ready for production

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>API Engineering</h3>
      <p>REST APIs, authentication, authorization, validation, service layers, async processing, background jobs and production-ready backend architecture.</p>
    </td>
    <td width="33%" valign="top">
      <h3>Automation</h3>
      <p>Business automation, ETL routines, spreadsheet workflows, PDF extraction, file pipelines, scheduled tasks, bots and system integrations.</p>
    </td>
    <td width="33%" valign="top">
      <h3>Data &amp; SQL</h3>
      <p>Data cleaning, exploratory analysis, descriptive statistics, dashboards, KPI pipelines, query optimization and database design for scalable products.</p>
    </td>
  </tr>
</table>

## Core technologies

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,fastapi,django,flask,postgres,mysql,sqlite,mongodb,redis,docker,linux,git,github,vscode&perline=14" alt="Python stack icons" />
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=nodejs,nestjs,nextjs,react,ts,js,express&perline=7" alt="JavaScript complementary stack icons" />
</p>

<table>
  <tr>
    <td width="170"><strong>Languages</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=FFD343" alt="Python" />
      <img src="https://img.shields.io/badge/SQL-0D1117?style=flat-square&logo=postgresql&logoColor=FFD343" alt="SQL" />
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
      <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=111111" alt="JavaScript" />
      <img src="https://img.shields.io/badge/Bash-121011?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
      <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML" />
      <img src="https://img.shields.io/badge/CSS-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS" />
    </td>
  </tr>
  <tr>
    <td><strong>Backend</strong></td>
    <td>
      <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
      <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white" alt="Django" />
      <img src="https://img.shields.io/badge/DRF-0A0A0A?style=flat-square&logo=django&logoColor=white" alt="Django REST Framework" />
      <img src="https://img.shields.io/badge/Flask-111111?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
      <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square" alt="SQLAlchemy" />
      <img src="https://img.shields.io/badge/Alembic-1A365D?style=flat-square" alt="Alembic" />
      <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square" alt="Pydantic" />
      <img src="https://img.shields.io/badge/Celery-37814A?style=flat-square" alt="Celery" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" alt="Redis" />
      <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=flat-square&logo=rabbitmq&logoColor=white" alt="RabbitMQ" />
      <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square" alt="Gunicorn" />
      <img src="https://img.shields.io/badge/Uvicorn-4051B5?style=flat-square" alt="Uvicorn" />
    </td>
  </tr>
  <tr>
    <td><strong>Databases</strong></td>
    <td>
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
      <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" alt="MySQL" />
      <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white" alt="SQLite" />
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB" />
      <img src="https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white" alt="MariaDB" />
      <img src="https://img.shields.io/badge/SQL_Server-CC2927?style=flat-square" alt="SQL Server" />
      <img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white" alt="Oracle" />
      <img src="https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=111111" alt="Firebase" />
      <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=flat-square&logo=supabase&logoColor=111111" alt="Supabase" />
    </td>
  </tr>
  <tr>
    <td><strong>Data Analysis</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" />
      <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />
      <img src="https://img.shields.io/badge/Polars-1E66F5?style=flat-square" alt="Polars" />
      <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square" alt="Matplotlib" />
      <img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white" alt="Plotly" />
      <img src="https://img.shields.io/badge/Seaborn-253B5E?style=flat-square" alt="Seaborn" />
      <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="Scikit-learn" />
      <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" alt="Jupyter Notebook" />
      <img src="https://img.shields.io/badge/OpenPyXL-1F6B75?style=flat-square" alt="OpenPyXL" />
      <img src="https://img.shields.io/badge/PyArrow-2B7DE9?style=flat-square" alt="PyArrow" />
      <img src="https://img.shields.io/badge/DuckDB-FFF000?style=flat-square" alt="DuckDB" />
    </td>
  </tr>
  <tr>
    <td><strong>Automation</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white" alt="Selenium" />
      <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" alt="Playwright" />
      <img src="https://img.shields.io/badge/BeautifulSoup-355C7D?style=flat-square" alt="BeautifulSoup" />
      <img src="https://img.shields.io/badge/Requests-1A365D?style=flat-square" alt="Requests" />
      <img src="https://img.shields.io/badge/Schedule-0F172A?style=flat-square" alt="Schedule" />
      <img src="https://img.shields.io/badge/AsyncIO-3C3C3C?style=flat-square" alt="AsyncIO" />
      <img src="https://img.shields.io/badge/Cron-243447?style=flat-square" alt="Cron" />
      <img src="https://img.shields.io/badge/ETL_Pipelines-3776AB?style=flat-square" alt="ETL Pipelines" />
      <img src="https://img.shields.io/badge/Task_Automation-1D9E7A?style=flat-square" alt="Task Automation" />
      <img src="https://img.shields.io/badge/Office_Automation-476072?style=flat-square" alt="Office Automation" />
      <img src="https://img.shields.io/badge/File_Processing-4C8CCB?style=flat-square" alt="File Processing" />
      <img src="https://img.shields.io/badge/Excel_Automation-217346?style=flat-square&logo=microsoftexcel&logoColor=white" alt="Excel Automation" />
      <img src="https://img.shields.io/badge/PDF_Automation-B30B00?style=flat-square" alt="PDF Automation" />
      <img src="https://img.shields.io/badge/CSV_Processing-FFD343?style=flat-square" alt="CSV Processing" />
    </td>
  </tr>
  <tr>
    <td><strong>Cloud &amp; Ops</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
      <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=111111" alt="Linux" />
      <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
      <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
      <img src="https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white" alt="Nginx" />
      <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=FF9900" alt="AWS" />
      <img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" alt="Azure" />
      <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Google Cloud" />
      <img src="https://img.shields.io/badge/DigitalOcean-0080FF?style=flat-square&logo=digitalocean&logoColor=white" alt="DigitalOcean" />
      <img src="https://img.shields.io/badge/Render-111111?style=flat-square&logo=render&logoColor=white" alt="Render" />
      <img src="https://img.shields.io/badge/Railway-0B0D0E?style=flat-square&logo=railway&logoColor=white" alt="Railway" />
    </td>
  </tr>
  <tr>
    <td><strong>APIs</strong></td>
    <td>
      <img src="https://img.shields.io/badge/REST_API-1A365D?style=flat-square" alt="REST API" />
      <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT" />
      <img src="https://img.shields.io/badge/OAuth-4285F4?style=flat-square" alt="OAuth" />
      <img src="https://img.shields.io/badge/Swagger-85EA2D?style=flat-square&logo=swagger&logoColor=111111" alt="Swagger" />
      <img src="https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square" alt="OpenAPI" />
      <img src="https://img.shields.io/badge/WebSockets-0D1117?style=flat-square" alt="WebSockets" />
      <img src="https://img.shields.io/badge/GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white" alt="GraphQL" />
    </td>
  </tr>
  <tr>
    <td><strong>Architecture</strong></td>
    <td>
      <img src="https://img.shields.io/badge/Clean_Architecture-1A365D?style=flat-square" alt="Clean Architecture" />
      <img src="https://img.shields.io/badge/DDD-2D3748?style=flat-square" alt="Domain-Driven Design" />
      <img src="https://img.shields.io/badge/SOLID-4A5568?style=flat-square" alt="SOLID" />
      <img src="https://img.shields.io/badge/Repository_Pattern-3776AB?style=flat-square" alt="Repository Pattern" />
      <img src="https://img.shields.io/badge/Service_Layer-244B73?style=flat-square" alt="Service Layer" />
      <img src="https://img.shields.io/badge/Dependency_Injection-0F766E?style=flat-square" alt="Dependency Injection" />
      <img src="https://img.shields.io/badge/Hexagonal_Architecture-1D4ED8?style=flat-square" alt="Hexagonal Architecture" />
      <img src="https://img.shields.io/badge/Microservices-95C11F?style=flat-square" alt="Microservices" />
    </td>
  </tr>
</table>

## Automation for business operations

Python is one of the main ways I turn repetitive workflows into reliable business systems.
I build automation routines that reduce manual effort, improve consistency and connect tools,
files and platforms through clean backend logic.

- Excel spreadsheet automation and multi-file processing
- PDF reading, structured extraction and document generation
- Report generation for operational and management routines
- Data imports, ETL jobs and scheduled synchronization pipelines
- Internal bots, scripts and administrative workflow automation
- API integrations between internal systems and third-party services
- Email dispatch, task orchestration and repetitive job automation
- File conversion, CSV handling and data normalization routines
- Monitoring scripts and automation for office and enterprise processes

## Data analysis & applied statistics

I use Python not only to build backend services, but also to support analytical workflows that
help transform raw operational data into actionable information.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Analytics capabilities</h3>
      <p>Data cleaning, descriptive statistics, exploratory data analysis, KPI tracking, dashboard-ready transformations, SQL analytics and pipeline-oriented modeling.</p>
    </td>
    <td width="50%" valign="top">
      <h3>Tooling</h3>
      <p>Pandas, NumPy, Polars, Plotly, Matplotlib, Seaborn, Jupyter, DuckDB, PyArrow and Scikit-learn for practical analysis and data workflows.</p>
    </td>
  </tr>
</table>

## SQL & database engineering

I work with SQL as an engineering tool for performance, integrity and business visibility.
This includes relational modeling, query optimization and designing schemas that support both
transactional systems and analytical workflows.

<p align="center">
  <img src="https://skillicons.dev/icons?i=postgres,mysql,sqlite,mongodb,redis,firebase,supabase" alt="Database icons" />
</p>

- Complex queries, joins, views and relational modeling
- Indexes, normalization and transactional consistency
- Stored procedures and database-oriented business rules
- Query tuning, performance diagnostics and SQL optimization
- Schema design for scalable backend services and data pipelines

## Also working with JavaScript ecosystem

JavaScript and TypeScript remain part of my professional toolkit for complementary scenarios,
especially when a product benefits from full-stack integration around a Python backend core.

<p align="center">
  <img src="https://img.shields.io/badge/Node.js-5FA04E?style=flat-square&logo=node.js&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white" alt="NestJS" />
  <img src="https://img.shields.io/badge/Next.js-111111?style=flat-square&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=111111" alt="React" />
  <img src="https://img.shields.io/badge/React_Native-61DAFB?style=flat-square&logo=react&logoColor=111111" alt="React Native" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" alt="Express" />
</p>

## Projetos em destaque (simples e diretos)

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>FastAPI CRUD API</h3>
      <p>API REST CRUD com OpenAPI/Swagger, validação com Pydantic e endpoints objetivos.</p>
      <p><a href="./projects/fastapi-crud-api">Abrir template</a></p>
    </td>
    <td width="50%" valign="top">
      <h3>Django + DRF CRUD API</h3>
      <p>API REST CRUD com Model, Serializer, ViewSet e Router (Django REST Framework).</p>
      <p><a href="./projects/django-drf-crud-api">Abrir template</a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Python Data Analysis</h3>
      <p>Análise de dados a partir de CSV com data cleaning, estatística descritiva e KPIs simples.</p>
      <p><a href="./projects/python-data-analysis">Abrir template</a></p>
    </td>
    <td width="50%" valign="top">
      <h3>Next.js Static Front (GitHub Pages)</h3>
      <p>Front estático (Next.js export) para apresentar os projetos, pronto para deploy no GitHub Pages.</p>
      <p><a href="./projects/nextjs-python-portfolio">Abrir template</a></p>
      <p><a href="https://reinaldobarreto.github.io/reinaldobarreto/" target="_blank" rel="noreferrer">Preview (Pages)</a></p>
    </td>
  </tr>
</table>

## GitHub analytics

<div align="center">
  <img src="https://raw.githubusercontent.com/reinaldobarreto/reinaldobarreto/output/metrics.svg" width="100%" alt="GitHub metrics" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=reinaldobarreto&theme=transparent&background=0D1117&ring=FFD343&fire=FFD343&currStreakLabel=4C8CCB&sideLabels=E6EDF3&currStreakNum=E6EDF3&dates=8BA3C1&sideNums=E6EDF3&stroke=244B73&border=244B73" height="180" alt="GitHub streak" />
</div>

<div align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=reinaldobarreto&hide_border=true&bg_color=0D1117&color=E6EDF3&line=4C8CCB&point=FFD343&area=true&area_color=1D9E7A&title_color=4C8CCB" width="100%" alt="Contribution graph" />
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/reinaldobarreto/reinaldobarreto/output/snake.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/reinaldobarreto/reinaldobarreto/output/snake-light.svg" />
  <img src="https://raw.githubusercontent.com/reinaldobarreto/reinaldobarreto/output/snake.svg" width="100%" alt="Animated contribution snake" />
</picture>

## Current engineering priorities

- Building scalable Python backend services for production
- Designing robust REST APIs and automation-heavy systems
- Improving business workflows with Python-based automation
- Working with SQL, analytics and data-oriented backend pipelines
- Applying clean architecture, modular design and maintainable patterns

## Contact

<p align="center">
  <a href="mailto:reinaldodevbarreto@gmail.com">
    <img src="https://img.shields.io/badge/Email-reinaldodevbarreto%40gmail.com-3776AB?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://www.linkedin.com/in/reinaldobarreto/">
    <img src="https://img.shields.io/badge/LinkedIn-Reinaldo_Barreto-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/reinaldobarreto">
    <img src="https://img.shields.io/badge/GitHub-@reinaldobarreto-0D1117?style=for-the-badge&logo=github&logoColor=FFD343" alt="GitHub" />
  </a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=reinaldobarreto&label=PROFILE+VIEWS&color=3776AB&style=for-the-badge" alt="Profile views" />
</p>

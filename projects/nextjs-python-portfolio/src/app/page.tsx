const repoUrl = "https://github.com/reinaldobarreto/reinaldobarreto";

const links = [
  {
    title: "FastAPI CRUD API",
    description: "API REST simples com OpenAPI/Swagger",
    href: `${repoUrl}/tree/main/projects/fastapi-crud-api`
  },
  {
    title: "Django + DRF CRUD API",
    description: "API REST simples com Model/Serializer/ViewSet/Router",
    href: `${repoUrl}/tree/main/projects/django-drf-crud-api`
  },
  {
    title: "Python Data Analysis",
    description: "Análise de dados + estatística descritiva a partir de CSV",
    href: `${repoUrl}/tree/main/projects/python-data-analysis`
  }
];

export default function Page() {
  return (
    <main className="shell">
      <header className="hero">
        <div className="badge">Python Backend · Automation · Data Analytics</div>
        <h1>Python-powered systems, ready for production</h1>
        <p>
          Vitrine simples dos meus templates: APIs (FastAPI e Django/DRF), automação e análise de
          dados com SQL-first mindset.
        </p>
        <div className="ctaRow">
          <a className="cta" href={repoUrl} target="_blank" rel="noreferrer">
            Ver repositório
          </a>
          <a className="cta secondary" href={`${repoUrl}#readme`} target="_blank" rel="noreferrer">
            Ver profile README
          </a>
        </div>
      </header>

      <section className="grid">
        {links.map((item) => (
          <a key={item.title} className="card" href={item.href} target="_blank" rel="noreferrer">
            <div className="cardTitle">{item.title}</div>
            <div className="cardDesc">{item.description}</div>
            <div className="cardHint">Abrir</div>
          </a>
        ))}
      </section>
    </main>
  );
}


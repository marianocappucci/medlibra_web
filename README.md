# MedLibra — Sitio Web / Landing

Landing page de marketing para [MedLibra](https://medlibra.com.ar), turnos y
gestión clínica para consultorios, profesionales y centros médicos. Mismo
patrón que `contalibra_web`/`restolibra_web`/`gestiolibra_web`: HTML estático
servido por nginx en un contenedor Docker.

## Estado actual (scaffold inicial)

- Landing completa: hero, módulos con badges por plan (dominio clínico
  siempre incluido), para quién, cómo funciona, planes y precios, CTA de
  contacto y footer con el resto de la familia Libra.
- **Todavía sin**: documentación técnica gateada por login (`/docs/`, patrón
  de `contalibra_web`), CI/CD (GitHub Actions), y deploy al VPS. Queda para
  una ronda siguiente, una vez validado el contenido de la landing.

## Desarrollo local

```bash
docker compose build
docker compose up -d
```

Sirve en `http://localhost:8084`.

## Estructura

```
public/
  index.html          — Landing completa
  css/style.css        — Estilos (Inter + Bootstrap Icons via CDN)
  img/                  — (vacío por ahora, sin foto de hero propia)
Dockerfile              — FROM nginx:1.27-alpine
nginx.conf              — gzip, try_files, headers de seguridad
docker-compose.yml      — servicio web, red stack_stack-net (VPS Donweb)
```

## Relacionado

- Producto documentado: [MedLibra](https://github.com/marianocappucci/medlibra)
- Mismo patrón: `contalibra_web`, `restolibra_web`, `gestiolibra_web`

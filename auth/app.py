"""Backend de acceso a /docs/ para la landing de MedLibra -- config sobre
libra_web_kit.docs_auth (extraído 2026-07-26, ver
wiki/analyses/auditoria-duplicacion-familia-libra.md)."""
from libra_web_kit.docs_auth import build_docs_login_app, DocsLoginTheme

app = build_docs_login_app(
    product_name="MedLibra",
    apex_domain_default="medlibra.com.ar",
    secret_key_env="DOCS_SESSION_SECRET",
    secret_key_default="medlibra-docs-secret-change-me",
    verify_path="/auth/verify",
    slug_placeholder="tu-consultorio",
    theme=DocsLoginTheme(accent="#0d9488", accent_hover="#0f766e"),
)

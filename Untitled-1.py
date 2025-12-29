import re
USERNAME_RE = re.compile(
    r"^[a-z0-9](?:[a-z0-9._]{0,28}[a-z0-9])?$",
    re.IGNORECASE
)


def parse_lista(lineas):
    """
    Extrae SOLO usernames válidos del texto copiado de Instagram.
    Todo lo demás se ignora.
    """
    personas = []
    seen = set()

    for raw in lineas:
        s = raw.strip()
        if not s:
            continue

        low = s.lower()

        if low.startswith("foto del perfil de"):
            continue
        if s == "·":
            continue

        if not USERNAME_RE.match(low):
            continue

        if low in seen:
            continue

        seen.add(low)
        personas.append({"cuenta": low})

    return personas

# =========================
# PEGÁ ACÁ LAS LISTAS CRUDAS
# =========================

seguidores_raw = """


laverapizza.lp
Somos La Vera Pizza


psychobred
PSYCHOBRED

javigilnavarroespn
Javier Fernando Gil Navarro

fireship_dev
fireship.io


""".strip().splitlines()
seguidos_raw = """


laverapizza.lp
Somos La Vera Pizza


psychobred
PSYCHOBRED

javigilnavarroespn
Javier Fernando Gil Navarro

fireship_dev
fireship.io


""".strip().splitlines()
# =========================
# PARSEO + COMPARACIÓN DEFINITIVA (ANTI FALSOS POSITIVOS)
# =========================

seguidores_set = {p["cuenta"] for p in parse_lista(seguidores_raw)}
seguidos_set   = {p["cuenta"] for p in parse_lista(seguidos_raw)}

no_me_siguen = sorted(seguidos_set - seguidores_set)

print("Personas que seguís y NO te siguen:\n")
for cuenta in no_me_siguen:
    print(f"- @{cuenta}")

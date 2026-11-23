<!-- translated-from: QUICKSTART.en.md sha256:9f8b8e3a6d68 -->
# NAOSO - Inicio rápido

*[English](../../../QUICKSTART.en.md) · [Tiếng Việt](../../../QUICKSTART.md) · [简体中文](../zh/QUICKSTART.md) · **Español** · [日本語](../ja/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md) · [Português](../pt-BR/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · [Bahasa Indonesia](../id/QUICKSTART.md)*

> Esta es una traducción automática de la guía de inicio rápido en inglés.

Pon NAOSO en marcha en pocos minutos. Guías completas: [docs/en/](../../../docs/en/README.md).

## Ordenador personal (Windows, macOS) - descarga el instalador

Instala NAOSO como cualquier otra app: descarga un archivo, ábrelo y tendrás un icono NAOSO para usar cada día. El instalador revisa qué le falta al equipo (Git, Python, Node, los cerebros de IA) e instala solo eso.

- **Windows 10/11:** descarga [Naota-Setup.exe](https://github.com/vuongtex/naota/releases/download/desktop/Naota-Setup.exe), haz doble clic y pulsa Next hasta el final. El progreso de la instalación se muestra dentro de la propia ventana de Setup, paso a paso (unos minutos), sin una ventana negra aparte. Al terminar hay un icono NAOSO en el Escritorio y en el menú Inicio.
- **macOS 11 o posterior:** abre **Terminal** (Launchpad, escribe Terminal), pega esta línea y pulsa Enter. Instalado así, macOS no muestra ninguna advertencia:
  ```
  curl -fsSL https://raw.githubusercontent.com/vuongtex/naota/main/packaging/macos/get-naota.sh | bash
  ```
  El comando descarga NAOSO, copia **NAOSO** en **Applications** y lo instala ahí mismo, en la ventana de Terminal (puede pedirte crear una cuenta de administrador de NAOSO y la contraseña del Mac una vez). Después, abre NAOSO desde Launchpad.

  ¿Prefieres un archivo? Descarga [Naota-macOS.dmg](https://github.com/vuongtex/naota/releases/download/desktop/Naota-macOS.dmg), ábrelo, arrastra **NAOSO** a **Applications** y ábrelo desde Launchpad. Aún no está firmado con un Apple Developer ID, así que macOS bloquea la primera apertura: cómo permitirlo está más abajo, en el apartado de descargas bloqueadas.

Al hacer clic en el icono, NAOSO se abre en su propia ventana (sin barra de direcciones), arranca con el equipo y el botón **Update** de la app funciona como siempre. Tus datos están en la carpeta `Naota` de tu carpeta de usuario; desinstalar la app conserva esa carpeta.

**Windows: instalar sin la pantalla de advertencia (recomendado).** El instalador de Windows aún no está firmado, así que una descarga con el navegador se bloquea la primera vez. Pega una línea en su lugar y obtienes el mismo instalador con el logo de NAOSO, sin bloqueo: pulsa Inicio, escribe `PowerShell`, ábrelo, pega esta línea y pulsa Enter:
```
irm https://raw.githubusercontent.com/vuongtex/naota/main/packaging/windows/get-naota.ps1 | iex
```

Si ya descargaste el archivo con el navegador y se bloqueó:
- Edge o Chrome dice "Naota-Setup.exe isn't commonly downloaded" y no guarda el archivo: en el cuadro de Descargas, pasa el ratón por esa línea, haz clic en los tres puntos, elige **Keep**, luego **Show more** y **Keep anyway**.
- Windows muestra "Windows protected your PC": pulsa **More info** y luego **Run anyway**.
- Tu antivirus borra el archivo, o Windows lo bloquea sin botón **Run anyway** (Smart App Control está activado): instala sin el .exe. Instala [Git](https://git-scm.com/download/win), abre PowerShell, pega esta línea y pulsa Enter. Al terminar, NAOSO se abre en http://localhost:7777 y arranca con el equipo:
  ```
  git clone https://github.com/vuongtex/naota.git "$env:USERPROFILE\NAOSO"; cd "$env:USERPROFILE\NAOSO"; powershell -ExecutionPolicy Bypass -File install.ps1
  ```
- macOS dice que no puede abrir la app: ve a **System Settings → Privacy & Security**, baja y pulsa **Open Anyway**, y vuelve a abrir NAOSO.

## Opción 1 - VPS de Hostinger (Docker Manager, en un clic)

> 🛒 **¿Aún no tienes VPS?** [Consigue un VPS de Hostinger aquí](https://www.hostinger.com?REFERRALCODE=VUONGTEX). Trae Docker Manager integrado, así que NAOSO se instala en un clic. Cuando esté listo, vuelve a los pasos de abajo.

1. hPanel → VPS → **Docker Manager** → **Compose** → **Compose from URL**.
2. Pega esta URL:
   ```
   https://raw.githubusercontent.com/vuongtex/naota/main/docker-compose.hostinger.yml
   ```
3. (Opcional, para HTTPS + un dominio) define esto en el cuadro **Environment**:
   ```
   DOMAIN_NAME=naota.<vps-hostname>.hstgr.cloud
   ```
   (El hostname está en hPanel → VPS, p. ej. `naota.srv1234567.hstgr.cloud`.)
4. **Deploy**. Espera de 1-3 minutos. Abre la app con el botón **Open** (o en `https://<DOMAIN_NAME>`).
5. En el primer arranque, la pantalla te pide crear una cuenta de administrador. Después, inicia sesión en Claude Code una vez desde el terminal del contenedor: `claude auth login --claudeai`.

Para actualizar: pulsa **Redeploy** en Docker Manager (imagen `:latest`, `pull_policy: always`). Los datos del Brain se conservan en el volumen.

## Opción 2 - Docker en cualquier máquina o VPS

> 🛒 **¿Necesitas un VPS?** Un [VPS de Hostinger](https://www.hostinger.com?REFERRALCODE=VUONGTEX) también sirve para esta opción.

```
docker compose -f docker-compose.yml up -d
```
Abre http://localhost:7777. Para HTTPS mediante Caddy, añade `-f docker-compose.https.yml`.

## Opción 3 - Ejecutarlo directamente (Windows, sin Docker)

1. Instala Python 3.12 + Node 22.
2. En la carpeta del proyecto, ejecuta `setup.bat` una vez: crea .venv, instala las dependencias e instala por ti los dos motores CLI (Claude Code, Codex).
3. `start-naota.bat` para ejecutarlo en segundo plano (`stop-naota.bat` para detenerlo).
4. Abre http://localhost:7777.

## Una vez en marcha

- **Elige un motor/modelo**: la página **Models** (Claude Code, ChatGPT/Codex, Antigravity CLI, OpenRouter, OpenAI, Google Gemini, Anthropic API, Groq, Ollama).
- **Configura las conexiones** (TPV, anuncios, calendario, Zalo...) para que los informes usen cifras reales: la página **Connections**; consulta [docs/09](../../../docs/en/09-connections-and-business-data.md).
- **Haz una copia de seguridad del Brain en GitHub** para no perder datos: la página **Self-learning**; consulta [docs/18](../../../docs/en/18-github-backup.md).
- **Vigila el gasto de tokens**: la página **Usage**; consulta [docs/23](../../../docs/en/23-usage-and-cost.md).

## Documentación completa

Consulta [docs/en/README.md](../../../docs/en/README.md): una guía por función (chat/voz, grafo de conocimiento, skills, agents, workflows, trabajos periódicos, Kanban, autoaprendizaje, conexiones, Telegram, Zalo, plugins, seguridad, copias de seguridad...). Las mismas guías en vietnamita: [docs/README.md](../../../docs/README.md).

## Problemas habituales

- **El botón de actualización de la app no hace nada en Hostinger**: es así por diseño; en Hostinger usa **Redeploy** en Docker Manager. El botón de la app necesita Watchtower, y Hostinger suele bloquear el socket de Docker.
- **ChatGPT/Codex dice "model not supported"**: elige un modelo de Codex válido en la página Models (p. ej. `gpt-5.5`). No uses `gpt-5-mini` ni `gpt-4o`: son modelos de API y una cuenta de Codex no puede ejecutarlos.
- Más: [docs/17 - Solución de problemas](../../../docs/en/17-troubleshooting.md).

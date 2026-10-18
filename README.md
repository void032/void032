<!--
  Profile README — Vineet Kumar (void032)
  Assets live in /assets (generated SVGs, dark + light variants)
-->
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/header-light.svg">
  <img src="assets/header-dark.svg" alt="VOID — Vineet Kumar, Creative Developer" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/terminal-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/terminal-light.svg">
  <img src="assets/terminal-dark.svg" alt="Terminal: whoami, focus, projects, status" width="100%">
</picture>

<br>

<img src="https://komarev.com/ghpvc/?username=void032&style=flat-square&color=161b22&label=PROFILE+VIEWS&labelColor=161b22" alt="Profile views" />
<img src="https://img.shields.io/github/followers/void032?style=flat-square&color=161b22&logo=github&logoColor=58a6ff&label=FOLLOWERS&labelColor=161b22" alt="Followers" />
<a href="https://shader-studio-teal.vercel.app"><img src="https://img.shields.io/badge/SHADER%20STUDIO-LIVE-161b22?style=flat-square&logo=threedotjs&logoColor=2DD4BF&labelColor=161b22" alt="Shader Studio" /></a>
<a href="https://www.linkedin.com/in/void032"><img src="https://img.shields.io/badge/LINKEDIN-CONNECT-161b22?style=flat-square&logo=linkedin&logoColor=0077B5&labelColor=161b22" alt="LinkedIn" /></a>

</div>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-about-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-about-light.svg">
  <img src="assets/sec-about-dark.svg" alt="ABOUT" width="100%">
</picture>

> **I build tools that eliminate friction — from AI automation to real-time 3D shaders.**

I'm a full-stack developer who bridges **practical utility** and **visual craft**. Whether it's a desktop video splitter, a browser shader studio, or an AI automation pipeline, I focus on shipping polished, performant tools.

```yaml
name:     Vineet Kumar
alias:    void032
focus:    Creative Dev, 3D Web, GLSL, Developer Tools, AI Automation
location: Behind a screen, shipping code
stack:    React, Three.js, Python, Node.js, GLSL
```

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-projects-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-projects-light.svg">
  <img src="assets/sec-projects-dark.svg" alt="PROJECTS" width="100%">
</picture>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/void032/shader-studio">Universal Shader Studio</a></h3>
      <p>Browser-based GLSL editor — real-time, zero setup, open source. Procedural terrain, GLB drag-and-drop, live vertex + fragment editing, multi-target export.</p>
      <p><img src="https://img.shields.io/badge/React-161b22?style=flat-square&labelColor=161b22&logo=react&logoColor=61DAFB" alt="React" /> <img src="https://img.shields.io/badge/Three.js-161b22?style=flat-square&labelColor=161b22&logo=three.js&logoColor=white" alt="Three.js" /> <img src="https://img.shields.io/badge/GLSL-161b22?style=flat-square&labelColor=161b22&logo=opengl&logoColor=white" alt="GLSL" /></p>
      <p><a href="https://shader-studio-teal.vercel.app">Live demo</a> · <a href="https://github.com/void032/shader-studio">Source</a></p>
    </td>
    <td width="50%" valign="top">
      <h3>SplitKit</h3>
      <p>Auto-split long videos with dual processing modes — Fast Copy (lossless) and Re-encode. Bundled with FFmpeg, ready-to-use installer.</p>
      <p><img src="https://img.shields.io/badge/Python-161b22?style=flat-square&labelColor=161b22&logo=python&logoColor=3776AB" alt="Python" /> <img src="https://img.shields.io/badge/PyQt6-161b22?style=flat-square&labelColor=161b22&logo=qt&logoColor=41CD52" alt="PyQt6" /> <img src="https://img.shields.io/badge/FFmpeg-161b22?style=flat-square&labelColor=161b22&logo=ffmpeg&logoColor=007808" alt="FFmpeg" /></p>
      <p><sub>Desktop app · Threading</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>Image Downloader Pro</h3>
      <p>Intelligent bulk image downloader Chrome extension. Detects &lt;img&gt; tags, CSS backgrounds, and lazy-loaded content, with batch processing.</p>
      <p><img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&labelColor=161b22&logo=javascript&logoColor=F7DF1E" alt="JavaScript" /> <img src="https://img.shields.io/badge/Chrome-161b22?style=flat-square&labelColor=161b22&logo=googlechrome&logoColor=4285F4" alt="Chrome" /></p>
      <p><sub>Extension · Chrome APIs · Batch download</sub></p>
    </td>
    <td width="50%" valign="top">
      <h3>Python Image Scraper</h3>
      <p>Headless browser automation for authenticated image scraping. Reuses existing Chrome profiles, handles lazy-loading, deduplicates, and organizes files.</p>
      <p><img src="https://img.shields.io/badge/Python-161b22?style=flat-square&labelColor=161b22&logo=python&logoColor=3776AB" alt="Python" /> <img src="https://img.shields.io/badge/Selenium-161b22?style=flat-square&labelColor=161b22&logo=selenium&logoColor=43B02A" alt="Selenium" /></p>
      <p><sub>CLI tool · Auth · Threading</sub></p>
    </td>
  </tr>
</table>

<details>
<summary><b>Shader Studio — features, tech stack &amp; architecture</b></summary>

<br>

- **Procedural terrain** — Perlin and Island generators
- **GLB upload** — drag and drop
- **Live GLSL** — vertex + fragment editing
- **Multi-export** — Three.js · R3F · raw GLSL · vanilla WebGL

| Layer | Technology |
|---|---|
| Renderer | Three.js r168 |
| Framework | React 18 + Vite 7 |
| Styling | Tailwind CSS v3 + shadcn/ui |
| Shaders | Raw GLSL (vertex + fragment) |
| Models | GLTFLoader + BufferGeometryUtils |
| Terrain | Custom Perlin noise implementation |
| Export | Three.js · R3F · Raw GLSL · Vanilla WebGL |

```
src/
├── components/
│   ├── scene/          # Terrain, Primitive, GLB controls
│   ├── tabs/           # Scene | Shader | Export | Code
│   └── ui/             # shadcn + custom components
├── context/
│   └── StudioContext   # Global state management
├── hooks/
│   ├── useThreeScene   # Scene lifecycle
│   ├── useShaderCompiler
│   ├── useTerrain      # Procedural generation
│   └── useGLBLoader    # Model ingestion
└── lib/
    ├── shaderPresets   # Built-in GLSL templates
    ├── codeTemplates   # Export generators
    └── colorPresets    # Terrain themes
```

</details>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-stack-light.svg">
  <img src="assets/sec-stack-dark.svg" alt="STACK" width="100%">
</picture>

**3D / Graphics**<br>
<img src="https://img.shields.io/badge/Three.js-161b22?style=flat-square&labelColor=161b22&logo=three.js&logoColor=white" alt="Three.js" />
<img src="https://img.shields.io/badge/WebGL-161b22?style=flat-square&labelColor=161b22&logo=webgl&logoColor=white" alt="WebGL" />
<img src="https://img.shields.io/badge/GLSL-161b22?style=flat-square&labelColor=161b22&logo=opengl&logoColor=white" alt="GLSL" />
<img src="https://img.shields.io/badge/GSAP-161b22?style=flat-square&labelColor=161b22&logo=greensock&logoColor=88CE02" alt="GSAP" />
<img src="https://img.shields.io/badge/React%20Three%20Fiber-161b22?style=flat-square&labelColor=161b22&logo=react&logoColor=61DAFB" alt="React Three Fiber" />

**Languages & Frontend**<br>
<img src="https://img.shields.io/badge/JavaScript-161b22?style=flat-square&labelColor=161b22&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
<img src="https://img.shields.io/badge/TypeScript-161b22?style=flat-square&labelColor=161b22&logo=typescript&logoColor=3178C6" alt="TypeScript" />
<img src="https://img.shields.io/badge/React-161b22?style=flat-square&labelColor=161b22&logo=react&logoColor=61DAFB" alt="React" />
<img src="https://img.shields.io/badge/Vite-161b22?style=flat-square&labelColor=161b22&logo=vite&logoColor=646CFF" alt="Vite" />
<img src="https://img.shields.io/badge/Tailwind%20CSS-161b22?style=flat-square&labelColor=161b22&logo=tailwind-css&logoColor=38B2AC" alt="Tailwind CSS" />
<img src="https://img.shields.io/badge/Python-161b22?style=flat-square&labelColor=161b22&logo=python&logoColor=3776AB" alt="Python" />
<img src="https://img.shields.io/badge/PHP-161b22?style=flat-square&labelColor=161b22&logo=php&logoColor=777BB4" alt="PHP" />
<img src="https://img.shields.io/badge/Django-161b22?style=flat-square&labelColor=161b22&logo=django&logoColor=44B78B" alt="Django" />
<img src="https://img.shields.io/badge/Node.js-161b22?style=flat-square&labelColor=161b22&logo=node.js&logoColor=43853D" alt="Node.js" />

**AI & Agents**<br>
<img src="https://img.shields.io/badge/Claude-161b22?style=flat-square&labelColor=161b22&logo=anthropic&logoColor=white" alt="Claude" />
<img src="https://img.shields.io/badge/Gemini-161b22?style=flat-square&labelColor=161b22&logo=googlegemini&logoColor=8E75B2" alt="Gemini" />
<img src="https://img.shields.io/badge/OpenAI-161b22?style=flat-square&labelColor=161b22&logo=openai&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Jules-161b22?style=flat-square&labelColor=161b22" alt="Jules" />

**Tools & Platforms**<br>
<img src="https://img.shields.io/badge/PyQt6-161b22?style=flat-square&labelColor=161b22&logo=qt&logoColor=41CD52" alt="PyQt6" />
<img src="https://img.shields.io/badge/Selenium-161b22?style=flat-square&labelColor=161b22&logo=selenium&logoColor=43B02A" alt="Selenium" />
<img src="https://img.shields.io/badge/Git-161b22?style=flat-square&labelColor=161b22&logo=git&logoColor=F05032" alt="Git" />
<img src="https://img.shields.io/badge/Chrome%20Extensions-161b22?style=flat-square&labelColor=161b22&logo=googlechrome&logoColor=4285F4" alt="Chrome Extensions" />
<img src="https://img.shields.io/badge/FFmpeg-161b22?style=flat-square&labelColor=161b22&logo=ffmpeg&logoColor=007808" alt="FFmpeg" />

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-analytics-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-analytics-light.svg">
  <img src="assets/sec-analytics-dark.svg" alt="ANALYTICS" width="100%">
</picture>

<div align="center">
  <img height="180" src="profile/stats.svg" alt="GitHub stats" />
  <img height="180" src="profile/top-langs.svg" alt="Top languages" />
</div>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=void032&hide_border=true&stroke=30363d&background=0d1117&ring=58a6ff&fire=2DD4BF&currStreakNum=f0f6fc&sideNums=f0f6fc&currStreakLabel=58a6ff&sideLabels=8b949e&dates=6e7681">
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=void032&hide_border=true&stroke=d1d9e0&background=ffffff&ring=0969da&fire=0d9488&currStreakNum=1f2328&sideNums=1f2328&currStreakLabel=0969da&sideLabels=59636e&dates=818b98">
  <img src="https://streak-stats.demolab.com/?user=void032&hide_border=true&stroke=30363d&background=0d1117&ring=58a6ff&fire=2DD4BF&currStreakNum=f0f6fc&sideNums=f0f6fc&currStreakLabel=58a6ff&sideLabels=8b949e&dates=6e7681" alt="GitHub streak" >
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=void032&theme=github-compact&hide_border=true&area=true&bg_color=0d1117&color=58a6ff&line=2DD4BF&point=58a6ff">
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=void032&hide_border=true&area=true&bg_color=ffffff&color=0969da&line=0d9488&point=0969da&title_color=1f2328">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=void032&theme=github-compact&hide_border=true&area=true&bg_color=0d1117&color=58a6ff&line=2DD4BF&point=58a6ff" alt="Contribution activity" width="100%">
</picture>

</div>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-exploring-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-exploring-light.svg">
  <img src="assets/sec-exploring-dark.svg" alt="EXPLORING" width="100%">
</picture>

```mermaid
graph LR
    A[GLSL / 3D Web] --> B[AI Integration]
    B --> C[Automation Tools]
    C --> D[Full-Stack Apps]
    D --> A
```

- **3D Web & Shaders** — cinematic scroll-driven experiences with Three.js + GSAP + GLSL
- **AI-Powered Solutions** — integrating LLMs into practical applications
- **Process Automation** — eliminating manual, repetitive tasks
- **Developer Tools** — utilities that ship fast and work clean

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/sec-connect-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/sec-connect-light.svg">
  <img src="assets/sec-connect-dark.svg" alt="CONNECT" width="100%">
</picture>

<div align="center">

<a href="https://www.linkedin.com/in/void032"><img src="https://img.shields.io/badge/LinkedIn-161b22?style=for-the-badge&logo=linkedin&logoColor=0077B5" alt="LinkedIn" /></a>
<a href="https://github.com/void032"><img src="https://img.shields.io/badge/GitHub-161b22?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
<a href="mailto:vineetkumar1639@gmail.com"><img src="https://img.shields.io/badge/Email-161b22?style=for-the-badge&logo=gmail&logoColor=D14836" alt="Email" /></a>
<a href="https://shader-studio-teal.vercel.app"><img src="https://img.shields.io/badge/Shader%20Studio-161b22?style=for-the-badge&logo=threedotjs&logoColor=2DD4BF" alt="Shader Studio" /></a>

<br><br>

<sub><i>The best code is the code that solves real problems efficiently.</i></sub>

</div>

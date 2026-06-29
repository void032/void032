<!-- 
  ╔══════════════════════════════════════════════════════════╗
  ║  Profile README — Vineet Kumar (void032)                ║
  ║  Modern Dark Aesthetic | Shader Studio Flagship         ║
  ╚══════════════════════════════════════════════════════════╝
-->

<div align="center">
  
  <!-- Animated Header -->
  <img src="https://capsule-render.vercel.app/api?type=venom&height=200&text=Vineet%20Kumar&fontSize=70&color=0:0d1117,100:161b22&fontColor=58a6ff&stroke=58a6ff&strokeWidth=2&animation=fadeIn" />
  
  <!-- Typing Animation -->
  <img src="https://readme-typing-svg.herokuapp.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=800&color=2DD4BF&center=true&vCenter=true&width=600&lines=Full-Stack+Developer;GLSL+Shader+Artist;AI+Automation+Engineer;Tool+Builder+%26+Problem+Solver" alt="Typing SVG" />
  
  <!-- Social Badges -->
  <p>
    <a href="https://github.com/void032">
      <img src="https://img.shields.io/github/followers/void032?label=Followers&style=for-the-badge&color=161b22&logo=github&logoColor=58a6ff&labelColor=0d1117" />
    </a>
    <a href="https://shader-studio-teal.vercel.app">
      <img src="https://img.shields.io/badge/Shader%20Studio-Live%20Demo-2DD4BF?style=for-the-badge&color=161b22&logo=three.js&logoColor=2DD4BF&labelColor=0d1117" />
    </a>
    <a href="https://www.linkedin.com/in/vineet-kumar-2ab15217b">
      <img src="https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&color=161b22&logo=linkedin&logoColor=0077B5&labelColor=0d1117" />
    </a>
  </p>
  
  <!-- Divider -->
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
  
</div>

<!-- About Section -->
## <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="35"> About Me

> **"I build tools that eliminate friction — from AI automation to real-time 3D shaders."**

I'm a full-stack developer who bridges the gap between **practical utility** and **visual craft**. Whether it's a desktop video splitter, a browser shader studio, or an AI automation pipeline — I focus on shipping polished, performant tools.

```yaml
name: Vineet Kumar
alias: void032
focus:    [Full-Stack, AI Automation, GLSL/3D, Developer Tools]
location: Behind a screen, shipping code
stack:    [React, Three.js, Python, Node.js, GLSL]

<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
<!-- ═══════════════════════════════════════════════════════ -->
<!-- FLAGSHIP PROJECT: SHADER STUDIO -->
<!-- ═══════════════════════════════════════════════════════ -->
🚀 Flagship Project
<div align="center">
  <!-- Project Banner -->
  <a href="https://shader-studio-teal.vercel.app">
    <img src="https://capsule-render.vercel.app/api?type=rect&height=80&text=⚡%20Shader%20Studio&fontSize=40&color=0:0d1117,100:161b22&fontColor=2DD4BF&stroke=2DD4BF&strokeWidth=1" width="100%" />
  </a>
  <p>
    <b>Universal GLSL Shader Editor — Browser-based, real-time, zero setup.</b>
  </p>
  <!-- Screenshot Grid -->
  <table>
    <tr>
      <td width="50%">
        <img src="https://github.com/void032/shader-studio/raw/main/screenshots/terrain.png" width="100%" style="border-radius: 12px; border: 1px solid #30363d;" />
        <p align="center"><sub>🏔️ Procedural Terrain with Perlin & Island Noise</sub></p>
      </td>
      <td width="50%">
        <img src="https://github.com/void032/shader-studio/raw/main/screenshots/shader-editor.png" width="100%" style="border-radius: 12px; border: 1px solid #30363d;" />
        <p align="center"><sub>⚡ Live GLSL Editor with Syntax Highlighting</sub></p>
      </td>
    </tr>
  </table>
  <!-- Feature Pills -->
  <p>
    <img src="https://img.shields.io/badge/🏔️%20Procedural%20Terrain-Perlin%20%26%20Island-2DD4BF?style=flat-square&color=0d1117" />
    <img src="https://img.shields.io/badge/📦%20GLB%20Upload-Drag%20%26%20Drop-2DD4BF?style=flat-square&color=0d1117" />
    <img src="https://img.shields.io/badge/⚡%20Live%20GLSL-Vertex%20%2B%20Fragment-2DD4BF?style=flat-square&color=0d1117" />
    <img src="https://img.shields.io/badge/📤%20Multi--Export-Three.js%20%7C%20R3F%20%7C%20WebGL-2DD4BF?style=flat-square&color=0d1117" />
  </p>
  <!-- Action Buttons -->
  <p>
    <a href="https://shader-studio-teal.vercel.app">
      <img src="https://img.shields.io/badge/🚀%20Live%20Demo-2DD4BF?style=for-the-badge&color=0d1117&logoColor=2DD4BF" />
    </a>
    <a href="https://github.com/void032/shader-studio">
      <img src="https://img.shields.io/badge/📂%20Source%20Code-2DD4BF?style=for-the-badge&color=0d1117&logoColor=2DD4BF" />
    </a>
  </p>
</div>
<details>
<summary><b>🛠️ Shader Studio — Tech Stack & Architecture</b></summary>
<br>

| Layer         | Technology                                |
| ------------- | ----------------------------------------- |
| **Renderer**  | Three.js r168                             |
| **Framework** | React 18 + Vite 7                         |
| **Styling**   | Tailwind CSS v3 + shadcn/ui               |
| **Shaders**   | Raw GLSL (Vertex + Fragment)              |
| **Models**    | GLTFLoader + BufferGeometryUtils          |
| **Terrain**   | Custom Perlin Noise Implementation        |
| **Export**    | Three.js · R3F · Raw GLSL · Vanilla WebGL |

src/
├── components/
│   ├── scene/          # Terrain, Primitive, GLB Controls
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

</details>
<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
<!-- ═══════════════════════════════════════════════════════ -->
<!-- OTHER PROJECTS -->
<!-- ═══════════════════════════════════════════════════════ -->
🧰 Other Projects
<table>
  <tr>
    <td width="33%" valign="top">
      <h3 align="center">🎬 SplitKit</h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white&color=0d1117" />
        <img src="https://img.shields.io/badge/PyQt6-41CD52?style=flat-square&logo=qt&logoColor=white&color=0d1117" />
      </p>
      <p>Auto-split long videos with dual processing modes — Fast Copy (lossless) & Re-encode. Bundled with FFmpeg, ready-to-use installer.</p>
      <p align="center"><sub><code>Desktop App</code> · <code>FFmpeg</code> · <code>Threading</code></sub></p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">🖼️ Image Downloader Pro</h3>
      <p align="center">
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=white&color=0d1117" />
        <img src="https://img.shields.io/badge/Chrome-4285F4?style=flat-square&logo=google-chrome&logoColor=white&color=0d1117" />
      </p>
      <p>Intelligent bulk image downloader Chrome extension. Smart detection of &lt;img&gt;, CSS backgrounds, and lazy-loaded content with batch processing.</p>
      <p align="center"><sub><code>Extension</code> · <code>Chrome APIs</code> · <code>Batch DL</code></sub></p>
    </td>
    <td width="33%" valign="top">
      <h3 align="center">🐍 Python Image Scraper</h3>
      <p align="center">
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white&color=0d1117" />
        <img src="https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white&color=0d1117" />
      </p>
      <p>Headless browser automation for authenticated image scraping. Uses existing Chrome profiles, handles lazy-loading, deduplicates, and organizes files.</p>
      <p align="center"><sub><code>CLI Tool</code> · <code>Auth</code> · <code>Threading</code></sub></p>
    </td>
  </tr>
</table>
<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
<!-- ═══════════════════════════════════════════════════════ -->
<!-- TECH STACK -->
<!-- ═══════════════════════════════════════════════════════ -->
🛠️ Tech Stack
<div align="center">
  <!-- Languages -->
  <h4>Languages</h4>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&color=161b22" />
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=F7DF1E&color=161b22" />
    <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=3178C6&color=161b22" />
    <img src="https://img.shields.io/badge/GLSL-5586A4?style=for-the-badge&logo=opengl&logoColor=5586A4&color=161b22" />
    <img src="https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=777BB4&color=161b22" />
  </p>
  <!-- Frontend & 3D -->
  <h4>Frontend & 3D</h4>
  <p>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB&color=161b22" />
    <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=three.js&logoColor=white&color=161b22" />
    <img src="https://img.shields.io/badge/Tailwind-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=38B2AC&color=161b22" />
    <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=646CFF&color=161b22" />
    <img src="https://img.shields.io/badge/shadcn/ui-000000?style=for-the-badge&logo=shadcnui&logoColor=white&color=161b22" />
  </p>
  <!-- Backend & Tools -->
  <h4>Backend & Tools</h4>
  <p>
    <img src="https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=43853D&color=161b22" />
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white&color=161b22" />
    <img src="https://img.shields.io/badge/PyQt6-41CD52?style=for-the-badge&logo=qt&logoColor=41CD52&color=161b22" />
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=F05032&color=161b22" />
  </p>
  <!-- AI & Automation -->
  <h4>AI & Automation</h4>
  <p>
    <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=412991&color=161b22" />
    <img src="https://img.shields.io/badge/Claude-FF6B35?style=for-the-badge&logo=anthropic&logoColor=FF6B35&color=161b22" />
    <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=43B02A&color=161b22" />
    <img src="https://img.shields.io/badge/Gemini-FF6F00?style=for-the-badge&logo=google&logoColor=FF6F00&color=161b22" />
  </p>
</div>
<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
<!-- ═══════════════════════════════════════════════════════ -->
<!-- GITHUB ANALYTICS -->
<!-- ═══════════════════════════════════════════════════════ -->
📊 GitHub Analytics
<div align="center">
  <img height="170em" src="https://github-readme-stats.vercel.app/api?username=void032&show_icons=true&theme=github_dark&hide_border=true&count_private=true&include_all_commits=true&bg_color=0d1117&title_color=58a6ff&icon_color=2DD4BF&text_color=c9d1d9" />
  <img height="170em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=void032&layout=compact&theme=github_dark&hide_border=true&langs_count=8&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" />


  <img src="https://github-readme-streak-stats.herokuapp.com/?user=void032&theme=github-dark-blue&hide_border=true&background=0d1117&stroke=30363d&ring=58a6ff&fire=2DD4BF&currStreakLabel=58a6ff" />


  <img src="https://github-readme-activity-graph.vercel.app/graph?username=void032&theme=github-compact&hide_border=true&area=true&bg_color=0d1117&color=58a6ff&line=2DD4BF&point=58a6ff" />
</div>
<!-- Divider -->
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png" width="100%" />
<!-- ═══════════════════════════════════════════════════════ -->
<!-- CONNECT -->
<!-- ═══════════════════════════════════════════════════════ -->
🤝 Let's Connect
<div align="center">
  <a href="https://www.linkedin.com/in/vineet-kumar-2ab15217b">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&color=161b22" />
  </a>
  <a href="https://github.com/void032">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white&color=161b22" />
  </a>
  <a href="mailto:vineetkumar1639@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&color=161b22" />
  </a>
  <a href="https://shader-studio-teal.vercel.app">
    <img src="https://img.shields.io/badge/Shader%20Studio-2DD4BF?style=for-the-badge&logo=three.js&logoColor=2DD4BF&color=161b22" />
  </a>
</div>
<!-- Footer -->
<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:161b22,100:30363d&height=120&section=footer&text=Thanks%20for%20visiting!&fontSize=24&fontColor=58a6ff&animation=twinkling" />
  <p>
    <i>💡 "The best code is the code that solves real problems efficiently."</i>
  </p>
  <img src="https://komarev.com/ghpvc/?username=void032&label=Profile%20Views&color=58a6ff&style=flat-square" alt="Profile Views" />
</div>
```

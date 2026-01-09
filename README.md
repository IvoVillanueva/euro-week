# 🏀 Euro Week - Seguimiento Semanal de Equipos Españoles en Europa

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Polars](https://img.shields.io/badge/Polars-Data_Processing-CD792C?style=for-the-badge&logo=polars&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

---

## 📋 Descripción

**Euro Week** es una herramienta automatizada que genera visualizaciones profesionales del calendario semanal de los equipos españoles de baloncesto que participan en competiciones europeas. El proyecto recopila datos en tiempo real de las principales competiciones continentales y crea gráficos elegantes y informativos.

### 🎯 Competiciones Monitoreadas

| Competición | Logo | Descripción |
|------------|------|-------------|
| **EuroLeague** | 🏆 | La máxima competición europea de clubes |
| **EuroCup** | 🥈 | Segunda división europea de clubes |
| **FIBA Champions League** | 🏀 | Competición FIBA de clubes europeos |
| **FIBA Europe Cup** | 🌍 | Segunda competición FIBA europea |

---

## ✨ Características Principales

- 🔄 **Actualización Automática**: Recopila datos en tiempo real de las APIs oficiales
- 📊 **Visualizaciones Profesionales**: Genera gráficos elegantes con logos y colores de equipos
- 🎨 **Diseño Personalizado**: Cada equipo se muestra con su identidad corporativa
- 📅 **Calendario Semanal**: Enfoque en los partidos de lunes a viernes
- 🇪🇸 **Equipos Españoles**: Seguimiento específico de clubes españoles en Europa
- 💾 **Procesamiento Eficiente**: Utiliza Polars para operaciones de datos ultrarrápidas
- 🖼️ **Exportación PNG**: Gráficos listos para compartir en redes sociales

---

## 🚀 Instalación

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación de Dependencias

```bash
# Clonar el repositorio
git clone https://github.com/IvoVillanueva/euro-week.git
cd euro-week

# Instalar las dependencias necesarias
pip install pandas polars great-tables selenium pillow
```

> **Nota para Forks**: Si has hecho fork del repositorio, usa la URL de tu fork en lugar de la URL original.

### Dependencias Principales

| Librería | Versión | Propósito |
|----------|---------|-----------|
| **Polars** | Latest | Motor de procesamiento de datos de alto rendimiento |
| **Pandas** | Latest | Análisis y manipulación de datos |
| **Great Tables** | Latest | Creación de tablas HTML elegantes y personalizables |
| **Selenium** | Latest | Automatización del navegador para capturas de pantalla |
| **Pillow (PIL)** | Latest | Procesamiento y manipulación de imágenes |

---

## 💻 Uso

### Ejecución de Scripts Individuales

Puedes ejecutar cada competición por separado:

```bash
# Generar datos de EuroLeague
python scripts/euroligue.py

# Generar datos de EuroCup
python scripts/eurocup.py

# Generar datos de FIBA Champions League
python scripts/fiba_championsleague.py

# Generar datos de FIBA Europe Cup
python scripts/fiba_europecup.py
```

### Generar el Gráfico Completo

Para crear la visualización completa con todas las competiciones:

```bash
python scripts/union_grafico.py
```

El gráfico generado se guardará en la carpeta `png/` con el nombre `desarrollo_europeo_py.png`.

---

## 📁 Estructura del Proyecto

```
euro-week/
│
├── 📂 scripts/               # Scripts de Python
│   ├── euroligue.py         # Procesamiento EuroLeague
│   ├── eurocup.py           # Procesamiento EuroCup
│   ├── fiba_championsleague.py  # Procesamiento Champions League
│   ├── fiba_europecup.py    # Procesamiento Europe Cup
│   └── union_grafico.py     # Generación del gráfico final
│
├── 📂 src/                   # Notebooks de Jupyter
│   ├── eurocup.ipynb
│   ├── euroligue.ipynb
│   ├── fiba_championsleague.ipynb
│   ├── fiba_europecup.ipynb
│   └── union_grafico.ipynb
│
├── 📂 png/                   # Gráficos generados
│   └── desarrollo_europeo_py.png
│
├── 📄 LICENSE                # Licencia MIT
└── 📄 README.md             # Este archivo
```

---

## 🎨 Ejemplo de Salida

El proyecto genera gráficos profesionales con:

- 📊 Calendario semanal de lunes a viernes
- 🎨 Logos y colores corporativos de cada equipo
- 🏆 Separación por competición europea
- 📅 Fechas y horarios de los partidos
- 🌐 Información de rival y localización (Local/Visitante)

Los gráficos se guardan en la carpeta `png/` con formato PNG listo para compartir.

> **Ejemplo**: Después de ejecutar `union_grafico.py`, encontrarás el gráfico en `png/desarrollo_europeo_py.png`

---

## 🔧 Tecnologías Utilizadas

<div align="center">

### Lenguaje Principal
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

### Procesamiento de Datos
![Polars](https://img.shields.io/badge/Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

### Visualización
![Great Tables](https://img.shields.io/badge/Great_Tables-FF6B6B?style=for-the-badge)
![Pillow](https://img.shields.io/badge/Pillow-8BC34A?style=for-the-badge)

### Automatización
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

</div>

---

## 📊 Fuentes de Datos

Los datos se obtienen en tiempo real de las siguientes fuentes:

- 🔗 **EuroLeague**: Datos oficiales de partidos y estadísticas
- 🔗 **EuroCup**: Información de la segunda competición europea
- 🔗 **FIBA**: Datos de Champions League y Europe Cup
- 🔗 **ACB**: Logos y colores corporativos de equipos españoles

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto:

1. 🍴 Fork el proyecto
2. 🌿 Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔃 Abre un Pull Request

---

## 📝 Casos de Uso

- **Medios de Comunicación**: Gráficos listos para publicar en artículos deportivos
- **Redes Sociales**: Contenido visual atractivo para compartir calendarios
- **Análisis Deportivo**: Seguimiento de la carga competitiva de equipos españoles
- **Aficionados**: Información clara sobre cuándo juegan sus equipos favoritos
- **Presentaciones**: Material profesional para informes y presentaciones

---

## 📈 Valor Añadido

### Para Clientes y Stakeholders

- ⚡ **Ahorro de Tiempo**: Automatiza la creación de calendarios semanales
- 🎯 **Precisión**: Datos actualizados automáticamente desde fuentes oficiales
- 🎨 **Profesionalidad**: Gráficos con diseño corporativo de cada equipo
- 📱 **Listo para Publicar**: Formato optimizado para redes sociales
- 🔄 **Escalable**: Fácil de adaptar a otras ligas o competiciones

### Diferenciadores Técnicos

- 🚀 **Alto Rendimiento**: Usa Polars, hasta 10x más rápido que Pandas
- 🛠️ **Modular**: Cada competición se procesa independientemente
- 📦 **Fácil Integración**: Se puede integrar en workflows automatizados
- 🎨 **Customizable**: Colores y logos configurables por equipo

---

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License - Copyright (c) 2025 Iván Villanueva Sabalete
```

---

## 👨‍💻 Autor

**Iván Villanueva Sabalete**

### Contacto y Redes Sociales

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-@elcheff-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/elcheff)
[![Instagram](https://img.shields.io/badge/Instagram-@sport__iv0-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/sport_iv0)
[![GitHub](https://img.shields.io/badge/GitHub-IvoVillanueva-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/IvoVillanueva)

</div>

---

## 🙏 Agradecimientos

- 🏀 **EuroLeague** - Por proporcionar datos de las competiciones
- 🏀 **EuroCup** - Por la información de partidos y equipos
- 🏀 **FIBA** - Por los datos de Champions League y Europe Cup
- 🏀 **ACB** - Por los recursos visuales de equipos españoles

---

## 📊 Estado del Proyecto

![Mantenimiento Activo](https://img.shields.io/badge/Mantenimiento-Activo-success?style=for-the-badge)
![Competiciones](https://img.shields.io/badge/Competiciones_Europeas-4-orange?style=for-the-badge)
![Actualización](https://img.shields.io/badge/Actualización-Semanal-blue?style=for-the-badge)

---

<div align="center">

### ⭐ Si te gusta este proyecto, dale una estrella en GitHub ⭐

**Hecho con ❤️ y 🏀 por Iván Villanueva**

</div>
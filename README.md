# Berlin Housing Decision Support System (DSS)

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://itsamarin.github.io/DSS-Berlin-Housing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data](https://img.shields.io/badge/data-2319%20listings-orange)](data/)

An interactive web-based Decision Support System for analyzing Berlin's accommodation market, helping tenants find perfect homes and landlords optimize occupancy.

## Features

- **Real-Time Analytics**: Interactive visualizations of 2,319+ accommodation listings (demo shows 1,000 sample listings)
- **Smart Matching Algorithm**: AI-powered recommendations based on price (30%), location (20%), satisfaction (30%), and verification (20%)
- **Multi-View Interface**: Overview Dashboard, Tenant View, and Landlord Analytics
- **No Installation Required**: Pure HTML5/CSS3/JavaScript with Chart.js 4.4.0

## Quick Start

### View Online
- **Landing Page**: [https://itsamarin.github.io/DSS-Berlin-Housing/](https://itsamarin.github.io/DSS-Berlin-Housing/)
- **Dashboard**: [https://itsamarin.github.io/DSS-Berlin-Housing/dashboard/Berlin_DSS_Dashboard.html](https://itsamarin.github.io/DSS-Berlin-Housing/dashboard/Berlin_DSS_Dashboard.html)

### Run Locally

```bash
# Clone repository
git clone https://github.com/itsamarin/DSS-Berlin-Housing.git
cd DSS-Berlin-Housing
```

#### To run the dashboard (HTML):

```bash
# macOS/Linux:
open dashboard/Berlin_DSS_Dashboard.html
# Windows:
start dashboard/Berlin_DSS_Dashboard.html
```

#### To run the backend data pipeline (main.py):

```bash
# macOS/Linux:
python3 main.py
# Windows:
python main.py
```

#### Or use a local server for the dashboard:

```bash
python -m http.server 8000
# Visit: http://localhost:8000/dashboard/Berlin_DSS_Dashboard.html
```

## Repository Structure

```
DSS-Berlin-Housing/
├── data/
│   ├── original/           # Raw, unprocessed datasets
│   └── cleaned/            # Processed, cleaned datasets
│
├── models/                 # Data models and analytical models
│
├── dashboard/              # Interactive web dashboard
│
├── docs/                   # Project documentation
│
├── src/                    # Python source code
│   ├── extraction/         # Data extraction scripts
│   │   └── data_extraction.py
│   ├── cleaning/           # Data cleaning scripts
│   │   └── data_cleaning.py
│   ├── feature_engineering/# Feature engineering scripts
│   │   └── feature_engineering.py
│   └── visualisation/      # Visualization scripts
│       └── basic_visualisation.py
│
├── index.html              # Landing page
├── README.md               # This file
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
├── DEPLOYMENT_GUIDE.md     # Deployment instructions
├── QUICK_START.md          # Quick start guide
├── setup.sh                # Setup script for Unix/Linux/macOS
├── setup.bat               # Setup script for Windows
└── .gitignore              # Git ignore configuration
```

## Data Overview

| Metric | Value |
|--------|-------|
| Total Listings | 2,319 |
| Total Tenants | 2,000 |
| Districts Covered | 12 |
| Average Satisfaction | 4.2/5.0 |
| Verification Rate | 62.5% |

## Documentation

- **[QUICK_START.md](QUICK_START.md)** - Getting started guide
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - GitHub Pages deployment
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[data/README.md](data/original/README.md)** - Dataset documentation
- **[models/README.md](models/README.md)** - Analytical models documentation
- **[dashboard/README.md](dashboard/README.md)** - Dashboard customization guide

## Use Cases

**For Tenants**: Find accommodations matching budget and preferences, compare districts and ratings, get AI recommendations

**For Landlords**: Analyze market trends, optimize pricing strategies, track occupancy rates, identify high-performing properties

**For Researchers**: Study housing market dynamics, analyze pricing correlations, explore geographic patterns

## Project Background

This DSS addresses Berlin's housing challenges including payment fragmentation, listing verification issues, and occupancy uncertainty through an integrated platform with verified listings, fraud detection, and occupancy optimization.

### DSS Components
1. **Data Management (DMSS)**: Data collection and cleaning
2. **Model Management (MMSS)**: Predictive models for matching and forecasting
3. **Knowledge Management (KMSS)**: Verification rules and eligibility criteria
4. **User Interface (UIS)**: Interactive dashboards

Based on Simon's Decision-Making Model: Intelligence → Design → Choice → Implementation

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Links

[Live Demo](https://itsamarin.github.io/DSS-Berlin-Housing/) · [Report Bug](https://github.com/itsamarin/DSS-Berlin-Housing/issues) · [Request Feature](https://github.com/itsamarin/DSS-Berlin-Housing/issues)

---

**Made for the Berlin housing community**

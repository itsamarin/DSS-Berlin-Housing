# Berlin Housing Decision Support System (DSS)

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://itsamarin.github.io/DSS-Berlin-Housing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data](https://img.shields.io/badge/data-2319%20listings-orange)](data/)

An interactive web-based Decision Support System for analyzing Berlin's accommodation market, helping tenants find perfect homes and landlords optimize occupancy.

## Features

- **Real-Time Analytics**: Interactive visualizations of 2,319+ accommodation listings (demo shows 1,000 sample listings)
- **Advanced AI-Powered Smart Matching**:
  - For Tenants: Find perfect accommodations based on budget, location, ratings, and preferences
  - For Landlords: Find ideal tenants with advanced scoring considering budget match (20-40%), location (15-35%), income stability (10-20%), verification (10-35%), property type match (10-15%), and occupation preference (5%)
  - Customizable priority modes: Balanced, Financial Stability, Location Match, or Verification Priority
- **Advanced Filter Search**:
  - Comprehensive filters for district, budget range, room type, occupation, and verification status
  - Multiple sort options and pagination for efficient browsing
  - Real-time filtering with instant results
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

# Open dashboard
open dashboard/Berlin_DSS_Dashboard.html

# Or use local server
python -m http.server 8000
# Visit: http://localhost:8000/dashboard/Berlin_DSS_Dashboard.html
```

## Repository Structure

```
DSS-Berlin-Housing/
├── data/                              # Data files
│   ├── original/                      # Raw, unprocessed datasets
│   │   └── README.md                  # Original data documentation
│   └── cleaned/                       # Processed, cleaned datasets
│       └── README.md                  # Cleaned data documentation
│
├── models/                            # Data models and analytical models
│   └── README.md                      # Models documentation
│
├── dashboard/                         # Interactive web dashboard
│   ├── Berlin_DSS_Dashboard.html     # Main dashboard file
│   ├── README.md                      # Dashboard documentation
│   ├── DASHBOARD_COMPONENTS.md       # Detailed component descriptions
│   ├── LANDLORD_ANALYTICS_FEATURES.md # AI-Powered matching & filter docs
│   └── IMPLEMENTATION_SUMMARY.md     # Summary of recent enhancements
│
├── docs/                              # Project documentation
│   └── README.md                      # Documentation index
│
├── index.html                         # Landing page
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── DEPLOYMENT_GUIDE.md                # Deployment instructions
├── QUICK_START.md                     # Quick start guide
├── setup.sh                           # Setup script for Unix/Linux/macOS
├── setup.bat                          # Setup script for Windows
└── .gitignore                         # Git ignore configuration
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
- **[dashboard/LANDLORD_ANALYTICS_FEATURES.md](dashboard/LANDLORD_ANALYTICS_FEATURES.md)** - AI-Powered matching & advanced filters
- **[dashboard/IMPLEMENTATION_SUMMARY.md](dashboard/IMPLEMENTATION_SUMMARY.md)** - Recent enhancements summary

## Use Cases

**For Tenants**: Find accommodations matching budget and preferences, compare districts and ratings, get AI recommendations

**For Landlords**: Find ideal tenants with AI-powered matching, analyze market trends, optimize pricing strategies, track occupancy rates, browse tenant applicants with advanced filters, identify high-performing properties

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

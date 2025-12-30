# Berlin Housing Decision Support System (DSS)

[![Live Demo](https://img.shields.io/badge/demo-live-success)](https://itsamarin.github.io/DSS-Berlin-Housing/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Data](https://img.shields.io/badge/data-2319%20listings-orange)](data/)

An interactive web-based Decision Support System for analyzing Berlin's accommodation market, helping tenants find perfect homes and landlords optimize occupancy.

## Features

### Real-Time Analytics Dashboard
- Interactive visualizations of 2,319+ accommodation listings (demo shows 1,000 sample listings)
- 2,000+ tenant profiles with booking history
- Live filtering and data exploration

### Smart Matching Algorithm
Our intelligent matching system scores properties based on:
- **Price Affordability** (30% weight)
- **Location Proximity** (20% weight)
- **Guest Satisfaction** (30% weight)
- **Verification Status** (20% weight)

### Multi-View Interface
1. **Overview Dashboard** - Market insights and key metrics from 1,000+ listings
2. **Find Accommodation** - Browse all listings, filter by preferences, and get AI-powered recommendations
3. **Landlord Analytics** - Optimize occupancy and revenue with performance insights

## Quick Start

### Option 1: View Online (Easiest)
**Landing Page:** [https://itsamarin.github.io/DSS-Berlin-Housing/](https://itsamarin.github.io/DSS-Berlin-Housing/)

**Direct Dashboard Access:** [https://itsamarin.github.io/DSS-Berlin-Housing/Berlin_DSS_Dashboard.html](https://itsamarin.github.io/DSS-Berlin-Housing/Berlin_DSS_Dashboard.html)

The dashboard features 1,000 property listings with real-time filtering and smart matching capabilities.

### Option 2: Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/itsamarin/DSS-Berlin-Housing.git
cd DSS-Berlin-Housing
```

2. **Open in browser**
```bash
# Simply open the HTML file
open Berlin_DSS_Dashboard.html

# Or use a local server (recommended)
python -m http.server 8000
# Then visit: http://localhost:8000
```

No installation or dependencies required.

## Repository Structure

```
berlin-housing-dss/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── DEPLOYMENT_GUIDE.md                # Deployment instructions
├── QUICK_START.md                     # Quick start guide
├── setup.sh                           # Setup script for Unix/Linux/macOS
└── setup.bat                          # Setup script for Windows
```

## Data Overview

### Accommodation Data
- **2,319 listings** across 12 Berlin districts
- Price ranges, room types, capacity
- Guest satisfaction and cleanliness ratings
- Location metrics (distance to center, metro, attractions)

### Tenant Data
- **2,000 tenant profiles**
- Booking history and behavior patterns
- Verification status and ratings
- Geographic distribution

### Key Metrics
| Metric | Value |
|--------|-------|
| Total Listings | 2,319 |
| Total Tenants | 2,000 |
| Average Satisfaction | 4.2/5.0 |
| Verification Rate | 62.5% |
| Districts Covered | 12 |

## Technology Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Chart.js 4.4.0
- **Fonts**: Google Fonts (Playfair Display, IBM Plex Sans)
- **No Backend Required**: Fully client-side application
- **No Build Process**: Ready to run

## Features in Detail

### Interactive Filtering
- Filter by district, room type, price range
- Real-time chart updates
- Instant search and sorting

### Data Visualizations
- **Bar Charts**: District distribution and performance
- **Pie/Donut Charts**: Room type and verification status
- **Scatter Plots**: Price vs. satisfaction analysis
- **Line Charts**: Distance and trend analysis
- **Radar Charts**: Multi-dimensional performance
- **Bubble Charts**: Quality vs. price comparison

### Responsive Design
- Desktop optimized (1920px+)
- Tablet friendly (768px - 1920px)
- Mobile compatible (< 768px)
- Touch-enabled interactions

## Documentation

Comprehensive guides available in the `docs/` folder:

1. **[PowerBI_Implementation_Guide.md](docs/PowerBI_Implementation_Guide.md)**
   - Step-by-step Power BI setup
   - Data modeling instructions
   - Publishing to Microsoft 365

2. **[DAX_Quick_Reference.md](docs/DAX_Quick_Reference.md)**
   - 50+ ready-to-use DAX formulas
   - KPI calculations
   - Matching algorithm measures

3. **[Dashboard_Layout_Guide.md](docs/Dashboard_Layout_Guide.md)**
   - Visual design specifications
   - Color palettes and typography
   - Layout templates

## Customization

### Update Data
Replace `dashboard_data.json` with your own data:

```javascript
{
  "accommodations": [...],  // Your accommodation data
  "tenants": [...],         // Your tenant data
  "summary": {...},         // Summary statistics
  "districts": {...},       // District aggregations
  "room_types": {...}       // Room type distribution
}
```

### Modify Colors
Edit CSS variables in `Berlin_DSS_Dashboard.html`:

```css
:root {
    --primary: #0f172a;      /* Main background */
    --accent: #f59e0b;       /* Highlight color */
    --text: #f1f5f9;         /* Text color */
    /* ... more variables */
}
```

### Add New Charts
Use Chart.js to create additional visualizations:

```javascript
new Chart(document.getElementById('myChart'), {
    type: 'bar',  // or 'line', 'pie', 'scatter', etc.
    data: { /* your data */ },
    options: { /* your options */ }
});
```

## Deploy to GitHub Pages

1. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from branch `main`
   - Folder: `/ (root)`
   - Save

2. **Your site will be live at:**
   ```
   https://itsamarin.github.io/DSS-Berlin-Housing/
   ```

3. **Custom Domain (Optional)**
   - Add `CNAME` file with your domain
   - Configure DNS records
   - Enable HTTPS

## Use Cases

### For Tenants
- Find accommodations matching your budget and preferences
- Explore different Berlin districts
- Compare satisfaction ratings and reviews
- Get personalized recommendations

### For Landlords
- Analyze market trends and competition
- Optimize pricing strategies
- Track occupancy rates by district
- Identify high-performing property types

### For Researchers
- Study Berlin's housing market dynamics
- Analyze pricing and satisfaction correlations
- Geographic distribution patterns
- Market segmentation analysis

## Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## Project Background

This Decision Support System was developed to address Berlin's housing challenges:

- **Problem**: Tenants face payment fragmentation, listing verification issues, and occupancy uncertainty
- **Solution**: Integrated platform with verified listings, fraud detection, and occupancy optimization
- **Approach**: Hybrid DSS combining Model-Driven, Data-Driven, and Knowledge-Driven components

### DSS Components
1. **Data Management (DMSS)**: Collects and cleans housing data
2. **Model Management (MMSS)**: Predictive models for matching and forecasting
3. **Knowledge Management (KMSS)**: Verification rules and eligibility criteria
4. **User Interface (UIS)**: Interactive dashboards (this project!)

## Academic Context

Based on Simon's Decision-Making Model:
- **Intelligence**: Data collection and validation
- **Design**: Optimal match generation
- **Choice**: Recommendation presentation
- **Implementation**: Allocation tracking

## Related Resources

- [Kaggle: Berlin Rental Market Dataset](https://www.kaggle.com/)
- [Power BI Documentation](https://docs.microsoft.com/power-bi/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [Berlin Open Data Portal](https://daten.berlin.de/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Berlin Open Data for providing city datasets
- Kaggle community for accommodation data
- Chart.js team for excellent visualization library
- Contributors and testers

---

**Made for the Berlin housing community**

[Report Bug](https://github.com/itsamarin/DSS-Berlin-Housing/issues) · [Request Feature](https://github.com/itsamarin/DSS-Berlin-Housing/issues) · [Live Demo](https://itsamarin.github.io/DSS-Berlin-Housing/)

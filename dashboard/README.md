# Interactive Dashboard

This folder contains the web-based interactive dashboard for the Berlin Housing DSS.

## Dashboard File

**`Berlin_DSS_Dashboard.html`** - Main dashboard application

## Features

### Three Main Views

1. **Overview Dashboard**
   - Market insights and key metrics
   - 1,000+ property listings visualization
   - District distribution charts
   - Room type analysis
   - Price vs. satisfaction correlation

2. **Tenant View**
   - **Smart Matching**: AI-powered recommendations based on budget, location, and preferences
   - **Browse All Listings**: Searchable table with advanced filters (district, price, rating, distance, verification)
   - Two-column layout for easy comparison

3. **Landlord Analytics**
   - Revenue analysis by district
   - Occupancy trends tracking
   - Price comparison by room type
   - Guest ratings distribution
   - Booking response time metrics
   - Seasonal revenue forecasting

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Visualization**: Chart.js 4.4.0
- **Design**: Responsive with gradient color scheme
- **Data**: 1,000 programmatically generated sample listings
- **No Backend Required**: Fully client-side application

## Usage

### Local Development
```bash
# Open directly
open Berlin_DSS_Dashboard.html

# Or use local server
python -m http.server 8000
# Visit: http://localhost:8000/dashboard/Berlin_DSS_Dashboard.html
```

### Online Access
Live demo available at: https://itsamarin.github.io/DSS-Berlin-Housing/dashboard/Berlin_DSS_Dashboard.html

## Customization

### Update Data
Modify the `generateListings()` function to change sample data.

### Change Colors
Edit CSS variables in the `<style>` section:
```css
--primary: #0f172a;
--accent: #f59e0b;
```

### Add Charts
Use Chart.js to create new visualizations:
```javascript
new Chart(ctx, {
    type: 'bar',
    data: {...},
    options: {...}
});
```

## Performance

- **Load Time**: <2 seconds
- **Chart Rendering**: Real-time
- **Filter Response**: Instant
- **Data Volume**: Handles 1,000+ listings smoothly

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

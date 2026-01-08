# Dashboard Components Description

Complete documentation of all components in the Berlin Housing DSS Dashboard.

---

## Header Section

### Title
**"Berlin Housing Decision Support System"**
- Main heading displaying the application name
- Gradient color effect (gold to orange to pink)
- Centered at the top of the page

### Subtitle
**"About Integrated Decision Support System (DSS) for Accommodation Matching and Occupancy Optimization in Berlin"**
- Descriptive subtitle explaining the system's purpose
- Light gray text color for contrast

---

## Navigation Tabs

Three main navigation tabs with distinct color schemes:

### 1. Overview Dashboard (Blue)
- **Color**: Blue gradient (#3b82f6 to #2563eb)
- **Purpose**: Provides market-level insights and analytics
- **Icon/Label**: "Overview Dashboard"

### 2. Tenant View (Green)
- **Color**: Green gradient (#10b981 to #059669)
- **Purpose**: Helps tenants find and match with accommodations
- **Icon/Label**: "Tenant View"

### 3. Landlord View (Orange)
- **Color**: Orange gradient (#f59e0b to #d97706)
- **Purpose**: Helps landlords find ideal tenants with AI-powered matching and filtering
- **Icon/Label**: "Landlord View"

---

## Tab 1: Overview Dashboard

### Stat Cards (4 Cards)

#### Card 1: Total Listings
- **Value**: 1,000
- **Label**: "Total Listings"
- **Color**: Blue (#60a5fa)
- **Purpose**: Shows total number of available properties in the system

#### Card 2: Average Price
- **Value**: €950
- **Label**: "Average Price (€/month)"
- **Color**: Green (#34d399)
- **Purpose**: Displays the mean monthly rental price across all listings

#### Card 3: Verified Properties
- **Value**: 820
- **Label**: "Verified Properties"
- **Color**: Orange (#fbbf24)
- **Purpose**: Shows count of verified/trusted listings

#### Card 4: Average Rating
- **Value**: 4.2/5
- **Label**: "Average Rating"
- **Color**: Red (#f87171)
- **Purpose**: Displays overall guest satisfaction score

### Charts (4 Visualizations)

#### Chart 1: Listings by District (Bar Chart)
- **Type**: Horizontal Bar Chart
- **Data**: Count of properties per Berlin district
- **Districts**: Mitte, Kreuzberg, Friedrichshain, Charlottenburg, Prenzlauer Berg
- **Color**: Primary blue gradient
- **Purpose**: Compare property distribution across districts
- **Insights**: Identifies districts with most/least availability

#### Chart 2: Room Type Distribution (Doughnut Chart)
- **Type**: Doughnut Chart
- **Categories**:
  - Entire Place (Blue - #3b82f6)
  - Private Room (Green - #10b981)
  - Shared Room (Orange - #f59e0b)
- **Data**: Percentage breakdown of room types
- **Purpose**: Visualize accommodation type composition
- **Insights**: Shows market preferences and supply

#### Chart 3: Price vs Satisfaction (Scatter Plot)
- **Type**: Scatter Plot
- **X-axis**: Price (€/month)
- **Y-axis**: Guest Satisfaction Rating (1-5)
- **Color**: Semi-transparent blue points
- **Purpose**: Analyze correlation between price and quality
- **Insights**: Identifies value-for-money properties

#### Chart 4: Monthly Booking Trends (Line Chart)
- **Type**: Line Chart with filled area
- **X-axis**: Months (Jan-Dec)
- **Y-axis**: Number of bookings
- **Color**: Blue gradient fill
- **Purpose**: Show seasonal booking patterns
- **Insights**: Helps predict demand fluctuations

### Landlord Performance Analytics Section

This section provides detailed landlord-specific metrics and forecasting within the Overview Dashboard.

#### Stat Cards (4 Metrics)

##### Card 1: Avg. Monthly Revenue
- **Value**: €1,245
- **Purpose**: Shows average income per property per month
- **Color**: Blue gradient

##### Card 2: Occupancy Rate
- **Value**: 78%
- **Purpose**: Percentage of time properties are booked
- **Color**: Green gradient

##### Card 3: Avg. Guest Rating
- **Value**: 4.3/5
- **Purpose**: Average satisfaction score from guests
- **Color**: Orange gradient

##### Card 4: Avg. Days to Book
- **Value**: 12.5
- **Purpose**: Average time from listing to first booking
- **Color**: Red gradient

#### Charts (6 Visualizations)

##### Chart 1: Revenue by District (Bar Chart)
- **Type**: Vertical Bar Chart
- **Data**: Average monthly revenue per district
- **Districts**: Mitte (€1,450), Kreuzberg (€1,200), Friedrichshain (€1,100), Charlottenburg (€1,350), Prenzlauer Berg (€1,250)
- **Color**: Primary gradient
- **Purpose**: Compare revenue performance across locations
- **Y-axis**: Revenue in euros
- **Insights**: Identifies most profitable districts

##### Chart 2: Occupancy Trends (Line Chart)
- **Type**: Line Chart with area fill
- **X-axis**: Weeks (Week 1-4)
- **Y-axis**: Occupancy Rate (0-100%)
- **Data**: Weekly occupancy percentages (72%, 78%, 82%, 76%)
- **Color**: Primary gradient with fill
- **Purpose**: Track booking rate over time
- **Insights**: Shows weekly performance trends

##### Chart 3: Average Price by Room Type (Bar Chart)
- **Type**: Vertical Bar Chart
- **Categories**:
  - Entire Place: €1,350 (Blue)
  - Private Room: €850 (Green)
  - Shared Room: €550 (Orange)
- **Color**: Multi-color (blue, green, orange)
- **Purpose**: Compare pricing across accommodation types
- **Insights**: Shows market rate differences

##### Chart 4: Guest Ratings Distribution (Doughnut Chart)
- **Type**: Doughnut Chart
- **Categories**:
  - 5 Stars: 245 properties (Green)
  - 4-4.9 Stars: 512 properties (Blue)
  - 3-3.9 Stars: 198 properties (Orange)
  - Below 3: 45 properties (Red)
- **Purpose**: Visualize quality distribution
- **Position**: Legend at bottom
- **Insights**: Shows overall portfolio quality

##### Chart 5: Booking Response Time (Line Chart)
- **Type**: Line Chart with points
- **X-axis**: Days of week (Mon-Sun)
- **Y-axis**: Response time in hours
- **Data**: Average response times per day (3.2h, 2.8h, 4.1h, 3.5h, 2.9h, 5.2h, 4.8h)
- **Color**: Pink (#ec4899)
- **Purpose**: Track landlord responsiveness
- **Insights**: Identifies slow response days

##### Chart 6: Seasonal Revenue Forecast (Dual-Line Chart)
- **Type**: Multi-line Chart
- **X-axis**: Months (Jan-Dec)
- **Y-axis**: Revenue (€ in thousands)
- **Lines**:
  1. **Actual Revenue** (Solid green line)
     - Data: Jan-Aug actual performance
     - Shows historical earnings
  2. **Forecast Revenue** (Dashed yellow line)
     - Data: Sep-Dec predictions
     - Shows projected earnings
- **Y-axis Format**: €30k, €35k, €40k, etc.
- **Purpose**: Compare actual vs predicted revenue
- **Insights**: Helps with financial planning

---

## Tab 2: Tenant View

Two-column layout with Smart Matching (left) and Browse Listings (right).

### Left Column: Smart Matching Section

#### Section Header
- **Title**: "Find Your Perfect Accommodation"
- **Color**: Pink (#f9a8d4)
- **Background**: Pink-purple gradient

#### Filter Panel: AI-Powered Smart Matching
- **Title**: "🎯 AI-Powered Smart Matching"
- **Description**: "Get personalized recommendations based on your preferences"
- **Background**: Pink-purple gradient with left border

##### Input Fields:
1. **Budget (€)**
   - Type: Number input
   - Default: 1000
   - Purpose: Set maximum monthly rent

2. **Preferred District**
   - Type: Dropdown select
   - Options: Mitte, Kreuzberg, Friedrichshain, Charlottenburg, Prenzlauer Berg
   - Purpose: Select desired location

3. **Min Rating**
   - Type: Number input
   - Range: 1-5 (step 0.1)
   - Default: 4.0
   - Purpose: Set minimum acceptable rating

##### Action Button:
- **Label**: "Find Best Matches"
- **Color**: Pink gradient (#ec4899 to #db2777)
- **Action**: Triggers AI matching algorithm

#### Results Section: Top Recommendations
- **Title**: "Top Recommendations"
- **Color**: Pink (#f9a8d4)
- **Display**: Cards showing matched properties
- **Content**: Property details with match score

### Right Column: Browse All Listings Section

#### Section Header
- **Title**: "Browse All Listings"
- **Color**: Blue (#60a5fa)
- **Background**: Blue-green gradient

#### Filter Panel: Filter Search
- **Title**: "🔍 Filter Search"
- **Background**: Blue-green gradient

##### Filter Fields:
1. **District**
   - Type: Dropdown
   - Options: All Districts, Mitte, Kreuzberg, Friedrichshain, Charlottenburg, Prenzlauer Berg
   - Purpose: Filter by location

2. **Max Price (€)**
   - Type: Number input
   - Purpose: Set price ceiling

3. **Room Type**
   - Type: Dropdown
   - Options: All Types, Private Room, Entire Place, Shared Room
   - Purpose: Filter by accommodation type

4. **Min Rating**
   - Type: Number input
   - Range: 1-5 (step 0.1)
   - Purpose: Set minimum rating threshold

5. **Max Distance (km)**
   - Type: Number input
   - Purpose: Limit distance from city center

6. **Verified Only**
   - Type: Dropdown
   - Options: All Properties, Verified Only, Unverified Only
   - Purpose: Filter by verification status

##### Action Button:
- **Label**: "Search Listings"
- **Color**: Blue gradient (#3b82f6 to #2563eb)
- **Action**: Applies all filters to listing table

#### Results Table: Property Listings
- **Columns**:
  1. Property - Name and description
  2. District - Berlin neighborhood
  3. Type - Room type (Entire/Private/Shared)
  4. Price (€/month) - Monthly rent
  5. Rating - Guest satisfaction score (x/5)
  6. Distance to Center - Distance in km
  7. Verified - Verification status (✓ Yes / ✗ No)
- **Features**:
  - Scrollable with horizontal overflow
  - Hover effect on rows
  - Empty state message when no results
  - Real-time filtering

---

## Tab 3: Landlord View

This tab focuses on helping landlords find ideal tenants through AI-powered matching and comprehensive filtering capabilities.

### Tenant Matching & Browse Section

Two-column layout with AI Smart Matching (left) and Manual Browse (right).

#### Info Box: Two Ways to Find Tenants
- **Background**: Pink-blue gradient
- **Border**: Left border in pink (#ec4899)
- **Content**:
  - Title: "💡 Two Ways to Find Tenants"
  - Left approach: "⚡ AI Smart Match" - Quick & intelligent recommendations
  - Right approach: "🔍 Manual Browse" - Full control over all tenants
- **Purpose**: Educates users about the two different search methods

### Left Column: AI-Powered Smart Matching

#### Section Header
- **Title**: "🤖 AI-Powered Smart Matching"
- **Badge**: "SMART MATCH" (gold with transparent background)
- **Color**: Pink (#f9a8d4)
- **Background**: Orange gradient

#### Filter Panel: Quick Match
- **Title**: "⚡ Quick Match: Your Best Tenants"
- **Description**: "Just enter your property details - AI instantly analyzes 6+ factors (budget fit, income stability, verification, location match, type preference) and ranks top 5 compatible tenants"
- **Background**: Orange-amber gradient with left gold border
- **Layout**: Two-column grid (label | input)

##### Input Fields:
1. **Your Property District**
   - Type: Dropdown select
   - Options: Mitte, Kreuzberg, Friedrichshain, Charlottenburg, Prenzlauer Berg
   - Purpose: Set property location for matching

2. **Your Asking Price (€)**
   - Type: Number input
   - Default: 1200
   - Purpose: Set monthly rent expectation

3. **Property Type**
   - Type: Dropdown select
   - Options: Entire Place, Private Room, Shared Room
   - Purpose: Specify accommodation type

4. **Min Tenant Budget (€)**
   - Type: Number input
   - Default: 1000
   - Purpose: Filter out tenants below budget threshold

5. **Preferred Tenant Type**
   - Type: Dropdown select
   - Options: All Occupations, Professional, Student, Researcher, Engineer
   - Purpose: Target specific tenant demographics

6. **Priority Factors**
   - Type: Dropdown select
   - Options:
     - Balanced (All Factors) - Default 30/20/15/15/15/5 weights
     - Financial Stability - 40/15/10/10/20/5 weights
     - Location Match - 25/35/15/10/10/5 weights
     - Verification Priority - 20/15/15/35/10/5 weights
   - Purpose: Customize AI weighting algorithm

##### Action Button:
- **Label**: "Find Best Tenant Matches"
- **Color**: Orange gradient (#f59e0b to #d97706)
- **Action**: Triggers AI matching algorithm

#### Results Section: Top 5 AI Recommendations
- **Title**: "Top 5 AI Recommendations"
- **Badge**: "SMART MATCH" (gold with transparent background)
- **Color**: Gold (#fbbf24)
- **Display**: Maximum 5 ranked recommendation cards

##### Recommendation Card Structure:
- **Header**: Rank number + tenant name + match quality badge
  - 🌟 Excellent Match (80-100 score)
  - ✨ Good Match (65-79 score)
  - ⭐ Fair Match (0-64 score)
- **AI Match Score**: 0-100 score with breakdown
- **Score Breakdown**: Shows contribution from each factor:
  - Budget (20-40 points)
  - Location (15-35 points)
  - Type (10-15 points)
  - Verification (10-35 points)
  - Income (10-20 points)
  - Occupation (5 points)
  - Compatibility Bonus (up to 5 points)
- **Details**:
  - Occupation
  - Budget with affordability ratio (Xx your price)
  - Income with 3x rule indicator:
    - ✓ Meets 3x rule (Green)
    - ~ Close to 3x rule (Orange)
    - ✗ Below 3x rule (Red)
  - Preferred District
  - Preferred Type
  - Verification status (✓ Yes / ✗ No)
- **Background**: Orange gradient with gold border
- **Empty State**: Message when no matches found

##### AI Scoring Algorithm:
1. **Budget Match** (20-40%):
   - Perfect: 1-1.3x property price = 100% of weight
   - Overqualified: >1.3x = 85% of weight
   - Below budget: Proportional reduction

2. **Location Match** (15-35%):
   - Exact district = 100% of weight
   - Different district = 50% of weight

3. **Property Type Match** (10-15%):
   - Exact match = 100% of weight
   - Different type = 40% of weight

4. **Verification Status** (10-35%):
   - Verified = 100% of weight
   - Unverified = 30% of weight

5. **Income Stability** (10-20%):
   - Income ≥ 3x rent = 100% of weight (3x rule)
   - Income ≥ 2.5x rent = 80% of weight
   - Below 2.5x = 40% of weight

6. **Occupation Match** (5%):
   - Matches preference = 100% of weight
   - Different occupation = 30% of weight
   - "All" selected = 100% of weight

7. **Compatibility Bonus** (up to 5%):
   - Verified + Income ≥ 3x + Budget matches = 5 bonus points
   - Score capped at 100 maximum

### Right Column: Manual Browse & Compare

#### Section Header
- **Title**: "Browse & Compare All Applicants"
- **Badge**: "FULL DATABASE" (blue with transparent background)
- **Color**: Blue (#60a5fa)
- **Background**: Blue-green gradient

#### Filter Panel: Manual Search & Sorting
- **Title**: "🔍 Manual Search & Sorting"
- **Description**: "Browse full database with custom filters and sorting - great for exploring all options or finding specific criteria"
- **Background**: Blue-green gradient
- **Layout**: Two-column grid (label | input)

##### Filter Fields:
1. **Preferred District**
   - Type: Dropdown
   - Options: All Districts, Mitte, Kreuzberg, Friedrichshain, Charlottenburg, Prenzlauer Berg
   - Purpose: Filter by tenant's preferred location

2. **Min Budget (€)**
   - Type: Number input
   - Purpose: Set minimum tenant budget threshold

3. **Max Budget (€)**
   - Type: Number input
   - Purpose: Set maximum tenant budget threshold

4. **Room Type Preference**
   - Type: Dropdown
   - Options: All Types, Entire Place, Private Room, Shared Room
   - Purpose: Filter by preferred accommodation type

5. **Occupation**
   - Type: Dropdown
   - Options: All Occupations, Student, Professional, Researcher, Engineer, Designer, Teacher, Developer
   - Purpose: Filter by tenant profession

6. **Verified Tenants**
   - Type: Dropdown
   - Options: All Tenants, Verified Only, Unverified Only
   - Purpose: Filter by verification status

7. **Sort By**
   - Type: Dropdown
   - Options:
     - Budget (High to Low) - Default
     - Budget (Low to High)
     - Verification Status
     - Name (A-Z)
   - Purpose: Control table ordering

##### Action Buttons:
- **Primary Button**:
  - Label: "Search Tenants"
  - Color: Blue gradient (#3b82f6 to #2563eb)
  - Action: Applies all filters and sorting
- **Secondary Button**:
  - Label: "Reset Filters"
  - Color: Gray gradient (#6b7280 to #4b5563)
  - Action: Clears all filters, resets to default

#### Results Section: All Tenant Applicants
- **Header Box**:
  - Title: "All Tenant Applicants"
  - Subtitle: "Compare side-by-side | Sort by any column | Filter by multiple criteria"
  - Live Count Badge: Shows filtered result count (e.g., "256 Tenants")
  - Background: Light blue transparent
  - Color: Blue (#60a5fa)

##### Results Table: Tenant Listing
- **Columns**:
  1. **Tenant Name** - Full name
  2. **Preferred District** - Desired location
  3. **Budget (€/month)** - Monthly rental budget
  4. **Income (€/month)** - Monthly income with ratio indicator
     - Color-coded: Green (≥3x), Orange (2.5-3x), Red (<2.5x)
     - Format: "€3,600 (3.0x)"
  5. **Room Type** - Preferred accommodation type
  6. **Occupation** - Professional background
  7. **Verified** - Verification status
     - ✓ Yes (Green) / ✗ No (Red)
- **Features**:
  - Horizontal scroll for overflow
  - Pagination: 50 tenants per page
  - Empty state message when no results
  - Real-time filtering with debounce (300ms)
  - Live tenant count updates

##### Pagination Controls:
- **Display**: Centered below table
- **Elements**:
  - Previous/Next buttons
  - Page numbers with current page highlight
  - Total items count
- **Behavior**:
  - Resets to page 1 on filter change
  - Disabled buttons at boundaries

---

## Color Scheme

### Primary Colors
- **Blue**: #3b82f6, #2563eb, #60a5fa
- **Green**: #10b981, #059669, #34d399
- **Orange**: #f59e0b, #d97706, #fbbf24
- **Pink**: #ec4899, #db2777, #f9a8d4
- **Red**: #ef4444, #f87171

### Background Colors
- **Main Background**: Linear gradient from dark blue (#1e3a8a) to indigo (#312e81) to purple (#4c1d95)
- **Card Backgrounds**: Semi-transparent white with blur effect
- **Chart Containers**: Transparent white (8% opacity) with blur

### Text Colors
- **Primary Text**: Light slate (#f1f5f9)
- **Secondary Text**: Cool gray (#cbd5e1)
- **Headings**: Various bright colors (gold #fbbf24, blue #60a5fa, pink #f9a8d4)

---

## Interactive Elements

### Buttons
- **Hover Effect**: Lift up 2px, yellow glow (#fbbf24)
- **Active State**: Returns to original position
- **Border Radius**: 8px rounded corners

### Tables
- **Row Hover**: Light blue highlight (rgba(59, 130, 246, 0.1))
- **Header**: Blue-green gradient background
- **Borders**: Transparent white dividers

### Charts
- **Hover**: Shows tooltip with exact values
- **Animation**: Smooth rendering on load
- **Responsive**: Auto-resize with window

---

## Data Generation

### Sample Data (1,000 Listings)
- **Districts**: 5 Berlin neighborhoods (random distribution)
- **Types**: Entire Place, Private Room, Shared Room (random)
- **Prices**: Based on type + random variation (€400-€2,200)
- **Ratings**: Random between 3.5 and 5.0
- **Distance**: Random between 1 km and 7 km
- **Verification**: 80% verified rate

### Naming Convention
Format: `[Adjective] [Property Type] [District]`
- Adjectives: Cozy, Modern, Spacious, Charming, Luxury, Budget, Central, etc. (28 options)
- Property Types: Apartment, Studio, Loft, Room, Penthouse, Flat, Suite, Space

---

## Responsive Design

### Desktop (1920px+)
- Full three-tab layout
- Two-column Tenant View
- All charts visible side-by-side

### Tablet (768px - 1920px)
- Maintained layout with adjusted sizing
- Charts stack in pairs

### Mobile (<768px)
- Single column layout
- Tabs stack vertically
- Charts display full-width
- Tables scroll horizontally

### Breakpoint: 1200px
- Two-column Tenant View becomes single column
- Smart Matching stacks above Browse Listings

---

## Performance Optimizations

- **Chart.js CDN**: Fast loading from CDN
- **Client-side Only**: No server requests
- **Lazy Rendering**: Charts render only when tab is active
- **Efficient Filtering**: DOM updates only on filter changes
- **Cached Calculations**: Pre-computed statistics

---

## Accessibility

- **Semantic HTML**: Proper heading hierarchy
- **Color Contrast**: WCAG AA compliant text/background ratios
- **Keyboard Navigation**: Tab-accessible form fields
- **Readable Fonts**: Segoe UI fallback stack
- **Large Click Targets**: Buttons and tabs ≥ 44px

---

## Browser Support

| Browser | Minimum Version |
|---------|----------------|
| Chrome | 90+ |
| Firefox | 88+ |
| Safari | 14+ |
| Edge | 90+ |

### Required Features
- CSS Grid
- Flexbox
- ES6 JavaScript
- Canvas API (for Chart.js)
- CSS Custom Properties

---

## Recent Updates

### Version 1.2 (January 2026)
- **Reorganized Dashboard Structure**:
  - Renamed "Landlord Analytics" tab to "Landlord View"
  - Moved Landlord Performance Analytics (4 stat cards + 6 charts) to Overview Dashboard
  - Landlord View now focuses exclusively on tenant matching and browsing

### Version 1.1 (January 2026)
- Added AI-Powered Smart Matching for landlord-tenant matching
- Implemented advanced scoring algorithm with 6+ factors
- Added customizable priority modes (Balanced, Financial, Location, Verification)
- Implemented Manual Browse & Compare with full database access
- Added live tenant count badge and advanced filtering
- Implemented income-to-rent ratio color coding (3x rule indicator)
- Added two-column grid layout for filter inputs
- Diversified AI Smart Match vs Manual Browse approaches

### Version 1.0 (December 2025)
- Initial dashboard release
- Overview Dashboard with 4 charts
- Tenant View with smart matching
- Landlord View with performance analytics
- Responsive design implementation

---

**Last Updated**: January 8, 2026
**Version**: 1.2
**Dashboard File**: Berlin_DSS_Dashboard.html

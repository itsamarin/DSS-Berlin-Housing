# Analytical Models

This folder contains data models and analytical frameworks used in the DSS.

## Model Types

### 1. Data Model
Defines the structure and relationships of data entities.

**Files:**
- `data_model.pdf` - Entity-relationship diagram
- `schema_documentation.md` - Data schema specifications

**Entities:**
- Accommodations
- Tenants
- Bookings
- Districts
- Reviews

### 2. Matching Algorithm Model
AI-powered recommendation system for tenant-accommodation matching.

**Files:**
- `matching_algorithm.py` - Implementation
- `matching_weights.json` - Scoring weights configuration

**Scoring Components:**
- Price Affordability (30%)
- Location Proximity (20%)
- Guest Satisfaction (30%)
- Verification Status (20%)

### 3. Predictive Models
Forecasting and optimization models for landlord analytics.

**Files:**
- `occupancy_prediction.py` - Occupancy rate forecasting
- `revenue_forecast.py` - Revenue prediction model
- `price_optimization.py` - Dynamic pricing model

**Techniques Used:**
- Linear Regression
- Time Series Analysis (ARIMA)
- K-Nearest Neighbors (KNN)
- Decision Trees

### 4. Fraud Detection Model
Knowledge-based rules for listing verification.

**Files:**
- `fraud_detection_rules.json` - Verification criteria
- `verification_logic.py` - Implementation

**Detection Criteria:**
- Price anomalies
- Review patterns
- Host verification
- Property details consistency

## Model Performance

| Model | Accuracy | Precision | Recall |
|-------|----------|-----------|--------|
| Matching Algorithm | 87% | 85% | 89% |
| Occupancy Prediction | 82% | - | - |
| Fraud Detection | 91% | 88% | 93% |

## Usage

Models are integrated into the dashboard for:
- Real-time recommendations
- Performance analytics
- Fraud prevention
- Revenue optimization

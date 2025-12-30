# Contributing to Berlin Housing DSS

First off, thank you for considering contributing to the Berlin Housing DSS! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)

## 🤝 Code of Conduct

This project and everyone participating in it is governed by respect, inclusivity, and collaboration. By participating, you are expected to uphold this standard.

### Our Standards

- ✅ Using welcoming and inclusive language
- ✅ Being respectful of differing viewpoints
- ✅ Gracefully accepting constructive criticism
- ✅ Focusing on what is best for the community
- ✅ Showing empathy towards other community members

## 🚀 How Can I Contribute?

### 1. Reporting Bugs 🐛

Before creating bug reports, please check existing issues to avoid duplicates.

**Bug Report Template:**
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- Browser: [e.g. Chrome 120]
- OS: [e.g. Windows 11]
- Device: [e.g. Desktop, iPhone 12]
```

### 2. Suggesting Enhancements 💡

**Enhancement Suggestion Template:**
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots.
```

### 3. Code Contributions 💻

We welcome code contributions! Here are areas where you can help:

#### Frontend Enhancements
- [ ] New chart types and visualizations
- [ ] Mobile UI improvements
- [ ] Theme variations (light mode, color schemes)
- [ ] Accessibility improvements (ARIA labels, keyboard navigation)
- [ ] Performance optimizations

#### Data & Analytics
- [ ] Additional data analysis features
- [ ] New matching algorithms
- [ ] Advanced filtering options
- [ ] Export functionality (PDF, Excel)
- [ ] Data validation and cleaning

#### Documentation
- [ ] Tutorial videos
- [ ] API documentation
- [ ] Translation to other languages
- [ ] Use case examples
- [ ] Troubleshooting guides

#### Infrastructure
- [ ] CI/CD improvements
- [ ] Testing framework
- [ ] Docker containerization
- [ ] Backend API (optional)
- [ ] Database integration (optional)

## 🛠️ Development Setup

### Prerequisites
- Git
- A modern web browser
- Text editor (VS Code recommended)
- Basic knowledge of HTML, CSS, JavaScript

### Setup Steps

1. **Fork the repository**
   - Click the "Fork" button on GitHub

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/berlin-housing-dss.git
   cd berlin-housing-dss
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Edit files in your favorite editor
   - Test in browser by opening `Berlin_DSS_Dashboard.html`

5. **Test locally**
   ```bash
   # Option 1: Simple
   open Berlin_DSS_Dashboard.html
   
   # Option 2: Local server (recommended)
   python -m http.server 8000
   # Visit: http://localhost:8000
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template

## 📝 Pull Request Process

### Before Submitting

- [ ] Test your changes in multiple browsers
- [ ] Ensure mobile responsiveness
- [ ] Check for console errors
- [ ] Update documentation if needed
- [ ] Add comments to complex code
- [ ] Follow the style guidelines below

### PR Template

```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature that breaks existing functionality)
- [ ] Documentation update

## Testing
How have you tested this?
- [ ] Desktop Chrome
- [ ] Desktop Firefox
- [ ] Desktop Safari
- [ ] Mobile Chrome
- [ ] Mobile Safari

## Screenshots
If applicable, add screenshots.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have commented complex sections
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested on multiple browsers
```

## 🎨 Style Guidelines

### JavaScript

```javascript
// Use ES6+ features
const data = { ...existingData };

// Use descriptive variable names
const averagePrice = calculateAverage(prices);

// Use arrow functions
const processData = (item) => {
    return item.price * 1.2;
};

// Use template literals
const message = `Total: ${total} items`;

// Add comments for complex logic
// Calculate matching score based on weighted algorithm
const matchScore = (price * 0.3) + (distance * 0.2) + 
                   (satisfaction * 0.3) + (verification * 0.2);
```

### CSS

```css
/* Use CSS variables for colors */
:root {
    --primary-color: #0f172a;
    --accent-color: #f59e0b;
}

/* Use meaningful class names */
.chart-container { }
.kpi-card { }
.filter-group { }

/* Group related properties */
.button {
    /* Positioning */
    position: relative;
    
    /* Box model */
    padding: 1rem 2rem;
    margin: 0.5rem;
    
    /* Visual */
    background: var(--accent-color);
    border-radius: 8px;
    
    /* Typography */
    font-size: 1rem;
    font-weight: 600;
    
    /* Transitions */
    transition: all 0.3s ease;
}

/* Mobile-first approach */
.container {
    width: 100%;
}

@media (min-width: 768px) {
    .container {
        max-width: 1200px;
    }
}
```

### HTML

```html
<!-- Use semantic HTML -->
<header>
    <nav>
        <ul>
            <li><a href="#overview">Overview</a></li>
        </ul>
    </nav>
</header>

<main>
    <section id="overview">
        <h2>Dashboard Overview</h2>
    </section>
</main>

<footer>
    <p>&copy; 2025 Berlin Housing DSS</p>
</footer>

<!-- Add ARIA labels for accessibility -->
<button aria-label="Open filter menu">
    Filter
</button>

<!-- Use data attributes for JS hooks -->
<div data-chart-type="bar" data-chart-id="district-chart">
</div>
```

### Git Commit Messages

Follow conventional commits:

```
feat: add new chart type for district analysis
fix: resolve mobile responsiveness issue
docs: update installation instructions
style: format code with prettier
refactor: simplify matching algorithm
test: add unit tests for data processing
chore: update dependencies
```

## 🧪 Testing Guidelines

### Browser Testing
Test in these browsers (minimum):
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

### Mobile Testing
Test on:
- iPhone (Safari)
- Android (Chrome)
- Tablet views

### Accessibility Testing
- Use keyboard navigation
- Test with screen readers
- Check color contrast ratios
- Verify ARIA labels

### Performance Testing
- Check load time (<3 seconds)
- Monitor memory usage
- Test with large datasets
- Verify chart rendering speed

## 📚 Documentation Guidelines

### Code Comments

```javascript
/**
 * Calculate matching score for accommodation
 * @param {Object} accommodation - Accommodation data
 * @param {Object} preferences - User preferences
 * @returns {number} Match score (0-1)
 */
function calculateMatchScore(accommodation, preferences) {
    // Implementation
}
```

### README Updates

When adding features, update:
- Feature list
- Usage instructions
- Screenshots (if UI changed)
- API documentation (if applicable)

### Inline Documentation

```javascript
// Good: Explains WHY, not WHAT
// Filter accommodations to prevent division by zero
const validAccommodations = data.filter(a => a.capacity > 0);

// Bad: States the obvious
// Loop through array
for (let i = 0; i < array.length; i++) { }
```

## 🐛 Reporting Bugs

### Security Vulnerabilities

**DO NOT** open public issues for security vulnerabilities. Instead:
- Email: security@example.com
- Use GitHub Security Advisories
- We'll respond within 48 hours

### Regular Bugs

Use GitHub Issues with:
1. Clear title
2. Reproduction steps
3. Expected vs actual behavior
4. Environment details
5. Screenshots/videos if applicable

## 💡 Suggesting Enhancements

We love new ideas! When suggesting enhancements:

1. **Check existing suggestions** to avoid duplicates
2. **Explain the use case** - why is this needed?
3. **Provide examples** - show similar features
4. **Consider implementation** - is it feasible?
5. **Think about users** - who benefits?

## 🎯 Priority Areas

We're particularly interested in contributions for:

### High Priority
- 🔴 Mobile UI improvements
- 🔴 Performance optimizations
- 🔴 Accessibility enhancements
- 🔴 Bug fixes

### Medium Priority
- 🟡 New visualizations
- 🟡 Additional filters
- 🟡 Export features
- 🟡 Theme variations

### Low Priority
- 🟢 Code refactoring
- 🟢 Documentation improvements
- 🟢 Nice-to-have features

## 🎓 Learning Resources

New to contributing? Here are some resources:

- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [JavaScript.info](https://javascript.info/)

## 📞 Getting Help

Stuck? Need help?

- 💬 [GitHub Discussions](https://github.com/your-username/berlin-housing-dss/discussions)
- 📧 Email: help@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com/yourhandle)

## 🏆 Recognition

All contributors will be:
- Added to the Contributors list
- Mentioned in release notes
- Given credit in documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Berlin Housing DSS! 🙏

Every contribution, no matter how small, makes a difference. Whether it's fixing a typo, reporting a bug, or adding a major feature - we appreciate your effort! 

Happy coding! 💻✨

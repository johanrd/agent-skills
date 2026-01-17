---
title: Semantic HTML and ARIA Attributes
impact: HIGH
impactDescription: Essential for screen reader users
tags: accessibility, a11y, semantic-html, aria
---

## Semantic HTML and ARIA Attributes

Use semantic HTML elements and proper ARIA attributes to make your application accessible to screen reader users. Prefer semantic elements over divs with ARIA roles.

**Incorrect (divs with insufficient semantics):**

```handlebars
<div class="button" {{on "click" this.submit}}>
  Submit
</div>

<div class="nav">
  <div class="nav-item">Home</div>
  <div class="nav-item">About</div>
</div>

<div class="alert">
  {{this.message}}
</div>
```

**Correct (semantic HTML with proper ARIA):**

```handlebars
<button type="submit" {{on "click" this.submit}}>
  Submit
</button>

<nav aria-label="Main navigation">
  <ul>
    <li><LinkTo @route="index">Home</LinkTo></li>
    <li><LinkTo @route="about">About</LinkTo></li>
  </ul>
</nav>

<div role="alert" aria-live="polite" aria-atomic="true">
  {{this.message}}
</div>
```

**For interactive custom elements:**

```handlebars
<div 
  role="button" 
  tabindex="0"
  {{on "click" this.handleClick}}
  {{on "keydown" this.handleKeyDown}}
  aria-label="Close dialog"
>
  <XIcon />
</div>
```

```javascript
// app/components/custom-button.js
import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class CustomButtonComponent extends Component {
  @action
  handleKeyDown(event) {
    // Support Enter and Space keys for keyboard users
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      this.handleClick();
    }
  }
  
  @action
  handleClick() {
    this.args.onClick?.();
  }
}
```

Always use native semantic elements when possible. When creating custom interactive elements, ensure they're keyboard accessible and have proper ARIA attributes.

Reference: [Ember Accessibility Guide](https://guides.emberjs.com/release/accessibility/)

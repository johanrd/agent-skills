---
title: Lazy Load Heavy Dependencies
impact: CRITICAL
impactDescription: 30-50% initial bundle reduction
tags: bundle, lazy-loading, dynamic-imports, performance
---

## Lazy Load Heavy Dependencies

Use dynamic imports to load heavy libraries only when needed, reducing initial bundle size.

**Incorrect (loaded upfront):**

```javascript
import Component from '@glimmer/component';
import Chart from 'chart.js/auto'; // 300KB library loaded immediately
import hljs from 'highlight.js'; // 500KB library loaded immediately

export default class DashboardComponent extends Component {
  get showChart() {
    return this.args.hasData;
  }
}
```

**Correct (lazy loaded when needed):**

```javascript
import Component from '@glimmer/component';
import { tracked } from '@glimmer/tracking';
import { action } from '@ember/object';

export default class DashboardComponent extends Component {
  @tracked ChartComponent = null;
  @tracked highlighter = null;

  @action
  async loadChart() {
    if (!this.ChartComponent) {
      const { default: Chart } = await import('chart.js/auto');
      this.ChartComponent = Chart;
    }
  }

  @action
  async highlightCode(code) {
    if (!this.highlighter) {
      const { default: hljs } = await import('highlight.js');
      this.highlighter = hljs;
    }
    return this.highlighter.highlightAuto(code);
  }
}
```

**Alternative (use template helper for components):**

```javascript
// app/helpers/ensure-loaded.js
import { helper } from '@ember/component/helper';

export default helper(async function ensureLoaded([modulePath]) {
  const module = await import(modulePath);
  return module.default;
});
```

Dynamic imports reduce initial bundle size by 30-50%, improving Time to Interactive.

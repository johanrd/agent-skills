---
title: Use Modifiers for DOM Side Effects
impact: LOW-MEDIUM
impactDescription: Better separation of concerns
tags: modifiers, dom, lifecycle, advanced
---

## Use Modifiers for DOM Side Effects

Use modifiers (element modifiers) to handle DOM side effects and lifecycle events in a reusable, composable way.

**Incorrect (component lifecycle hooks):**

```javascript
// app/components/chart.js
import Component from '@glimmer/component';
import { action } from '@ember/object';

export default class ChartComponent extends Component {
  chartInstance = null;
  
  @action
  setupChart(element) {
    this.chartInstance = new Chart(element, this.args.config);
  }
  
  willDestroy() {
    super.willDestroy(...arguments);
    this.chartInstance?.destroy();
  }
}
```

```handlebars
<canvas {{did-insert this.setupChart}}></canvas>
```

**Correct (reusable modifier):**

```javascript
// app/modifiers/chart.js
import Modifier from 'ember-modifier';
import { registerDestructor } from '@ember/destroyable';

export default class ChartModifier extends Modifier {
  chartInstance = null;

  modify(element, [config]) {
    // Cleanup previous instance if config changed
    if (this.chartInstance) {
      this.chartInstance.destroy();
    }
    
    this.chartInstance = new Chart(element, config);
    
    // Register cleanup
    registerDestructor(this, () => {
      this.chartInstance?.destroy();
    });
  }
}
```

```handlebars
<canvas {{chart @config}}></canvas>
```

**For commonly needed modifiers, use ember-modifier helpers:**

```javascript
// app/modifiers/autofocus.js
import { modifier } from 'ember-modifier';

export default modifier((element) => {
  element.focus();
});
```

```handlebars
<input {{autofocus}} type="text" />
```

**Use ember-resize-observer-modifier for resize handling:**

```bash
ember install ember-resize-observer-modifier
```

```handlebars
<div {{on-resize this.handleResize}}>
  Content that responds to size changes
</div>
```

Modifiers provide a clean, reusable way to manage DOM side effects without coupling to specific components.

Reference: [Ember Modifiers](https://guides.emberjs.com/release/components/template-lifecycle-dom-and-modifiers/)

---
title: Avoid Heavy Computation in Templates
impact: MEDIUM
impactDescription: 40-60% reduction in render time
tags: templates, performance, getters, helpers
---

## Avoid Heavy Computation in Templates

Move expensive computations from templates to cached getters in the component class. Templates should only display data, not compute it.

**Incorrect (computation in template):**

```handlebars
<div class="stats">
  <p>Total: {{sum (map this.items "price")}}</p>
  <p>Average: {{div (sum (map this.items "price")) this.items.length}}</p>
  <p>Max: {{max (map this.items "price")}}</p>
  
  {{#each (sort-by "name" this.items) as |item|}}
    <div>{{item.name}}: {{multiply item.price item.quantity}}</div>
  {{/each}}
</div>
```

**Correct (computation in component):**

```javascript
// app/components/stats.js
import Component from '@glimmer/component';
import { cached } from '@glimmer/tracking';

export default class StatsComponent extends Component {
  @cached
  get total() {
    return this.args.items.reduce((sum, item) => sum + item.price, 0);
  }
  
  @cached
  get average() {
    return this.args.items.length > 0 
      ? this.total / this.args.items.length 
      : 0;
  }
  
  @cached
  get maxPrice() {
    return Math.max(...this.args.items.map(item => item.price));
  }
  
  @cached
  get sortedItems() {
    return [...this.args.items].sort((a, b) => 
      a.name.localeCompare(b.name)
    );
  }
  
  @cached
  get itemsWithTotal() {
    return this.sortedItems.map(item => ({
      ...item,
      total: item.price * item.quantity
    }));
  }
}
```

```handlebars
<div class="stats">
  <p>Total: {{this.total}}</p>
  <p>Average: {{this.average}}</p>
  <p>Max: {{this.maxPrice}}</p>
  
  {{#each this.itemsWithTotal key="id" as |item|}}
    <div>{{item.name}}: {{item.total}}</div>
  {{/each}}
</div>
```

Moving computations to cached getters ensures they run only when dependencies change, not on every render.

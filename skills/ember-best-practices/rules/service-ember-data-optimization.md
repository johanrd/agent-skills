---
title: Optimize Ember Data Queries
impact: MEDIUM-HIGH
impactDescription: 40-70% reduction in API calls
tags: ember-data, performance, api, optimization
---

## Optimize Ember Data Queries

Use Ember Data's query features effectively to reduce API calls and load only the data you need.

**Incorrect (multiple queries, overfetching):**

```javascript
// app/routes/posts.js
export default class PostsRoute extends Route {
  @service store;
  
  async model() {
    // Loads all posts (could be thousands)
    const posts = await this.store.findAll('post');
    
    // Then filters in memory
    return posts.filter(post => post.status === 'published');
  }
}
```

**Correct (filtered query with pagination):**

```javascript
// app/routes/posts.js
export default class PostsRoute extends Route {
  @service store;
  
  queryParams = {
    page: { refreshModel: true },
    filter: { refreshModel: true }
  };
  
  model(params) {
    // Server-side filtering and pagination
    return this.store.query('post', {
      filter: {
        status: 'published'
      },
      page: {
        number: params.page || 1,
        size: 20
      },
      include: 'author', // Sideload related data
      fields: { // Sparse fieldsets
        posts: 'title,excerpt,publishedAt,author',
        users: 'name,avatar'
      }
    });
  }
}
```

**Use findRecord with includes for single records:**

```javascript
// app/routes/post.js
export default class PostRoute extends Route {
  @service store;
  
  model(params) {
    return this.store.findRecord('post', params.post_id, {
      include: 'author,comments.user', // Nested relationships
      reload: true // Force fresh data
    });
  }
}
```

**For frequently accessed data, use peek to avoid API calls:**

```javascript
// app/components/user-badge.js
export default class UserBadgeComponent extends Component {
  @service store;
  
  get user() {
    // Check store first, avoiding API call if already loaded
    const cached = this.store.peekRecord('user', this.args.userId);
    if (cached) {
      return cached;
    }
    
    // Only fetch if not in store
    return this.store.findRecord('user', this.args.userId);
  }
}
```

**Use adapterOptions for custom queries:**

```javascript
model() {
  return this.store.query('post', {
    adapterOptions: {
      include: 'author,tags',
      customParam: 'value'
    }
  });
}
```

Efficient Ember Data usage reduces network overhead and improves application performance significantly.

Reference: [Ember Data Guides](https://guides.emberjs.com/release/models/)

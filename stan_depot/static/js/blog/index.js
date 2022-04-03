let app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  data: {
    posts: [],
    pageSize: 1,
    width: window.innerWidth,
  },
  methods: {
    async getPosts(pageSize) {
      await fetch(`http://127.0.0.1:8000/blog/api/posts/?format=json&page_size=${pageSize}`)
        .then(response => response.json())
        .then(data => {
          for (const result of data['results']) {
            result['url'] = `${document.URL}${result['slug']}/`;
            this.posts.push(result);
          }
          this.pageSize += 1;
        }).catch(() => console.error('No more posts'));

    },
    async scrollGetPosts() {
      let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
      if (bottomOfWindow) {
        await this.getPosts(this.pageSize);
      }
    }
  },
  async beforeMount() {
    await this.getPosts(this.pageSize);
  },
  async mounted() {
    window.addEventListener('scroll', await this.scrollGetPosts);
  },
});


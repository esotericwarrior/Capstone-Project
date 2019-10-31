<template>
  <div class="home">
    <NewsFeed />
  </div>
</template>

<script>
import { NewsFeed } from "@/components/Application/NewsFeed";

export default {
  name: "home",
  components: {
    NewsFeed
  }
};
</script>

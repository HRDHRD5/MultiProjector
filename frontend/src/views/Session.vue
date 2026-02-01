<template>
  <div class="fixed top-5 left-5">
    <Button asChild v-slot="slotProps" class="absolute">
      <RouterLink :to="`/`" :class="slotProps.class">
        Home
      </RouterLink>
    </Button>
  </div>
  <div v-if="session" class="p-20 min-h-[80vh]">
    <Card class="min-h-[60vh] w-full">
      <template #title>
        {{ session.title }}
      </template>
      <template #content>

      </template>
      <template #footer>
        Open since {{ new Date(session["start"]).toLocaleString(locale, {
          year: 'numeric', month:
            'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit'
        }) }}
      </template>
    </Card>
  </div>
  <div v-if="!session" class="fixed top-0 left-0 w-full h-full flex items-center justify-center">
    <Card v-if="loaded">
      <template #title>
        Failed to load session
      </template>
    </Card>
    <Card v-else class="text-center! flex! items-center! justify-center!">
      <template #title>
        <h1 class="text-[1.5rem]">Loading...</h1>
      </template>
      <template #content>
        <i class="pi pi-spin pi-spinner text-[4rem]!"></i>
      </template>
    </Card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const session = ref();
const loaded = ref(false);

function loadSession() {
  fetch(`/streaming-api/sessions/${route.params.session_id}/`).then(response => response.json().then(data => {
    session.value = data;
    loaded.value = true;
  })).catch(error => {
    loaded.value = true;
  });
}

loadSession();
</script>
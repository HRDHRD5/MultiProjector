<template>
  <div class="grid grid-cols-4 gap-20 p-10 overflow-hidden">
    <Card v-for="session in sessions">
      <template #title>
        {{ session["title"] }} ({{ session["resolution_x"] }}x{{ session["resolution_y"] }})
      </template>
      <template #subtitle>
        Open since {{ new Date(session["start"]).toLocaleString(locale, {
          year: 'numeric', month:
            'numeric', day: 'numeric', hour: '2-digit', minute: '2-digit'
        }) }}
      </template>
      <template #footer>
        <div class="flex justify-end">
          <Button asChild v-slot="slotProps">
            <RouterLink :to="`/session/${session['id']}`" :class="slotProps.class">
              Join
            </RouterLink>
          </Button>
        </div>
      </template>
    </Card>
    <Card>
      <template #title>
        Add your own Session
      </template>
      <template #subtitle>
        Open a public Session
      </template>
      <template #footer>
        <div class="flex justify-end">
          <CreateSession @created="loadSessions"/>
        </div>
      </template>
    </Card>
    <div v-if="sessions.length == 0" class="fixed z-[-50] top-0 left-0 w-full h-full flex items-center justify-center">
      <Card v-if="loaded">
        <template #title>
          There are no sessions available!
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
  </div>
</template>

<script setup lang="ts">
import CreateSession from '@/components/dialogs/CreateSession.vue';
import { ref } from 'vue';

const sessions = ref([]);
const loaded = ref(false);

function loadSessions() {
  fetch(`/streaming-api/sessions/`).then(response => response.json().then(data => {
    sessions.value = data;
    loaded.value = true;
  })).catch(error => {
    loaded.value = true;
  });
}

loadSessions();
</script>
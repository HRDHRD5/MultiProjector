<template>
    <Button label="Create" @click="createsessionVisible = true;" />
    <Dialog v-model:visible="createsessionVisible" modal header="Create Session" :style="{ width: '25rem' }">
        <div class="flex items-center gap-4 mb-4">
            <label class="font-semibold w-24">Name</label>
            <InputText v-model="sessionName" placeholder="Session Name" class="flex-auto" autocomplete="off" />
        </div>
        <div class="flex items-center gap-4 mb-4">
            <label class="font-semibold w-24">Resolution</label>
            <Select v-model="selectedResolution" :options="standardResolutions" placeholder="Select Resolution"
                option-label="name"></Select>
        </div>
        <div v-if="customResolution" class="flex items-center gap-4 mb-2">
            <label class="font-semibold w-24">Custom Resolution</label>
            <InputText type="number" v-model="resolutionX" class="max-w-1/4" autocomplete="off" />
            <InputText type="number" v-model="resolutionY" class="max-w-1/4" autocomplete="off" />
        </div>
        <template #footer>
            <Button label="Cancel" text severity="secondary" @click="createsessionVisible = false" autofocus />
            <Button label="Create" variant="outlined" @click="createSession();" autofocus />
        </template>
    </Dialog>
</template>

<script setup lang="ts">
import { getCookie } from '@/global';
import { ref, watch } from 'vue';

const emit = defineEmits(['created']);

const createsessionVisible = ref(false);
const customResolution = ref(false);
const selectedResolution = ref();
const sessionName = ref("");
const resolutionX = ref();
const resolutionY = ref();

const standardResolutions = ref([
    { name: 'Custom', code: 'custom', x: 1920, y: 1080 },
    { name: '1280 x 720', code: '1280x720', x: 1280, y: 720 },
    { name: '1920 x 1080', code: '1920x1080', x: 1920, y: 1080 },
    { name: '2560 x 1440', code: '2560x1440', x: 2560, y: 1440 },
    { name: '3840 x 2160', code: '3840x2160', x: 3840, y: 2160 },
    { name: '7680 x 4320', code: '7680x4320', x: 7680, y: 4320 },
]);

watch(selectedResolution, (selected) => {
    if (selected == null) { return; }
    customResolution.value = selected.code == "custom";

    resolutionX.value = selected.x;
    resolutionY.value = selected.y;
});

function createSession() {
    fetch(`/streaming-api/sessions/`, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            "title": sessionName.value,
            "resolution_x": resolutionX.value,
            "resolution_y": resolutionY.value
        })
    }).then(response => {
        if (response.status >= 200 && response.status < 300) {
            emit("created");
            createsessionVisible.value = false;
        }
    });
}

watch(createsessionVisible, () => {
    if (createsessionVisible) {
        sessionName.value = "";
        customResolution.value = false;
        selectedResolution.value = null;
        resolutionX.value = null;
        resolutionY.value = null;
    }
});
</script>
import './assets/main.css'

import { createApp } from 'vue';
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import { definePreset } from '@primeuix/themes';
import App from './App.vue';
import router from './router';
import { getCookie, setCookie, setDarkMode } from './global';

const app = createApp(App)

const customDesign = definePreset(Aura, {
    semantic: {
        primary: {
            50: '{zinc.50}',
            100: '{zinc.100}',
            200: '{zinc.200}',
            300: '{zinc.300}',
            400: '{zinc.400}',
            500: '{zinc.500}',
            600: '{zinc.600}',
            700: '{zinc.700}',
            800: '{zinc.800}',
            900: '{zinc.900}',
            950: '{zinc.950}'
        },
        colorScheme: {
            light: {
                primary: {
                    color: '#00ff99',
                    inverseColor: '#ffffff',
                    hoverColor: '{zinc.900}',
                    activeColor: '{zinc.800}'
                },
                highlight: {
                    background: '{zinc.950}',
                    focusBackground: '{zinc.700}',
                    color: '#ffffff',
                    focusColor: '#ffffff'
                },
            },
            dark: {
                primary: {
                    color: '#00ff99',
                    inverseColor: '{zinc.950}',
                    hoverColor: '{zinc.100}',
                    activeColor: '{zinc.200}'
                },
                highlight: {
                    background: 'rgba(250, 250, 250, .16)',
                    focusBackground: 'rgba(250, 250, 250, .24)',
                    color: 'rgba(255,255,255,.87)',
                    focusColor: 'rgba(255,255,255,.87)'
                },
            }
        }
    }
});

app.use(PrimeVue, {
    // Default theme configuration
    theme: {
        preset: customDesign,
        options: {
            prefix: 'p',
            darkModeSelector: '.dark-mode',
            cssLayer: false
        }
    }
});

// Handle initial Dark Mode
const darkModeEnabled = getCookie("dark-mode");
if (darkModeEnabled === null) {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        setCookie("dark-mode", "true", 100000000000);
        setDarkMode(true);
    }
    else {
        setCookie("dark-mode", "false", 100000000000);
        setDarkMode(false);
    }
}
else if (darkModeEnabled.toLowerCase() == "false") {
    setDarkMode(false);
}
else {
    setDarkMode(true);
}

app.use(router)

app.mount('#app')

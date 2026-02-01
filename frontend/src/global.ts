export function setDarkMode(enabled: boolean) {
	if (enabled) {
		document.documentElement.classList.add('dark-mode');
	}
	else {
		document.documentElement.classList.remove('dark-mode');
	}
	setCookie("dark-mode", enabled ? "true" : "false", 100000000000);
}

export function getCookie(name: string): string | null {
	const nameLenPlus = (name.length + 1);
	return document.cookie
		.split(';')
		.map(c => c.trim())
		.filter(cookie => {
			return cookie.substring(0, nameLenPlus) === `${name}=`;
		})
		.map(cookie => {
			return decodeURIComponent(cookie.substring(nameLenPlus));
		})[0] || null;
}

export function setCookie(name: string, value: string, days: number) {
	var expires = "";
	if (days) {
		var date = new Date();
		date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		expires = "; expires=" + date.toUTCString();
	}
	document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

export default { getCookie };
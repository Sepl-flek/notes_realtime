const editor = document.getElementById("editor");
const status = document.getElementById("status");

let protocol = window.location.protocol === "https:" ? "wss" : "ws";
let wsUrl = `${protocol}://${window.location.host}/ws/notes/`;
let socket = new WebSocket(wsUrl);

socket.onopen = () => {
    status.textContent = "🟢 Подключено";
};

socket.onclose = () => {
    status.textContent = "🔴 Отключено";
};

socket.onerror = () => {
    // подавим всплытие в консоли, статус уже обновится onclose
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    if (editor.value !== data.message) {
        editor.value = data.message;
    }
};

let timeout = null;
editor.addEventListener("input", () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => {
        if (socket && socket.readyState === WebSocket.OPEN) {
            socket.send(JSON.stringify({ message: editor.value }));
        }
    }, 300);
});

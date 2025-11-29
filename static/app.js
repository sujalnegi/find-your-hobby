const apiBase = "";

function el(q) { return document.querySelector(q) }

function escapeHtml(s) { return s && s.replace ? s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;") : s }

function buildPayload() {
    return {
        interest: (el("#interest") && el("#interest").value) ? el("#interest").value.trim() : "",
        environment: el("#environment").value,
        physical: el("#physical") ? el("#physical").value : "low",
        creative: el("#creative").value,
        social: el("#social").value,
        budget: el("#budget").value,
        time: el("#time").value
    }
}

function attachHandlers() {
    console.log("App initialized. Waiting for user interaction...");
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
        attachHandlers();
    })
} else {
    attachHandlers();
}

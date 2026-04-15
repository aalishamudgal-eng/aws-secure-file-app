const API_URL = "YOUR_API_GATEWAY_URL";

async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];

    if (!file) {
        alert("Select a file first!");
        return;
    }

    const response = await fetch(API_URL + "/upload", {
        method: "POST",
        body: file
    });

    const result = await response.json();
    alert(result.message);

    loadFiles();
}

async function loadFiles() {
    const response = await fetch(API_URL + "/files");
    const files = await response.json();

    const list = document.getElementById("fileList");
    list.innerHTML = "";

    files.forEach(file => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${file.url}" target="_blank">${file.name}</a>`;
        list.appendChild(li);
    });
}

window.onload = loadFiles;

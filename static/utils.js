
function copyToClipboard(elementId) {
    const text = document.getElementById(elementId).value;
    navigator.clipboard.writeText(text).then(() => {
        alert("Copied to clipboard!");
    });
}
function clearFields(...ids) {
    ids.forEach(id => {
        const el = document.getElementById(id);
        if (el) el.value = '';
    });
}
function livePreview(inputId, outputId, transformFn) {
    document.getElementById(inputId).addEventListener('input', function () {
        document.getElementById(outputId).innerText = transformFn(this.value);
    });
}

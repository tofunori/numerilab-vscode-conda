// Force download for .ipynb files
function downloadNotebook(url, filename) {
    fetch(url)
        .then(response => response.blob())
        .then(blob => {
            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);
            link.download = filename;
            link.click();
            window.URL.revokeObjectURL(link.href);
        })
        .catch(error => {
            console.error('Download failed:', error);
            // Fallback to opening in new tab
            window.open(url, '_blank');
        });
}

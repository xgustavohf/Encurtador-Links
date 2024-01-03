document.addEventListener('DOMContentLoaded', function () {
    var clipboard = new ClipboardJS('#btnCopiar', {
        text: function () {
            return document.getElementById('linkEncurtado').href;
        }
    });

    clipboard.on('success', function (e) {
        alert('Link copiado com sucesso!');
        e.clearSelection();
    });
});
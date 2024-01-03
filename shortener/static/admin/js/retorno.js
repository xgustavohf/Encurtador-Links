function copiarLink() {
    var linkEncurtado = document.getElementById("linkEncurtado");
    
    if (linkEncurtado) {
        var textoAreaTransferencia = document.createElement("textarea");
        textoAreaTransferencia.value = linkEncurtado.textContent;

        document.body.appendChild(textoAreaTransferencia);

        textoAreaTransferencia.select();
        textoAreaTransferencia.setSelectionRange(0, 99999); 

        document.execCommand("copy");

        document.body.removeChild(textoAreaTransferencia);

        alert("Link copiado para a área de transferência!");
    } else {
        alert("Elemento com ID 'linkEncurtado' não encontrado.");
    }
}

document.getElementById("copiarLinkBtn").addEventListener("click", copiarLink);

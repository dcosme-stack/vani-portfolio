
function openModal(param) {
    let img_details = param.src;
    let alt_details = param.alt;
    document.getElementById("modal-img").src = img_details;
    document.getElementById("modal-img").alt = alt_details;
    document.getElementById("modal-container").style.display = "block";
}
function closeModal() {
    let checkObj = event.target.id;
    if (checkObj === "modal-container") {
        document.getElementById("modal-container").style.display = "none";
    }
}

function closeModalX() {
    document.getElementById("modal-container").style.display = "none";
}

window.addEventListener("keydown",(event)=>{
    if (event.key ==='Escape'){
        document.getElementById("modal-container").style.display = "none";
    }
});
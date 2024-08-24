function Favorite(number_card) {
    let toastLiveExample = document.getElementById("favorite_card" + number_card);
    let toast = new bootstrap.Toast(toastLiveExample);
    toast.show();
}
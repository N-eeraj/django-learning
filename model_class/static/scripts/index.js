// alert("Welcome to this Web App")

const showImg = img => {
    img = "static/images/" + img;
    document.getElementById("selected").setAttribute('src', img);
    document.getElementById("hidden").style.transform = "scale(1)";
}

const closeImg = () => document.getElementById("hidden").style.transform = "scale(0)";
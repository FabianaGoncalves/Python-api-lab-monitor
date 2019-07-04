let userAction;
userAction = async () => {

    const response = await fetch('http://localhost:3030/sala/pc/Laboratório de Redes', {mode: 'cors', method: 'get'},);
    const myJson = await response.json(); //extract JSON from the http response
    var data = myJson;
    console.log(myJson);

    var patrimonio1 = data.patrimonios[0];
    var usuario1 = data.usuarios[0];
    var a = document.getElementById("tabela").rows[1].cells;
    a[0].innerHTML = patrimonio1;
    var b = document.getElementById("tabela").rows[1].cells;
    b[1].innerHTML = usuario1;

    // ---------------------------------------------------------------------------------------------
    // Buttons on off linha 1

    var desligar1 = document.createElement("button");
    desligar1.innerHTML = "Desligar";
    desligar1.style ="background-color:#ff6347; color: white";
    var body = document.getElementById("tabela").rows[1].cells;
    body[2].appendChild(desligar1);
    desligar1.addEventListener("click", function() {
        event.preventDefault();
        window.location.href="http://localhost:3030/att_status/"+patrimonio1+"/False", "_blank";
        alert("Internet de " + usuario1 + " foi desligada");
    });

    var ligar1 = document.createElement("button");
    ligar1.innerHTML = "Ligar";
    ligar1.style = "background-color:green; color: white";
    var body = document.getElementById("tabela").rows[1].cells;
    body[3].appendChild(ligar1);
    ligar1.addEventListener("click", function() {
        event.preventDefault();
        window.location.href="http://localhost:3030/att_status/"+patrimonio1+"/True", "_blank";
        alert("Internet de " + usuario1 + " foi ligada");
    });

    // ----------------------------------------------------------------------------------------
    // normal

    var patrimonio2 = data.patrimonios[1];
    var usuario2 = data.usuarios[1];
    var c = document.getElementById("tabela").rows[2].cells;
    c[0].innerHTML = patrimonio2;
    var d = document.getElementById("tabela").rows[2].cells;
    d[1].innerHTML = usuario2;

// ---------------------------------------------------------------------------------------------
    // Buttons on off linha 2

    var desligar2 = document.createElement("button");
    desligar2.innerHTML = "Desligar";
    desligar2.style ="background-color:#ff6347; color: white";
    var body = document.getElementById("tabela").rows[2].cells;
    body[2].appendChild(desligar2);
    desligar2.addEventListener("click", function() {
        event.preventDefault();
        window.location.href="http://localhost:3030/att_status/"+patrimonio2+"/False";
        alert("Internet de " + usuario2 + " foi desligada");
    });

    var ligar2 = document.createElement("button");
    ligar2.innerHTML = "Ligar";
    ligar2.style = "background-color:green; color: white";
    var body = document.getElementById("tabela").rows[2].cells;
    body[3].appendChild(ligar2);
    ligar2.addEventListener("click", function() {
    event.preventDefault();
        window.location.href="http://localhost:3030/att_status/"+patrimonio2+"/True", "_blank";
        alert("Internet de " + usuario2 + " foi ligada");
    });

    // ----------------------------------------------------------------------------------------
    // normal

    var patrimonio3 = data.patrimonios[2];
    var usuario3 = data.usuarios[2];
    var e = document.getElementById("tabela").rows[3].cells;
    e[0].innerHTML = patrimonio3;
    var f = document.getElementById("tabela").rows[3].cells;
    f[1].innerHTML = usuario3;

    // ---------------------------------------------------------------------------------------------
    // Buttons on off linha 3

//    var desligar3 = document.createElement("button");
//    desligar3.innerHTML = "Desligar";
//    desligar3.style ="background-color:#ff6347; color: white";
//    var body = document.getElementById("tabela").rows[3].cells;
//    body[2].appendChild(desligar3);
//    desligar3.addEventListener("click", function() {
//        event.preventDefault();
//        window.location.href="http://localhost:3030/att_status/"+patrimonio3+"/False";
//        alert("Internet de " + usuario3 + " foi desligada");
//    });
//
//    var ligar3 = document.createElement("button");
//    ligar3.innerHTML = "Ligar";
//    ligar3.style = "background-color:green; color: white";
//    var body = document.getElementById("tabela").rows[3].cells;
//    body[3].appendChild(ligar3);
//    ligar3.addEventListener("click", function() {
//        event.preventDefault();
//        window.location.href="http://localhost:3030/att_status/"+patrimonio3+"/False";
//        alert("Internet de " + usuario3 + " foi ligada");
//    });

    // ----------------------------------------------------------------------------------------
    // normal

    var patrimonio4 = data.patrimonios[3];
    var usuario4 = data.usuarios[3];
    var g = document.getElementById("tabela").rows[4].cells;
    g[0].innerHTML = patrimonio4;
    var h = document.getElementById("tabela").rows[4].cells;
    h[1].innerHTML = usuario4;
};

// ---------------------------------------------------------------------------------------------
    // Buttons on off linha 4

//    var desligar4 = document.createElement("button");
//    desligar4.innerHTML = "Desligar";
//    desligar4.style ="background-color:#ff6347; color: white";
//    var body = document.getElementById("tabela").rows[4].cells;
//    body[2].appendChild(desligar4);
//    desligar4.addEventListener("click", function() {
//        event.preventDefault();
//        window.location.href="http://localhost:3030/att_status/"+patrimonio4+"/False";
//        alert("Internet de " + usuario4 + " foi desligada");
//    });
//
//    var ligar4 = document.createElement("button");
//    ligar4.innerHTML = "Ligar";
//    ligar4.style = "background-color:green; color: white";
//    var body = document.getElementById("tabela").rows[4].cells;
//    body[3].appendChild(ligar4);
//    ligar4.addEventListener("click", function() {
//        event.preventDefault();
//        window.location.href="http://localhost:3030/att_status/"+patrimonio4+"/False";
//        alert("Internet de " + usuario4 + " foi ligada");
//    });

    // ----------------------------------------------------------------------------------------
    // normal

window.onload = function() {
    userAction();
};



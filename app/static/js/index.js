$(function() {
    // Cargar y renderizar el header
    $.get("/static/components/header.hbs", function(templateSource) {
        var template = Handlebars.compile(templateSource);
        $("#header").html(template({titulo: "Mi Tienda"}));
    });

    // Cargar y renderizar las tarjetas de productos
    $.get("/static/components/card.hbs", function(templateSource) {
        var template = Handlebars.compile(templateSource);
        $.getJSON("/products/productos", function(data) {
            var html = '';
            data.forEach(function(producto) {
                html += '<div class="col-md-4">' + template(producto) + '</div>';
            });
            $("#product-cards").html(html);
        });
    });

    // Cargar y renderizar el footer
    $.get("/static/components/footer.hbs", function(templateSource) {
        var template = Handlebars.compile(templateSource);
        $("#footer").html(template({pie_de_pagina: "Todos los derechos reservados."}));
    });
});
odoo.define('theme_cim.team', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var utils = require("web.utils");
    var qweb = core.qweb;
    var lang = utils.get_cookie("frontend_lang");
    jQuery(document).ready(function($) {
    console.log('----------------team------------',lang);
        $('.carousel-team').owlCarousel({
            rtl:(lang === "ar_SY") ? true : false,
            loop: true,
            nav: true,
            dots: true,
            margin: 20,
            navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
            autoplay: 4000,
            smartSpeed: 1000,
            responsive: {
                0: {
                    items: 1,
                },
                576: {
                    items: 2,
                },
                768: {
                    items: 3,
                }
            }
        })


    })
});
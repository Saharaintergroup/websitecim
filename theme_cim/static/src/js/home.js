odoo.define('theme_cim.home', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var utils = require("web.utils");
    var qweb = core.qweb;
    var lang = utils.get_cookie("frontend_lang");
    console.log('lang==>',lang);
    jQuery(document).ready(function($) {
        $('.my-news-ticker').AcmeTicker({
            type: 'marquee',
            /*horizontal/horizontal/Marquee/type*/
            direction: (lang === "ar_SY") ? "right" : "left",
            /*up/down/left/right*/
            speed: 0.05,
            /*true/false/number*/ /*For vertical/horizontal 600*/ /*For marquee 0.05*/ /*For typewriter 50*/
            controls: {
                toggle: $('.acme-news-ticker-pause'),
                /*Can be used for horizontal/horizontal/typewriter*/ /*not work for marquee*/
            }
        });

        function animateElements() {
            // skill circle progress bar
            var skillLevel1 = $('.skill-item .first').data('skill-level');
            var skillLevel2 = $('.skill-item .second').data('skill-level');
            var skillLevel3 = $('.skill-item .third').data('skill-level');
            var skillLevel4 = $('.skill-item .fourth').data('skill-level');
            console.log('skillLevel1===>', skillLevel1);
            //first.circle
            $('.first.circle').circleProgress({
                value: skillLevel1 / 100,
                size: 100,
                thickness: 10,
                emptyFill: "#B2BDC8",
                fill: {
                    color: "#F9B40E"
                }
            }).on('circle-animation-progress', function(event, progress) {
                $(this).find('h6').html(Math.round(skillLevel1 * progress) + '<span>%</span>');
            });

            //second.circle
            $('.second.circle').circleProgress({
                value: skillLevel2 / 100,
                size: 100,
                thickness: 10,
                emptyFill: "#B2BDC8",
                fill: {
                    color: "#F10020"
                }
            }).on('circle-animation-progress', function(event, progress) {
                $(this).find('h6').html(Math.round(skillLevel2 * progress) + '<i>%</i>');
            });

            //third.circle
            $('.third.circle').circleProgress({
                value: skillLevel3 / 100,
                size: 100,
                thickness: 10,
                emptyFill: "#B2BDC8",
                fill: {
                    color: "#12BFFF"
                }
            }).on('circle-animation-progress', function(event, progress) {
                $(this).find('h6').html(Math.round(skillLevel3 * progress) + '<span>%</span>');
            });

            //fourth.circle
            $('.fourth.circle').circleProgress({
                value: skillLevel4 / 100,
                size: 100,
                thickness: 10,
                emptyFill: "#B2BDC8",
                fill: {
                    color: "#C683FF"
                }
            }).on('circle-animation-progress', function(event, progress) {
                $(this).find('h6').html(Math.round(skillLevel4 * progress) + '<span>%</span>');
            });
        }

        // Show animated elements
        animateElements();
        $(window).scroll(animateElements);

        console.log('2 lang==>',lang);
        $('.carousel-partners').owlCarousel({
            rtl:(lang === "ar_SY") ? true : false,
            loop: true,
            nav: false,
            dots: false,
            margin: 10,
            navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
            autoplay: 4000,
            smartSpeed: 2000,
            responsive: {
                0: {
                    items: 3,
                },
                576: {
                    items: 5,
                },
                768: {
                    items: 7,
                },
                992: {
                    items: 9,
                },
                1200: {
                    items: 10,
                }
            }
        })


    })
});
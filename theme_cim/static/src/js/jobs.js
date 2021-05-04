odoo.define('theme_cim.jobs', function(require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var utils = require("web.utils");
    var qweb = core.qweb;

    jQuery(document).ready(function($) {
        console.log('--------jobs---------');

        $('#input_file').change(function() {
        console.log('--------change---------');
          var i = $(this).next('label').clone();
          var file = $('#input_file')[0].files[0].name;
          $(this).next('label').text(file);
        });
    })

});
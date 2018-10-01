/*global opener */
(function() {
    'use strict';
    var initData = JSON.parse(document.getElementById('izi-popup-response-constants').dataset.popupResponse);
    switch(initData.action) {
    case 'change':
        opener.izi.dismissChangeRelatedObjectPopup(window, initData.value, initData.obj, initData.new_value);
        break;
    case 'delete':
        opener.izi.dismissDeleteRelatedObjectPopup(window, initData.value);
        break;
    default:
        opener.izi.dismissAddRelatedObjectPopup(window, initData.value, initData.obj);
        break;
    }
})();

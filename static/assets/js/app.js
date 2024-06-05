$(function() {
  'use:static';

  // start loading page
  var pLoad = $('#loading p').text('pleas wait page loading' + ' . .');
  $(document).ready(function() {
      $("#loading").css('display', 'none');
  });
  // end loading page

  // start dorpdown menu with hover
  $('.navbar .dropdown').on('hover',function() {
      $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideDown();
  }, function() {
      $(this).find('.dropdown-menu').first().stop(true, true).delay(100).slideUp();
  });
  // end dropdown menu without click

  // start page up button
  $('#footer .up a').on('click', function() {
      $('html , body').animate({
          scrollTop: $('#top-nav').offset().top
      }, 1000);
  });
  // end page up button

  // dir section
  var pageName = $('#dir .left p').text();
  $('#dir .right p').text('Home' + ' / ' + pageName);
  // end dir section

  // start about page

  // start services page
  var icon = $('#video .icon');
  var over = $('#video .over-img');

  over.mouseover(function() {
      $(this).css({
          'opacity': '0.5'
      });
      icon.css({
          'transform': 'scale(1.2)'
      });
  });

  icon.mouseover(function() {
      over.css({
          'opacity': '0.5'
      });
      icon.css({
          'transform': 'scale(1.2)'
      });
  });

  over.mouseleave(function() {
      $(this).css({
          'opacity': '0.1'
      });
      icon.css({
          'transform': 'scale(1)'
      });
  });
  // end services page
});

$('.form-control').on("focus", function() {
  $(this).parent('.input-group').addClass("input-group-focus");
}).on("blur", function() {
  $(this).parent(".input-group").removeClass("input-group-focus");
});

AOS.init({
    easing: 'ease-out-back',
    duration: 1000
});

var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
(function(){
var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
s1.async=true;
s1.src='https://embed.tawk.to/59f5afbbbb0c3f433d4c5c4c/default';
s1.charset='UTF-8';
s1.setAttribute('crossorigin','*');
s0.parentNode.insertBefore(s1,s0);
})();
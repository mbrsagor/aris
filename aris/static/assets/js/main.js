(function($) {

	"use strict";

	/*
	|--------------------------------------------------------------------------
	| Template Name: Stray
	| Author: ThemeMarch
	| Developer: Tamjid Bin Murtoza
	| Version: 1.0.0
	|--------------------------------------------------------------------------
	|--------------------------------------------------------------------------
	| TABLE OF CONTENTS:
	|--------------------------------------------------------------------------
	|
	| 1. Scripts initialization
	| 2. Preloader
	| 3. Primary Menu
	| 4. Scroll Function
	| 5. Section Active and Scrolling Animation
	| 6. Scroll Up
	| 7. Owl Carousel
	| 8. Portfolio
	| 9. Ripple
	| 10. Magnific Popup
	| 11. Ajax Contact Form
	| 12. Mailchimp js
	| 13. Swiper Slider
	| 14. Particle JS
	| 15. Google Map
	|
	*/

	/*--------------------------------------------------------------
		1. Scripts initialization
	--------------------------------------------------------------*/

	$(window).on('load', function() {
		$(window).trigger("scroll");
		$(window).trigger("resize");
		preloaderSetup();
		portfolioMsSetup();
	});

	$(document).on('ready', function() {
		$(window).trigger("resize");
		primaryMenuSetup();
		mobileMenu();
		scrollAnimation();
		sectionActive();
		scrollUp();
		owlCarouselSetup();
		portfolioMsSetup();
		rippleSetup();
		magnificPopupSetup();
		contactForm();
		swiperSliderSetup();
		new WOW().init();
		$(".player").YTPlayer();
		$('.parallax').parallax("50%", 0.3);
		$('.counter').tamjidCounter();
		$(".js-video-button").modalVideo();

	});

	$(window).on('resize', function() {
		mobileMenu();
		portfolioMsSetup();
		$(".full-height").css("height", $(window).height());
	});

	$(window).on('scroll', function() {
		scrollFunction();
	});

	$.exists = function(selector) {
        return ($(selector).length > 0);
    }
	/*--------------------------------------------------------------
		2. Preloader
	--------------------------------------------------------------*/

	function preloaderSetup() {

		$("body").imagesLoaded(function () {
	      $(".preloader-wave").fadeOut();
	      $("#preloader").delay(200).fadeOut("slow").remove();
	    });

	}

	/*--------------------------------------------------------------
		3. Primary Menu
	--------------------------------------------------------------*/

	function primaryMenuSetup() {

		$( ".primary-nav-list" ).before( "<div class='m-menu-btn'><span></span></div>" );

		$(".m-menu-btn").on('click', function(){
			$( this ).toggleClass( "m-menu-btn-ext" );
			$(this).siblings('.primary-nav-list').slideToggle("slow");
		});

		$( ".menu-item-has-children > ul" ).before( "<i class='fa fa-plus m-dropdown'></i>" );

		$('.m-dropdown').on('click', function() {
			$(this).siblings('ul').slideToggle("slow");
			$(this).toggleClass("fa-plus fa-minus")
		});

	}

	function mobileMenu() {

		if ($(window).width() <= 983){
			$('.primary-nav').addClass('m-menu').removeClass('primary-nav');
		} else {
			$('.m-menu').addClass('primary-nav').removeClass('m-menu');
		}

	}

	/*--------------------------------------------------------------
		4. Scroll Function
	--------------------------------------------------------------*/

	function scrollFunction() {

		var scroll = $(window).scrollTop();

		if(scroll >= 10) {
			$(".site-header").addClass("small-height");
		} else {
			$(".site-header").removeClass("small-height");
		}
		// For Scroll Up
		if(scroll >= 350) {
			$(".scrollup").addClass("scrollup-show");
		} else {
			$(".scrollup").removeClass("scrollup-show");
		}

	}

	/*--------------------------------------------------------------
		5. Section Active and Scrolling Animation
	--------------------------------------------------------------*/

	function scrollAnimation() {

		$('a:not(.portfolio-filter ul li a):not(.portfolio-item .item-inner):not(.services a)').on('click', function(event) {
			var $anchor = $(this);
			$('html, body').stop().animate({
				scrollTop: ($($anchor.attr('href')).offset().top - 30)
				}, 1250, 'easeInOutExpo');
				event.preventDefault();
		});

	}

	function sectionActive() {

		$('body').scrollspy({
			target: '.site-header',
			offset: 70
		});

	}


	/*--------------------------------------------------------------
		6. Scroll Up
	--------------------------------------------------------------*/

	function scrollUp() {

		$( "body" ).append( "<span class='scrollup'></span>" );

		$('.scrollup').on('click', function(e) {
			e.preventDefault();
			$('html,body').animate({
				scrollTop: 0
			}, 1000);
		});

	}

	/*--------------------------------------------------------------
		7. Owl Carousel
	--------------------------------------------------------------*/

	function owlCarouselSetup() {

		/* Owl Carousel For hero-slider */
	    $('.hero-slider').owlCarousel({
	        items: 1,
            animateOut: 'fadeOut',
            loop: true,
            nav: true,
            navText: ['<i class="fa fa-caret-left"></i>','<i class="fa fa-caret-right"></i>'],
            autoplay: false
        });

        /* Owl Carousel For About Us */
        $('.about-slider').owlCarousel({
            items: 1,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            loop: true,
            autoplay: false,
            autoplayTimeout: 6000,
            smartSpeed: 1000,
            nav: false,
            dots: true
        });

        /* Owl Carousel For Team member */
		var owl = $('.member-carousel');
		owl.owlCarousel({
		    loop:true,
		    nav:false,
		    autoplay:true,
		    margin:0,
		    autoplayTimeout: 6000,
            smartSpeed: 1000,
		    responsive:{
		        0:{
		            items:1
		        },
		        575:{
		            items:2
		        },
		        1000:{
		            items:3
		        },
		        1300:{
		            items:4
		        }
		    }
		});

        /* Owl Carousel For Testimonial-1 */
        $('.testimonial-1').owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            nav: false,
            autoplayHoverPause: false,
            smartSpeed: 1000,
            autoplayTimeout: 6000
        });

        /* Owl Carousel For Testimonial-2 */
        $('.testimonial-2').owlCarousel({
        	items: 1,
            animateOut: 'slideOutDown',
            animateIn: 'flipInX',
            loop: true,
            autoplay: true,
            autoplayTimeout: 6000,
            smartSpeed: 1000,
            nav: false
        });

        /* Owl Carousel For Testimonial-3 */
        $('.testimonial-3').owlCarousel({
            items: 1,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            loop: true,
            autoplay: true,
            autoplayTimeout: 6000,
            smartSpeed: 1000,
            nav: false
        });

        /* Owl Carousel For Blog Post Carousel */
	    $('.blog-post-carousel').owlCarousel({
	        items: 1,
            animateOut: 'fadeOut',
            loop: true,
            nav: true,
            navText: ['',''],
            autoplay: true
        });

	}

	/*--------------------------------------------------------------
		8. Portfolio
	--------------------------------------------------------------*/

	function portfolioMsSetup() {

		if ($.exists('.portfolio')) {

	        $('.portfolio').isotope({
				itemSelector: '.portfolio-item',
				transitionDuration: '0.60s',
				percentPosition: true,
				masonry: {
					columnWidth: '.grid-sizer'
				}
			});

			/* Active Class of Portfolio*/
			$('.portfolio-filter ul li').on('click', function(event) {
				$(this).siblings('.active').removeClass('active');
				$(this).addClass('active');
					event.preventDefault();
			});

			/*=== Portfolio filtering ===*/
			$('.portfolio-filter ul').on('click', 'a', function() {
				var filterElement = $(this).attr('data-filter');
				$(this).parents(".portfolio-filter").next().isotope({
					filter: filterElement
				});
			});
    	}

	}

	/*--------------------------------------------------------------
		9. Ripple
	--------------------------------------------------------------*/

	function rippleSetup() {

        if ($.exists('.ripple-version')) {

            $('.ripple-version').ripples({
				resolution: 500,
		        perturbance: 0.04
			});

        }

	}

  	/*--------------------------------------------------------------
   		10. Magnific Popup
  	--------------------------------------------------------------*/

  	function magnificPopupSetup() {

	    $('.zoom-gallery').magnificPopup({
	        delegate: 'a',
	        type: 'image',
	        closeOnContentClick: false,
	        closeBtnInside: false,
	        mainClass: 'mfp-with-zoom mfp-img-mobile',
	        gallery: {
	            enabled: true
	        },
	        zoom: {
	            enabled: true,
	            duration: 300, // don't foget to change the duration also in CSS
	            opener: function(element) {
	                return element.find('img');
	            }
	        }

	    });

  	}

	/*--------------------------------------------------------------
		11. Ajax Contact Form
	--------------------------------------------------------------*/

	function contactForm() {

		$('.cf-msg').hide();
	    $('form#cf button#submit').on('click', function() {
	        var name = $('#name').val();
	        var subject = $('#subject').val();
	        var email = $('#email').val();
	        var msg = $('#msg').val();
			var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

			if (!regex.test(email)) {
				$('.cf-msg').fadeIn().html('<div class="alert alert-danger"><strong>Warning!</strong> Please Enter Valied Email.</div>');
				return false;
			}

	        name = $.trim(name);
	        subject = $.trim(subject);
	        email = $.trim(email);
	        msg = $.trim(msg);

	        if (name != '' && email != '' && msg != '') {
	            var values = "name=" + name + "&subject=" + subject + "&email=" + email + " &msg=" + msg;
	            $.ajax({
	                type: "POST",
	                url: "assets/php/mail.php",
	                data: values,
	                success: function() {
	                    $('#name').val('');
	                    $('#subject').val('');
	                    $('#email').val('');
	                    $('#msg').val('');

	                    $('.cf-msg').fadeIn().html('<div class="alert alert-success"><strong>Success!</strong> Email has been sent successfully.</div>');
	                    setTimeout(function() {
	                        $('.cf-msg').fadeOut('slow');
	                    }, 4000);
	                }
	            });
	        } else {
				$('.cf-msg').fadeIn().html('<div class="alert alert-danger"><strong>Warning!</strong> All fields are required.</div>');
	        }
	        return false;
	    });

	}

	/*--------------------------------------------------------------
	    12. Mailchimp js
	--------------------------------------------------------------*/
	// mailchimp start
    if ($('.mailchimp').length > 0) {
        $('.mailchimp').ajaxChimp({
            language: 'es',
            callback: mailchimpCallback
        });
    }

    function mailchimpCallback(resp) {
        if (resp.result === 'success') {
            $('.subscription-success').html('<i class="fa fa-check"></i><br/>' + resp.msg).fadeIn(1000);
            $('.subscription-error').fadeOut(500);

        } else if (resp.result === 'error') {
            $('.subscription-error').html('<i class="fa fa-times"></i><br/>' + resp.msg).fadeIn(1000);
        }
    }
    $.ajaxChimp.translations.es = {
        'submit': 'Submitting...',
        0: 'We have sent you a confirmation email',
        1: 'Please enter a value',
        2: 'An email address must contain a single @',
        3: 'The domain portion of the email address is invalid (the portion after the @: )',
        4: 'The username portion of the email address is invalid (the portion before the @: )',
        5: 'This email address looks fake or invalid. Please enter a real email address'
    };


	/*--------------------------------------------------------------
	    13. Swiper Slider
	--------------------------------------------------------------*/

    function swiperSliderSetup() {

        if ($.exists('.swiper-container')) {
            var swiper = new Swiper('.swiper-container', {
            loop: false,
            speed: 1000,
            grabCursor: false,
            mousewheel: false,
            keyboard: true,
            simulateTouch: false,
            parallax: true,
            effect: 'slide',
            pagination: {
                el: '.swiper-pagination',
                type: 'progressbar',
            },
            navigation: {
                nextEl: '.swiper-arrow-right',
                prevEl: '.swiper-arrow-left',
            }
            });
            $('.swiper-slide-count span:first-child').text('1');
            $('.swiper-slide-count span:last-child').text(swiper.slides.length);
            swiper.on('slideChange', function () {
                $('.swiper-slide-count span:first-child').text(swiper.activeIndex + 1);
            });

        }

    }

	/*--------------------------------------------------------------
	    14. Particle JS
	--------------------------------------------------------------*/

    if ($.exists('#particles')) {
        document.addEventListener('DOMContentLoaded', function () {
		  particleground(document.getElementById('particles'), {
		    dotColor: 'rgba(32, 48, 60, 0.4)',
		    lineColor: 'rgba(32, 48, 60, 0.1)'
		  });
		  var intro = document.getElementById('intro');
		}, false);

    }

	/*--------------------------------------------------------------
	    15. Google Map
	--------------------------------------------------------------*/

   if ($('#map').length > 0) {

      var contactmap = {
         lat: 39.742043,
         lng: -104.991531
      };

      $('#map')
         .gmap3({
            zoom: 12,
            center: contactmap,
            scrollwheel: false,
            mapTypeId: "shadeOfGrey",
            mapTypeControlOptions: {
               mapTypeIds: [google.maps.MapTypeId.ROADMAP, "shadeOfGrey"]
            }
         })

         .styledmaptype(
            "shadeOfGrey", [

               {
                  "featureType": "administrative",
                  "elementType": "geometry.stroke",
                  "stylers": [{
                     "color": "#fefefe"
                  }, {
                     "lightness": 17
                  }, {
                     "weight": 1.2
                  }]
               },
               {
                  "featureType": "administrative",
                  "elementType": "geometry.fill",
                  "stylers": [{
                     "color": "#fefefe"
                  }, {
                     "lightness": 20
                  }]
               },
               {
                  "featureType": "transit",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f2f2f2"
                  }, {
                     "lightness": 19
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.icon",
                  "stylers": [{
                     "visibility": "off"
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.text.fill",
                  "stylers": [{
                     "saturation": 36
                  }, {
                     "color": "#333333"
                  }, {
                     "lightness": 40
                  }]
               },
               {
                  "featureType": "all",
                  "elementType": "labels.text.stroke",
                  "stylers": [{
                     "visibility": "on"
                  }, {
                     "color": "#ffffff"
                  }, {
                     "lightness": 16
                  }]
               },
               {
                  "featureType": "poi",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f5f5f5"
                  }, {
                     "lightness": 21
                  }]
               },
               {
                  "featureType": "road.local",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 16
                  }]
               },
               {
                  "featureType": "road.arterial",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 18
                  }]
               },
               {
                  "featureType": "road.highway",
                  "elementType": "geometry.stroke",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 29
                  }, {
                     "weight": 0.2
                  }]
               },
               {
                  "featureType": "road.highway",
                  "elementType": "geometry.fill",
                  "stylers": [{
                     "color": "#ffffff"
                  }, {
                     "lightness": 17
                  }]
               },
               {
                  "featureType": "landscape",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#f5f5f5"
                  }, {
                     "lightness": 20
                  }]
               },
               {
                  "featureType": "water",
                  "elementType": "geometry",
                  "stylers": [{
                     "color": "#e9e9e9"
                  }, {
                     "lightness": 17
                  }]
               }
            ], {
               name: "HQ"
            }
         )

         .marker({
            position: contactmap,
            icon: 'assets/img/map-marker.png'
         })

	}

    /*--------------------------------------------------------------
	    ## Color Customizer
	--------------------------------------------------------------*/
	$(document).ready(function() {
	    $("button[data-theme]").on('click', function() {
	      $("head link#theme").attr("href", $(this).data("theme"));
	    });
	    $('.customizer-btn').on('click', function() {
	      $(this).parent().toggleClass('cs-hide');
	    })
	});

})(jQuery); // End of use strict

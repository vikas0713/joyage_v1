/* global jQuery:false, window:false, Hammer:false, atbb:false, MediaBox:false */


window.atp_isotop_settings = {
	itemSelector: '.atp-project:not(.atp-to-load)',
	transitionDuration: '0.8s'/*,
	hiddenStyle: { opacity: 0 },
	visibleStyle: { opacity: 1 }*/
};

(function($) {
	'use strict';

	/* Document ready */
	$(document).ready(function() {

		if( $('body').hasClass('is-phone') ) {
			$(window).off('scroll.nebula');
		}

		$(window).trigger('resize.nebula');
		$(window).trigger('scroll.nebula');

		/* declare that the site is still loading */
		$('body').addClass('site-loading');



		/* Scroll down indicator user interaction */
		$('.scroll-down-indicator').on('click', function(){
			var to = 0;
			if( $('body').hasClass('single-atp_project') ) {
				to = $('#header-image-wrapper').height() - 56;
			} else {
				to = $('#header-image-wrapper').height() - 112;
			}
			
			smoothScrollTo( to );
		});
		/* Interval to remind to scroll  */
		setInterval(function() {
			$('body').addClass('scroll-reminder');
			setTimeout(function(){
				$('body').removeClass('scroll-reminder');
			}, 650);
		}, 5000);




		/* handle search input focus and blur events */
		$('.searchform-header-wrapper input').on('touchstart', function() {
			//console.log('touchstart');
			$(this).trigger( 'focus' );
		});

		$('.searchform-header-wrapper input').on('blur', function() {
			//console.log('blur');
			$('#search-openee').prop('checked', false);
		});

		$('#search-openee').on('change', function() {
			var input = $( '.searchform-header-wrapper input' );
			//var search_opener = $('#header .search-opener');

			if( $('body').hasClass('is-mobile') ) {
				if( $(this).prop('checked') ) {
					input.trigger('touchstart');
					if( $('body').hasClass('header-large') ) {
						smoothScrollTo( input.offset().top - 56, 500 );
					}
				} else {
					setTimeout(function() {
						input.trigger('blur');
					}, 50);
				}
				//console.log(input);
			}
		});



		/* handle mobile "swipe to close" menu */
		if( window.Hammer ) {
			var hammer = new Hammer( $('body').get(0) );

			if( $('body').hasClass('nav-sidebar-left') ) {
				hammer.on('swipeleft', function() {
					$('#main-nav-openee').prop('checked', false);
					//console.log( 'swipe close menu' );
				});
				hammer.on('swiperight', function(e) {
					if( e.center.x - e.distance < 100 ) {
						$('#main-nav-openee').prop('checked', true);
						//console.log( 'swipe open menu' );
					}
				});
			} else if( $('body').hasClass('nav-sidebar-right') ) {
				hammer.on('swiperight', function() {
					$('#main-nav-openee').prop('checked', false);
					//console.log( 'swipe close menu' );
				});
				hammer.on('swipeleft', function(e) {
					if( e.center.x + e.distance > $(window).width() - 100 ) {
						$('#main-nav-openee').prop('checked', true);
						//console.log( 'swipe open menu', e.center.x, e.distance );
					}
				});
			}
		}





		/* mobile nav fallback */
		$('.header-large #header .navigation, .sticky-header .navigation, .header-small #header .navigation').each(function() {
			build_fallback_nav( $(this) );
		});


	}); //END document ready


	function build_fallback_nav( nav ) {
		var fallback = $('<select/>',{
			'class': 'fallback-navigation'
		});
		nav.find('li').each(function() {
			var item = $('<option/>', {
				value: $(this).children('a').attr('href'),
				selected: $(this).hasClass('current-menu-item') ? true : false
			});
			if( $(this).parent().hasClass('sub-menu') ) {
				item.html( '&nbsp;&nbsp;' + $(this).children('a').text() );
			} else {
				item.text( $(this).children('a').text() );
			}
			item.appendTo( fallback );
		});

		nav.after( fallback );

		fallback.on('change', function() {
			window.location = $(this).val();
		});
	}

	
	/* Winodw resize */
	$(window).on('resize.nebula', function() {
		if( $('body').hasClass('header-image-height-window') ) {
			fitHeaderHeight();
		}
		//console.log('resize');
	});




	/* Window load */
	$(window).load(function() {
		/* init grid portfolios */
		$('.atp-grid-portfolio').each(function() {
			$(this).ATPGridPortfolio();
		});

		$('.nebula-gallery').each(function() {
			var gallery = $(this).nebulaGallery();
				gallery.on('gallery:changed', function() {
					reapplyMasonryBlog();
				});
		});

		/* init mediabox (lightbox) */
		if( window.atbb !== undefined && atbb.lightbox !== undefined ) {
			atbb.lightbox.addGallery( '.media-gallery,.lightbox-enabled,.atbb-grid-gallery,.atbb-slider-gallery' );
		} else {
			new MediaBox({
				//element: 'a.show_review_form',
				gallery: '.media-gallery,.lightbox-enabled,.atbb-grid-gallery,.atbb-slider-gallery',
				duration: 900,
				easing: 'easeOutExpo',
				exclude: '.atbb-no-lightbox,.gallery-caption a'
			});
		}

		/* apply masonry on blog */
		applyMasonryBlog();
		
		/* preload overlay and site load */
		setTimeout(function() {
			$('body').addClass('site-ready').removeClass('site-loading');
			setTimeout(function() {
				$('.preload-ovarlay').remove();
			}, 600);
		}, 600);

		$('.format-video .post-thumbnail').fitVids({
			customSelector: 'iframe[src^="http://videohive.net"]'
		});
	}); //END window load







	/* Winodw scroll */
	$(window).on('scroll.nebula', function() {
		if( $('body').hasClass('preview') ) return;
		
		/* sticky nav -------------------------------- */
		var scrolltop = $(window).scrollTop();
		var trigger = 0;
		var resizer = 0;
		var painter = 0;

		if( $('body').hasClass('header-large') ) {
			trigger = $('#main-container').offset().top - ($('.sticky-header').height() + 7);
			resizer = $('#header').height();
		} else {
			trigger = $('#header').outerHeight(true);
			resizer = $('#header').outerHeight(true);
		}

		if( scrolltop >= trigger ) {
			$('body').addClass( 'sticky-nav' );
		} else {
			$('body').removeClass( 'sticky-nav' );
		}

		if( scrolltop >= resizer ) {
			$('body').addClass( 'sticky-nav-resize' );
		} else {
			$('body').removeClass( 'sticky-nav-resize' );
		}




		if( $('body').hasClass('has-header-image') ) {
			painter = $('#header-image-wrapper').outerHeight() - $('#header').height();
			/* apply parallax effect */
			headerParallax();
		}

		if( scrolltop >= painter ) {
			$('body').addClass( 'sticky-nav-header-image' );
		} else {
			$('body').removeClass( 'sticky-nav-header-image' );
		}




		if( scrolltop >= 56 ) {
			$('body').removeClass( 'show-scroll-indicator' );
		} else {
			$('body').addClass( 'show-scroll-indicator' );
		}

		/* ------------------------------------------- */
	});







	function smoothScrollTo( to, duration, callback ) {
		$('body, html').animate({
			scrollTop: to
		}, duration !== undefined ? duration : 1200, 'easeInOutCubic', function() {
			if( callback !== undefined ){
				callback();
			}
		});
	}



	function applyMasonryBlog() {
		var columnWidth = '.masonry-blog-grid-sizer';
		var gutter = '.masonry-blog-gutter-sizer';

		if( $('body').hasClass('blog-layout-masonry') ) {
			$('.blog-layout-masonry .content-container').isotope({
				isOriginLeft: $('body').hasClass('rtl') ? false : true,
				itemSelector: 'article',
				masonry: {
					columnWidth: columnWidth,
					gutter: gutter
				}
			});
		} // END if masonry
	}

	function reapplyMasonryBlog() {
		if( $('body').hasClass('blog-layout-masonry') ) {
			$('.blog-layout-masonry .content-container').isotope();
		} // END if masonry
	}






	function fitHeaderHeight() {
		$('#header-image-wrapper').css({
			height: $(window).height()
		});
	}


	function headerParallax() {
		if( $('body').hasClass('is-mobile') ) return;
		
		var element = $('.header-image');
		
		var offsetTop = element.parent().offset().top;
		var cont_height = element.parent().height();
		var element_height = element.outerHeight();
		var admin_bar_height = $('#wpadminbar').height();

		var scrollTop = $(window).scrollTop() + (admin_bar_height ? admin_bar_height : 0);

		if( scrollTop > cont_height ) { return; }

		var zeroed_offset = scrollTop - (offsetTop - cont_height);
		var perc = zeroed_offset * 100 / (cont_height + element_height );
		var pos = (cont_height * perc / 100) - element_height / 2;

		var perc_title = zeroed_offset * 100 / (cont_height + element_height );
		var pos_title = ((cont_height * perc_title / 100) - element_height / 2) * 1.45;

		//console.log(perc);

		if( scrollTop < offsetTop + element_height  ) {
			if( pos > 0 ) {
				element.css({
					'-webkit-transform': 'translate3d(0, '+pos.toFixed(2)+'px, 0)',
					'transform': 'translate3d(0, '+pos.toFixed(2)+'px, 0)'
				});
				$('.header-image-content-container').css({
					'-webkit-transform': 'translate3d(0, '+pos_title.toFixed(2)+'px, 0)',
					'transform': 'translate3d(0, '+pos_title.toFixed(2)+'px, 0)'
				});
			} else {
				element.css({
					'-webkit-transform': 'translate3d(0, 0, 0)',
					'transform': 'translate3d(0, 0, 0)'
				});
				$('.header-image-content-container').css({
					'-webkit-transform': 'translate3d(0, 0, 0)',
					'transform': 'translate3d(0, 0, 0)'
				});
			}
		}
	} //end headerParallax











	jQuery.fn.nebulaGallery = function() {
		var gallery = this;
		var ul = gallery.find('.gallery');
		var columnWidth = '.masonry-gallery-grid-sizer';
		var gutter = 0;

		if( gallery.hasClass('slider-gallery') ) {
			initSliderGallery();
		} else if( gallery.hasClass('masonry-gallery') ) {
			initMasonryGallery();
		}

		function initMasonryGallery() {
			ul.isotope({
				isOriginLeft: $('body').hasClass('rtl') ? false : true,
				itemSelector: 'li.gallery-item',
				masonry: {
					columnWidth: columnWidth,
					gutter: gutter
				}
			});

			ul.isotope('on', 'layoutComplete', function() {
				//console.log( 'nebulaGallery layoutComplete' );
				//gallery.trigger('gallery:changed');
			});
			
		} // End initMasonryGallery
		/**/
		function initSliderGallery() {
			gallery.flexslider({
				animation: 'slide',
				selector: '.gallery > li',
				smoothHeight: true,
				controlNav: true,
				directionNav: false,
				prevText: '',
				nextText: '',
				slideshow: false,
				start: function() {
					gallery.find('.gallery > li.clone').find('a').addClass('atbb-no-lightbox');
					gallery.trigger('gallery:changed');
				},
				after: function() {
					gallery.trigger('gallery:changed');
				}
			});
		} // End initSliderGallery

		return gallery;
	};













	jQuery.fn.ATPGridPortfolio = function() {
		var portfolio = this;
		var load_button_wrapper = portfolio.find('.atp-load-more-wrapper');
		//var load_button = load_button_wrapper.find('.atp-load-more');
		var projects_ul = portfolio.find('ul.atp-projects');
		var projects_per_portfolio = load_button_wrapper.attr('data-load-count');
		var filters = portfolio.find('.atp-filters');
		var openee = portfolio.find('#atp-filter-openee');

		var loaded_projects = [];




		function build_fallback_filters() {
			var fallback = $('<select/>',{
				'class': 'atp-fallback-filters'
			});
			filters.find('li').each(function() {
				var item = $('<option/>', {
					value: $(this).attr('data-filter'),
					selected: $(this).hasClass('atp-active-filter') ? true : false,
				});

				item.text( $(this).children('a').text() );
				item.appendTo( fallback );
			});

			filters.after( fallback );

			fallback.on('change', function() {
				var filter = $(this).val();
				//console.log(filter);
				projects_ul.isotope({
					filter: filter !== 'all' ? filter : '.atp-project'
				});

				filters.children().removeClass('atp-active-filter');
				filters.children('li[data-filter="'+filter+'"]').addClass('atp-active-filter');
			});
		}
		build_fallback_filters();



		function preload_projects() {
			if( portfolio.hasClass('atp-all-loaded') ) return;

			var unloaded_projects = projects_ul.children('li.atp-to-load').slice( 0, projects_per_portfolio );
				loaded_projects = [];

			unloaded_projects.each(function() {
				var project = $(this);

				var placeholder = project.find('.atp-project-thumb .thumb-placeholder');

				var img = $('<img/>');

					placeholder.after( img );

					img.on('load', { project: project, count: unloaded_projects.length }, project_loaded);
					img.attr({ 
						src: placeholder.attr('data-src'),
						width: placeholder.attr('data-width'),
						height: placeholder.attr('data-height'),
						alt: placeholder.attr('data-alt')
					});
				
				placeholder.remove();
			});

			portfolio.addClass( 'atp-loading atp-smooth-height' );
			return false;
		}

		function project_loaded( e ) {
			var project = e.data.project;
			var count = e.data.count;
			//console.log(count);
			
			loaded_projects.push( project );

			if( loaded_projects.length === count ) {
				load_complete( loaded_projects );
			}
		}

		function load_complete( projects ) {

			setTimeout(function() {
				$.each(projects, function() { this.removeClass('atp-to-load'); });

				projects_ul.isotope('once', 'layoutComplete', function() {
					//console.log('layoutComplete');
					$.each(projects, function() { this.removeClass('atp-invisible'); });
				});

				setTimeout(function() {
					projects_ul.isotope('reloadItems').isotope();
					check_for_more();
				}, 500);

				portfolio.removeClass( 'atp-loading' );
			}, 1500);

		}

		function check_for_more() {
			if( projects_ul.children('li.atp-to-load').length === 0 ) {
				portfolio.addClass( 'atp-all-loaded' );
			}
		}

		check_for_more();

		/* user interaction */
		load_button_wrapper.on('click', preload_projects);

		openee.on('change', function() {
			var fallback_fillter = portfolio.find('.atp-fallback-filters');
			if( $(this).prop('checked') && fallback_fillter.css('display') !== 'none' ) {
				fallback_fillter.trigger('click');
			}
		});

		/*portfolio.find('.atp-fallback-filters').on('click', function(){
			console.log('click');
		});*/
	};


})(jQuery);
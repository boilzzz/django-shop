$.Tween.propHooks.number = {
	get: function ( tween ){
		var num = tween.elem.innerHTML.replace(/^[^\d-]+/, '');
		return  parseFloat(num) || 0;
	},

	set: function( tween ) {
		var opts = tween.options;
		tween.elem.innerHTML = (opts.prefix || '')
		+ tween.now.toFixed(opts.fixed || 0)
		+ (opts.postfix || '');
	}
};
$(document).ready(function() {
	$('.add_to_cart').bind('click', function(e){
		e.preventDefault();
		var id = parseInt($(this).attr('href').replace('#', '')),
		summ_price = parseInt($('.cart__summ').text()),
		cart_count = parseInt($('.cart__count').text()),
		price = parseInt($(this).parent().find($('.price')).text())
		summ_price = summ_price+price;
		$('.cart__count').text(cart_count+1);
		$('.cart__summ').animate({ number: summ_price }, {
			duration: 100
		});
		$.ajax({
			type: 'GET',
			url: '/add_to_cart',
			data: {
				id:id
			},
			success: function(data) {
				if(data != 'error'){
					response = jQuery.parseJSON(data);
					message($('.message'),'Товар "'+response[0].fields.name+'" добавлен в корзину','success',3) 
				}else{
					message($('.message'),'Товар не найден','error',3) 
				}
			},
			error: function(xhr, str) {
				console.log(str)
			}
		})
	})
	$('.all_remove_to_cart').bind('click',function(e) {
		cart_count = parseInt($('.cart__count').text());
		if(cart_count != 0){
			$('.pruct-wrapper').addClass('hinge-custom animated');
			setTimeout(function() {
				$.ajax({
					type: 'GET',
					url: '/cart',
					data: {
						clear_cart:1
					},
					success: function(data) {					
						$('body').html(data);
						message($('.message'),'Все товары удалены','success',1) 
					},
					error: function(xhr, str) {
						console.log(str)
					}
				})
			},2000)
		}else{
			message($('.message'),'Товары не найдены','error',1)
		}
	})
})
var timer,item_hide = 0;
function message(obj,text,modif,val) {
	$this = obj;
	counter(3);
	if($this.children().length >= val){
		var first_p = $this.find($('p')[item_hide]);
		first_p.slideUp('slow');
		$this.append($('<p></p>').text(text).addClass('fadeIn animated message_'+modif)).slideDown('slow');
		item_hide++
	}else{
		$this.append($('<p></p>').text(text).addClass('fadeInDown animated  message_'+modif)).slideDown('slow');
	}
	function counter(max_time) {
		var counterVal = 1;
		if (timer) {
			clearInterval(timer);
		}
		timer = setInterval(function() {
			if(counterVal > max_time){
				clearInterval(timer);
				item_hide = 0
				$this.slideUp('slow',function() {
					$this.html(' ').removeClass('message_'+modif);
				});	
			}
			counterVal++
		}, 1000);
	}
}

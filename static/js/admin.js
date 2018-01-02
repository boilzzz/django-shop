$(document).ready(function() {
	$("#modal").iziModal({
		title: "Выбери аватарку или загрузи свою!",
		icon: 'icon-star',
		headerColor: '#1E88E5',
		width: 600,
		transition: 'fadeInDown',
		    bodyOverflow:true // Here transitionIn is the same property.
		});
	var avatar_src = $('.field-base_photo input').val();
	$('.field-base_photo > div ').append('<a href="#" class="trigger-open-modal-avatar-profile trigger-open-modal-avatar-profile__admin">Изменить</a> <div style="width: 200px;height:200px;text-align: center;    display: inline;" class="trigger-open-modal-avatar-profile__admin"><img src="/static/img/avatar/'+avatar_src+'" width="200" height="200" class="fadeIn animated img_avatar" style="display: block"> </div>')
	var $option__img, img_name;
	$(document).on('click', '.trigger-open-modal-avatar-profile__admin', function (event) {
		event.preventDefault();
		$('#modal').iziModal('open');
	});
	$(document).on('opening', '#modal', function (e) {
		$('.default-avatar-option').click(function(e) {
			$option = $(this).find($('.default-avatar-option__img'));
			$option__img = $option.attr('src');
			$('.field-base_photo input').val($option.attr('data-img-name'));
			$('.field-base_photo input').attr('value', $option.attr('data-img-name'));
			$('.img_avatar').addClass('zoomOut animated');
			$('#modal').iziModal('close');
			setTimeout(function() {
				$('.img_avatar').removeClass('zoomOut');
				$('.img_avatar').addClass('zoomIn');
			},500)
		})
	});
	$(document).on('closed', '#modal', function (e) {
		$('.img_avatar').attr('src',$option__img);
	});	
})
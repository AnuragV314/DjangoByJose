// jQuary Events
/*
Mouse Events	Keyboard Events	    Form Events	    Document/Window Events
click	        keypress	        submit	        load
dblclick	    keydown	            change	        resize
mouseenter	    keyup	            focus	        scroll
mouseleave	 	blur	            unload
*/

// Mouse Events

// click()
$('h1').click(function(){
    console.log('There was a click!')
})

// hover()
$('h1').hover(function(){
    $(this).css('cursor', 'pointer')
})

$('h1').click(function(){
    $(this).text('I was changed.')
})


$('li').click(function(){
    console.log('any li was clicked.')
})



// Keyboard Events

// keypress()
$('input').eq(0).keypress(function(){
    $('h3').toggleClass('turnBlue')
})


// $('input').eq(0).keypress(function(event){
//     console.log(event)
// })

$('input').eq(0).keypress(function(event){
    if(event.which === 13){
        $('h3').toggleClass('turnRed')
    }
})



// on() method

$('h1').on('dblclick', function(){
    $(this).toggleClass('turnBlue')
    console.log('double clicked.')
})


$('h1').on('mouseenter', function(){
    $(this).toggleClass('turnBlue')
})


// Effects & animations

// $('input').eq(1).on('click', function(){
//     $('.container').fadeOut(3000);
// })

$('input').eq(1).on("click",function(){
    $(".container").slideUp(1000) ;
  })

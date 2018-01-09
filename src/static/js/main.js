$( "#search-input" ).autocomplete({

    source: function( request, response ) {

        $.ajax( {
            url: $SCRIPT_ROOT +  "/search/" + request.term,
            success: function( data ) {
                response( data.results );
            }
        } );

    },
    minLength: 1,
    select: function( event, ui ) {

        console.log( "name " + ui.item.name );
	showDetailProduct( ui.item.name );

    }
} )
.autocomplete( "instance" )._renderItem = function( ul, item ) {
    return $( "<li>" )
        .append( $( "<div>" ).text( item.name) )
        .appendTo( ul );
};

function showDetailProduct ( itemName ) {

    $.ajax( {
            url: $SCRIPT_ROOT +  "/search/" + itemName,
            method: "POST",
            success: function(response){
                console.log( "name : " + response.name );

                $('h3').text( response.name );
                $('h5').text( 'Model : ' +response.model );

		        $('#sku').text( response.sku );
		        $('#type').text( response.type );
		        $('#price').text( response.price );
                $('#descritpion').text( response.description );
        		$('img').attr('src', response.image );

                $('#welcome-page').hide();
                $('#result').show();

            },
            error: function(error){
                console.log(error);
            }
        } );
}

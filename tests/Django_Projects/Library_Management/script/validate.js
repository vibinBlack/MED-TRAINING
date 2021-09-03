function validate() {
      
    if( document.myForm.title.value == "" ) {
       alert( "Please provide title!" );
       document.myForm.title.focus() ;
       return false;
    }
    if( document.myForm.author.value == "" ) {
       alert( "Please provide author!" );
       document.myForm.author.focus() ;
       return false;
    }
    if( document.myForm.ISBN.value == "" || isNaN( document.myForm.ISBN.value )) {
       alert( "Please provide ISBN!" );
       document.myForm.ISBN.focus() ;
       return false;
    }
    if( document.myForm.publication.value == "" ){
       
       alert( "Please provide publication" );
       document.myForm.publication.focus() ;
       return false;
    }
    
    return( true );
  }
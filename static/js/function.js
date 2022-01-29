console.log("Estamos en nuevo proyecto");

const saveButtonBook = document.getElementById('saveBook')

const bookName = document.getElementById('bookName')
const bookPrize = document.getElementById('bookPrize')
const bookPages = document.getElementById('bookPages')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const url = window.location.href + "save_book/"



console.log("la ruta de urls",url);

saveButtonBook.addEventListener('click', ()=>{
  
  $.ajax({
    type:'POST',
    url:url,
    data:{
      'csrfmiddlewaretoken': csrf[0].value,
      'name':bookName.value,
      'prize': bookPrize.value,
      'pages':bookPages.value,
    },
    success: function(response){
      console.log(response)
    },
    error:function(error){
      console.log(error);
    }
  })
  
  console.log(bookName.value);
  console.log(bookPrize.value);
  console.log(bookPages.value);
})


  // Get search form and page links
  let searchForm = document.getElementById('searchForm')
  let pageLinks = document.getElementsByClassName('page-link')

  // check if page form exists 
  if(searchForm) {
    for(let i=0; pageLinks.length>i; i++){
      pageLinks[i].addEventListener('click', function(e) {
        e.preventDefault()
      
        //get the data attribute
        let page = this.dataset.page
      
        //Add hiden input to search form
        searchForm.innerHTML += `<input value=${page} name="page"/>`
        //submit form
        searchForm.submit()
      })
    }
  }

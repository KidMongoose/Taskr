$(() => {

//    var contact 
   $('#task-contact-edit').on('click', (e) => {
       e.preventDefault()
       $('#taskr-contact-body ul li span').attr({'contenteditable' : 'true', 'class' : 'data-contact-field'})

   })


   $('#task-contact-submit').on('click', (e) => {
            //e.preventDefault()
            //$('#taskr-contact-body ul li span').attr({'contenteditable' : 'false', 'class' : 'data-contact-field'})
            var telephone =  document.getElementById('contact-data-telephone').innerHTML
            var email = document.getElementById('contact-data-email').innerHTML
            var category = document.getElementById('contact-data-category').innerHTML
            var company = document.getElementById('contact-data-company').innerHTML
            var contactType =  document.getElementById('data-contact-type').innerHTML
            var title =  document.getElementById('contact-data-title').innerHTML
            var name = document.getElementById('contact-data-name').innerHTML
            var image = document.getElementById('contact-data-image').getAttribute("src")
            var notes = document.getElementById('contact-data-notes').innerHTML
            var id = document.getElementById('contact-data-id').innerHTML
            var upload_image = $('#upload-file')[0].files[0]['name']
        

            $.ajax({
              type: 'POST',
              url: '/edit/contact',
              data: JSON.stringify({
                   telephone : telephone,
                   email : email, 
                   category : category,
                   company : company,
                   contact_type : contactType,
                   title : title, 
                   name : name,
                   image : upload_image,
                   notes : notes,
                   id : id
              }),
              dataType: 'json',
              contentType: "application/json",
              success: (response) => {
                  console.log(response)
              }

          })


    
     //alert(id)
    })


    $('#upload-image').on('click', (e) => {
        $('#upload-file').click()
    })



    $('#upload-file').on('change', (e) => {
        //e.preventDefault()
        var file = $(this).val().replace(/C:\\fakepath\\/ig,'')
        //$('#upload-status').text(file)
        document.getElementById('contact-data-image').getAttribute('src').replace(file)

        // $.ajax({
        //     type : 'POST',
        //     url : '/add-image',
        //     data : file,
        //     success: (response) => {
        //         console.log(success)
        //     }
        // })

    
    })



})


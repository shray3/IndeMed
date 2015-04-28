$("#header").load('polls/templates/header.html');
    $("#footer").load('polls/templates/footer.html');
    jQuery(document).ready(function($) {
        var table = $('#myTable').DataTable();

        $('#myTable tbody').on( 'click', 'tr', function () {
                var f_name = $('td', this).eq(0).text();
                var l_name = $('td', this).eq(1).text();
                var db = Date.parse($('td', this).eq(2).text());
                var status = $('td', this).eq(3).text();
                var phone = $('td', this).eq(4).text();
                var doctor = $('td', this).eq(5).text(); 
                var nurse = $('td', this).eq(6).text(); 
                var inst = $('td', this).eq(7).text();
                var addr = $('td', this).eq(8).text();
                var desc = $('td', this).eq(9).text(); 

                document.getElementById("first_name").value = f_name;
                document.getElementById("last_name").value = l_name;
                //dob
                document.getElementById("p_tel").value = phone;
                document.getElementById("p_status").value = status;
                $("#p_doc").val(doctor);
                $("#p_nurse").val(nurse);
                $("#p_inst").val(inst)
                document.getElementById("p_address").value = addr;
                document.getElementById("p_des").value = desc;
                if ( $(this).hasClass('selected') ) {
                    $(this).removeClass('selected');
                }
                else {
                    table.$('tr.selected').removeClass('selected');
                    $(this).addClass('selected');
                }
            } );
        $('#button').click( function () {
            table.row('.selected').remove().draw( false );
        } );

        $('#addRow').on( 'click', function () {
            table.row.add( [
                '.1',
                '.2',
                '.3',
                '.4',
                '.5'
            ] ).draw();
        });
        console.log("form submitted!")  // sanity check
        $( "#addPatient" ).click(function() {
          create_post();
        });
    });

    function create_post() {
        console.log($('#test').text());
        // var f_name = document.getElementById("first_name").value
        // var l_name = document.getElementById("last_name").value 
        // //dob
        // var phone = document.getElementById("p_tel").value 
        // var status = document.getElementById("p_status").value
        // var p_doc = $("#p_doc").val();
        // var p_nurs = $("#p_nurse").val()
        // var p_inst = $("#p_inst").val()
        // var p_desc = document.getElementById("p_des").value
        $.ajax({
            url : "create_patient/", // the endpoint
            type : "POST", // http method
            data : { 
              'csrfmiddlewaretoken': '{{csrf_token}}',
              f_name : document.getElementById("first_name").value,
              l_name : document.getElementById("last_name").value, 
              phone : document.getElementById("p_tel").value,
              status : document.getElementById("p_status").value,
              p_doc : $("#p_doc").val(),
              p_nurse : $("#p_nurse").val(),
              p_inst : $("#p_inst").val(),
              p_addr: $("#p_address").val(),
              p_desc : document.getElementById("p_des").value,
              the_post : $('#test').text()}, // data sent with the post request
            // handle a successful response
            success : function(json) {
                $('#post-text').text(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },  

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };
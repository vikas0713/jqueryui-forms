$(window).load(function() {
		// Animate loader off screen
		$(".se-pre-con").fadeOut("slow");;
	});

    $(document).ready(function(){
        $(" .carrier").hide()
    }
                   );
$(document).ready(function(){
        $("#shipper2,#advanced").hide();
    }
                      );
    $(document).ready(function() {
   $('a').click(function() {
       if($(this).attr('id') == 'carrier1') {
            $('.carrier').show();           
       }

       else {
            $('.carrier').hide();   
       }
   });
});
      
    $(document).ready(function() {
   $('a').click(function() {
       if($(this).attr('id') == 'driver1') {
            $('.driver').show();           
       }

       else {
            $('.driver').hide();   
       }
   });
});
      
    function submit_form(){
    $('#myForm').submit();
}

   function submit_driver(){
    $('#mydriver').submit();
   }
  function submit_carrier(){
    $('#myshipper').submit();
   }
 function submit_truck(){
    $('#mytruck').submit();
   }
 function submit_trailer(){
    $('#mytrailer').submit();
   }
 $("document").ready(function() {
            $("#dialog5").dialog({
                autoOpen: false,
                modal: true,
                minHeight:500,
                minWidth:600,
                changeYear:true,
                buttons: [
                    {
                        text: "Cancel",
                        click: function () {
                            $(this).dialog("close");
                        }
                    },
                    {
                        text: "OK",
                        click: function () {
                           submit_carrier();
                        }
                    }
                ]
            });
            $("#opencarrier").click(function() {
                $("#dialog5").dialog("open");
            });
     
          $("#dialog6").dialog({
                autoOpen: false,
                modal: true,
                minHeight:500,
                minWidth:600,
                changeYear:true,
                buttons: [
                    {
                        text: "Cancel",
                        click: function () {
                            $(this).dialog("close");
                        }
                    },
                    {
                        text: "OK",
                        click: function () {
                            submit_truck();
                        }
                    }
                ]
            });
            $("#opentruck").click(function() {
                $("#dialog6").dialog("open");
            });
     
     $("#dialog7").dialog({
                autoOpen: false,
                modal: true,
                minHeight:500,
                minWidth:600,
                changeYear:true,
                buttons: [
                    {
                        text: "Cancel",
                        click: function () {
                            $(this).dialog("close");
                        }
                    },
                    {
                        text: "OK",
                        click: function () {
                            submit_trailer();
                        }
                    }
                ]
            });
            $("#opentrailer").click(function() {
                $("#dialog7").dialog("open");
            });

            $("#dialog4").dialog({
                autoOpen: false,
                modal: true,
                minHeight:500,
                minWidth:600,
                changeYear:true,
                buttons: [
                    {
                        text: "Cancel",
                        click: function () {
                            $(this).dialog("close");
                        }
                    },
                    {
                        text: "OK",
                        click: function () {
                            submit_driver();
                        }
                    }
                ]
            });
            $("#opendriver").click(function() {
                $("#dialog4").dialog("open");
            });

            $("#dialog3").dialog({
                autoOpen: false,
                closeOnEscape: false,
                show: {
            effect: "blind",
            duration: 500
            },
                modal: true,
                draggable: false,
                minHeight:500,
                minWidth:600,
                changeYear:true,
                buttons: [
                    {
                        text: "CANCEL",
                        click: function () {
                            $(this).dialog("close");
                        }
                    },
                    {
                        text: "SUBMIT",
                        click: function() {
                            submit_form();

                        }
                    }
                ]
            });
            $("#openDlg3").click(function() {
                $("#dialog3").dialog("open");
            });
        }); 

$('a').click(function() {
       if($(this).attr('id') == 'advance_click') {
            $('#advanced').show();           
       }

       else {
            $('.driver').hide();   
       }
   });

$(function() {
    $( "#datepicker" ).datepicker();
    $( "#datepicker1" ).datepicker();
    $( "#datepicker2" ).datepicker();
    $( "#datepicker3" ).datepicker();
    $( "#datepicker4" ).datepicker();
    $( "#datepicker5" ).datepicker();
    $( "#datepicker6" ).datepicker();
    $( "#datepicker7" ).datepicker();
    $( "#datepicker8" ).datepicker();
    $( "#datepicker9" ).datepicker();
    $( "#datepicker10" ).datepicker();
    $( "#datepicker11" ).datepicker();
    $( "#datepicker12" ).datepicker();
    $( "#datepicker13" ).datepicker();
    $( "#datepicker14" ).datepicker();
    $( "#datepicker15" ).datepicker();
    $( "#datepicker16" ).datepicker();
    $( "#datepicker17" ).datepicker();
    $( "#datepicker18" ).datepicker();
    $( "#datepicker19" ).datepicker();
    $( "#datepicker20" ).datepicker();
  });


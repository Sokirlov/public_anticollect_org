// <script>
//             $(document).ready(function () {
//                 $('#id_tel').usPhoneFormat({format: '(xxx) xxx-xxxx',});
//                 var phones = [{ "mask": "38 (###) ### ## ##"}, { "mask": "(###) ### ## ##"}];
//
//                 $('#id_tel').inputmask({
//                     mask: phones,
//                     greedy: false,
//                     definitions: { '#': { validator: "[0-9]", cardinality: 1}} });
//
//                 $("a").click(function () {
//                     var elementClick = $(this).attr("href")
//                     console.log(elementClick)
//                     var destination = $(elementClick).offset().top - $('#menuContainer').height();
//                     console.log(destination)
//                     jQuery("html:not(:animated),body:not(:animated)").animate({scrollTop: destination}, 5000);
//                     return false;
//                 });
//             });
//     </script>

$(document).ready(function () {
    var phones = [{ "mask": "+38 (###) ### ## ##"}, { "mask": "(###) ### ## ##"}];
    $('#id_tel').inputmask({
        mask: phones,
        greedy: false,
        definitions: { '#': { validator: "[0-9]", cardinality: 1}} });

    $("a").click(function () {
        var elementClick = $(this).attr("href")
        var searchLink = elementClick.match(/#.+/)
        var destination = 0
        if(searchLink == null) {
            return elementClick
        }else{
            if (searchLink[0] == '#contactForm') {
                destination = $(searchLink[0]).offset().top - 50
                $('html, body').animate({ scrollTop: destination}, 1500);
                $('#navbarNav ').attr('aria-expanded', 'false');

            }else{
                destination = $(searchLink[0]).offset().top - $('#menuContainer').height() - 30
                $('html, body').animate({ scrollTop: destination}, 500);
                console.log('work')
                $('.navbar-toggler').attr('aria-expanded', 'false');
                $('#navbarNav').removeClass('show')
            }
        }

        return false
      });
});
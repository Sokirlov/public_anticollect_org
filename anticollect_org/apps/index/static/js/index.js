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
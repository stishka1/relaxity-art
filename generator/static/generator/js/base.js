// $(document).ready(function() {
//     $('.valid_code').click(function(e) {
//       // Stop form from sending request to server
//       e.preventDefault();
  
//       var btn = $(this);
//       var date = Date.now();
  
//       $.ajax({
//         method: "GET",
//         url: "/js",
//         dataType: "json",
//         data: {
//           "date": date,
//         },
//         success: function(result) {
//             window.open(
//                 result.url, // ссылка из ответа
//                '_blank' // в новой вкладке
//             );
//         },
//         // error: function(er) {
//         //   console.log(er);
//         // }
//       });
//     })
//   });
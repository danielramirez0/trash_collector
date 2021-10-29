loginToast = document.getElementById("login-toast");
firstView = localStorage.getItem('isFirstView')
if (loginToast && firstView === null) {
  login = new bootstrap.Toast(loginToast);
  login.show();
  localStorage.setItem('isFirstView', "No")
}
// document.getElementById('login-toast').show()

// function initToast(id) {
//   document.getElementById(id).onclick = function () {
//     var toastElList = [].slice.call(document.querySelectorAll(".toast"));
//     var toastList = toastElList.map(function (toastEl) {
//       return new bootstrap.Toast(toastEl);
//     });
//     toastList.forEach((toast) => toast.show());
//   };
// }

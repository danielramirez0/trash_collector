const zipCodes = document.getElementsByName("zip-code");
const weekdays = document.getElementsByName("weekly_pickup");
let sortMethod = document.getElementById("sort-method");
let sortValue = document.getElementById("sort-value");
sortMethod.addEventListener("change", function () {
  zipCodes.forEach((el) => (el.style = "display:none"));
  weekdays.forEach((el) => (el.style = "display:none"));
  if (sortMethod.value === "All") {
    sortValue.style = "display: none;";
  }
  if (sortMethod.value === "zip_code") {
    sortValue.style = "display: block;";
    zipCodes.forEach((el) => {
      el.style = "";
      el.innerText = el.value;
    });
  } else if (sortMethod.value === "weekly_pickup") {
    sortValue.style = "display: block;";
    weekdays.forEach((el) => {
      el.style = "";
      el.innerText = el.value;
    });
  }
});

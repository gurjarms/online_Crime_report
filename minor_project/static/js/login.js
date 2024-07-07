
function hide() {
      document.getElementById('message').style.display = 'none';
}

function validation() {
      var exp = /[A-Z\s]+$/;
      var input = document.getElementById('username').value;

      var result = exp.test(input)
      if (result) {
            document.getElementById('username').value = "";
            document.getElementById('username').style.border = "1px solid red";
            document.getElementById('label').style.color = "red";
            document.getElementById('message').style.display = 'block';
            document.getElementById('message').innerHTML = '<strong>Warning</strong> Capital later and spaces are not allowed  <button id="btn" onclick="hide()" type="button" title="close" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button> ';



      }
      else {
            document.getElementById('username').disabled = false;
            document.getElementById('username').style.border = "1px solid rgb(121, 183, 208)";
            document.getElementById('label').style.color = "rgb(121, 183, 208)";

      }

}


const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

togglePassword.addEventListener("click", function () {
      // toggle the type attribute
      const type = password.getAttribute("type") === "password" ? "text" : "password";
      password.setAttribute("type", type);

      // toggle the icon
      this.classList.toggle("bi-eye");
});

document.addEventListener('DOMContentLoaded', (event) => {
  const modal = document.getElementById("loginModal");
  const btn = document.getElementsByClassName("login-btn")[0]; 
  const span = document.getElementsByClassName("close")[0];

  btn.onclick = function() {
      modal.style.display = "block";
      modal.style.top = "0";
  }

  span.onclick = function() {
      modal.style.display = "none";
      
  }

  window.onclick = function(event) {
      if (event.target == modal) {
          modal.style.display = "none";
      }
  }
});
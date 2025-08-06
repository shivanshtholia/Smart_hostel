const loginText = document.querySelector(".title-text .login");
  const loginForm = document.querySelector("form.login");
  const loginBtn = document.querySelector("label.login");
  const signupBtn = document.querySelector("label.signup");
  const signupLink = document.querySelector("form .signup-link a");
  const slide = document.querySelector(".form-inner");
  const sliderTab = document.querySelector(".slider-tab");

  signupBtn.onclick = () => {
    slide.style.marginLeft = "-100%";
    sliderTab.style.left = "50%";
    loginText.style.marginLeft = "-50%";
  };
  loginBtn.onclick = () => {
    slide.style.marginLeft = "0%";
    sliderTab.style.left = "0%";
    loginText.style.marginLeft = "0%";
  };
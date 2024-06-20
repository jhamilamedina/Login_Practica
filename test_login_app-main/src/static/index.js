const btnSend = document.getElementById('send');
btnSend.addEventListener('click', function (e) {
  e.preventDefault()
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;

  data = {
    email,
    password,
  };

  const url = 'http://127.0.0.1:5000/validate';
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((r) => {
      // console.log(r);
      window.location.href =r.url
    })
    .catch((err) => alert('falla en ' + err.message));
});

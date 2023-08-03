formElem.onsubmit = async (e) => {
  e.preventDefault();
  console.log(new FormData(formElem).get('username'))
  let response = await fetch('/auth/login', {
    method: 'POST',
    body: new FormData(formElem)
  });

  // let result = await response.json();

  // alert(result.message);
};
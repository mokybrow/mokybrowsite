formElem.onsubmit = async (e) => {
  e.preventDefault();
  let response = await fetch('/auth/login', {
    method: 'POST',
    body: new FormData(formElem)
  });
  let result = await response;

  if (result.status==400){
    new Toast({
      title: 'Ошибка',
      text: 'Неверные Логин/Пароль',
      theme: 'danger',
      autohide: true,
      interval: 5000,
    });

  }
  if (result.status==204){
    window.location.href = '/admin/dashboard';
  }
  // let result = await response.json();
};

const ExitFromSite = async () => {
  let response = await fetch('/auth/logout', {
    method: 'POST',
    body: new FormData(formElem)
  });
}

let search = 'aliexpress'

const mailElements = document.querySelectorAll('.mail');

mailElements.forEach(mailElement => {
   const senderButton = mailElement.querySelector('.button_sender');
   if (senderButton) {
		const senderEmail = senderButton.getAttribute('title');
      if (senderEmail.includes(search)){
         console.log(senderEmail);
         const checkbox = mailElement.querySelector(".button_checkbox_wrap input[type='checkbox']");
         checkbox.checked = true; // false: 체크 취소
      }
   }
});

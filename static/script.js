const close_message_icon = document.getElementById("close_icon");
const message_box = document.getElementsByClassName("message_box");

function closeMessageBox() {
  console.log("Closing");
  message_box[0].classList.add("close");
}

close_message_icon[i].addEventListener("click", closeMessageBox);
